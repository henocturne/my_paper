剔除应用背景与具体示例，纯粹从**数学方程、向量演算与动力学推导**的角度，论文的核心理论体系与导出过程可以梳理如下：

---

### 一、 系统的非线性离散映射表示

将具有 $ L $ 个隐藏层的深度前馈神经网络视为非自治离散动力系统。设状态向量 $ x^{(l)} \in \mathbb{R}^{N_l} $（$ l = 0, 1, \dots, L+1 $ 表示层数，对应离散时间），前向传播映射公式为：
$ x_i^{(l)} = g\left( \sum_{j=1}^{N_{l-1}} w_{ij}^{(l)} x_j^{(l-1)} - \theta_i^{(l)} \right) \quad (i = 1, \dots, N_l) $
其中 $ g(\cdot) $ 为连续可微非线性激活函数，$ w_{ij}^{(l)} $ 为权重矩阵 $ W^{(l)} $ 的元素，$ \theta_i^{(l)} $ 为偏置。

---

### 二、 局部线性化、雅可比矩阵与 FTLE 张量推导

#### 1. 局部扰动的线性化传播
在输入 $ x^{(0)} \equiv x $ 处施加微小扰动 $ \delta x $，通过一阶泰勒展开，扰动在第 $ l $ 层的传播为：
$ \delta x^{(l)} = J_l(x) \delta x $
其中 $ J_l(x) \in \mathbb{R}^{N_l \times N_0} $ 为切映射（雅可比矩阵），具有如下链式积表示：
$ J_l(x) = D^{(l)} W^{(l)} \cdots D^{(2)} W^{(2)} D^{(1)} W^{(1)} = \prod_{k=1}^l \left( D^{(k)} W^{(k)} \right) $
这里 $ D^{(k)} $ 为对角切变矩阵，对角元为激活前信号的导数：
$ D_{ij}^{(k)} = g'\left(b_i^{(k)}\right) \delta_{ij}, \quad b_i^{(k)} = \sum_{j=1}^{N_{k-1}} w_{ij}^{(k)} x_j^{(k-1)} - \theta_i^{(k)} $

#### 2. 右 Cauchy-Green 张量与最大 FTLE
定义第 $ l $ 层的右 Cauchy-Green 变形张量为对称半正定矩阵 $ C_l(x) \equiv J_l^\top(x) J_l(x) \in \mathbb{R}^{N_0 \times N_0} $。
其最大奇异值 $ \Lambda_1^{(l)}(x) $ 即为 $ C_l(x) $ 最大特征值的平方根：
$ \Lambda_1^{(l)}(x) = \sqrt{\lambda_{\max}\left( J_l^\top(x) J_l(x) \right)} $
定义最大有限时间李雅普诺夫指数（Maximal FTLE）$ \lambda_1^{(l)}(x) $ 为：
$ \lambda_1^{(l)}(x) \equiv \frac{1}{l} \log \Lambda_1^{(l)}(x) = \frac{1}{l} \log \frac{|\delta x^{(l)}|}{|\delta x|} $
最大伸缩方向由 $ C_l(x) $ 对应于 $ \lambda_{\max} $ 的特征向量确定。

---

### 三、 随机初始化极限与信号稳定性分析

在初始化阶段，权重独立同分布于高斯分布 $ w_{ij}^{(l)} \sim \mathcal{N}(0, \sigma_l^2) $，其中 $ \sigma_l^2 \sim N_l^{-1} $。
根据乘法遍历定理（Multiplicative Ergodic Theorem），当 $ L \to \infty $ 时，$ \lambda_1^{(L)}(x) $ 收敛至与 $ x $ 无关的极限。
在宽度无限极限 $ N_l = N \to \infty $ 下，最大 FTLE 的渐近标度为：
$ \lambda_1^{(L)} \sim \log(G N \sigma^2) $
（其中 $ G $ 为依赖于激活函数 $ g $ 的常数）。
为保证初始信号在多层传播中既不指数爆炸也不指数衰减，必须满足临界条件 $ G N \sigma^2 = 1 $，此时初始 $ \lambda_1^{(L)} = 0 $。

---

### 四、 梯度反向传播对偶性与 FTLE 的自组织推导

随机梯度下降（SGD）中权重参数的更新量满足：
$ \delta w_{mn}^{(l)} \propto \Delta_m^{(l)} x_n^{(l-1)} $
其中反向传播误差向量 $ [\Delta^{(l)}]^\top \in \mathbb{R}^{1 \times N_l} $ 的迭代关系为：
$ [\Delta^{(l)}]^\top = [\Delta^{(L)}]^\top D^{(L)} W^{(L)} \cdots D^{(l+1)} W^{(l+1)} D^{(l)} $
将反向传播的算子乘积与正向雅可比矩阵 $ J_l $ 对比可见，两者在代数结构上互为转置对偶：
- 若 $ \lambda_1^{(L)}(x) < 0 $，反向传播算子将导致 $ \Delta^{(l)} \to 0 $，出现梯度消失，权重更新停滞；
- 若 $ \lambda_1^{(L)}(x) \gg 0 $，权重更新量剧烈发散导致训练不稳定。

因此，优化过程表现出**自组织效应**：无论初始 $ \sigma^2 $ 如何取值，经过梯度更新后，FTLE 的整体分布会自动调整并集中在 0 附近。

---

### 五、 标度律（Scaling Laws）与临界宽度 $ N_c $ 的推导

#### 1. 决策边界与背景区域的 FTLE 渐近行为
- **决策边界区域（Boundary, $ d $）**：为使跨越边界微小距离 $ \delta x $ 时输出实现 $ O(1) $ 的有限变化，网络在边界处的平均 FTLE 必须满足饱和标度关系：
  $ L \langle \lambda_1^{(L)}(x) \rangle_d \to C_d \quad (L \to \infty, \text{常数 } C_d \text{ 与 } N \text{ 无关}) $
- **背景/中心区域（Center, $ c $）**：远离决策边界的背景区域，平均 FTLE 随深度 $ L $ 和宽度 $ N $ 满足如下对数渐近标度：
  $ L \langle \lambda_1^{(L)}(x) \rangle_c \approx -C_c L + \log N \quad (\text{其中 } C_c > 0) $

#### 2. 相变临界宽度 $ N_c $ 的严格导出
当网络宽度 $ N $ 增加时，背景区域的 FTLE 抬升。当背景 FTLE 赶上决策边界处的 FTLE 峰值水平时，即发生机制相变：
$ \langle \lambda_1^{(L)}(x) \rangle_c \approx \langle \lambda_1^{(L)}(x) \rangle_d $
代入两侧的标度方程：
$ \frac{-C_c L + \log N_c}{L} \approx \frac{C_d}{L} \implies -C_c L + \log N_c \approx C_d $
解得临界宽度 $ N_c $ 为：
$ \log N_c \approx C_d + C_c L \implies N_c \sim \exp(C_d + C_c L) $

该推导解析地证明了：**发生相变的临界宽度 $ N_c $ 对网络深度 $ L $ 存在严格的指数依赖关系**。

---

💡 **下一步建议**：如果需要进一步了解补充材料（SM）中关于更复杂的卷积运算对雅可比矩阵结构的修正，或者想对特定推导式进行更细致的数学展开，请随时告诉我！