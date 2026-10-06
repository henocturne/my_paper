脱离具体的生物学或流行病学背景，该论文在数学本质上建立了一类**带有连续性状空间的反应-扩散偏微分方程（Reaction-Diffusion PDE）与全局标量资源约束耦合的动力学框架**。论文的核心数学工作包含**偏微分方程构建、矩动态（Moment Dynamics）推导、早期渐近展开、受控分段系统的混合近似（Hybrid Approximation）以及基于 Lambert W 函数的极值解析求解**。

以下是该论文完整的数学体系与推导过程：

---

### 一、 系统偏微分方程与核心定义

设连续状态变量 $ \lambda \in \mathbb{R} $，$ \rho(\lambda, t) $ 表示 $ t $ 时刻状态空间中的密度分布函数。系统定义了三个全局宏观量：
1. **全域总密度（零阶矩）**：$ i(t) = \int \rho(\lambda, t) d\lambda $
2. **累积消耗量**：$ r(t) = \mu \int_0^t i(t') dt' $（即 $ \frac{dr(t)}{dt} = \mu i(t) $）
3. **全局资源标量**：$ s(t) = 1 - i(t) - r(t) $

系统由如下反应-扩散偏微分方程组控制：
$ \frac{\partial \rho(\lambda, t)}{\partial t} = \underbrace{k \lambda s(t) \rho(\lambda, t)}_{\text{非线性选择项}} - \underbrace{\mu \rho(\lambda, t)}_{\text{常系数衰减项}} + \underbrace{\frac{D}{2} \frac{\partial^2 \rho(\lambda, t)}{\partial \lambda^2}}_{\text{连续扩散项}} \quad $

其中 $ D = \mathcal{D}(\Delta \lambda)^2 $ 为有效扩散系数，在离散网格缩放变换下具有不变性。

同时，定义性状分布的**一阶矩（加权均值）**与**时变有效增益因子**：
$ \bar{\lambda}(t) = \frac{\int \lambda \rho(\lambda, t) d\lambda}{i(t)}, \quad \mathcal{R}_0(t) = \frac{k \bar{\lambda}(t)}{\mu} \quad $

---

### 二、 复制子-突变子映射与矩动态推导

#### 1. 连续复制子-突变子方程映射
引入归一化概率密度 $ x(\lambda, t) = \frac{\rho(\lambda, t)}{i(t)} $（满足 $ \int x d\lambda = 1 $）。对其求时间导数，并将 $ \frac{di}{dt} = (k s(t) \bar{\lambda}(t) - \mu) i(t) $ 代入，可严格导出：
$ \frac{\partial x(\lambda, t)}{\partial t} = k s(t) \left( \lambda - \bar{\lambda}(t) \right) x(\lambda, t) + \frac{D}{2} \frac{\partial^2 x(\lambda, t)}{\partial \lambda^2} \quad $
此方程结构完全等价于带有时间依赖平均场选择项 $ k s(t)(\lambda - \bar{\lambda}) $ 与扩散项 $ \frac{D}{2}\partial_{\lambda\lambda} x $ 的**连续复制子-突变子方程（Replicator-Mutator Equation）**。

#### 2. 一阶矩（均值）的演化方程
对一阶矩 $ \bar{\lambda}(t) $ 求导，衰减项 $ \mu $ 在分母与分子中完全抵消。在无通量边界或对称分布假设下，扩散项对一阶矩的直接贡献为零，导出均值变化率仅正比于分布的**二阶中心矩（方差）**：
$ \frac{d\bar{\lambda}(t)}{dt} = k s(t) \operatorname{Var}(\lambda; t) \quad $
其中 $ \operatorname{Var}(\lambda; t) = \frac{\int \lambda^2 \rho(\lambda, t) d\lambda}{i(t)} - \bar{\lambda}(t)^2 $。

#### 3. 方差的扩散驱动增长与闭合
对方差 $ \operatorname{Var}(\lambda) $ 求导，其演化可分解为扩散贡献与选择贡献（对应三阶中心矩 $ \langle (\lambda-\bar{\lambda})^3 \rangle $）。通过二次分部积分与边界绝热假设，导出一个纯扩散项的常数贡献：
$ \left.\frac{d \operatorname{Var}(\lambda)}{dt}\right|_{\text{diff}} \approx D \quad $
在尖锐初始条件下，高阶中心矩可忽略（高斯近似下三阶矩为 0），积分得到方差的线性增长闭合表达：
$ \operatorname{Var}(\lambda; t) \approx D t \quad $

---

### 三、 早期渐近展开与超指数增长

在系统演化早期（$ t \to 0 $），资源消耗微弱，可设 $ s(t) \approx 1 $。

1. **一阶矩的二次方演化**：
   将 $ \operatorname{Var}(\lambda) \approx D t $ 代入均值方程积分得：
   $ \bar{\lambda}(t)\big|_{t\to 0} = \lambda_0 + \frac{1}{2} k D t^2 \quad $

2. **全域总密度的超指数显式解**：
   将 $ \bar{\lambda}(t) $ 代入总密度对数微分方程 $ \frac{d \ln i(t)}{dt} = k \bar{\lambda}(t) - \mu = \mu(\mathcal{R}_0 - 1) + \frac{1}{2} k^2 D t^2 $，积分得到早期演化显式解：
   $ i(t)\big|_{t\to 0} = i_0 \exp\left[ \mu(\mathcal{R}_0 - 1) t + \frac{k^2 D}{6} t^3 \right] \quad $
   **数学结论**：扩散项 $ D $ 在对数项中引入了立方时间项 $ t^3 $，导致系统总密度呈现出超越经典单指数的**超指数（Superexponential）早期增长**。

---

### 四、 参数缩放控制与混合近似框架

#### 1. 参数缩放的结构因子 $ \alpha $
引入有限时间窗口 $ t \in [0, \tau] $ 内的比例缩放因子 $ \epsilon \in (0, 1) $。不同参数缩放对矩动态的影响不同：
* **作用于选择系数**（如 $ k \to \epsilon k $ 或 $ \lambda \to \epsilon \lambda $）：选择项被缩放，设结构因子 $ \alpha = \epsilon $。
* **作用于常数衰减率**（如 $ \mu \to \mu / \epsilon $）：由于衰减项在 $ \bar{\lambda} $ 的求导中抵消，不影响选择项演化，设结构因子 $ \alpha = 1 $。

受控区间内的渐近解写为统一形式：
$ \bar{\lambda}(t, \epsilon) = \lambda_0 + \frac{1}{2} \alpha k D t^2 \quad $
$ i(t, \epsilon) = i_0 \exp\left[ \frac{\mu \alpha}{\epsilon} (\epsilon \mathcal{R}_0 - 1) t + \frac{\alpha^2 k^2}{6} D t^3 \right] \quad $

#### 2. 混合近似（Hybrid Approximation）
假设系统在 $ t = \tau $ 时恢复无控制状态。将 $ t = \tau $ 时的系统状态 $ s(\tau), i(\tau), r(\tau)) $ 以及有效增益 $ \mathcal{R}_0(\tau) = \frac{k \bar{\lambda}(\tau)}{\mu} $ 作为无受控系统的初始条件。无受控阶段系统的最大密度极值表达式为：
$ i_{\max}(\tau) \approx 1 - r(\tau) - \frac{1}{\mathcal{R}_0(\tau)} \left[ 1 + \ln\left( \mathcal{R}_0(\tau) s(\tau) \right) \right] \quad $

