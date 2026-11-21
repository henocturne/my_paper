从纯数学方程与理论推导的视角，该论文的核心工作是**在比例渐近热力学极限（$ P, N_\ell \to \infty $，且纵横比 $ \alpha_\ell = P / N_\ell \sim \mathcal{O}(1) $ 有限）下，解析计算贝叶斯全连接深度神经网络的配分函数并求解其泛化统计量**。

以下是论文完整的数学建模与推导推展过程：

---

### 1. 数学模型与场论形式化定义

设训练集为 $ \mathcal{T} = \{(\mathbf{x}^\mu, y^\mu)\}_{\mu=1}^P $，其中输入 $ \mathbf{x}^\mu \in \mathbb{R}^{N_0} $，标量目标 $ y^\mu \in \mathbb{R} $。

* **前向传播网络方程**：
  对 $ L-1 $ 个隐藏层（$ \ell = 1, \dots, L-1 $），递归定义前激活变量：
  $ h_{i_\ell}^{(\ell)\mu} = \frac{1}{\sqrt{N_{\ell-1}}} \sum_{i_{\ell-1}=1}^{N_{\ell-1}} W_{i_\ell, i_{\ell-1}}^{(\ell)} \sigma\left(h_{i_{\ell-1}}^{(\ell-1)\mu}\right)
   $
  最底层 $ h_{i_1}^{(1)\mu} = \frac{1}{\sqrt{N_0}} \sum_{i_0=1}^{N_0} W_{i_1, i_0}^{(1)} x_{i_0}^\mu $。线性标量输出为：
  $ f_{\text{DNN}}(\mathbf{x}^\mu) = \frac{1}{\sqrt{N_{L-1}}} \sum_{i_{L-1}=1}^{N_{L-1}} v_{i_{L-1}} \sigma\left(h_{i_{L-1}}^{(L-1)\mu}\right)
   $
* **贝叶斯配分函数**：
  采用二次损失与高斯先验（$ L_2 $ 正则项缩放为 $ 1/\beta $）：
  $ \mathcal{L}(\theta) = \frac{1}{2} \sum_{\mu=1}^P \left[y^\mu - f_{\text{DNN}}(\mathbf{x}^\mu)\right]^2 + \frac{\lambda_L}{2\beta} \sum_{i_L} v_{i_L}^2 + \sum_{\ell=1}^{L-1} \frac{\lambda_\ell}{2\beta} \|W^{(\ell)}\|_F^2
   $
  系统的全配分函数表示为对所有权重 $ \theta = \{W^{(\ell)}, \mathbf{v}\} $ 的泛函/路径积分：
  $ Z = \int \mathcal{D}\theta \, e^{-\beta \mathcal{L}(\theta)}
   $

---

### 2. 单隐藏层（1HL）配分函数的解析消解

以单隐藏层（1HL，即 $ L=2 $，神经元数为 $ N_1 $）为例，其推导核心为**利用场论中的辅助变量逐步解耦各层权重并积分消去**。

#### 步骤 1：利用 Dirac $ \delta $ 变换解耦输出与前激活
引入输出辅助变量 $ s^\mu $ 与前激活变量 $ h_{i_1}^\mu $：
$ s^\mu \equiv \frac{1}{\sqrt{N_1}} \sum_{i_1=1}^{N_1} v_{i_1} \sigma(h_{i_1}^\mu)
 $
通过傅里叶共轭变量 $ \bar{s}^\mu $ 表示 $ \delta $ 约束：$ \delta(s^\mu - \dots) = \int \frac{d\bar{s}^\mu}{2\pi} e^{i \bar{s}^\mu \left(s^\mu - \frac{1}{\sqrt{N_1}} \sum_{i_1} v_{i_1} \sigma(h_{i_1}^\mu)\right)} $。

#### 步骤 2：对第一层权重 $ W^{(1)} $ 积分与输入协方差
积掉第一层高斯先验权重 $ W^{(1)} $，前激活 $ \{h_{i_1}^\mu\}\_{\mu=1}^P $ 退化为相互独立的高斯向量，每个神经元服从以输入协方差矩阵 $ C $ 为核的多元高斯分布：
$ P_1(\{h^\mu\}) = \frac{1}{\sqrt{(2\pi)^P \det C}} \exp\left( -\frac{1}{2} \sum_{\mu,\nu=1}^P h^\mu (C^{-1})_{\mu\nu} h^\nu \right), \quad C_{\mu\nu} = \frac{1}{\lambda_0 N_0} \sum_{i_0=1}^{N_0} x_{i_0}^\mu x_{i_0}^\nu
 $

