基于论文 **《Separation of scales and a thermodynamic description of feature learning in some CNNs》**，以下从核心亮点（Highlights）、方法论（Methodology）、模型基本定义以及主要推导方法四个维度进行系统介绍：

---

### 一、 核心亮点（Highlights）

1. **发现隐藏层的“尺度分离”（Separation of Scales）与近高斯性**：
   在有限通道数/神经元宽度的网络中（$ C, N \gg 1 $），通道或神经元之间的直接相关性被抑制（弱至 $ \mathcal{O}(10^{-3}) $）。网络隐藏层之间仅通过两个**慢变量（第二累积量/核矩阵）**发生解耦耦合：第 $ l $ 层的**预核（Pre-kernel $ K^{(l)} $）**与前一层的**后核（Post-kernel $ Q^{(l)} $）**。在平衡态下，预激活信号依然呈现**近乎严格的多维高斯涨落**。
2. **构建“自适应高斯过程”（Data-Aware GP）与闭式状态方程（Equations of State, EoS）**：
   突破了无限宽网络（NNGP/NTK）核函数僵化且缺失特征学习的瓶颈，将有限宽深度学习映射为一个核函数随数据自适应演化的等效高斯过程回归（GPR），并推导出显式统摄全网各层核演化的矩阵状态方程组。
3. **识别出“特征学习标度”（FLS, $ \chi $）并阐明微扰论失效机制**：
   定义了无量纲特征学习标度 $ \chi \approx \frac{n \cdot \lambda \cdot \text{MSE}}{\sigma^2 N} $（或对应通道数 $ C $）。由于训练样本数 $ n $ 带来的 $ n^2 $ 放大因子，即便在 $ C, N \gg 1 $ 时，$ \chi $ 依然可达 $ \mathcal{O}(1) $ 或更大。状态方程在数学上等价于对 $ \chi $ 进行了**非微扰的全阶求和**，解释了为什么传统的 $ 1/N $ 级数展开在大样本下收敛缓慢甚至失效。
4. **首次给出有限宽非线性 CNN 的解析泛化性能预测**：
   对于两层非线性 CNN（带有误差函数 erf 激活与局部感受野切块），状态方程退化为关于目标重合度标量 $ \alpha $ 的单变量方程并求出显式解析解，其测试集泛化预测与实验测定完全吻合。
5. **在真实复杂深度卷积架构（Myrtle-5 / CIFAR-10）上的实证**：
   在含池化层、ReLU 激活以及 $ C=256 $ 的 Myrtle-5 真实深度视觉网络中证实，随着层数加深，预激活的高斯性进一步增强恢复，支撑了均值场与高斯近似的普适性。

---

### 二、 方法论体系（Methodology）

1. **函数空间贝叶斯后验与场论作用量表象**：
   采用函数空间（Function Space）视角代替复杂的权重空间，结合朗之万动力学（Langevin Dynamics/ULA）将全网络训练的稳态映射为贝叶斯 Gibbs 后验分布，系统总负对数后验被严格形式化为场论作用量 $ S $。
2. **两阶段均值场解耦（Mean-Field Decoupling）**：
   - **层间与通道间解耦**：利用 $ C, N \gg 1 $ 抹平通道微观涨落，将复杂的非线性耦合作用量因式分解为各层独立的平均场作用量 $ S_{\text{MF}}^{(l)} $；
   - **层内数据点解耦**：借鉴原子核物理中的自洽 Hartree-Fock 方法，采用**变分高斯近似（VGA）**对层内非二次作用量进行变分极值求解。
3. **实验采样与自洽数值求解**：
   - 使用带权重衰减和外部白噪声的全批次朗之万算法（ULA）对两层/三层 CNN、三层 FCN 及 Myrtle-5 进行充分退火与平衡态抽样；
   - 采用 Newton-Krylov 算法与 JAX 自动微分对状态方程进行逆核与协方差的自洽定点数值求解。

---

### 三、 模型的基本定义（Model Definitions）

#### 1. 前馈网络架构与前向传播
对于 $ L $ 层前馈网络，输入 $ \mathbf{x} \in \mathbb{R}^d $，前向递推定义为：
$ h_i^{(1)}(\mathbf{x}) = W_i^{(1)} \mathbf{x}, \quad h_i^{(l)}(\mathbf{x}) = \sum_{j=1}^{N_{l-1}} W_{ij}^{(l)} \phi\left(h_j^{(l-1)}(\mathbf{x})\right), \quad f(\mathbf{x}) = \sum_{j=1}^{N_L} w_j^{(L)} \phi\left(h_j^{(L-1)}(\mathbf{x})\right) \tag{1} $
其中 $ \phi(\cdot) $ 为逐元素非线性激活函数（论文主要选取反对称函数 $ \phi = \text{erf} $ 或非负的 ReLU），参数先验为独立高斯分布 $ W_{ij}^{(l)} \sim \mathcal{N}(0, \sigma_l^2 / N_{l-1}) $。