---

### 五、 极值响应与 Lambert W 函数解析闭合解

#### 1. 导数分析与竞争机制
对极值 $ i_{\max} $ 关于窗口长度 $ \tau $ 求导，利用链式法则展开：
$ \frac{d i_{\max}}{d\tau} = -\mu i(\tau) \frac{\alpha (1-\epsilon)}{\epsilon} + \frac{\dot{\mathcal{R}}_0(\tau)}{\mathcal{R}_0(\tau)^2} \ln\left( \mathcal{R}_0(\tau) s(\tau) \right) \quad $
其中 $ \dot{\mathcal{R}}_0(\tau) = \frac{\alpha k^2 D \tau}{\mu} > 0 $。第一项代表因密度消耗带来的**负向抑制项**，第二项代表由一阶矩扩散增加带来的**正向放大项**。

#### 2. 最恶劣窗口长度 $ \tau^\star $ 的解析求解
令 $ \frac{d i_{\max}}{d\tau} = 0 $。在早期近似 $ s(\tau) \approx 1, \mathcal{R}_0(\tau) \approx \mathcal{R}_0, \ln(\mathcal{R}_0 s) \approx \ln \mathcal{R}_0 $ 下，结合 $ i(\tau) $ 的显式解导出超越方程：
$ C D \tau \approx \frac{\mu (1-\epsilon)}{\epsilon} i_0 \exp\left( A \tau + B D \tau^3 \right) \quad $
其中定义常数：
$ A = \frac{\mu \alpha}{\epsilon} (\epsilon \mathcal{R}_0 - 1), \quad B = \frac{\alpha^2 k^2}{6}, \quad C = \frac{k^2 \ln \mathcal{R}_0}{\mu \mathcal{R}_0^2} \quad $

当立方演化项占据主导（$ B D \tau^3 \gg |A \tau| $）时，令 $ x \equiv -3 B D \tau^3 $，超越方程可化为标准的 Lambert 方程形式：
$ x e^x \approx -\frac{3 B \mu^3 (1-\epsilon)^3 i_0^3}{\epsilon^3 C^3 D^2} \quad $

利用 **Lambert W 函数**的负实数分支 $ W_{-1} $，求得极值窗口长度 $ \tau^\star $ 的**闭合解析解**：
$ \tau^\star \approx \left[ -\frac{1}{3 B D} W_{-1}\left( -\frac{3 B \mu^3 (1-\epsilon)^3 i_0^3}{\epsilon^3 C^3 D^2} \right) \right]^{1/3} \quad $

#### 3. 临界扩散强度 $ D_c(\tau) $ 的闭合表达
同理，利用 Lambert W 函数的主分支 $ W_0 $，可导出使 $ \frac{d i_{\max}}{d\tau} > 0 $（即触发极值反转）的临界扩散系数 $ D_c(\tau) $ 的闭合解析解：
$ D_c(\tau) = -\frac{1}{P(\tau)} W_0 \left[ -P(\tau) Q(\tau) \right] \quad $
其中 $ P(\tau) = \frac{\alpha^2 k^2 \tau^3}{6} $，$ Q(\tau) = \frac{\mu^2 (1-\epsilon) \mathcal{R}_0^2}{\epsilon k^2 \tau \ln \mathcal{R}_0} i_0 e^{\frac{\mu \alpha}{\epsilon}(\epsilon \mathcal{R}_0 - 1)\tau} $。