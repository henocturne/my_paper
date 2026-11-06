论文《**Local kernel renormalization as a mechanism for feature learning in overparametrized convolutional neural networks**》（发表于 *Nature Communications*, 2024/2025）系统研究了过参数化浅层卷积网络在有限宽度下的特征学习机制。以下为您梳理其核心亮点、方法论体系、模型基本定义与主要推导方法：

---

### 一、 论文核心亮点（Highlights）

1. **解释了 CNN 与 FCN 经验表现反差的物理机制**：
   在计算机视觉等任务中，无限宽（懒惰训练/NTK）全连接网络（FCN）往往优于其有限宽对应物；而在卷积神经网络（CNN）中，有限通道数的有限宽网络却经常取得优于无限宽核的性能。论文通过统计力学框架为这一经验反差给出了清晰的理论解释。
2. **提出“局部核重整化”（Local Kernel Renormalization）机制**：
   在比例热力学极限（Proportional limit）下，FCN 的核仅经历由单一标量参数 $ Q $ 调控的**平凡全局重整化（Global renormalization）**；而 CNN 由于兼具**局部连接（Locality）**与**权重共享（Weight sharing）**，其核矩阵会经历由矩阵 $ Q_{ij} $ 调控的**局部核重整化**。网络可以根据数据驱动自适应调整不同空间局部图像块（Patches）之间的相关性权重。
3. **证明权值共享的不可替代性**：
   论文证明局部连接网络（LCN，有局部连接但无权重共享）仅能调控对角向量 $ Q_i $（自相关），无法捕捉不同局部块间的空间关联。只有 CNN 能优化完整的参数矩阵 $ Q_{ij} $，实现了真正的特征学习。
4. **证明有限宽 CNN 泛化性能可超越最优无限宽核**：
   在偏差主导的机制下（Bias-dominated regime），调整 $ Q_{ij} \neq \mathbf{1} $ 能够突破由最优超参数（温度 $ T^* $ 与先验 $ \lambda_1^* $）界定的无限宽 NNGP 核的泛化性能下界，从而在理论上超越无限宽 CNN。
5. **揭示内部表征演化的有限尺寸标度规律**：
   通过分析训练前后内部表征相似度矩阵的变化 $ \Delta K_{\mu\nu} $，证明了 FCN 表征的变化在比例热力学极限下是衰减消失的有限尺寸效应（$ \mathcal{O}(1/N_1) $）；而 CNN 的表征变化在热力学极限下依然保持有限值（$ \Delta K^{\text{CNN}} \sim \mathcal{O}(P/N_1) $），呈现真正的特征学习行为。

---

### 二、 方法论体系（Methodology）

1. **平衡态贝叶斯统计力学与有效作用量分析**：
   利用配分函数 $ Z = \int d\mu(\theta) e^{-\beta \mathcal{L}(\theta)} $ 将带有二次损失和高斯先验的训练网络映射为正则吉布斯系综，通过泛函积分将其转化为关于序参量矩阵 $ Q, \widetilde{Q} $ 的鞍点积分，解析导出有效作用量 $ S(Q, \widetilde{Q}) $。
2. **高斯等价性（Gaussian Equivalence）假说**：
   利用非线性高斯场泛函的广义中心极限定理（Breuer-Major 定理），在输入维度 $ N_0 $ 与样本数 $ P $ 同阶发散的假设下，将隐藏层激活的非线性相关有效高斯化，从而闭合平均场配分函数。
3. **架构横向对比法（FCN vs. LCN vs. CNN）**：
   在一个统一的形式体系中系统推导全连接、局部连接与卷积层三种架构的有效作用量与重整化核形式，严格分离“局部连接”与“权重共享”各自产生的物理效应。
