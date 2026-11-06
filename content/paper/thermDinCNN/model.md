在论文 **《Separation of scales and a thermodynamic description of feature learning in some CNNs》** 中，作者将有限宽/通道深度神经网络的特征学习表述为一个**统计场论（Statistical Field Theory）中的非平衡向平衡态映射、平均场解耦与变分高斯近似（VGA）理论框架**。

以下从数学定义、配分函数与作用量、平均场解耦、状态方程推导及特征学习标度展开推演：

---

### 一、 数学定义与函数空间概率测度

考虑由数据集 $ \mathcal{D}_n = \{(\mathbf{x}_\mu, y_\mu)\}_{\mu=1}^n $ 训练的 $ L $ 层神经网络，网络参数 $ \boldsymbol{\theta} $ 服从独立高斯先验 $ W_{ij}^{(l)} \sim \mathcal{N}(0, \sigma_l^2 / N_{l-1}) $。网络前向递归关系为：
$ h_i^{(l)}(\mathbf{x}) = \sum_{j=1}^{N_{l-1}} W_{ij}^{(l)} \phi\left(h_j^{(l-1)}(\mathbf{x})\right), \quad f(\mathbf{x}) = \sum_{j=1}^{N_L} w_j^{(L)} \phi\left(h_j^{(L-1)}(\mathbf{x})\right) \tag{1} $
其中 $ \mathbf{h}^{(l)} \in \mathbb{R}^n $ 为训练集上的预激活向量，$ f_\mu \equiv f(\mathbf{x}_\mu) $ 为标量输出。

采用均方误差损失（MSE）和方差为 $ \sigma^2 $ 的高斯观测噪声，贝叶斯后验概率密度在函数空间（预激活 $ \mathbf{h}^{(l)} $ 和输出 $ \mathbf{f} $ 构成的空间）中可由 Gibbs 分布形式表示：
$ p(\mathbf{f}, \{\mathbf{h}^{(l)}\} \mid \mathcal{D}_n) = \frac{1}{\mathcal{Z}} e^{-S\left(\mathbf{f}, \{\mathbf{h}^{(l)}\}\right)} $
配分函数 $ \mathcal{Z} = \int \mathcal{D}\mathbf{f} \prod_{l=1}^{L-1} \mathcal{D}\mathbf{h}^{(l)} \, e^{-S} $，其中系统总作用量（负对数后验）$ S $ 严格表示为（**公式 3**）：
$ S = \frac{1}{2} \sum_{i=1}^{N_1} \mathbf{h}_i^{(1)\top} \left[Q^{(1)}\right]^{-1} \mathbf{h}_i^{(1)} + \frac{1}{2} \sum_{l=2}^{L-1} \sum_{i=1}^{N_l} \mathbf{h}_i^{(l)\top} \left[\widetilde{Q}^{(l)}(\mathbf{h}^{(l-1)})\right]^{-1} \mathbf{h}_i^{(l)} + \frac{1}{2} \mathbf{f}^\top \left[\widetilde{Q}_f(\mathbf{h}^{(L-1)})\right]^{-1} \mathbf{f} + \frac{1}{2\sigma^2} \sum_{\mu=1}^n (f_\mu - y_\mu)^2 \tag{3} $

各层激活协方差矩阵（后核算子，Post-kernels）定义为（**公式 4**）：
$ \widetilde{Q}^{(l+1)}(\mathbf{h}^{(l)})_{\mu\nu} = \frac{\sigma_{l+1}^2}{N_l} \sum_{i=1}^{N_l} \phi\left(h_{i\mu}^{(l)}\right) \phi\left(h_{i\nu}^{(l)}\right), \quad \widetilde{Q}_f(\mathbf{h}^{(L-1)})_{\mu\nu} = \frac{\sigma_L^2}{N_{L-1}} \sum_{j=1}^{N_{L-1}} \phi\left(h_{j\mu}^{(L-1)}\right) \phi\left(h_{j\nu}^{(L-1)}\right) \tag{4} $

---

### 二、 尺度分离与平均场作用量（Mean-Field Decoupling）

