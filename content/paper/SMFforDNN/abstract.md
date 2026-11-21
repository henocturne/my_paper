这篇发表于 *Nature Machine Intelligence*（2023）的论文 **《A statistical mechanics framework for Bayesian deep neural networks beyond the infinite-width limit》**，利用统计力学方法研究了**有限宽贝叶斯深度神经网络**的泛化性能与理论性质。以下为您梳理其主要亮点（Highlight）、研究方法（Methodology）、模型基本定义以及核心推导流程：

---

### 一、 论文的核心亮点（Highlight）

1. **突破无限宽假设，进入比例渐近热力学极限**：
   传统的深度学习核极限理论（如 NNGP）通常假设隐藏层神经元宽度 $ N_\ell \to \infty $ 且训练集样本数 $ P $ 固定。该论文建立了在 $ N_\ell, P \to \infty $ 但保持纵横比 $ \alpha_\ell = P / N_\ell $ 为**有限非零常数**（比例热力学极限）下的统计力学框架，更贴近实际深度学习的超参数化场景。
2. **推导出有限宽网络泛化误差的闭式解析解**：
   在单隐藏层（1HL）及多层深层网络中，导出了依赖有限个序参量（Order Parameters）的有效作用量（Effective Action），并给出了测试泛化误差的偏差-方差分解闭式解。
3. **发现向 Student’s $ t $-过程的转变**：
   论文证明，当样本数 $ P $ 与网络宽度 $ N_1 $ 处于同阶时，有限宽效应导致前激活与输出变量不再严格服从高斯分布，而是自然地从无限宽时的**高斯过程（Gaussian Process, GP）**转变为**多元 Student’s $ t $-分布/过程**，量化刻画了非高斯修正。
4. **提出判定有限宽优于无限宽的定量判据**：
   推导出了一个标量指标 $ s_L = \frac{1}{P} \mathbf{y}^T K_L^{-1} \mathbf{y} $；在 ReLU 激活函数等情况下，当且仅当 $ s_L < 1 $ 时，有限宽网络的泛化损失预期会优于无限宽对应的网络。

---

### 二、 模型的基本定义（Model Definition）

1. **网络架构（Architecture）**：
   考虑一个具有 $ L-1) $ 个隐藏层、输出层为线性读出的全连接深度神经网络 $ f_{\text{DNN}}(\mathbf{x}) $。
   - 输入层维度为 $ N_0 $，样本为 $ \mathbf{x}^\mu \in \mathbb{R}^{N_0} $，目标标签为标量 $ y^\mu \in \mathbb{R} $（$ \mu = 1, \dots, P $）。
   - 隐藏层各层神经元数量为 $ N_\ell $（$ \ell = 1, \dots, L-1 $）。各层的前激活递归定义为：
     $ h_{i_\ell}^{(\ell)} = \frac{1}{\sqrt{N_{\ell-1}}} \sum_{i_{\ell-1}} W_{i_\ell, i_{\ell-1}}^{(\ell)} \sigma(h_{i_{\ell-1}}^{(\ell-1)}) + b_{i_\ell}^{(\ell)} $
   - 输出层（单输出）：$ f_{\text{DNN}}(\mathbf{x}) = \frac{1}{\sqrt{N_{L-1}}} \sum_{i_{L-1}} v_{i_{L-1}} \sigma(h_{i_{L-1}}^{(L-1)}) $。

2. **损失函数与先验（Loss & Prior）**：
   针对回归任务采用带有权重衰减（$ L_2 $ 正则化）的二次损失函数：
   $ \mathcal{L} = \frac{1}{2} \sum_{\mu=1}^P [y^\mu - f_{\text{DNN}}(\mathbf{x}^\mu)]^2 + \mathcal{L}_{\text{reg}} $
   其中正则化项为：
   $ \mathcal{L}_{\text{reg}} = \frac{\lambda_L}{2\beta} \sum_{i_L} v_{i_L}^2 + \frac{1}{2\beta} \sum_{\ell=0}^{L-1} \lambda_\ell \|W^{(\ell)}\|^2 $
   参数 $ \beta = 1/T $ 为逆温度；将正则项按 $ 1/\beta $ 缩放对应于贝叶斯学习中权重服从高斯先验的设定，在 $ \beta \to \infty $（零温极限）下对应最小化经验训练误差。