#### 2. 函数空间总作用量（Action）
在包含 $ n $ 个样本的数据集 $ \mathcal{D}_n = \{(\mathbf{x}_\mu, y_\mu)\}_{\mu=1}^n $ 上采用均方误差损失（MSE），后验概率分布在函数空间中表示为 $ p(\mathbf{f}, \{\mathbf{h}^{(l)}\} \mid \mathcal{D}_n) \propto e^{-S} $。总作用量 $ S $ 显式定义为（**公式 3**）：
$ S = \frac{1}{2} \sum_{i=1}^{N_1} \mathbf{h}_i^{(1)\top} \left[Q^{(1)}\right]^{-1} \mathbf{h}_i^{(1)} + \frac{1}{2} \sum_{l=2}^{L-1} \sum_{i=1}^{N_l} \mathbf{h}_i^{(l)\top} \left[\widetilde{Q}^{(l)}(\mathbf{h}^{(l-1)})\right]^{-1} \mathbf{h}_i^{(l)} + \frac{1}{2} \mathbf{f}^\top \left[\widetilde{Q}_f(\mathbf{h}^{(L-1)})\right]^{-1} \mathbf{f} + \frac{1}{2\sigma^2} \sum_{\mu=1}^n (f_\mu - y_\mu)^2 \tag{3} $
其中经验后核算子定义为（**公式 4**）：
$ \widetilde{Q}^{(l+1)}(\mathbf{h}^{(l)})_{\mu\nu} = \frac{\sigma_{l+1}^2}{N_l} \sum_{i=1}^{N_l} \phi\left(h_{i\mu}^{(l)}\right) \phi\left(h_{i\nu}^{(l)}\right), \quad \widetilde{Q}_f(\mathbf{h}^{(L-1)})_{\mu\nu} = \frac{\sigma_L^2}{N_{L-1}} \sum_{j=1}^{N_{L-1}} \phi\left(h_{j\mu}^{(L-1)}\right) \phi\left(h_{j\nu}^{(L-1)}\right) \tag{4} $

#### 3. 预核（Pre-kernel）与后核（Post-kernel）
- **后核（Post-kernel）$ Q^{(l)} $**：由前一层输出激活通过非线性映射形成的协方差，$ [Q^{(l)}]_{\mu\nu} = \sigma_l^2 [G(K^{(l-1)})]_{\mu\nu} $；
- **预核（Pre-kernel）$ K^{(l)} $**：第 $ l $ 层预激活在变分高斯分布下的协方差矩阵 $ \mathbf{h}_i^{(l)} \sim \mathcal{N}(0, K^{(l)}) $。在无限宽极限下 $ K^{(l)} \propto Q^{(l)} $；但在有限宽特征学习区间，二者由于上下游反馈发生分离。

---

### 四、 主要推导方法（Theoretical Derivations）

#### 1. 平均场解耦（Mean-Field Decoupling）
当 $ N_l, C \gg 1 $ 时，对经验核 $ \widetilde{Q} $ 的涨落取平均场近似，总作用量解耦为各层独立的平均场作用量之和：
$ S_{\text{MF}} = \sum_{l=1}^{L-1} S_{\text{MF}}^{(l)} + S_{f,\text{MF}} \tag{10} $
输出层作用量表现为带自适应核 $ Q_f $ 的高斯过程形式：
$ S_{f,\text{MF}} = \frac{1}{2\sigma^2} \sum_{\mu=1}^n (f_\mu - y_\mu)^2 + \frac{1}{2} \mathbf{f}^\top Q_f^{-1} \mathbf{f} \tag{11} $
各隐藏层受到来自下游残差的逆反馈张量 $ A^{(l+1)} $ 调控：
$ S_{\text{MF}}^{(l)} = \frac{1}{2} \sum_{j=1}^{N_l} \mathbf{h}_j^{(l)\top} \left[Q^{(l)}\right]^{-1} \mathbf{h}_j^{(l)} + \frac{1}{2} N_{l+1} \mathrm{Tr}\left[ A^{(l+1)} \widetilde{Q}^{(l+1)}(\mathbf{h}^{(l)}) \right] \tag{12} $
其中末层反馈张量由预测残差驱动：$ A^{(L)} = \sigma^{-4} (\mathbf{y} - \mathbf{f})(\mathbf{y} - \mathbf{f})^\top - \left[Q_f + \sigma^2 I_n\right]^{-1} $。

#### 2. 变分高斯近似（VGA）与变分自由能极小化
隐藏层作用量包含激活函数 $ \phi $ 的高阶非二次项。作者采用变分高斯测度 $ q_K(\mathbf{h}^{(l)}) \sim \mathcal{N}(0, K^{(l)}) $ 来逼近真实概率分布，极小化变分自由能（等价于最小化与非二次测度的 KL 散度）：
$ \mathcal{F}_{\text{var}}[K^{(l)}] = \mathcal{D}_{\text{KL}}\left( \mathcal{N}(0, K^{(l)}) \,\parallel\, \mathcal{N}(0, Q^{(l)}) \right) + \frac{1}{2} N_{l+1} \mathrm{Tr}\left[ A^{(l+1)} \mathbb{E}_{q_K}\left[\widetilde{Q}^{(l+1)}\right] \right] $
其中两个高斯测度之间的 KL 散度为闭式解：$ \mathcal{D}_{\text{KL}}(K \parallel Q) = \frac{1}{2} \left[ \mathrm{Tr}(Q^{-1} K) - n - \log \det(Q^{-1} K) \right] $。