4. **有限尺寸标度数值验证（Finite-size Scaling）**：
   构建包含线性教师任务的合成高斯数据集以及 CIFAR-10 图像分类任务，利用 Adam 优化器训练的梯度下降网络与 Langevin 动力学贝叶斯网络，检验内部表征差值 $ \Delta K_{\mu\nu} $ 的均值与方差随 $ P, N_1 $（固定 $ \alpha = P/N_1 $）缩放的理论预测。

---

### 三、 模型的基本定义（Model Definitions）

#### 1. 单隐层网络架构
* **卷积层预激活**（针对一维卷积，易推广至 $ d $ 维）：
  $ h_i^a(x) = \frac{1}{\sqrt{M}} \sum_{m=-\lfloor M/2 \rfloor}^{\lfloor M/2 \rfloor} W_m^a x_{Si+m} \quad $
  其中 $ x \in \mathbb{R}^{N_0} $ 为输入，$ M $ 为卷积核尺寸，$ S $ 为步长（Stride），$ i = 1, \dots, \lfloor N_0/S \rfloor $ 为空间位置索引，$ a = 1, \dots, N_c $ 为通道索引，$ W_m^a $ 为共享的卷积权重。
* **全连接读出层输出**：
  $ f_{\text{CNN}}(x) = \frac{1}{\sqrt{N_c \lfloor N_0/S \rfloor}} \sum_{i=1}^{\lfloor N_0/S \rfloor} \sum_{a=1}^{N_c} v_i^a \sigma\left(h_i^a(x)\right) \quad $
  其中 $ \sigma(\cdot) $ 为奇非线性激活函数，$ v_i^a $ 为最后一层的读出权重。
  *(注：若将 $ W_m^a $ 增加空间索引 $ i $ 变为 $ W_{m,i}^a $，则退化为局部连接网络 LCN)。*

#### 2. 贝叶斯先验与损失泛函
* **均方误差损失（MSE Loss）**：
  在包含 $ P $ 个训练样本的数据集 $ X = \{x_\mu\}_{\mu=1}^P, \mathbf{y} = \{y_\mu\}_{\mu=1}^P $ 上，损失定义为：
  $ \mathcal{L}(\theta) = \frac{1}{2} \sum_{\mu=1}^P \left( y_\mu - f(x_\mu; \theta) \right)^2 \quad $
* **参数高斯先验**：
  各层参数服从标准独立正态先验，$ \mu(W) \propto e^{-\frac{\lambda_0}{2} \|W\|_F^2} $，$ \mu(v) \propto e^{-\frac{\lambda_1}{2} \|v\|_F^2} $。超参数 $ \lambda_0, \lambda_1 $ 充当 $ L_2 $ 正则化项。

#### 3. 比例热力学极限（Proportional Limit）
考虑热力学极限：样本数量 $ P \to \infty $，隐层通道数 $ N_c \to \infty $（或神经元数 $ N_1 \to \infty $），同时保持其比值有限：
$ \alpha_c = \frac{P}{N_c} = \mathcal{O}(1) \quad (\text{或 } \alpha_1 = \frac{P}{N_1} = \mathcal{O}(1)) \quad $

---

### 四、 主要推导方法与理论推演

#### 1. 局部协方差张量与局部核的构建
局部空间切块（Patches）之间的协方差矩阵由输入数据给出：
$ C_{\mu\nu}^{ij} = \frac{1}{\lambda_0 M} \sum_{m=-\lfloor M/2 \rfloor}^{\lfloor M/2 \rfloor} x_{Si+m}^\mu x_{Sj+m}^\nu \quad $
由此定义带有四个索引（2个样本索引 $ \mu,\nu $，2个空间块索引 $ i,j $）的**局部核（Local Kernel）**：
$ K_{\mu\nu}^{ij} = \int dt_1 dt_2 \, \mathcal{N}\left(\mathbf{t} \mid 0, \widetilde{C}_{\mu\nu}^{ij}\right) \sigma(t_1) \sigma(t_2) \quad $
在无限通道极限 $ N_c \to \infty $ 下，CNN 和 LCN 的有效核退化为所有对角局部块的空间均匀平均（即标准 NNGP 核）：
$ K_{\mu\nu} = \frac{1}{\lambda_1 \lfloor N_0/S \rfloor} \sum_{i=1}^{\lfloor N_0/S \rfloor} K_{\mu\nu}^{ii} \quad $

