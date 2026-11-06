从动力系统、线性代数算子与渐近标度分析的角度，该论文建立的纯数学方程与理论推导体系如下：

---

### 1. 前向离散动力系统与切空间局部线性化

将 $ L $ 个隐藏层的全连接前馈网络形式化为离散动力系统，其中层索引 $ l = 0, \dots, L+1 $ 对应离散时间步：
$ x_i^{(l)} = g\left( \sum_{j=1}^{N_{l-1}} w_{ij}^{(l)} x_j^{(l-1)} - \theta_i^{(l)} \right) = g\left(b_i^{(l)}\right) $
其中 $ b_i^{(l)} $ 为激活前局部场，$ g(\cdot) $ 为连续可微的非线性激活函数（论文取 $ g(b) = \tanh(b) $）。

在输入端 $ x^{(0)} = x $ 施加无穷小摄动 $ \delta x $，通过一阶泰勒展开进行局部线性化，扰动在第 $ l $ 层的演化满足递推方程：
$ \delta x^{(l)} = D^{(l)} W^{(l)} \delta x^{(l-1)} $
自底向上累积展开，得到前向切映射雅可比矩阵 $ J_l(x) $（**公式 1**）：
$ \delta x^{(l)} = D^{(l)} W^{(l)} \cdots D^{(2)} W^{(2)} D^{(1)} W^{(1)} \delta x \equiv J_l(x) \delta x \quad \text{—— (1)} $
其中对角导数矩阵为：
$ D_{ij}^{(l)} = g'\left(b_i^{(l)}\right) \delta_{ij} = \left. \frac{d g(b)}{db} \right|_{b = b_i^{(l)}} \delta_{ij} $

---

### 2. 右 Cauchy-Green 变形张量与最大 FTLE

定义输入空间的右 Cauchy-Green 变形张量为对称半正定算子：
$ C_l(x) \equiv J_l^\top(x) J_l(x) \in \mathbb{R}^{N_0 \times N_0} $
其特征方程为：
$ C_l(x) \mathbf{v}_i(x) = \left( \Lambda_i^{(l)}(x) \right)^2 \mathbf{v}_i(x), \quad \Lambda_1^{(l)} > \Lambda_2^{(l)} > \dots \ge 0 $
其中 $ \Lambda_1^{(l)}(x) = \| J_l(x) \|_2 $ 即为雅可比矩阵 $ J_l(x) $ 的**谱范数 / 最大奇异值**。

* **最大有限时间李雅普诺夫指数（Maximal FTLE）**：定义为扰动模长放大的对数增长率：
  $ \lambda_1^{(l)}(x) \equiv \frac{1}{l} \log \Lambda_1^{(l)}(x) = \frac{1}{2l} \log \lambda_{\max}\left(J_l^\top(x) J_l(x)\right) $
* **最大拉伸方向（Maximal Stretching Direction）**：由主特征向量 $ \mathbf{v}_1(x) $ 给定，对应于在输入端能够引起输出模长产生最大放大的摄动方向。

---

### 3. 随机矩阵极限下的初始化理论与临界条件

在初始化阶段，权重独立服从高斯分布 $ w_{ij}^{(l)} \sim \mathcal{N}(0, \sigma_l^2) $。雅可比矩阵 $ J_L(x) $ 退化为随机矩阵乘积。

根据乘性遍历定理（Multiplicative Ergodic Theorem），当 $ L \to \infty $ 时，李雅普诺夫指数收敛于一个与位置 $ x $ 无关的空间均匀极限。在隐藏层宽度 $ N \to \infty $ 的渐近极限下，其渐近标度关系满足：
$ \lambda_1^{(L)} \sim \log\left( G N \sigma^2 \right) $
其中常数 $ G $ 由激活函数形式决定。
* **临界无偏条件**：为防止多层传播中信号发生指数发散或衰减，临界方差必须设定为：
  $ G N \sigma^2 = 1 \implies \lambda_1^{(L)} \approx 0 $

---

### 4. 反向传播算子的转置对偶性与梯度流动