#### 步骤 3：广义 Breuer–Major 定理与高斯等价性（Gaussian Equivalence）
为了对 $ h^\mu $ 积分，引入标量聚合变量：
$ q = \frac{1}{\sqrt{\lambda_1 N_1}} \sum_{\mu=1}^P \bar{s}^\mu \sigma(h^\mu)
 $
在 $ N_1, P \to \infty $ 且 $ P/N_1 = \alpha_1 $ 的比例极限下，应用 **Breuer–Major 定理及其扩展（Bardet & Surgailis）**，只要激活函数 $ \sigma $ 的 Hermite 秩 $ R \ge 1 $ 且满足协方差可求和条件，变量 $ q $ 在分布上弱收敛于零均值高斯分布 $ \mathcal{N}(0, Q(\bar{\mathbf{s}}, C)) $，其方差由无限宽 NNGP 核 $ K $ 给定：
$ Q(\bar{\mathbf{s}}, C) = \frac{1}{\lambda_1 N_1} \sum_{\mu,\nu=1}^P \bar{s}^\mu K_{\mu\nu}(C) \bar{s}^\nu, \quad K_{\mu\nu}(C) = \int dP_1(\{h^\rho\}) \, \sigma(h^\mu)\sigma(h^\nu)
 $
对 $ q $ 与最后一层权重 $ \mathbf{v} $ 积分后，产生有效非高斯项：
$ \prod_{i_1=1}^{N_1} [Q(\bar{\mathbf{s}}, C) + 1]^{-1/2} = \left( 1 + \frac{1}{\lambda_1 N_1} \sum_{\mu,\nu=1}^P \bar{s}^\mu K_{\mu\nu}(C) \bar{s}^\nu \right)^{-N_1 / 2}
 $
*注：此因子的逆傅里叶变换直接表明了变量从高斯过程向多元 **Student’s $ t $-分布/过程** 的跃迁*。

#### 步骤 4：引入序参量与有效作用量（Effective Action）
插入标量序参量 $ Q $ 及其共轭拉格朗日乘子 $ \bar{Q} $：
$ 1 = \int dQ \, \delta\left( Q - \frac{1}{\lambda_1 N_1} \bar{\mathbf{s}}^T K \bar{\mathbf{s}} \right) = \int \frac{dQ \, d\bar{Q}}{2\pi i} \exp\left( \frac{N_1}{2} Q \bar{Q} - \frac{\bar{Q}}{2\lambda_1} \bar{\mathbf{s}}^T K \bar{\mathbf{s}} \right)
 $
此时对 $ \mathbf{s} $ 和 $ \bar{\mathbf{s}} $ 的多元积分完全转化为高斯积分，可解析完成，配分函数缩减为二维标量积分：
$ Z = \int dQ \, d\bar{Q} \exp\left[ -\frac{N_1}{2} S(Q, \bar{Q}) \right]
 $
其中标量有效作用量 $ S(Q, \bar{Q}) $ 为：
$ S(Q, \bar{Q}) = -Q\bar{Q} + \log(1+Q) + \frac{\alpha_1}{P} \operatorname{Tr} \log\left(\frac{\mathbb{I}}{\beta} + \frac{\bar{Q}}{\lambda_1} K\right) + \frac{\alpha_1}{P} \mathbf{y}^T \left(\frac{\mathbb{I}}{\beta} + \frac{\bar{Q}}{\lambda_1} K\right)^{-1} \mathbf{y}
 $

---

### 3. 鞍点法求解与零温极限（$ \beta \to \infty $）

在热力学极限 $ N_1 \to \infty $ 下，积分由作用量 $ S(Q, \bar{Q}) $ 的鞍点主导：$ \frac{\partial S}{\partial Q} = 0 $, $ \frac{\partial S}{\partial \bar{Q}} = 0 $。

在零温极限 $ \beta \to \infty $（对应训练误差严格最小化的插值态）下，鞍点方程化简为：
$ \bar{Q} = \frac{1}{1+Q}, \qquad Q = \frac{\alpha_1}{\bar{Q}} - \frac{\alpha_1}{\bar{Q}^2} \cdot \frac{1}{P} \mathbf{y}^T \left(\frac{K}{\lambda_1}\right)^{-1} \mathbf{y}
 $
定义无量纲标量观测量 $ s_1 \equiv \frac{1}{P} \mathbf{y}^T \left(\frac{K}{\lambda_1}\right)^{-1} \mathbf{y} $，由 $ Q \ge -1 $ 的物理约束可得 $ \bar{Q}^* $ 的**显式唯一正实根解析解**：
$ \bar{Q}^* = \frac{1}{2} \left[ (\alpha_1 - 1) + \sqrt{(\alpha_1 - 1)^2 + 4 \alpha_1 s_1} \right]
 $
