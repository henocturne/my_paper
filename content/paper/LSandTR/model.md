抛开应用场景与物理直观类比，论文的核心工作可形式化为一套**高维非凸优化解流形的拓扑临界性、微分动力学标度渐近性、以及再生核在特征演化下的泛化界分析**。以下完全从纯数学定义、方程与理论推导展开陈述。

---

### 一、 形式化定义与优化动力学系统

#### 1. 网络映射与参数化系统
考虑 $ L $ 层前馈映射 $ \tilde{f}_\theta: \mathbb{R}^d \to \mathbb{R} $，中间层宽度均为 $ h $，参数集合 $ \theta = \{W^{(l)}, B^{(l)}\}_{l=1}^{L+1} $：
$ a^{(1)} = \frac{1}{\sqrt{d}} W^{(1)} \mathbf{x} + B^{(1)}, \quad a^{(l)} = \frac{1}{\sqrt{h}} W^{(l)} \sigma(a^{(l-1)}) + B^{(l)} \quad (l=2,\dots,L+1) \quad $
其中 $ \sigma $ 为逐元素非线性激活函数（满足非齐次或分段齐次性，如 ReLU），$ W_{\alpha\beta}^{(l)} \sim \mathcal{N}(0, 1) $ 采用 LeCun 缩放初始化。总参数维度为 $ N \sim L h^2 $。

引入标度调控参数 $ \alpha > 0 $ 构建预测函数：
$ f_\theta(\mathbf{x}) \equiv \alpha \left[ \tilde{f}_\theta(\mathbf{x}) - \tilde{f}_{\theta_0}(\mathbf{x}) \right], \quad \theta_0 = \theta(t=0) \quad $
无量纲重标度初始化参数定义为 $ \tilde{\alpha} \equiv \alpha \sqrt{h} $。

#### 2. 损失泛函与梯度流微分方程
给定 $ P $ 个样本点 $ \{(\mathbf{x}_\mu, y_\mu)\}_{\mu=1}^P $（$ y_\mu \in \{-1, +1\} $），经验风险定义为：
$ \mathcal{L}(\theta) = \frac{1}{P} \sum_{\mu=1}^P \ell(y_\mu f_\theta(\mathbf{x}_\mu)) \quad $
损失函数 $ \ell $ 为二次 Hinge 损失：$ \ell(z) = \frac{1}{2} \max(0, 1-z)^2 = \frac{1}{2} \Delta_\mu^2 \mathbb{I}(\Delta_\mu > 0) $，其中未满足约束（即未达到单位间隔裕度）定义为：
$ \Delta_\mu(\theta) \equiv 1 - y_\mu f_\theta(\mathbf{x}_\mu) \quad $
定义未满足样本索引子集为 $ m(\theta) = \{\mu \in \{1,\dots,P\} : \Delta_\mu(\theta) > 0\} $，基数为 $ N_\Delta = |m(\theta)| $。经验损失化简为约束平方和：
$ \mathcal{L}(\theta) = \frac{1}{2P} \sum_{\mu \in m(\theta)} \Delta_\mu(\theta)^2 \quad $
参数沿负梯度流连续演化：
$ \frac{d\theta}{dt} = -\nabla_\theta \mathcal{L}(\theta) = \frac{1}{P} \sum_{\mu \in m(\theta)} \Delta_\mu \nabla_\theta (y_\mu f_\theta(\mathbf{x}_\mu)) \quad $

#### 3. 神经切线核（NTK）张量定义
对于任意两点 $ \mathbf{x}, \mathbf{y} $，定义切线核 Gram 算子：
$ \Theta(\theta, \mathbf{x}, \mathbf{y}) \equiv \nabla_\theta \tilde{f}_\theta(\mathbf{x}) \cdot \nabla_\theta \tilde{f}_\theta(\mathbf{y}) \quad $
输出函数值随时间的变化率满足封闭积分微分方程：
$ \frac{d f_\theta(\mathbf{x})}{dt} = \alpha^2 \nabla_\theta \tilde{f}_\theta(\mathbf{x}) \cdot \frac{d\theta}{dt} = \frac{\alpha^2}{P} \sum_{\mu \in m(\theta)} \Delta_\mu(\theta) y_\mu \Theta(\theta, \mathbf{x}, \mathbf{x}_\mu) \quad $