在随机梯度下降（SGD）算法中，参数更新量表示为：
$ \delta w_{mn}^{(l)} \propto \Delta_m^{(l)} x_n^{(l-1)} $
误差传递向量 $ \Delta^{(l)} $ 满足显式逆向乘积公式（**公式 2**）：
$ \left[ \Delta^{(l)} \right]^\top = \left[ \Delta^{(L)} \right]^\top D^{(L)} W^{(L)} \cdots D^{(l+1)} W^{(l+1)} D^{(l)} \quad \text{—— (2)} $
末层边界误差为 $ \Delta_j^{(L)} = g'\left(b^{(L+1)}\right) \left[ x^{(L+1)} - t(x) \right] g'\left(b_j^{(L)}\right) w_j^{(L+1)} $。

* **算子对偶性**：公式 (2) 中的逆向反传算子与公式 (1) 中的前向切映射算子 $ J_{L:l} $ 呈现互为**转置伴随算子**的结构。
* **谱范数约束**：误差向量的增益直接受控于雅可比矩阵的奇异值 $ \Lambda_1^{(L)} $（即 $ e^{L \lambda_1^{(L)}} $）：
  * 当 $ \lambda_1^{(L)} < 0 $ 时，算子范数收缩，$ \Delta^{(l)} $ 呈指数衰减，引发梯度消失；
  * 当 $ \lambda_1^{(L)} \gg 0 $ 时，反向误差被指数级放大，引发参数更新发散。

---

### 5. 标度律推导与向懒惰学习（Lazy Learning）相变的临界解

训练后，FTLE 场 $ \lambda_1^{(L)}(x) $ 在输入空间发展出强烈的空间不均匀性。论文推导了两组核心标度方程：

1. **决策边界区域的局部 FTLE 均值 $ \langle \lambda_1^{(L)} \rangle_d $**：
   由于网络必须使相距 $ |\delta x^{(0)}| $ 的决策边界两侧输入在输出层产生 $ O(1) $ 级的跃变（$ \delta x^{(L+1)} \sim 1 $），故随着深度 $ L $ 增加，边界处累积 FTLE 趋向饱和常数：
   $ L \langle \lambda_1^{(L)}(x) \rangle_d \to C_d \quad (\text{与 } N \text{ 无关}) $

2. **远离边界的背景区域局部 FTLE 均值 $ \langle \lambda_1^{(L)} \rangle_c $**：
   背景敏感度随隐藏层神经元数 $ N $ 呈对数标度增长：
   $ L \langle \lambda_1^{(L)}(x) \rangle_c \approx -C_c L + \log N \quad (C_c > 0) $

3. **相变临界宽度 $ N_c $ 的显式解**：
   脊线对比度消失的相变临界点由边界均值与背景均值的相等条件确定：
   $ \langle \lambda_1^{(L)}(x) \rangle_c \approx \langle \lambda_1^{(L)}(x) \rangle_d \implies -C_c L + \log N_c \approx C_d $
   解得临界网络宽度 $ N_c $ 对网络深度 $ L $ 呈**指数依赖关系**：
   $ N_c \sim \exp\left( C_d + C_c L \right) $
   当 $ N > N_c $ 时，空间方差 $ \text{Var}[\lambda_1^{(L)}(x)] \to 0 $，高维切映射趋于空间均匀平坦，系统进入隐藏层参数无需调整的随机嵌入 / 懒惰学习（Lazy Learning）机制。

---

### 6. 预测不确定性的后验分布熵

对于分类输出，将输出概率化后，利用网络集成平均预测向量 $ \langle x_i^{(L+1)} \rangle $ 计算后验预测分布的香农熵 $ H $：
$ H = -\sum_{i} \langle x_i^{(L+1)} \rangle \log \langle x_i^{(L+1)} \rangle $
理论上，高 FTLE 对应于局部李雅普诺夫指数极值，使得微小输入扰动直接破坏分类确定性，从而在数学上导出 $ H(x) $ 与 $ \lambda_1^{(L)}(x) $ 之间的正单调相关性。