*(当 $ \alpha_1 \to 0 $ 时，退化为 $ \bar{Q}^* = 1 $，即严格恢复无限宽 NNGP 核极限)*。

---

### 4. 测试集泛化误差推导与有限宽判据

将新测试样本 $ \mathbf{x}_0, y_0) $ 引入配分函数求平均，泛化误差 $ \langle \epsilon_g(\mathbf{x}_0, y_0) \rangle = \frac{1}{Z} \int \mathcal{D}\theta \, [y_0 - f_{\text{DNN}}(\mathbf{x}_0)]^2 e^{-\beta \mathcal{L}(\theta)} $ 可严格分解为偏差-方差形式：
$ \langle \epsilon_g(\mathbf{x}_0, y_0) \rangle = (y_0 - \Gamma_1)^2 + \sigma_1^2
 $
其中各分量为：
$ \begin{cases}
\Gamma_1 = \boldsymbol{\kappa}(\mathbf{x}_0)^T K^{-1} \mathbf{y} & \text{（Bias 项，形式上与无限宽相同）} \\
\sigma_1^2 = \frac{\bar{Q}^*}{\lambda_1} \left[ \kappa_0(\mathbf{x}_0) - \boldsymbol{\kappa}(\mathbf{x}_0)^T K^{-1} \boldsymbol{\kappa}(\mathbf{x}_0) \right] & \text{（Variance 项，由重整化序参量 } \bar{Q}^* \text{ 调制）}
\end{cases}
 $
其中 $ \kappa_\mu(\mathbf{x}_0) $ 和 $ \kappa_0(\mathbf{x}_0) $ 为由新测试点诱导的协方差核向量与自协方差标量。

* **有限宽优于无限宽的定量判据**：
  对比有限宽误差与无限宽（$ \bar{Q}^*=1 $）误差的差值：
  $ \Delta \epsilon_g \propto (\bar{Q}^* - 1) \propto \alpha_1 (s_1 - 1)
   $
  由此得出明确的解析判据：**当且仅当 $ s_1 < 1 $ 时，有限宽网络的方差降低，从而泛化误差严格优于对应的无限宽核方法**。

---

### 5. 扩展至 $ L $ 层深层架构的前向递归核重整化

对于 $ L-1 $ 个隐藏层的深层全连接网络，反向层间积分会因非线性而阻塞。作者引入**从输入层逐层向前的嵌套积分（Forward-propagating Method）**：

1. **递归重整化核（Recursive Kernels）**：
   定义每层的重整化核矩阵 $ K_\ell^{(R)}(\{\bar{Q}\}) $ 遵循前向映射递归方程：
   $ K_\ell^{(R)} = \mathcal{T}_{\sigma}\left( \frac{\bar{Q}_{\ell-1}}{\lambda_{\ell-1}} K_{\ell-1}^{(R)} \right)
    $
   其中 $ \mathcal{T}_\sigma $ 是针对激活函数 $ \sigma $ 的 NNGP 积分变换算符（如对于 ReLU 对应于著名的 Cho-Saul 算符）。
2. **多层有效作用量**：
   配分函数被化简为包含 $ 2L $ 个标量序参量 $ \{Q_\ell, \bar{Q}_\ell\}_{\ell=1}^L $ 的有效场论作用量：
   $ Z_{\text{DNN}} = \int \prod_{\ell=1}^L dQ_\ell d\bar{Q}_\ell \exp\left[ -\frac{N_L}{2} S_{\text{DNN}}\left(\{Q_\ell, \bar{Q}_\ell\}\right) \right]
    $
   $ S_{\text{DNN}} = \sum_{\ell=1}^L \frac{\alpha_L}{\alpha_\ell} \left[ -Q_\ell \bar{Q}_\ell + \log(1+Q_\ell) \right] + \frac{\alpha_L}{P} \operatorname{Tr} \log\left( \frac{\mathbb{I}}{\beta} + K_L^{(R)}(\{\bar{Q}\}) \right) + \frac{\alpha_L}{P} \mathbf{y}^T \left( \frac{\mathbb{I}}{\beta} + K_L^{(R)}(\{\bar{Q}\}) \right)^{-1} \mathbf{y}
    $
   在鞍点和零温极限下，深层网络的判据推广为标量指标 $ s_L = \frac{1}{P} \mathbf{y}^T K_L^{-1} \mathbf{y} $ 是否小于 1。