3. **配分函数（Partition Function）与后验**：
   系统的平衡态与学习后验由吉布斯分布及配分函数描述：
   $ Z = \int \mathcal{D}\theta \, e^{-\beta \mathcal{L}(\theta)} $
   其中 $ \theta = \{W^{(\ell)}, \mathbf{v}\} $ 表示对所有网络权重做路径积分。

---

### 三、 研究方法与主要推导步骤（Methodology & Derivations）

论文的推导核心在于**利用统计力学场论手段，将对大量权重维度的积分积掉，转化为对极少数序参量的积分，并用鞍点法求解**。具体推导路线如下：

1. **引入辅助场与解耦层间权重（Decoupling Weights via Auxiliary Fields）**：
   - 为解耦各层权重在损失函数中的相互纠缠，利用两组狄拉克 $ \delta $ 函数（及其傅里叶积分表示），分别引入隐藏层前激活变量与网络输出变量的辅助变量。
   - 对单隐藏层（1HL），将网络输出表示为 $ s^\mu = \frac{1}{\sqrt{N_1}} \sum_{i_1} v_{i_1} \sigma(h_{i_1}^\mu) $，此时关于各层权重的积分可以逐层分解并解析积分出来。

2. **广义中心极限定理与高斯等价性（Breuer–Major Theorem & Gaussian Equivalence）**：
   - 在积掉第一层权重后，前激活变量 $ h_{i_1}^\mu $ 联合服从协方差矩阵为 $ C_{\mu\nu} = \frac{\mathbf{x}^\mu \cdot \mathbf{x}^\nu}{\lambda_0 N_0} $ 的高斯分布。
   - 当计算关于非线性激活值加权和的分布时，借助 **Breuer–Major 定理**（及其由 Bardet & Surgailis 推广的极限定理），在 $ \alpha_1 = P/N_1 $ 有限的比例热力学极限下，证明了变量在分布上渐近高斯等价，使得核积分能够封闭到经典的 NNGP 协方差核 $ K(C) $ 上。

3. **导出有效作用量（Effective Action）**：
   - 插入共轭变量 $ Q $ 与 $ \bar{Q} $，将配分函数化简为仅含标量序参量的二维积分：
     $ Z = \int dQ d\bar{Q} \exp\left[ -\frac{N_1}{2} S(Q, \bar{Q}) \right] $
     有效作用量 $ S(Q, \bar{Q}) $ 表示为：
     $ S(Q, \bar{Q}) = -Q\bar{Q} + \log(1+Q) + \frac{\alpha_1}{P} \operatorname{Tr} \log \left(\frac{\mathbb{I}}{\beta} + \frac{\bar{Q}}{\lambda_1} K\right) + \frac{\alpha_1}{P} \mathbf{y}^T \left(\frac{\mathbb{I}}{\beta} + \frac{\bar{Q}}{\lambda_1} K\right)^{-1} \mathbf{y} $
   - 该结构表明，$ Q, \bar{Q} $ 充当了有效重整化参数，无限宽极限则对应于 $ \alpha_1 \to 0 $ 时的特殊解 $ Q^* = \bar{Q}^* = 1 $。

4. **前向递归传播（Forward-propagating Method for Deep Networks）**：
   - 对于 $ L $ 层深层网络，由于非线性的存在，以往在线性网络中使用的反向传播积分不再适用。作者提出了从输入层开始向前推进的**嵌套积分法**。
   - 最终将深层配分函数缩减为 $ 2L $ 维积分，有效作用量由一组递归重整化核 $ K^{(R)}_\ell(\{\bar{Q}\}) $ 及其共轭序参量 $ \{Q_\ell, \bar{Q}_\ell\} $ 组成。

5. **鞍点方程与零温极限解析求解（Saddle-point Method & $ \beta \to \infty $）**：
   - 在热力学极限下，积分由鞍点方程 $ \partial_Q S = 0, \partial_{\bar{Q}} S = 0 $ 统治。
   - 在 $ \beta \to \infty $ 的过参数化插值相下，鞍点方程具备严格解析解，从而得到了新测试样本 $ \mathbf{x}_0, y_0) $ 的泛化误差 $ \langle \epsilon_g \rangle $ 的显式闭式公式（偏置项 $ \Gamma $ 与方差项 $ \sigma^2 $）。

---