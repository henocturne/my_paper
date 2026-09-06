根据提供的源文件，论文**《Dynamical Phase Transitions in Nonequilibrium Networks》**提出了一个解释经典非平衡网络动力学相变（DPT）的理论框架。以下是该模型的详细定义及其数学推导过程：

### **一、 模型基本定义**

模型考虑一个拥有 $N$ 个顶点的有向网络，其演化由边缘（edges）的随机添加和移除驱动。

1.  **边添加率 (Birth Rate $\gamma^+_{ij}$):** 包含自发生成项和由相互作用驱动的非线性项：
    $$\gamma^+_{ij} = \frac{\alpha}{N} + \beta(A^2)_{ij} \tag{S6, 10}$$
    *   $\alpha$：自发边生成的速率常数。
    *   $1/N$：确保网络稀疏性的缩放因子。
    *   $\beta$：非线性耦合常数。
    *   $(A^2)_{ij} = \sum_k A_{ik}A_{kj}$：代表**三元闭合（Triadic Closure）**机制，即节点 $i$ 和 $j$ 如果拥有共同邻居 $k$，则成边概率增加。

2.  **边移除率 (Death Rate $\gamma^-$):** 假定为常数 $\gamma$：
    $$\gamma^-_{ij} = \gamma \tag{10, S6}$$

### **二、 数学推导过程**

#### **1. 基础演化方程 (Master Equations)**
推导从描述边状态（$s=0$ 或 $1$）切换的生灭过程开始。对于任何物理观测值 $O(A)$，其期望值的演化遵循以下通用方程：
$$\frac{d\langle O(A)\rangle}{dt} = \sum_{e \in E} \langle [(1-A_e)\gamma^+_e(A) - A_e\gamma^-_e(A)] (O(A|A_e=1) - O(A|A_e=0)) \rangle \tag{S4}$$

#### **2. Schwinger-Dyson (SD) 方程的推导**
为了量化网络的结构变化，研究者推导了连通子图密度 $\rho(G)$ 的演化方程。
*   对于最简单的子图——**平均度 $z$**（即单条边的密度），其演化方程为：
    $$\frac{dz}{dt} = \alpha - \gamma z + \beta(z^2 - \Delta) \tag{11, S10}$$
    其中，$\Delta$ 是**三角形密度**。非线性项 $\beta(z^2 - \Delta)$ 引入了一个放大集群化的反馈循环。

*   由于 $\Delta$ 的演化又取决于更高阶的四顶点子图密度，产生了一个无穷方程链（SD 方程的特征）。三角形密度的演化大致遵循：
    $$\frac{d\Delta}{dt} = \beta(z^2 - \Delta) - 3\gamma\Delta + O(\beta^3) \tag{12, S14}$$

#### **3. 树图级截断与解析解 (Tree-level Truncation)**
在弱相互作用极限下，应用微扰截断方案，忽略三角形密度 $\Delta$ 的贡献（即 $\Delta \sim O(\beta)$）。
*   当处于非平衡相（$\beta > \gamma^2/4\alpha$）时，平均度 $z(t)$ 的解析解为：
    $$z(t) = \frac{\gamma}{2\beta} + \frac{\omega}{\beta} \cot(\omega(t_c - t)) \tag{S15}$$
    其中 $\omega = \sqrt{|\alpha\beta - \gamma^2/4|}$。
*   这导致了在**有限临界时间 $t_c$** 处的**双曲发散**（Hyperbolic Divergence）：
    $$z(t) \sim (t_c - t)^{-1} \tag{4, 14}$$
    临界时间 $t_c$ 定义为 $t_c = \omega^{-1}[\text{acot}(2\omega) + \pi/2]$。

#### **4. 度分布的解析求解 (Generating Function Method)**
为了研究临界点附近的度分布 $P(k, t)$，研究者使用**生成函数法**求解主方程。
*   定义生成函数 $G(x, t) = \sum_k x^k P(k, t)$，将其转化为偏微分方程：
    $$\frac{\partial G(x, t)}{\partial t} = (x-1) \left( \alpha G(x, t) - (\gamma - \beta z(t)x) \frac{\partial G(x, t)}{\partial x} \right) \tag{S17}$$
*   通过变量替换和积分，求得 $G(x, t)$ 的显式解。
*   当 $t \to t_c$ 时，对生成函数进行逆傅里叶变换，证明了度分布会自发演化为**无标度形式**：
    $$P(k, t \to t_c) \sim k^{-1} \tag{23, 53}$$

### **三、 模型的进一步修正与验证**
*   **耦合常数重整化：** 考虑三角形密度的修正后，引入“穿衣”耦合常数（dressed coupling constant） $\beta_0 \approx \beta - \beta^2/3\gamma$，这显著提高了理论预测与模拟的一致性。
*   **一阶相变特征：** 定义序参量 $q$（边占完全图比例），发现其在 $t_c$ 处从 $0$ 跃迁至非零值，表现出类似“潜热”的一阶相变特征。
*   **热力学极限：** 模拟表明，随着系统规模 $N$ 增大，相变变得更加陡峭，最终收敛于理论预测的非连续性跳跃。