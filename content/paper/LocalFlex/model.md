从数学建模、概率主方程与渐近分析的纯理论角度，论文提出并解析了**局部灵活优先连接（LFPA）模型**及其连续化拓扑相图。以下为论文的核心数学方程、定量推导与定理体系总结：

---

### 一、 转移概率方程与模型定义

1. **LFPA 模型的转移概率 (Attachment Weight)**
   网络在 $ N $ 个节点状态下，新节点首先以非线性优先连接概率选择初级目标节点 $ i $：$ P_i \propto d_i^\alpha $。随后在节点 $ i $ 的 1-阶图邻域（节点 $ i $ 及其当前度数为 $ d_i $ 的邻居）中**等概率随机重定向**。
   节点 $ i $ 发生重定向的概率为**度数依赖的非均一概率**：
   $ r_i = \frac{d_i}{d_i + 1} \in \left[\frac{1}{2}, 1\right) $
   节点 $ i $ 最终获得新连接的有效权重（Attachment Weight）方程为：
   $ w_i^{(\alpha)} = (1 - r_i) d_i^\alpha + \sum_{j \sim i} r_j d_j^{\alpha-1} = \frac{d_i^\alpha}{d_i + 1} + \sum_{j \sim i} \frac{d_j^\alpha}{d_j + 1} $
   归一化因子（全图总权重）为 $ W \equiv \sum_i w_i = \sum_i d_i^\alpha $。

2. **常数重定向（CR）模型扩展**
   为便于解析推导，将异质概率 $ r_i $ 替换为各向同性的固定常数 $ r \in $，构建了参数空间为 $ \alpha, r) $ 的两维连续相空间。

---

### 二、 超线性相 ($ \alpha > 1 $：图权重最大化与分层层次结构推导