当隐藏神经元数 $ N_l \gg 1 $（或 CNN 的通道数 $ C \gg 1 $）时，随机涨落出现**尺度分离（Separation of Scales）**：
1. **通道/神经元间解耦**：同层不同通道之间的协方差按 $ \mathcal{O}(1/N_l) $ 衰减，层与层之间的直接关联被平均场抑制；
2. **核算子的慢变量性质**：经验核 $ \widetilde{Q}^{(l)} $ 是大量通道的均值，涨落微弱，可替换为其热力学平均（即预核 $ K $ 和后核 $ Q $ 构成的慢变量）。

在此尺度分离极限下，总作用量解耦为各层独立的平均场作用量之和（**公式 10**）：
$ S_{\mathrm{MF}} = \sum_{l=1}^{L-1} S_{\mathrm{MF}}^{(l)} + S_{f,\mathrm{MF}} \tag{10} $
其中输出层作用量为：
$ S_{f,\mathrm{MF}} = \frac{1}{2\sigma^2} \sum_{\mu=1}^n (f_\mu - y_\mu)^2 + \frac{1}{2} \mathbf{f}^\top Q_f^{-1} \mathbf{f} \tag{11} $
而各隐藏层的平均场作用量表现为由下游反馈算子 $ A^{(l+1)} $ 调控的非二次形式（**公式 12**）：
$ S_{\mathrm{MF}}^{(l)} = \frac{1}{2} \sum_{j=1}^{N_l} \mathbf{h}_j^{(l)\top} \left[Q^{(l)}\right]^{-1} \mathbf{h}_j^{(l)} + \frac{1}{2} N_{l+1} \mathrm{Tr}\left[ A^{(l+1)} \widetilde{Q}^{(l+1)}(\mathbf{h}^{(l)}) \right] \tag{12} $
其中末层反馈张量由预测残差驱动：
$ A^{(L)} = \sigma^{-4} (\mathbf{y} - \mathbf{f})(\mathbf{y} - \mathbf{f})^\top - \left[Q_f + \sigma^2 I_n\right]^{-1} \tag{12} $

---

### 三、 变分高斯近似（VGA）与变分自由能

隐藏层作用量 $ S_{\mathrm{MF}}^{(l)} $ 由于非线性激活函数 $ \phi(\cdot) $ 的存在而包含任意高阶项。论文采用**变分高斯近似（Variational Gaussian Approximation, VGA）**，在所有零均值多元高斯试验测度 $ q_K(\mathbf{h}^{(l)}) \sim \mathcal{N}(0, K^{(l)}) $ 中寻找最优的第二累积量 $ K^{(l)} $（称为**预核，Pre-kernel**）。

根据 Gibbs-Bogoliubov-Feynman 变分原理，变分自由能上界为：
$ \mathcal{F}_{\mathrm{var}}[K^{(l)}] = \mathbb{E}_{q_K}[S_{\mathrm{MF}}^{(l)}] - \mathcal{S}[q_K] = \mathcal{D}_{\mathrm{KL}}\left( \mathcal{N}(0, K^{(l)}) \,\parallel\, \mathcal{N}(0, Q^{(l)}) \right) + \frac{1}{2} N_{l+1} \mathrm{Tr}\left[ A^{(l+1)} \mathbb{E}_{q_K}\left[\widetilde{Q}^{(l+1)}\right] \right] $
其中两个高斯分布间的 Kullback-Leibler (KL) 散度具有闭式解析解：
$ \mathcal{D}_{\mathrm{KL}}(K \parallel Q) = \frac{1}{2} \left[ \mathrm{Tr}(Q^{-1} K) - n - \log \det(Q^{-1} K) \right] $

---

### 四、 鞍点变分导数与状态方程（Equations of State, EoS）

对变分参数矩阵 $ K^{(l)} $ 求泛函极值变分，令 $ \frac{\partial \mathcal{F}_{\mathrm{var}}}{\partial K_{\mu\nu}^{(l)}} = 0 $，导出统摄全网络各层参数自洽演化的**状态方程组（**公式 5**）**：