#### 3. 泛函变分与状态方程组（Equations of State, EoS）
对预核矩阵求极值条件 $ \frac{\partial \mathcal{F}_{\text{var}}}{\partial K_{\mu\nu}^{(l)}} = 0 $，导出控制全网络各层特征学习的自洽**状态方程组（公式 5）**：
1. **输出预测方程**：
   $ \mathbf{f} = Q_f \left[ Q_f + \sigma^2 I_n \right]^{-1} \mathbf{y} \tag{5} $
2. **倒数第二层预核的“逆核位移”（Inverse Kernel Shift）方程**：
   $ \left[ K^{(L-1)} \right]_{\mu\nu}^{-1} = \left[ Q^{(L-1)} \right]_{\mu\nu}^{-1} - \frac{1}{N_{L-1}} \mathrm{Tr}\left[ A^{(L)} \frac{\partial Q_f}{\partial K_{\mu\nu}^{(L-1)}} \right] \tag{5} $
3. **中间隐藏层的向后逆核递归方程**：
   $ \left[ K^{(l-1)} \right]_{\mu\nu}^{-1} = \left[ Q^{(l-1)} \right]_{\mu\nu}^{-1} + \frac{2 N_l}{N_{l-1}} \frac{\partial \mathcal{D}_{\text{KL}}\left(K^{(l)} \parallel Q^{(l)}\right)}{\partial K_{\mu\nu}^{(l-1)}} \quad (\forall l \in [2, L-1]) \tag{5} $
4. **输入层权重协方差 $ \Sigma $ 方程**：
   $ \Sigma_{ss'}^{-1} = \frac{d}{\sigma_1^2} \delta_{ss'} + \frac{2 N_1}{N_0} \frac{\partial \mathcal{D}_{\text{KL}}\left(K^{(2)} \parallel Q^{(2)}\right)}{\partial \Sigma_{ss'}} \tag{5, 26} $

#### 4. 倒数第二层线性化与特征学习标度导出
当倒数第二层为线性时，逆核位移方程简化为直观的 rank-1 修正结构（**公式 6**）：
$ \sigma_L^2 Q_f^{-1} = \left[ Q^{(L-1)} \right]^{-1} - \frac{\sigma_L^2}{N_{L-1}} \left( \boldsymbol{\varepsilon} \boldsymbol{\varepsilon}^\top - \left[ Q_f + \sigma^2 I_n \right]^{-1} \right) \tag{6} $
其中 $ \boldsymbol{\varepsilon} = \frac{\mathbf{y} - \mathbf{f}}{\sigma^2} $ 为训练预测残差。
- 项 $ \boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top $ 降低了网络沿训练误差方向的刚度，使网络在数据标签方向更加敏感自适应（即发生特征学习）；
- 泰勒展开的一阶项严格给出了特征学习标度 $ \chi = \frac{1}{N_{L-1}} \boldsymbol{\varepsilon}^\top Q^{(L-1)} \boldsymbol{\varepsilon} \approx \frac{n \cdot \lambda \cdot \text{MSE}}{\sigma^2 N_{L-1}} $。

#### 5. 两层 CNN 的闭式解析解法
针对两层 CNN 模型 $ f(\mathbf{x}) = \sum_{i=1}^N \sum_{c=1}^C a_{ic} \text{erf}(\mathbf{w}_c \cdot \mathbf{x}_i) $，在大样本 $ n \gg 1 $ 与大局部维数 $ S \gg 1 $ 下，利用等效核（Equivalent Kernel）积分连续化处理，残差函数展现旋转对称性 $ \boldsymbol{\varepsilon}(\mathbf{x}) = \alpha y(\mathbf{x}) $。状态方程组被完全简化为标量 $ \alpha $ 的单一非线性方程（**公式 9**）：
$ \sigma^2 \alpha = 1 - q_{\text{train}} \frac{S \lambda_1 l_*}{S \lambda_1 l_* + \sigma^2 / n} \tag{9} $
其中 $ l_* = \frac{1}{S}[1 - \chi_2]^{-1} $，特征学习标度为 $ \chi_2 = C^{-1} \alpha^2 n^2 \lambda_\infty^2 $。直接解出标量 $ \alpha $ 即可显式闭式求出测试集预测与输入权重核的离群特征值。

---

🎯 是否需要针对两层 CNN 状态方程的连续化积分细节，或者其对 ReLU 激活函数的均值修正方案做进一步深入推导？