---

### 二、 损失曲面零测度临界相变推导

该部分旨在证明：在欠参数化向过参数化转变的相变点 $ N^* $，为什么局部极小值曲率谱（Hessian 谱）会出现严格孤立的零模 $ \delta $ 测度与正谱隙（Spectral Gap）。

#### 1. 解流形的存在性上界（约束计数）
在极小值处实现零训练损失 $ \mathcal{L}(\theta^*) = 0 $，等价于要求所有 $ \mu \in m $ 处的约束同时满足 $ \Delta_\mu(\theta^*) \le 0 $。
在临界饱和界面处，存在 $ N_\Delta $ 个激活约束 $ \Delta_\mu(\theta) = 0 $。每个独立的光滑标量方程在 $ \mathbb{R}^N $ 中定义一个余维数为 1 的超曲面。
若解流形存在非空交集，自由度 $ N $ 必须不小于独立约束方程数：
$ N \ge N_\Delta \iff \frac{N_\Delta}{N} \le 1 \quad $

#### 2. Hessian 稳定性下界（半正定性条件）
对于损失函数 $ U = \frac{1}{2} \sum_{\mu \in m} \Delta_\mu^2 $，其 Hessian 矩阵 $ H_U = \nabla^2 U \in \mathbb{R}^{N \times N} $ 可严格分解为外积和项与曲率微扰项：
$ H_U = \sum_{\mu \in m} \nabla \Delta_\mu \otimes \nabla \Delta_\mu + \sum_{\mu \in m} \Delta_\mu H_{\Delta_\mu} \equiv H_0 + H_p \quad $
其中：
- $ H_0 = \sum_{\mu \in m} \nabla \Delta_\mu \otimes \nabla \Delta_\mu $ 为 $ N_\Delta $ 个秩-1 半正定矩阵之和，因此 $ \operatorname{rank}(H_0) \le N_\Delta $。其零空间维度满足：
  $ \dim(\ker(H_0)) \ge N - N_\Delta \quad $
- $ H_p = \sum_{\mu \in m} \Delta_\mu H_{\Delta_\mu} $，当趋近临界点时 $ \Delta_\mu \to 0^+ $，$ H_p $ 构成小量扰动算子。

若平衡态为稳定局部极小值，必须满足无负曲率特征方向，即 $ H_U \succeq 0 $（全局半正定）。
设 $ H_p $ 在整个 $ \mathbb{R}^N $ 空间中的负本征值个数为 $ N^- $，由 Weyl 本征值交错定理与极小极大原理（Courant-Fischer 紧致性），$ H_0 $ 的正本征空间必须完全覆盖 $ H_p $ 的负特征空间，否则必在 $ \ker(H_0) $ 内诱导出负本征值：
$ \operatorname{rank}(H_0) \ge N^- \implies N_\Delta \ge N^- \quad $

#### 3. 次等度刚性（Hypostatic Jamming）与谱结构
对于深度神经网络，$ \Delta_\mu = 1 - y_\mu f(\mathbf{x}_\mu) $ 的 Hessian 为 $ H_{\Delta_\mu} = -y_\mu \nabla^2 f(\mathbf{x}_\mu) $。
- 由于 ReLU 等多层网络的内部预激活存在对称旋转与非线性重构，在随机初始化先验下，曲率矩阵 $ \nabla^2 f $ 具有中心对称的实对角本征谱，满足 $ N^- = C_0 N $，其中 $ C_0 \approx 1/2 $（严格小于 1）。
- 结合上下界不等式链：
  $ C_0 N \le N_\Delta \le N \quad $