#### 2. 配分函数转化与有效作用量推导
通过引入拉格朗日乘子与辅助矩阵变量，将对全网高维权重的积分 $ \int d\mu(\theta) e^{-\beta \mathcal{L}(\theta)} $ 转化为对半正定序参量矩阵 $ Q $ 与共轭矩阵 $ \widetilde{Q} $ 的鞍点积分：
$ Z = \int \mathcal{D}Q \mathcal{D}\widetilde{Q} \, e^{-\frac{N_c}{2} S(Q, \widetilde{Q})} \quad $
通过鞍点方法导出的**有效作用量（Effective Action）**显式形式为：
$ S(Q, \widetilde{Q}) = \mathrm{Tr}(Q \widetilde{Q}) + \mathrm{Tr}\log(1 + Q) - \frac{\alpha_c}{P} \mathrm{Tr}\log\left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X; Q) \right] + \frac{\alpha_c}{P} \mathbf{y}^\top \left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X; Q) \right]^{-1} \mathbf{y} \quad $
其中 $ Q $ 为 $ \lfloor N_0/S \rfloor \times \lfloor N_0/S \rfloor $ 维的特征矩阵，物理上对应于不同空间块对应的读出权重之间的热力学平均相关性。

#### 3. 三类网络架构的重整化核对比
鞍点方程极小化决定了重整化核矩阵 $ K^{(R)} $ 的最终形态：
* **FCN（全连接）**：$ K_{\text{FC}}^{(R)} = \frac{Q}{\lambda_1} K_{\mu\nu} $，重整化退化为全局标量乘子 $ Q $ 对 NNGP 核的单纯缩放，无法改变核矩阵的谱结构与相对权重；
* **LCN（局部连接无共享）**：$ K_{\text{LCN}}^{(R)} = \frac{1}{\lambda_1 \lfloor N_0/S \rfloor} \sum_i Q_i K_{\mu\nu}^{ii} $，仅含对角矢量 $ Q_i $，只能调整各个局部块的自相关，无法跨块交互；
* **CNN（卷积网络）**：
  $ K_{\text{CNN}}^{(R)}(x_\mu, x_\nu; Q) = \frac{1}{\lambda_1 \lfloor N_0/S \rfloor} \sum_{i,j=1}^{\lfloor N_0/S \rfloor} Q_{ij} K_{\mu\nu}^{ij}(x_\mu, x_\nu) \quad $
  通过数据驱动微调整张矩阵 $ Q_{ij} $，实现了对任意两个空间切块 $ i, j $ 之间局部关联的加权调控（即局部核重整化）。

#### 4. 后验预测分布与泛化误差
对于新测试样本 $ x_0, y_0) $，网络预测输出 $ f_0 $ 服从高斯分布 $ \mathcal{N}(\Gamma, \sigma^2) $：
$ \Gamma(x_0) = K^{(R)}(x_0, X) \left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X) \right]^{-1} \mathbf{y} \quad $
$ \sigma^2(x_0) = K^{(R)}(x_0, x_0) - K^{(R)}(x_0, X) \left[ \frac{1}{\beta} \mathbf{1} + K^{(R)}(X, X) \right]^{-1} K^{(R)}(X, x_0) \quad $
该形式与高斯过程回归（GPR）在数学结构上完全一致，但这里的核矩阵 $ K^{(R)} $ 是由数据驱动自适应重整化后的物理核，直接建立了有效作用量与测试泛化误差 $ \epsilon_g = (y_0 - \Gamma)^2 + \sigma^2 $ 之间的闭式解析关联。