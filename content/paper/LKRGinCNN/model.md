在论文 **《Local kernel renormalization as a mechanism for feature learning in overparametrized convolutional neural networks》** 中，作者将有限宽（比例极限）下的神经网络学习抽象为一个**统计力学配分函数的鞍点变分积分问题**。通过建立有效作用量（Effective Action），对比了全连接网络（FCN）、局部连接网络（LCN）与卷积网络（CNN）在热力学极限下的核演化形式。

以下纯粹从**数学定义、统计力学配分函数、高斯等价性与鞍点积分推导、重整化核对比以及有限尺寸标度分析**五个步骤展开推导：

---

### 1. 模型架构与贝叶斯统计力学基础定义

考虑包含 $ P $ 个样本的数据集 $ X = \{x_\mu\}_{\mu=1}^P $，其中 $ x_\mu \in \mathbb{R}^{N_0} $，目标标签标量为 $ y_\mu \in \mathbb{R} $。采用均方误差损失函数（MSE）：
$ \mathcal{L}(\theta) = \frac{1}{2} \sum_{\mu=1}^P \left( y_\mu - f(x_\mu; \theta) \right)^2 \tag{17} $

网络权重参数 $ \theta = (W, v) $ 赋予独立高斯先验测度 $ d\mu(\theta) = d\mu(W) d\mu(v) $：
$ d\mu(W) \propto \exp\left(-\frac{\lambda_0}{2} \|W\|_F^2\right) dW, \quad d\mu(v) \propto \exp\left(-\frac{\lambda_1}{2} \|v\|_F^2\right) dv \tag{18} $
超参数 $ \lambda_0, \lambda_1 $ 充当高斯先验精度（或等价于温度 $ T = 1/\beta $ 缩放后的 $ L_2 $ 正则化项）。

#### 架构数学形式（以单隐层、奇非线性激活 $ \sigma $ 为例）：
* **全连接网络（FCN）**：
  $ h_i(x) = \frac{1}{\sqrt{N_0}} \sum_{j=1}^{N_0} W_{ij} x_j + b_i, \quad f_{\text{FC}}(x) = \frac{1}{\sqrt{N_1}} \sum_{i=1}^{N_1} v_i \sigma\left(h_i(x)\right) \tag{19, 20} $
* **卷积神经网络（CNN，以 1D 卷积为例）**：
  输入按步长 $ S $ 切块，空间切块索引 $ i = 1, \dots, \lfloor N_0/S \rfloor $，通道索引 $ a = 1, \dots, N_c $，卷积核尺寸为 $ M $：
  $ h_i^a(x) = \frac{1}{\sqrt{M}} \sum_{m=-\lfloor M/2 \rfloor}^{\lfloor M/2 \rfloor} W_m^a x_{Si+m} \tag{22} $
  读出层将各通道与局部位置线性加权输出：
  $ f_{\text{CNN}}(x) = \frac{1}{\sqrt{N_c \lfloor N_0/S \rfloor}} \sum_{i=1}^{\lfloor N_0/S \rfloor} \sum_{a=1}^{N_c} v_i^a \sigma\left(h_i^a(x)\right) \tag{23} $
* **局部连接网络（LCN，无权值共享）**：权重带有空间索引 $ W_{m,i}^a $，每个切块位置拥有独立的卷积滤波器组。

---

### 2. 局部协方差张量与无限宽 NNGP 核

对输入样本对 $ x_\mu, x_\nu) $ 及空间切块位置 $ i, j) $，定义**局部协方差张量**：
$ C_{\mu\nu}^{ij} = \frac{1}{\lambda_0 M} \sum_{m=-\lfloor M/2 \rfloor}^{\lfloor M/2 \rfloor} x_{Si+m}^\mu x_{Sj+m}^\nu \tag{7} $
由此诱导出由激活函数 $ \sigma $ 进行非线性积分后的四阶张量**局部核（Local Kernel）**：
$ K_{\mu\nu}^{ij} = \int dt_1 dt_2 \, \mathcal{N}\left(\mathbf{t} \mid \mathbf{0}, \widetilde{C}_{\mu\nu}^{ij}\right) \sigma(t_1) \sigma(t_2) \tag{8} $
其中 2 维联合高斯协方差矩阵为：
$ \widetilde{C}_{\mu\nu}^{ij} = \begin{pmatrix} C_{\mu\mu}^{ii} & C_{\mu\nu}^{ij} \\ C_{\mu\nu}^{ij} & C_{\nu\nu}^{jj} \end{pmatrix} \tag{8} $

