论文提出了**扩展平均场理论（Extended Mean-Field Theory）**，旨在解决朴素平均场理论无法建模真实神经网络高维集体活动的问题。以下是该模型的基本数学定义、完整推导过程及临界性判据的详细推导。

---

### 一、 模型的基本定义与最大熵框架

1. **神经元状态与低维投影**  
   考虑由 \$ N\ $ 个二进制神经元组成的网络，每个神经元在短时间窗口内的状态为 \$ s_n \in \{+1, -1\}\ $（\$ +1\ $ 表示放电，\$ -1\ $ 表示静息），网络组态矢量记为 \$ \mathbf{s} = \{s_1, s_2, \dots, s_N\}\ $。  
   定义网络沿权重矢量 \$ \mathbf{W} = (W_1, \dots, W_N)\ $ 的低维投影变量为：
   \$ \varphi = \frac{1}{\sqrt{N}} \sum_{n=1}^N W_n s_n\ $

2. **约束条件与最大熵原理**  
   根据最大熵原理（Maximum Entropy Principle），在满足以下两项实验约束的条件下构造概率分布 \$ P(\mathbf{s})\ $：
   * 匹配每个神经元的平均放电率：\$ \langle s_n \rangle_P = \langle s_n \rangle_{\text{exp}}\ $；
   * 匹配投影变量的完整实验概率分布：\$ P(\varphi)_P = P_{\text{exp}}(\varphi)\ $。

3. **能量函数与玻尔兹曼分布**  
   满足上述约束的最大熵分布为玻尔兹曼分布：
   \$ P(\mathbf{s}) = \frac{1}{Z_{\text{dist}}} \exp[-E_{\text{dist}}(\mathbf{s})]\ $
   能量函数定义为：
   \$ E_{\text{dist}}(\mathbf{s}) = -\sum_{n=1}^N h_n s_n + N U(\varphi)\ $
   其中：
   * \$ h_n\ $ 为局部外场（拉格朗日乘子），用于精确匹配各神经元的平均放电率 \$ \langle s_n \rangle\ $；
   * \$ U(\varphi)\ $ 为非线性势能函数（Potential），用于匹配投影分布 \$ P_{\text{exp}}(\varphi)\ $；因子 \$ N\ $ 保证势能在热力学极限下保持 \$ O(1)\ $ 量级。

---

### 二、 配分函数 \$ Z_{\text{dist}}\ $ 的场积分表象推导

配分函数的原始定义为对所有 \$ 2^N\ $ 种自旋组态求和：
\$ Z_{\text{dist}} = \sum_{\mathbf{s}} \exp\left[ \sum_{n=1}^N h_n s_n - N U\left( \frac{1}{\sqrt{N}} \sum_{n=1}^N W_n s_n \right) \right]\ $

#### Step 1: 引入 Delta 函数解耦非线性势能
为解耦自旋组态 \$ \mathbf{s}\ $ 与非线性势能 \$ U(\varphi)\ $，引入 Dirac Delta 函数：
\$ Z_{\text{dist}} = \sum_{\mathbf{s}} \int d\varphi \, \delta\left( \varphi - \frac{1}{\sqrt{N}} \sum_{n=1}^N W_n s_n \right) \exp\left[ \sum_{n=1}^N h_n s_n - N U(\varphi) \right]\ $

#### Step 2: 傅里叶变换引入隐场 \$ z\ $
使用 Delta 函数的傅里叶积分表示 \$ \delta(x) = \int \frac{dz}{2\pi} e^{-i z x}\ $（其中 \$ z\ $ 为辅助场/隐场）：
\$ Z_{\text{dist}} = \int \frac{dz}{2\pi} \int d\varphi \, \exp[-N U(\varphi) - i z \varphi] \sum_{\mathbf{s}} \exp\left[ \sum_{n=1}^N \left( h_n + \frac{i z W_n}{\sqrt{N}} \right) s_n \right]\ $

#### Step 3: 对自旋组态显式求和
由于指数项对各个自旋 \$ s_n \in \{+1, -1\}\ $ 已完全解耦，可直接求和：
\$ \sum_{s_n = \pm 1} \exp\left[ \left( h_n + \frac{i z W_n}{\sqrt{N}} \right) s_n \right] = 2 \cosh\left( h_n + \frac{i z W_n}{\sqrt{N}} \right)\ $