1. **输出预测方程（GPR 结构）**：
   $ \mathbf{f} = Q_f \left[ Q_f + \sigma^2 I_n \right]^{-1} \mathbf{y} $

2. **末端隐藏层的逆核位移方程（Penultimate Layer EoS）**：
   $ \left[ K^{(L-1)} \right]_{\mu\nu}^{-1} = \left[ Q^{(L-1)} \right]_{\mu\nu}^{-1} - \frac{1}{N_{L-1}} \mathrm{Tr}\left[ A^{(L)} \frac{\partial Q_f}{\partial K_{\mu\nu}^{(L-1)}} \right] $

3. **中间隐藏层的向后逆核递归方程**：
   $ \left[ K^{(l-1)} \right]_{\mu\nu}^{-1} = \left[ Q^{(l-1)} \right]_{\mu\nu}^{-1} + \frac{2 N_l}{N_{l-1}} \frac{\partial \mathcal{D}_{\mathrm{KL}}\left(K^{(l)} \parallel Q^{(l)}\right)}{\partial K_{\mu\nu}^{(l-1)}} \quad (\forall l \in [2, L-1]) $

4. **输入层权重协方差自洽方程**：
   $ \Sigma_{ss'}^{-1} = \frac{d}{\sigma_1^2} \delta_{ss'} + \frac{2 N_1}{N_0} \frac{\partial \mathcal{D}_{\mathrm{KL}}\left(K^{(2)} \parallel Q^{(2)}\right)}{\partial \Sigma_{ss'}} $

其中后核算子由预核通过激活函数的核变换积分 $ G(K) $ 给出：$ [Q^{(l)}]_{\mu\nu} = \sigma_l^2 [G(K^{(l-1)})]_{\mu\nu} $。对于误差函数激活函数 $ \phi(x) = \mathrm{erf}(x) $，其闭式映射由 Cho-Saul 积分给出：
$ G(K)_{\mu\nu} = \frac{2}{\pi} \arcsin\left( \frac{2 K_{\mu\nu}}{\sqrt{(1 + 2 K_{\mu\mu})(1 + 2 K_{\nu\nu})}} \right) $

---

### 五、 特征学习标度（FLS）与非微扰机制

当末层为线性时，逆核位移方程简化为直观形式（**公式 6**）：
$ \sigma_L^2 Q_f^{-1} = \left[ Q^{(L-1)} \right]^{-1} - \frac{\sigma_L^2}{N_{L-1}} \left( \boldsymbol{\varepsilon} \boldsymbol{\varepsilon}^\top - \left[ Q_f + \sigma^2 I_n \right]^{-1} \right) \tag{6} $
其中 $ \boldsymbol{\varepsilon} \equiv \frac{\mathbf{y} - \mathbf{f}}{\sigma^2} $ 表示训练预测残差向量。

由此定义出**无量纲特征学习标度（Feature Learning Scale, FLS）** $ \chi $：
$ \chi \equiv \frac{1}{N_{L-1}} \boldsymbol{\varepsilon}^\top Q^{(L-1)} \boldsymbol{\varepsilon} \sim \frac{n \cdot \lambda_{\max} \cdot \mathrm{MSE}}{\sigma^2 N_{L-1}} \tag{24, 26} $
* **常规微扰论失效机制**：传统针对 $ 1/N $ 的泰勒级数展开将 $ \chi $ 隐式视作 $ \mathcal{O}(1/N) $ 的微扰小量；但在大样本数（$ n \gg 1 $ 且 $ \lambda \sim \mathcal{O}(n) $）时，即便 $ N \gg 1 $，因子 $ n^2/N $ 依然使 **$ \chi \sim \mathcal{O}(1) $ 甚至更大**。
* **非微扰全阶求和**：状态方程在数学上等价于对特征学习标度 $ \chi $ 进行了**重整化全阶求和（Summing all orders of $ \chi $）**，仅将真实的 $ 1/N $ 涨落视作小量，从而构建了一个在保持预激活高斯性的同时容纳大幅度非线性特征自适应的自洽解。