在通道数趋于无穷的无限宽极限（$ N_c \to \infty $）下，重整化参数退化，CNN 与 LCN 均退化为空间切块对角元的均匀平均核（标准 NNGP 核）：
$ K_{\mu\nu} = \frac{1}{\lambda_1 \lfloor N_0/S \rfloor} \sum_{i=1}^{\lfloor N_0/S \rfloor} K_{\mu\nu}^{ii} \tag{9} $

---

### 3. 比例热力学极限与有效作用量推导

#### 比例极限（Proportional Limit）
定义热力学极限为样本量 $ P \to \infty $ 与通道数 $ N_c \to \infty $（对于 FCN 为隐层神经元数 $ N_1 \to \infty $），同时保持其比值有限：
$ \alpha_c \equiv \frac{P}{N_c} = \mathcal{O}(1), \quad \alpha_1 \equiv \frac{P}{N_1} = \mathcal{O}(1) $
同时利用广义中心极限定理（Breuer-Major 定理），在输入维数 $ N_0 \to \infty $ 与步长 $ S \sim \mathcal{O}(N_0) $ 缩放下建立**高斯等价性（Gaussian Equivalence）**，封闭平均场高阶矩。

#### 鞍点积分与有效作用量
在逆温度 $ \beta = 1/T $ 下，系统的正则配分函数写为参数先验与似然的积分：
$ Z = \int d\mu(\theta) e^{-\beta \mathcal{L}(\theta)} \tag{1} $
通过引入序参量半正定矩阵 $ Q $（空间维数 $ \lfloor N_0/S \rfloor \times \lfloor N_0/S \rfloor $）及其共轭矩阵 $ \widetilde{Q} $，将高维网络权重积分重塑为矩阵系综的鞍点积分：
$ Z = \int \mathcal{D}Q \mathcal{D}\widetilde{Q} \exp\left( -\frac{N_c}{2} S(Q, \widetilde{Q}) \right) $

通过积分求值导出的**有效作用量（Effective Action）**解析形式为（**公式 2**）：
$ S(Q, \widetilde{Q}) = -\mathrm{Tr}(Q \widetilde{Q}) + \mathrm{Tr}\log(\mathbf{1} + Q) + \frac{\alpha_c}{P} \mathrm{Tr}\log\left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X; Q) \right] + \frac{\alpha_c}{P} \mathbf{y}^\top \left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X; Q) \right]^{-1} \mathbf{y} \tag{2} $

* **物理含义**：矩阵 $ Q_{ij} $ 的物理本质是网络训练达到平衡态时，对应于空间切块 $ i $ 与 $ j $ 的读出层权重向量之间的**热力学平均自相关/互相关**：
  $ Q_{ij} \sim \langle v_i \cdot v_j \rangle $

---

### 4. 鞍点解与重整化核（$ K^{(R)} $）的架构分异

在热力学比例极限下，对 $ S(Q, \widetilde{Q}) $ 求鞍点变分极小化。不同架构的重整化核 $ K^{(R)} $ 呈现出截然不同的数学形式：

| 架构 | 序参量结构 | 重整化核 $ K^{(R)}(x_\mu, x_\nu; Q) $ 数学表达式 | 核重整化机制性质 |
| :--- | :--- | :--- | :--- |
| **FCN** | 标量 $ Q \in \mathbb{R} $ | $ K_{\text{FC}}^{(R)} = \frac{Q}{\lambda_1} K(x_\mu, x_\nu) \tag{13} $ | **平凡全局重整化（Global Renormalization）**：$ Q $ 仅作为标量因子等比例缩放 NNGP 核，不改变核的特征谱或相对模式。其泛化性能被最优超参数下的无限宽核所严格约束。 |
| **LCN** | 对角向量 $ Q_i \in \mathbb{R}^{\lfloor N_0/S \rfloor} $ | $ K_{\text{LCN}}^{(R)} = \frac{1}{\lambda_1 \lfloor N_0/S \rfloor} \sum_{i=1}^{\lfloor N_0/S \rfloor} Q_i K_{\mu\nu}^{ii} \tag{6} $ | **局部对角重整化**：只能调节不同切块各自的自相关强度 $ Q_i $，无法感知不同局部块之间的空间关联。 |
| **CNN** | 完整方阵 $ Q_{ij} $ | $ K_{\text{CNN}}^{(R)} = \frac{1}{\lambda_1 \lfloor N_0/S \rfloor} \sum_{i,j=1}^{\lfloor N_0/S \rfloor} Q_{ij} K_{\mu\nu}^{ij}(x_\mu, x_\nu) \tag{5} $ | **局部核重整化（Local Kernel Renormalization）**：网络利用数据驱动优化全矩阵 $ Q_{ij} $，自由调控任意两局部块 $ i, j) $ 间的相关性权重，实现非平凡特征学习。 |