将求和结果代回配分函数，得到配分函数的场积分精确表达式：
\$ Z_{\text{dist}} = 2^N \int \frac{dz}{2\pi} \int d\varphi \, \exp\left[ -N f_{\text{dist}}(\varphi, z) \right]\ $
其中**有效自由能（Effective Free Energy）** \$ f_{\text{dist}}(\varphi, z)\ $ 定义为：
\$ f_{\text{dist}}(\varphi, z) = U(\varphi) + \frac{1}{N} \left[ i z \varphi - \sum_{n=1}^N \ln \cosh\left( h_n + \frac{i z W_n}{\sqrt{N}} \right) \right]\ $

---

### 三、 鞍点近似（Saddle-Point Approximation）与模型参数求解

在热力学极限 \$ N \to \infty\ $ 下，配分函数积分由鞍点 \$ \varphi_{\text{sp}}, z_{\text{sp}})\ $ 统治：
\$ \ln Z_{\text{dist}} \approx N \ln 2 - N f_{\text{dist}}(\varphi_{\text{sp}}, z_{\text{sp}})\ $

#### Step 1: 鞍点方程组
对自由能求偏导数并令其为 0：
1. \$ \frac{\partial f_{\text{dist}}}{\partial \varphi} = 0 \implies U'(\varphi_{\text{sp}}) + \frac{i z_{\text{sp}}}{N} = 0 \implies z_{\text{sp}} = i N U'(\varphi_{\text{sp}})\ $；
2. \$ \frac{\partial f_{\text{dist}}}{\partial z} = 0 \implies i \varphi_{\text{sp}} - \sum_{n=1}^N \frac{i W_n}{\sqrt{N}} \tanh\left( h_n + \frac{i z_{\text{sp}} W_n}{\sqrt{N}} \right) = 0\ $：
   \$ \varphi_{\text{sp}} = \frac{1}{\sqrt{N}} \sum_{n=1}^N W_n \tanh\left( h_n + \frac{i z_{\text{sp}} W_n}{\sqrt{N}} \right)\ $

#### Step 2: 规范变换与局部外场 \$ h_n\ $ 的确定
能量函数 \$ E_{\text{dist}}(\mathbf{s})\ $ 在规矩变换 \$ U(\varphi) \to U(\varphi) - \varphi U'(\varphi_{\text{sp}})\ $ 和 \$ h_n \to h_n + \frac{W_n}{\sqrt{N}} N U'(\varphi_{\text{sp}})\ $ 下保持不变。  
利用该规范对称性，可固定 \$ U'(\varphi_{\text{sp}}) = 0\ $，从而使得鞍点处的隐场 \$ z_{\text{sp}} = 0\ $。

在此规范下，单个神经元的平均活动简化为：
\$ \langle s_n \rangle = \frac{\partial \ln Z_{\text{dist}}}{\partial h_n} = \tanh(h_n) \implies h_n = \text{atanh}(\langle s_n \rangle_{\text{exp}})\ $
这表明局部外场 \$ h_n\ $ 仅由单个神经元的平均放电率直接决定，形式与独立神经元模型完全相同！

#### Step 3: 反演反解势能函数 \$ U(\varphi)\ $
沿着投影方向的概率分布在鞍点近似下表示为：
\$ P(\varphi) \propto \exp\left[ -N f_{\text{dist}}(\varphi, z^*(\varphi)) \right]\ $
对任意给定的 \$ \varphi\ $，\$ z^*(\varphi)\ $ 为下述实数代数方程的解：
\$ \frac{1}{\sqrt{N}} \sum_{n=1}^N W_n \tanh\left( h_n + \frac{i W_n z^*(\varphi)}{\sqrt{N}} \right) = \varphi\ $

结合实验测量的分布 \$ P_{\text{exp}}(\varphi)\ $，代回自由能表达式即可显式计算出非线性势能 \$ N U(\varphi)\ $：
\$ N U(\varphi) = \ln P_{\text{exp}}(\varphi) - i \varphi z^*(\varphi) + \sum_{n=1}^N \ln \cosh\left( h_n + \frac{i z^*(\varphi) W_n}{\sqrt{N}} \right)\ $