- **谱的直接推导结果**：由于 $ \operatorname{rank}(H_0) \approx C_0 N < N $，在相变点处，$ H_0 $ 的零空间维度具有宏观尺度 $ \dim(\ker(H_0)) \approx (1 - C_0)N > 0 $。
  这直接证明了：临界点处 Hessian 谱密度 $ \mathcal{D}(\lambda) $ 在 $ \lambda = 0 $ 处包含权重为 $ 1 - C_0 $ 的 **Dirac $ \delta(0) $ 峰**，且在 $ 0, \lambda_{\min}^+) $ 之间严格存在**谱隙（Gap）**，随之连接连续带谱。
- **全局极小值保证**：由于 $ N_\Delta \le P $，满足无坏极小值且存在全局零损失解的参数量下界由常数约束：$ N^*(P) \le P/C_0 \sim \mathcal{O}(P) $。

---

### 三、 临界发散、函数波动与泛化泛函标度律

#### 1. 临界相变点处预测器范数的代数发散（Landau 形式）
将经验未满足间隔 $ \epsilon $ 视为微扰参数，临界参数线展开为：
$ N^*(\epsilon) = N^*(0) + N'^*(0)\epsilon + \mathcal{O}(\epsilon^2) \quad $
当固定参数量 $ N $ 仅略微高于 $ N^*(0) $ 时（$ 0 < N - N^*(0) \ll 1 $），原始单位间隔（$ \epsilon = 1 $）无法严格被包含在解空间内。
网络动力学被迫通过放大全局输出模长 $ \|f_N\| $ 来实现等效几何裕度收缩：
$ \tilde{\epsilon} = \epsilon \frac{N - N^*(0)}{N'^*(0)} \implies \|f_N\| \propto \frac{1}{\tilde{\epsilon}} \propto \left( N - N^*(0) \right)^{-1} \quad $
预测器函数范数 $ \|f_N\| $ 在临界点处产生代数极点发散，导致分类器边界过度扭曲，定量导出了测试误差在临界点的奇异尖峰（双重下降峰）。

#### 2. 过参数化相中的函数涨落衰减（Fluctuation Scaling）
在 $ N > N^* $ 的过参数化区域中，函数解关于初始化随机参数 $ \theta_0 $ 的系综波动被严格量化：
- **Lazy/NTK 机制**：$ \Theta_N $ 矩阵由 $ N $ 个独立偏导向量内积求和构成，根据大数定律与随机矩阵涨落理论：
  $ \|\Theta_N - \langle \Theta_N \rangle\| \sim h^{-1/2} \sim N^{-1/4} \quad $
- **Feature Learning 机制**：单隐层神经元参数经验测度 $ \rho_h = \frac{1}{h}\sum_{i=1}^h \delta_{\theta_i} $ 趋于均场密度 $ \rho $，中心极限定理导致测度波动量阶为 $ \delta\rho \sim h^{-1/2} \sim N^{-1/4} $。
- **预测器波动传递**：在线性化或非线性均场积分算子下，预测函数波动严格承袭初始扰动：
  $ \|f_N - \langle f_N \rangle\| \sim N^{-1/4} \quad $

#### 3. 泛化误差的有限尺寸修正
设测试集上的真实泛化误差泛函为 $ \mathcal{R}(f) = \mathbb{E}_{(\mathbf{x}, y)} [\ell_{\text{test}}(y f(\mathbf{x}))] $。在总体系综均值 $ \langle f_N \rangle $ 附近进行泛函 Taylor 展开：
$ \mathcal{R}(f_N) = \mathcal{R}(\langle f_N \rangle) + \delta \mathcal{R} \cdot (f_N - \langle f_N \rangle) + \frac{1}{2} (f_N - \langle f_N \rangle)^\top \mathcal{H}_{\mathcal{R}} (f_N - \langle f_N \rangle) + \dots $
由于 $ \langle f_N - \langle f_N \rangle \rangle = 0 $，一阶变分在系综均值下消逝，由二阶正定 Fréchet 导数占优：
$ \langle \mathcal{R}(f_N) \rangle - \mathcal{R}(\langle f_N \rangle) \approx \frac{1}{2} \operatorname{Tr}\left( \mathcal{H}_{\mathcal{R}} \operatorname{Cov}(f_N) \right) \sim \mathbb{E}\left[ \|f_N - \langle f_N \rangle\|^2 \right] \sim \left( N^{-1/4} \right)^2 = N^{-1/2} \quad $
- **结论**：过参数化不仅不恶化泛化，反而以 $ N^{-1/2} $ 的标度消除随机初始化方差；当直接计算系综平均 $ \langle f_N \rangle $ 时，方差项被完全滤除，双重下降峰随之恒等消失。

---

### 四、 NTK 与特征学习相边界的微扰渐近推导

考察参数空间 $ h, \alpha) $ 中两种动力学机制的分界渐近线。