#### 泛化预测方程与高斯过程回归（GPR）结构
对于未知测试样本 $ x_0, y_0) $，网络在平衡态下的后验预测服从高斯分布 $ p(f_0 \mid X, \mathbf{y}) = \mathcal{N}(\Gamma, \sigma^2) $（**公式 10–12**）：
$ \Gamma(x_0) = K^{(R)}(x_0, X) \left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X) \right]^{-1} \mathbf{y} \tag{10} $
$ \sigma^2(x_0) = K^{(R)}(x_0, x_0) - K^{(R)}(x_0, X) \left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X) \right]^{-1} K^{(R)}(X, x_0) \tag{11} $
总泛化误差由偏差（Bias）和方差（Variance）决定：
$ \epsilon_g(x_0, y_0) = (y_0 - \Gamma(x_0))^2 + \sigma^2(x_0) \tag{12} $
在偏差主导极限（$ \sigma^2 \to 0 $）下，选择非平庸特征矩阵 $ Q_{ij} \neq \delta_{ij} $ 可直接突破由最优 $ T^*, \lambda_1^* $ 界定的无限宽 CNN 泛化误差下界。

---

### 5. 内部表征差异的有限尺寸标度分析（Finite-Size Scaling）

定义训练前后网络后激活（Post-activations）内部表征相似度矩阵的变化量：
$ \mathcal{O}_{\mu\nu} = \frac{1}{N_1} \sum_{i=1}^{N_1} \sigma(h_i^\mu) \sigma(h_i^\nu), \quad \Delta K_{\mu\nu} \equiv \langle \mathcal{O}_{\mu\nu} \rangle - K_{\mu\nu} \tag{14} $

在零温度极限下，对其在吉布斯系综下的解析期望展开：
* **FCN 的表征变化方程**：
  $ \Delta K_{\mu\nu}^{\text{FC}} = -\frac{1}{N_1} \left[ \frac{\lambda_1}{Q} K_{\mu\nu} - y_\mu y_\nu \right] \tag{15} $
  * **标度渐近推导**：方括号内的项为 $ \mathcal{O}(1) $，前置因子为 $ 1/N_1 $。因此在比例热力学极限（$ P, N_1 \to \infty $ 且 $ P/N_1 = \mathcal{O}(1) $）下：
    $ \Delta K_{\mu\nu}^{\text{FC}} \sim \mathcal{O}\left(\frac{1}{N_1}\right) \xrightarrow{N_1 \to \infty} 0 $
    其方差以 $ \sim 1/N_1^2 $ 衰减。这从理论上证明了 **FCN 表征的改变纯粹是有限尺寸效应（Finite-size effect），在热力学极限下完全消失**。

* **CNN 的表征变化方程**：
  $ \Delta K_{\mu\nu}^{\text{CNN}} = -\frac{1}{\lambda_1 N_1 \lfloor N_0/S \rfloor} \sum_{ij, \lambda\rho=1}^{\lfloor N_0/S \rfloor, P} Q_{ij} P_{\mu\lambda\nu\rho}^{ij} \left[ K^{(R)} \right]_{\lambda\rho}^{-1} - \frac{1}{N_1} \sum_{\lambda\rho\epsilon\omega} \left[ K^{(R)} \right]_{\lambda\epsilon}^{-1} \left[ K^{(R)} \right]_{\rho\omega}^{-1} y_\epsilon y_\omega \sum_{ij} Q_{ij} \mathcal{T}_{\mu\lambda\nu\rho}^{ij} \tag{16} $
  * **标度渐近推导**：公式中右侧方括号包含了对样本索引 $ \lambda, \rho $ 的**双重求和（产生 $ P^2 $ 项，或对 $ P $ 项求和）**。
  * 当 $ P \sim \mathcal{O}(N_1) $ 时，$ P $ 阶的求和项补偿了外层 $ 1/N_1 $ 的消失前因子：
    $ \Delta K_{\mu\nu}^{\text{CNN}} \propto \mathcal{O}\left(\frac{P}{N_1}\right) \sim \mathcal{O}(1) $
    即使 $ N_1, P \to \infty $，$ \Delta K^{\text{CNN}} $ 依然保持有限常数阶，**严格推导出浅层卷积网络在热力学极限下具有自发、非平庸的真实特征学习机制**。