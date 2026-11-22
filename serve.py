#!/usr/bin/env python3
"""Local preview server for the paper library.

Serves the generated site under /my_paper/ and exposes a local-only API used
by the delete button on paper cards. Deleting a paper removes its content
directory and the PDF referenced by its front matter.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"
BUILD_DIR = ROOT / ".serve-public"
CONTENT = ROOT / "content" / "paper"
STATIC = ROOT / "static"
HUGO = ROOT / ("hugo.exe" if os.name == "nt" else "hugo")
BASE_PATH = "/my_paper"
PDF_RE = re.compile(r'^pdf:\s*["\']?([^"\'\r\n]+?)["\']?\s*$', re.MULTILINE)


def read_pdf_param(paper_dir: Path):
    index = paper_dir / "index.md"
    if not index.is_file():
        return None
    try:
        match = PDF_RE.search(index.read_text(encoding="utf-8"))
    except OSError:
        return None
    return match.group(1).strip() if match else None


def pdf_used_elsewhere(pdf_ref: str, exclude_name: str) -> bool:
    for other in CONTENT.iterdir():
        if not other.is_dir() or other.name == exclude_name:
            continue
        if read_pdf_param(other) == pdf_ref:
            return True
    return False


def rebuild_site(base_url: str):
    if not HUGO.is_file():
        return False, f"未找到 Hugo 可执行文件：{HUGO}"
    cmd = [
        str(HUGO),
        "--source", str(ROOT),
        "--destination", str(BUILD_DIR),
        "--baseURL", base_url,
        "--minify",
        "--cleanDestinationDir",
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, f"Hugo 构建失败：{exc}"
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        return False, "Hugo 构建失败：" + (detail[-600:] or f"退出码 {proc.returncode}")
    return True, None


def delete_paper(dir_name: str, base_url: str):
    dir_name = (dir_name or "").strip()
    if (
        not dir_name
        or dir_name.startswith(".")
        or dir_name in {".", ".."}
        or any(char in dir_name for char in ("/", "\\", "\x00"))
    ):
        return {"ok": False, "message": "无效的论文目录"}

    paper_dir = (CONTENT / dir_name).resolve()
    if paper_dir.parent != CONTENT.resolve() or not paper_dir.is_dir() or paper_dir.is_symlink():
        return {"ok": False, "message": "未找到该论文目录"}

    pdf_ref = read_pdf_param(paper_dir)
    pdf_shared = bool(pdf_ref) and pdf_used_elsewhere(pdf_ref, dir_name)

    try:
        shutil.rmtree(paper_dir)
    except OSError as exc:
        return {"ok": False, "message": f"删除论文目录失败：{exc}"}

    deleted_pdf = None
    warnings = []
    if pdf_ref:
        rel = pdf_ref.lstrip("/")
        candidate = (STATIC / rel).resolve()
        try:
            candidate.relative_to(STATIC.resolve())
        except ValueError:
            warnings.append("PDF 路径不在 static 目录内，已跳过文件删除")
        else:
            if candidate.suffix.lower() != ".pdf":
                warnings.append("论文 PDF 参数不是 .pdf 文件，已跳过文件删除")
            elif pdf_shared:
                warnings.append("该 PDF 被其他论文引用，已保留文件")
            elif candidate.is_file():
                try:
                    candidate.unlink()
                    deleted_pdf = str(candidate.relative_to(ROOT))
                except OSError as exc:
                    warnings.append(f"PDF 文件删除失败：{exc}")
            else:
                warnings.append("front matter 中的 PDF 文件不存在")

    built, build_error = rebuild_site(base_url)
    if not built:
        warnings.append(build_error)

    result = {
        "ok": True,
        "message": "论文已删除",
        "deletedDir": dir_name,
        "deletedPdf": deleted_pdf,
        "rebuilt": built,
    }
    if warnings:
        result["warning"] = "；".join(warnings)
    return result


class PaperLibraryHandler(SimpleHTTPRequestHandler):
    server_version = "PaperLibrary/1.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BUILD_DIR), **kwargs)

    def _api_path(self):
        path = urllib.parse.urlsplit(self.path).path
        for prefix in (BASE_PATH + "/api/", "/api/"):
            if path.startswith(prefix):
                return path[len(prefix):]
        return None

    def _send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _same_origin(self):
        origin = self.headers.get("Origin")
        if not origin:
            return True
        port = self.server.server_address[1]
        return origin in {
            f"http://localhost:{port}",
            f"http://127.0.0.1:{port}",
        }

    def do_GET(self):
        api = self._api_path()
        if api == "ping":
            self._send_json(200, {"ok": True})
            return
        if api is not None:
            self._send_json(404, {"ok": False, "message": "未知的 API"})
            return

        path = urllib.parse.urlsplit(self.path).path
        if path in ("/", BASE_PATH):
            self.send_response(302)
            self.send_header("Location", BASE_PATH + "/")
            self.end_headers()
            return
        if path != BASE_PATH and not path.startswith(BASE_PATH + "/"):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        path = urllib.parse.urlsplit(self.path).path
        if path != BASE_PATH and not path.startswith(BASE_PATH + "/"):
            self.send_error(404)
            return
        super().do_HEAD()

    def do_POST(self):
        if self._api_path() != "delete-paper":
            self._send_json(404, {"ok": False, "message": "未知的 API"})
            return
        if not self._same_origin():
            self._send_json(403, {"ok": False, "message": "仅允许本机页面调用"})
            return
        content_type = (self.headers.get("Content-Type") or "").lower()
        if not content_type.startswith("application/json"):
            self._send_json(415, {"ok": False, "message": "请求必须使用 application/json"})
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(length) or b"{}")
        except (ValueError, OSError):
            self._send_json(400, {"ok": False, "message": "请求格式错误"})
            return
        result = delete_paper(
            str(data.get("dir") or ""),
            getattr(self.server, "local_base_url", f"http://localhost:{self.server.server_address[1]}/my_paper/"),
        )
        self._send_json(200 if result["ok"] else 400, result)

    def translate_path(self, path):
        clean = urllib.parse.urlsplit(path).path
        if clean == BASE_PATH:
            rel = "/"
        elif clean.startswith(BASE_PATH + "/"):
            rel = clean[len(BASE_PATH):]
        else:
            return str(BUILD_DIR / "__not_found__")
        return super().translate_path(rel)


def main():
    parser = argparse.ArgumentParser(description="论文库本地预览与删除服务")
    parser.add_argument("--port", type=int, default=1313)
    parser.add_argument("--no-build", action="store_true", help="跳过启动时的站点构建")
    args = parser.parse_args()

    local_base_url = f"http://localhost:{args.port}/my_paper/"
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), PaperLibraryHandler)
    except OSError as exc:
        print(f"无法监听端口 {args.port}：{exc}", file=sys.stderr)
        print("请关闭占用该端口的程序，或使用 --port 指定其他端口。", file=sys.stderr)
        return 1
    server.local_base_url = local_base_url

    if not args.no_build or not BUILD_DIR.is_dir():
        print("正在构建站点 ...")
        built, error = rebuild_site(local_base_url)
        if not built:
            server.server_close()
            print(error, file=sys.stderr)
            return 1

    print(f"论文库预览已启动：http://localhost:{args.port}/my_paper/")
    print("删除按钮仅在通过此服务打开时可用。按 Ctrl+C 停止。")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