---

### 四、 涨落 Hessian 矩阵与临界性判据

为了确定鞍点解的稳定性及系统的相变临界点，计算自由能 \$ f_{\text{dist}}(\varphi, z)\ $ 关于 \$ \varphi, z)\ $ 的二阶导数矩阵（Hessian 矩阵） \$ H\ $：
\$ H = \begin{pmatrix} \frac{\partial^2 f}{\partial \varphi^2} & \frac{\partial^2 f}{\partial \varphi \partial z} \\ \frac{\partial^2 f}{\partial z \partial \varphi} & \frac{\partial^2 f}{\partial z^2} \end{pmatrix} = \begin{pmatrix} U''(\varphi_{\text{sp}}) & \frac{i}{N} \\ \frac{i}{N} & \frac{1}{N^2} \sum_{n=1}^N W_n^2 \left[ 1 - \tanh^2\left( h_n + \frac{i z_{\text{sp}} W_n}{\sqrt{N}} \right) \right] \end{pmatrix}\ $

在 \$ z_{\text{sp}} = 0\ $ 鞍点处，计算 Hessian 矩阵的行列式（代表自由能曲率）：
\$ \det H = U''(\varphi_{\text{sp}}) \cdot \frac{1}{N^2} \sum_{n=1}^N W_n^2 [1 - \langle s_n \rangle^2] - \left( \frac{i}{N} \right)^2 = \frac{1}{N} \left[ 1 + N U''(\varphi_{\text{sp}}) \Delta \right]\ $
其中 \$ \Delta\ $ 定义为神经元互相独立假定下的投影活动方差：
\$ \Delta = \frac{1}{N} \sum_{n=1}^N W_n^2 \left( 1 - \langle s_n \rangle^2 \right)\ $

#### 临界点条件与磁化率（Susceptibility）
1. **连续相变临界条件**：当自由能曲率消失（\$ \det H = 0\ $）时，鞍点失去稳定性，系统发生二阶相变：
   \$ 1 + N U''(\varphi_{\text{sp}}) \Delta = 0 \implies N U''(\varphi_{\text{sp}}) = -\Delta^{-1}\ $
2. **涨落磁化率 \$ \chi\ $**：网络总体响应易受性/磁化率与 Hessian 矩阵的逆成正比：
   \$ \chi = \frac{\Delta}{1 + N U''(\varphi_{\text{sp}}) \Delta}\ $
   当指标 \$ 1 + N U''(\varphi_{\text{sp}}) \Delta \to 0\ $ 时，磁化率 \$ \chi \to \infty\ $，反映出系统处于临界发散边缘。

---

### 五、 模型的熵（Entropy）推导

基于熵的定义 \$ S_{\text{dist}} = \ln Z_{\text{dist}} + \langle E_{\text{dist}}(\mathbf{s}) \rangle\ $：
1. 平均能量为：\$ \langle E_{\text{dist}} \rangle = -\sum_{n=1}^N h_n \langle s_n \rangle + N \langle U(\varphi) \rangle\ $。
2. 包含一圈涨落修正的配分函数为：\$ \ln Z_{\text{dist}} \approx N \ln 2 - N f_{\text{dist}}(\varphi_{\text{sp}}, z_{\text{sp}}) - \frac{1}{2} \ln \det H\ $。

将其与完全独立神经元模型的熵 \$ S_0 = N \ln 2 + \sum_{n=1}^N [\ln \cosh h_n - h_n \langle s_n \rangle]\ $ 相减，得到扩展平均场模型带来的**熵减（Entropy Reduction）**表达式：
\$ \delta S_{\text{dist}} = S_{\text{dist}} - S_0 \approx N \left[ \langle U(\varphi) \rangle - U(\varphi_{\text{sp}}) \right] - \frac{1}{2} \ln \left[ 1 + N U''(\varphi_{\text{sp}}) \Delta \right]\ $

这表明，约束单个低维投影的概率分布不仅消除了朴素模型的双峰假相变，还能捕获高阶统计依赖，带来显著的熵减。