#### 1. 预激活值的摄动展开
设重标度损失函数 $ \tilde{\mathcal{L}} \equiv \mathcal{L} / \alpha^2 $，使得梯度流演化时间尺度在 $ \alpha \to \infty $ 时为 $ \mathcal{O}(1) $：
$ \frac{\partial \tilde{\mathcal{L}}}{\partial f} \sim \frac{1}{\alpha^2} \quad $
考虑第 $ l $ 层的标称预激活值 $ a^{(l)} $。由链式法则反向传播，由于顶层权重服从 $ W^{(L+1)} \sim 1/\sqrt{h} $，输出对内部任意中间预激活的灵敏度具有统一标度：
$ \frac{\partial f}{\partial a} \sim \alpha \frac{\partial \tilde{f}}{\partial a} \sim \frac{\alpha}{\sqrt{h}} \quad $

#### 2. 积分位移标度与破缺阈值
在有限时间 $ t \sim \mathcal{O}(1) $ 内，由偏置或权重更新诱导的预激活总位移 $ \Delta a $ 满足一阶积分估计：
$ \Delta a \sim \int_0^t \left( -\frac{\partial \tilde{\mathcal{L}}}{\partial f} \right) \left( \frac{\partial f}{\partial a} \right) dt' \sim t \cdot \left(\frac{1}{\alpha^2}\right) \cdot \left(\frac{\alpha}{\sqrt{h}}\right) \sim \frac{1}{\alpha \sqrt{h}} \quad $
- **线性核机制（Lazy/NTK）**：当 $ \Delta a \ll 1 $ 时，激活函数 $ \sigma(a + \Delta a) \approx \sigma(a) + \sigma'(a)\Delta a $ 保持一阶局部线性，NTK 变分比值满足 $ \|\Delta \Theta\| / \|\Theta(0)\| \ll 1 $。
- **特征学习机制（Feature Learning）**：当 $ \Delta a \sim \mathcal{O}(1) $ 时，非线性项被高阶激发，内部表征发生非平凡重组，$ \|\Delta \Theta\| / \|\Theta(0)\| \ge 1 $。

由此严密确定相分离过渡线（Cross-over line）渐近方程为：
$ \alpha^* \sqrt{h} \sim \mathcal{O}(1) \iff \tilde{\alpha}^* = \text{const} \quad $

---

### 五、 数据流形不变性与特征压缩标度推导（条带模型）

#### 1. 各向异性坐标分解
设输入空间正交分解为 $ \mathbf{x} = (\mathbf{x}_\parallel, \mathbf{x}_\perp) \in \mathbb{R}^d $，目标标签仅依赖于 $ d_\parallel $ 维有效坐标：$ y(\mathbf{x}) = y(\mathbf{x}_\parallel) $，其余 $ d_\perp = d - d_\parallel $ 维为无关特征。

