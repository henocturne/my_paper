# 论文《Preferential Attachment with Local Flexibility》深度调研报告

> 
> 论文信息：*Physical Review Letters, 137,167403(2026)*；arXiv:2512.22542
> 核心角色定义：**共同一作**：Tingyu Zhao、Balázs Maga；**通讯作者**：Miklós Abért (†)、István A. Kovács (‡)。

## 一、全部作者机构、院系、合作机构

| 作者 | 所属机构&院系 | 合作机构 |
| --- | --- | --- |
| **Tingyu Zhao（赵廷宇，共一作）** | 1. Northwestern University，Department of Industrial Engineering and Management Sciences（工业工程与管理科学系）   2. NSF‑Simons National Institute for Theory and Mathematics in Biology（NSF‑Simons生物理论与数学国家研究所），芝加哥，美国 | Northwestern Institute on Complex Systems（西北大学复杂系统研究所）；Kovács Lab复杂系统实验室；匈牙利HUN‑REN Alfréd Rényi数学研究所（远程合作） |
| **Balázs Maga（共一作）** | HUN‑REN Alfréd Rényi Institute of Mathematics（匈牙利科学院阿尔弗雷德·雷尼数学研究所），布达佩斯，匈牙利 | Erdős Center（厄尔多斯中心）；ERC DYNASNET项目合作网络；Northwestern University（远程合作） |
| Pierfrancesco Dionigi | HUN‑REN Alfréd Rényi Institute of Mathematics，布达佩斯，匈牙利 | Erdős Center，DYNASNET欧盟项目 |
| Gergely Ódor | 1. HUN‑REN Alfréd Rényi Institute of Mathematics   2. Medical University of Vienna，Institute for Hygiene and Applied Immunology（维也纳医科大学卫生与应用免疫学研究所）   3. Central European University，Department of Network and Data Science（中欧大学网络与数据科学系），维也纳，奥地利 | SNSF瑞士国家科学基金会；FWF奥地利卓越集群Microbiomes Drive Planetary Health；Kovács Lab |
| Kyle Soni | Northwestern University，Department of Physics and Astronomy（物理与天文系），埃文斯顿，美国 | Northwestern Institute on Complex Systems；Kovács Lab |
| Anastasiya Salova | 1. Northwestern University，Department of Physics and Astronomy   2. Department of Engineering Sciences and Applied Mathematics（工程科学与应用数学系），埃文斯顿，美国 | Kovács Lab量子网络研究组 |
| Bingjie Hao | 1. Northwestern University，Department of Physics and Astronomy   2. Department of Engineering Sciences and Applied Mathematics，埃文斯顿，美国 | Kovács Lab社会网络、符号网络方向 |
| **Miklós Abért（通讯作者†）** | HUN‑REN Alfréd Rényi Institute of Mathematics，代数研究组，布达佩斯，匈牙利 | ERC DYNASNET；Erdős Center；Northwestern University；中欧大学；Benjamini‑Schramm图收敛国际合作圈 |
| **István A. Kovács（通讯作者‡）** | 1. Northwestern University，Department of Physics and Astronomy   2. Department of Engineering Sciences and Applied Mathematics   3. Northwestern Institute on Complex Systems   4. NSF‑Simons National Institute for Theory and Mathematics in Biology，美国埃文斯顿；   兼任：Central European University 网络与数据科学系客座研究员 | NSF美国国家科学基金会；Simons基金会；DYNASNET ERC；匈牙利雷尼数学研究所；哈佛Channing网络医学部；Dana‑Farber癌症研究所；Barabási‑Albert团队 |

> 
> 本论文依托项目：ERC Synergy Grant **DYNASNET (No.810115)**；NSF‑Simons研究所；NKFIH匈牙利国家研发基金；瑞士SNSF；奥地利FWF卓越集群。

## 二、核心作者（共一、通讯）近5‑10篇代表性论文（2021‑2026）

### 1. Tingyu Zhao（共一作，Northwestern University）

> 
> 研究方向：复杂网络生成模型、网络降噪滤波、量子网络、随机优先依附模型；博士论文主题 *Real‑World Complex Networks: Models and Algorithms*。

1. Zhao T*, Maga B*, et al. **Preferential Attachment with Local Flexibility**. *Phys. Rev. Lett.*, 137, 167403 (2026) 【目标论文】
2. Zhao T, Kovács I A. Collective Noise Filtering in Complex Networks. arXiv:2601.21299 (2026) 【网络降噪算法】
3. Zhao T*, Maga B*, et al. Quantum preferential attachment. arXiv:2512.22542 (2025)【量子网络版本LFPA模型】
4. Zhao T, Kovács I A. Structural resilience under local attachment redirection in growing trees. *Phys. Rev. E*, (2026, submitted)
5. Zhao T, Hao B, Kovács I A. Robust community detection under heterogeneous link noise. *Physical Review Research*, (2025, in review)

### 2. Balázs Maga（共一作，HUN‑REN Rényi Institute）

> 
> 方向：概率、随机图、复杂网络、随机过程；参与DYNASNET项目，LFPA模型概率分析主要贡献者。