在 $ \alpha > 1 $ 的超线性区间，高度数节点的重定向概率渐近趋于 $ 1 $ ($ r_i \to 1 $，导致系统无平稳度分布，呈现非平稳的层次化拓扑演化。

1. **三层层次结构极值推导 (Theorem 5)**
   设定图 $ G_N $ 存在以指数级标度划分的层级结构：第 $ i $ 层节点的度数标度为 $ d \asymptotically N^{\beta_i} $（满足归一化条件 $ \sum_{i=1}^k \beta_i = 1 $）。
   期望一步全图权重增量表示为：
   $ \mathbb{E}[W(G_{N+1}) - W(G_N) \mid G_N] = \frac{\gamma_\alpha(N)}{m_\alpha(N)} $
   其中主导项为 $ m_\alpha(N) = \sum_i d_i^\alpha $，$ \gamma_\alpha(N) \approx 2\alpha \sum_{i \sim j} (d_i d_j)^{\alpha-1} $。
   **极值变分推导**表明，使权重增长率最大的拓扑演化自发收敛至**三层层次结构（Three-tier Hierarchy）**：
   * **主导节点 (Tier-1 Hub)**：单个节点，度数标度为 **$ d_1 = \Theta\left(N^{\frac{\alpha}{2\alpha - 1}}\right) $**；
   * **富随者 (Tier-2 Rich Followers)**：邻居节点结构，度数标度为 **$ d_2 = \Theta\left(N^{\frac{\alpha - 1}{2\alpha - 1}}\right) $**；
   * **外围节点 (Tier-3 Leaves/Poor)**：度数保持有限 $ O(1) $。

2. **拓扑平衡不变量 (Remark 1)**
   上述权重极值结构诱导出一个全局拓扑不变量 $ \eta_i $：
   $ \eta_i \equiv \frac{\sum_{j \sim i} d_j^{\alpha-1}}{d_i} \asymptotically \text{常数} $
   说明在强度异质性演化中，网络全局自发涌现出局部邻域维度的各向同性平衡。

3. **无限强连接极限 ($ \alpha \to \infty $ 的极限定理**
   * **富人俱乐部相 ($ r=1 $**：主导节点与随者节点的度数阶差消失，演化出 $ \Theta(\sqrt{N}) $ 个最高度节点，各自度数均为 **$ D_1(N) = \Theta(\sqrt{N}) $** (Theorem 3)，且最高度节点的身份在无穷步内切换无限多次 (Theorem 4)。
   * **单主导点稳定相 ($ r < 1 $**：最高度节点在有限步后几乎必然（a.s.）固定，度数以线性速率 $ 1-r)N $ 增长，网络直径渐近收敛为有限值 (Theorem 1)。

---

### 三、 （亚）线性相 ($ \alpha \le 1 $：BA 动力学破缺与马尔可夫主方程

在 $ \alpha \le 1 $ 区间，系统存在平稳度分布，但局部灵活性破坏了传统 Barabási-Albert (BA) 模型的无标度特性。

1. **线性特例 ($ \alpha = 1 $, LFBA) 的失稳推导**
   * **叶节点比例严格上限 (Theorem 8)**：由于边 $ i, j) $ 上 $ d_i > d_j \implies r_i > r_j $，重定向流偏向低度数节点。推导得到 LFBA 叶节点的有效权重满足 $ w_{\text{leaf}}^{\text{LFBA}} \ge 7/6 $，导出渐近叶节点比例上限 **$ p_{\text{leaf}} \le 12/19 \approx 0.63 $**（严格小于 BA 树的 $ 2/3 $）。
   * **BA 巨型 Hub 结构失稳 (Theorem 9 & 10)**：假设存在符合 BA 条件度分布的 Hub $ D_N \asymptotically N^{1/2} $，异质重定向会抑制高度数节点的接纳率。严密证明导出 LFBA 最大度的增长被限制为 **$ D_N = O\left(N^{0.322+\varepsilon}\right) $**，断言了 BA 幂律指数 $ \gamma=3 $ 的破缺，并推导出平稳指数满足 $ \gamma \ge 11/3 \approx 3.67 $。

2. **强负非线性极限 ($ \alpha \to -\infty $ 的马尔可夫主方程与 Weibull 衰减**
   在此极限下，新节点必然先选择叶节点，随后以 $ 1/2 $ 概率重定向至其唯一邻居。
   * **平稳线性递推方程 (Theorem 11)**：设 $ q_{k,l} $ 为拥有 $ k $ 个叶邻居和 $ l $ 个非叶邻居的节点渐近比例，由一步转移状态主方程推导得出双下标平稳递推关系：
     $ (2k + 1) q_{k,l} = (k - 1) q_{k-1,l} + (k + 1) q_{k+1,l-1} $
     初始条件为 $ q_{0,1} = 1/2, q_{1,1} = 1/6 $，总度分布为 $ p_x = \sum_{k+l=x} q_{k,l} $。
   * **矩有限性与非幂律证明 (Theorem 12)**：利用截断级数与线性代数构造算子，证明度分布的所有高阶矩均有限：
     $ \sum_{k \ge 0, l \ge 1} (k + l)^s q_{k,l} < \infty, \quad \forall s > 0 $
     数学上严格否定了幂律尾部的存在（幂律尾部必然导致阶数 $ s \ge \gamma - 1 $ 的矩发散）。
   * **极值标度与 Weibull 拟合**：数值解与极值统计分析表明，度分布呈 **Weibull 延伸指数衰减** $ f(d) = \frac{k}{\lambda} \left(\frac{d}{\lambda}\right)^{k-1} e^{-(d/\lambda)^k} $（其中形状参数 $ k \approx 0.335 $，尺度参数 $ \lambda \approx 0.063 $），极大度标度律相应满足 **$ d_{\max} = \Theta\left((\log N)^{1/k}\right) $**。

---

### 四、 参数空间 $ \alpha, r) $ 极限标度律汇总表

| 相区 / 极限条件 | 最大度标度 $ d_{\max}(N) $ | 叶节点比例 $ p_{\text{leaf}} $ | 拓扑渐近形态 / 度分布衰减特征 | 证明定理引用 |
| :--- | :--- | :--- | :--- | :--- |
| **LFPA ($ \alpha > 1 $** | $ \Theta\left(N^{\frac{\alpha}{2\alpha-1}}\right) $ | $ \Theta(N)/N $ | 三层层次结构（无平稳度分布） | **Theorem 5** |
| **LFPA ($ \alpha \to \infty $** | $ \Theta(\sqrt{N}) $ | $ \Theta(N)/N $ | 富人俱乐部（Rich Club，多 Hub 频繁交替） | **Theorem 3, 4** |
| **CR ($ \alpha \to \infty, r < 1 $** | $ 1-r)N $ (线性增长) | $ N - 1 $ | 核心星形结构（Hub 稳定，直径有限 $ O(1) $） | **Theorem 1, 2** |
| **LFPA ($ \alpha = 1 $** | $ O\left(N^{0.322+\varepsilon}\right) $ | $ \le 12/19 $ | 较轻尾幂律（$ \gamma \ge 11/3 $） | **Theorem 8, 9, 10** |
| **LFPA / CR ($ \alpha \to -\infty $** | $ \Theta\left((\log N)^{1/k}\right) $ ($ k\approx 0.335 $ | $ r $ ($ r=1/2 $ 时为 $ 1/2 $ | Weibull 延伸指数衰减（矩全收敛，非幂律） | **Theorem 11, 12** |

---

💡 **下一步**：如果您希望进一步探索，我可以为您**推导 Theorem 5 中的三层层次结构极值变分过程**，或者计算 **Theorem 11 状态递推方程的边缘分布性质**。