#### 2. 权重演化方程与非对称生长
考虑两层前馈网络，首层权重向量沿信息方向与正交方向分解为 $ \vec{W}_i = (\vec{W}_{i,\parallel}, \vec{W}_{i,\perp}) $。
其连续梯度流方程为：
$ \frac{d \vec{W}_{i,\parallel}}{dt} = \frac{1}{P} \sum_{\mu \in m} \Delta_\mu y_\mu W_i^{(2)} \sigma'(a_i^\mu) \mathbf{x}_{\mu,\parallel} \quad $
$ \frac{d \vec{W}_{i,\perp}}{dt} = \frac{1}{P} \sum_{\mu \in m} \Delta_\mu y_\mu W_i^{(2)} \sigma'(a_i^\mu) \mathbf{x}_{\mu,\perp} \quad $
- 由于标签 $ y_\mu $ 独立于 $ \mathbf{x}_{\mu,\perp} $，在正交子空间中，样本平均漂移为零：$ \mathbb{E}[\Delta_\mu y_\mu \mathbf{x}_{\mu,\perp}] = 0 $。正交权重的生长纯粹受限于有限样本经验测度的方差波动，表现为中心极限定理随机游走：
  $ \left\| \frac{d \vec{W}_{i,\perp}}{dt} \right\| \sim \frac{1}{\sqrt{P}} \quad $
- 相反，沿有效信息方向 $ \mathbf{x}_{\mu,\parallel} $，梯度具有非零投影均值，呈现确定性线性漂移增长：
  $ \left\| \frac{d \vec{W}_{i,\parallel}}{dt} \right\| \sim \mathcal{O}(1) \quad $

#### 3. 几何压缩因子 $ \Lambda $ 与特征压缩定理
积分至收敛时间，两方向的有效权重范数比值产生极端各向异性：
$ \Lambda \equiv \frac{\|\vec{W}_\parallel\|}{\|\vec{W}_\perp\|} \sim \frac{\mathcal{O}(1)}{\mathcal{O}(1/\sqrt{P})} \sim \sqrt{P} \quad $
神经元输出端内积可等价重写为坐标重标度映射：
$ \vec{W} \cdot \mathbf{x} = \vec{W}_\parallel \cdot \mathbf{x}_\parallel + \vec{W}_\perp \cdot \mathbf{x}_\perp = \vec{W}_\parallel \cdot \left( \mathbf{x}_\parallel + \frac{1}{\Lambda} \frac{\vec{W}_\perp}{\|\vec{W}_\parallel\|} \cdot \mathbf{x}_\perp \right) \equiv \vec{W}_\parallel \cdot \hat{\mathbf{x}}_\Lambda \quad $
该变换严格等价于输入数据在正交无信息流形方向被各向异性几何算子压缩了 $ \Lambda \sim \sqrt{P} $ 倍。

#### 4. 泛化误差衰减指数 $ \beta $ 的严格推导
根据积分核算子与静电势格林函数类比展开，在判别界面光滑且支持非零测度下，测试误差随样本量的标度关系 $ \epsilon \sim P^{-\beta} $ 由数据有效距离与界面局域测度积分决定：
- **各向同性线性核（Lazy/NTK）机制**：
  由于核函数未发生各向异性旋转，全空间 $ d $ 维均参与最近邻距离发散，衰减指数严格受制于全维度：
  $ \beta_{\text{Lazy}} = \frac{d}{3d - 2} \quad $
- **特征学习（Feature Learning）机制**：
  正交维度被 $ \Lambda \sim P^{1/2} $ 因子自适应压缩，等效有效体积微分由 $ d^d x \to d^{d_\parallel} x_\parallel \cdot \Lambda^{-d_\perp} d^{d_\perp} x_\perp $ 调控，将维数贡献代数替换后解得修正幂律：
  $ \beta_{\text{Feature}} = \frac{d + \frac{d_\perp}{2}}{3d - 2} \quad $
- **结论**：因为 $ d_\perp \ge 1 $，恒有 $ \beta_{\text{Feature}} > \beta_{\text{Lazy}} $，严格证明了特征学习通过有限样本驱动的自适应各向异性梯度流，实现了有效相空间的维度收缩，从代数结构上克服了高维下 $ 1/d $ 泛化率的下确界限制。