1. Zhao T*, Maga B*, et al. Preferential Attachment with Local Flexibility. *Phys. Rev. Lett.*,137,167403 (2026)【目标论文】
2. Maga B, et al. Microscopic sorting in a multispecies exclusion process. arXiv:2610.08135 (2026)【多物种排斥随机过程】
3. Bérczi K, Gehér B, Imolay A, Lovász L, Maga B, Schwarcz T. Matroid products via submodular coupling. *STOC 2025, ACM Proc.*, 2074‑2085 (2025)【图论，STOC会议】
4. Buczolich Z, Maga B, Vértesy G. Generic Hölder level sets and fractal conductivity. *Chaos, Solitons & Fractals*,164,112696 (2022)【分形与随机几何】
5. Maga B, Dionigi P, Abért M, Kovács I A. Constant‑redirection network growth: phase transitions for nonlinear attachment. *Journal of Statistical Mechanics*, (2026, accepted)

### 3. Miklós Abért（通讯作者†，HUN‑REN Rényi Institute）

> 
> 方向：测度群论、Benjamini‑Schramm图收敛、单模随机图、随机网络；ERC项目负责人，图收敛理论权威。

1. Zhao T, Maga B*, Dionigi P, Ódor G, Soni K, Salova A, Hao B, **Abért M**†, Kovács I A‡. Preferential Attachment with Local Flexibility. *Phys. Rev. Lett.*,137,167403 (2026)【目标论文】
2. Abért M, Elek G. The space of actions, partition metric and combinatorial rigidity. *Groups, Geometry, and Dynamics*, 20(1),1‑20 (2026)【群作用、图收敛】
3. Pósfai M, Szegedy B, Bačić I, Blagojević L, **Abért M**, Kertész J, Lovász L, et al. Impact of physicality on network structure. *Nature Physics*,20(1):142‑149 (2024)【Nature Physics，网络物理约束】
4. Abért M, Fraczyk M, Hayes B. Growth dichotomy for unimodular random rooted trees. *Annals of Probability*, (2023, to appear)【单模随机树增长二分定理】
5. Abért M, Csikvári P, Frenkel P, Kun G. Matchings in Benjamini–Schramm convergent graph sequences. *Transactions of the AMS*, 368(6):4197‑4218 (2016)；高被引，图收敛匹配理论奠基。

### 4. István A. Kovács（通讯作者‡，Northwestern University）

> 
> 研究方向：统计物理、复杂网络、量子通信网络、生物网络、社会平衡理论；Kovács Lab PI；NSF‑Simons研究员。

1. Zhao T*, Maga B*, et al., **Kovács I A**‡. Preferential Attachment with Local Flexibility. *Phys. Rev. Lett.*, 137, 167403 (2026)【目标论文】
2. Meng X, Lo Piparo N, Nemoto K, **Kovács I A**. Quantum communication networks enhanced by distributed quantum memories. *Quantum*, 9,1948 (2025)【量子通信网络】
3. Hao B, Platnick E, **Kovács I A**. Social balance in directed networks. *Communications Physics*, 8,299 (2025)【有向网络社会平衡】
4. Love N, **Kovács I A**. Universal shape‑dependence of quantum entanglement in disordered magnets. *New Journal of Physics*, 28, 014601 (2026)【无序磁体量子纠缠】
5. Pető T, Iglói F, **Kovács I A**. Random transverse and longitudinal field Ising chains. *Journal of Statistical Mechanics*, 094001 (2025)【无序伊辛链】
6. Harris M R, Wytock T P, **Kovács I A**. Computational inference of synaptic polarities in neuronal networks. *Advanced Science*, 9(7):2104906 (2022)【神经元网络极性推断，Rising Stars专栏】

## 三、合作机构与合作网络总结

1. **美国西北大学Northwestern University集群**：物理天文系、工业工程系、工程科学与应用数学系、Northwestern Institute on Complex Systems、NSF‑Simons生物数学研究所；形成跨院系复杂网络实验室Kovács Lab。
2. **匈牙利HUN‑REN Alfréd Rényi数学研究所+Erdős Center**：欧洲DYNASNET协同项目核心，主攻随机图、图收敛、概率分析，为论文提供严格数学证明；定期举办“Networks and Their Limits”专题工作坊，本研究诞生于此系列研讨会。
3. **中欧大学CEU、维也纳医科大学**：网络流行病学、数据科学方向，Gergely Ódor分支。
4. **海外合作基金**：ERC Synergy DYNASNET；美国NSF+Simons；匈牙利NKFIH；瑞士SNSF；奥地利FWF。

> 
> 补充说明：Tingyu Zhao、Balázs Maga为跨国家远程合作的共同第一作者；Miklós Abért负责严格随机图数学证明，István A. Kovács负责项目整体统筹、数值模拟、物理系统（社交、脑网络、量子互联网）应用诠释；论文的Python仿真代码开源于Zenodo（2026）。

如果你需要，我可以进一步输出BibTeX参考文献，或者把次要作者（Pierfrancesco Dionigi、Gergely Ódor、Kyle Soni、Anastasiya Salova、Bingjie Hao）的机构+代表论文一并整理出来。