在论文《**Mutual information, neural networks and the renormalization group**》（*Nature Physics*, 2018）中，作者剥离具体物理模型的细节，将重整化群（RG）的“粗粒化”（Coarse-graining）和“相关自由度提取”严格抽象为一个**基于信息瓶颈（Information Bottleneck）与实空间互信息最大化（RSMI）的概率推断与变分优化问题**。

从纯数学方程、统计力学形式化和理论推导的角度，其核心工作可系统化表述如下：

---

### 一、 概率空间形式化与空间区域划分

设离散随机场系统由微观局域自由度构型 $ X = \{x_1, \dots, x_N\} \in \Omega_X $ 构成，其平衡态服从未知的玻尔兹曼概率测度 $ P(X) \propto e^{-\beta \mathcal{H}(X)} $。

在实空间中引入空间划分算子，将总自由度集 $ X $ 分解为三个互不相交的子空间：
$ X = \mathcal{V} \cup \mathcal{B} \cup \mathcal{E} $
* **$ \mathcal{V} = \{v_i\} $（可见域 / Visible area）**：执行粗粒化的局部紧凑几何区域。
* **$ \mathcal{B} $（缓冲隔离带 / Buffer zone）**：空间上紧邻并包围 $ \mathcal{V} $ 的过渡区域，其几何宽度大于系统的局域短程关联截断尺度，用于在测度中滤除局域平庸短程相关。
* **$ \mathcal{E} = \{e_i\} $（外部环境 / Environment）**：代表距 $ \mathcal{V} $ 渐近远离的宏观背景系统。

引入粗粒化隐随机变量 $ H = \{h_j\} $，目标是构建从微观局域构型 $ \mathcal{V} $ 到宏观粗粒化表征 $ H $ 的条件转移概率测度 $ P_\Lambda(H \mid \mathcal{V}) $，其中 $ \Lambda $ 为参数空间。

---

### 二、 优化目标：实空间互信息（RSMI）泛函与马尔可夫链

系统的因果生成机制构成严格的**局部马尔可夫链**：
$ \mathcal{E} \longleftrightarrow \mathcal{V} \longleftrightarrow H $
即给定局域构型 $ \mathcal{V} $ 时，粗粒化变量 $ H $ 条件独立于外部环境 $ \mathcal{E} $。

联合概率分布与隐变量的边际概率分布在测度变换下可因式分解为：
$ P_\Lambda(\mathcal{E}, H) = \sum_{\mathcal{V}} P(\mathcal{V}, \mathcal{E}) P_\Lambda(H \mid \mathcal{V}) $
$ P_\Lambda(H) = \sum_{\mathcal{V}} P(\mathcal{V}) P_\Lambda(H \mid \mathcal{V}) $

根据信息论，在保持 $ H $ 的信息熵受限（即隐藏单元维度有限）的约束下，**相关物理自由度**被严格定义为最大化其与远端环境 $ \mathcal{E} $ 的香农互信息（Mutual Information）的映射参数 $ \Lambda^* $：
$ \Lambda^* = \arg\max_\Lambda I_\Lambda(H : \mathcal{E}) $

实空间互信息泛函的显式积分表达为：
$ I_\Lambda(H : \mathcal{E}) = \sum_{H, \mathcal{E}} P_\Lambda(\mathcal{E}, H) \log \left( \frac{P_\Lambda(\mathcal{E}, H)}{P_\Lambda(H) P(\mathcal{E})} \right) = \mathbb{E}_{P_\Lambda(\mathcal{E}, H)} \left[ \log \frac{P_\Lambda(\mathcal{E}, H)}{P_\Lambda(H) P(\mathcal{E})} \right] $

---

### 三、 神经网络参数化与自由能解析表征

由于配分函数不可积以及环境状态空间 $ |\Omega_\mathcal{E}| $ 随系统尺寸呈指数爆炸，直接对环境状态求和在计算上是不可行的（intractable）。作者利用两台预训练受限玻尔兹曼机（RBM）的自由能结构，实现对 $ P(\mathcal{V}, \mathcal{E}) $ 和 $ P(\mathcal{V}) $ 的解析边际化：

#### 1. RBM 能量函数与边缘分布
对于带有可见层 $ V $、隐藏层 $ K $ 的能量二部图，能量泛函形式化为：
$ E_\Theta(V, K) = -\sum_j b_j k_j - \sum_i a_i v_i - \sum_{i,j} v_i \theta_{ij} k_j $
对隐藏二值单元 $ K \in \{0, 1\}^M $ 解析求和边缘化，得到可见层构型的无条件概率密度：
$ P_\Theta(V) = \frac{1}{Z_\Theta} \sum_K e^{-E_\Theta(V, K)} = \frac{1}{Z_\Theta} e^{-\mathcal{F}_\Theta(V)} $
其中自由能泛函 $ \mathcal{F}_\Theta(V) $ 具有解析闭式解：
$ \mathcal{F}_\Theta(V) = -\sum_i a_i v_i - \sum_j \log \left( 1 + e^{b_j + \sum_i v_i \theta_{ij}} \right) $

利用对比散度（Contrastive Divergence, CD）算法优化两组 RBM 参数：
* $ \Theta(\mathcal{V}, \mathcal{E}) $：逼近联合概率分布 $ P(\mathcal{V}, \mathcal{E}) $；
* $ \Theta(\mathcal{V}) $：逼近边际概率分布 $ P(\mathcal{V}) $。

#### 2. RSMI 转移算子参数化
主网络的粗粒化映射算子采用广义玻尔兹曼/逻辑形式参数化，参数集 $ \Lambda = \{a_i, b_j, \lambda_i^j\} $：
$ P_\Lambda(h_j = 1 \mid \mathcal{V}) = \sigma\left( b_j + \sum_i \lambda_i^j v_i \right) = \frac{1}{1 + e^{-\left(b_j + \sum_i \lambda_i^j v_i\right)}} $
其中矩阵元 $ \lambda_i^j $ 对应连续空间粗粒化中的投影核函数 / 线性投影算子。

---

### 四、 梯度推导与变分优化算法

为了通过随机梯度上升法最大化 $ I_\Lambda(H : \mathcal{E}) $，需要推导目标泛函对投影权重 $ \lambda_i^j $ 的泛函导数：

展开互信息的导数链式法则：
$ \frac{\partial I_\Lambda(H : \mathcal{E})}{\partial \lambda_i^j} = \sum_{H, \mathcal{E}} \left( \frac{\partial P_\Lambda(\mathcal{E}, H)}{\partial \lambda_i^j} \log \frac{P_\Lambda(\mathcal{E}, H)}{P_\Lambda(H) P(\mathcal{E})} + P_\Lambda(\mathcal{E}, H) \left[ \frac{\frac{\partial P_\Lambda(\mathcal{E}, H)}{\partial \lambda_i^j}}{P_\Lambda(\mathcal{E}, H)} - \frac{\frac{\partial P_\Lambda(H)}{\partial \lambda_i^j}}{P_\Lambda(H)} \right] \right) $

注意到项：
$ \sum_{H, \mathcal{E}} \frac{\partial P_\Lambda(\mathcal{E}, H)}{\partial \lambda_i^j} = \frac{\partial}{\partial \lambda_i^j} \sum_{H, \mathcal{E}} P_\Lambda(\mathcal{E}, H) = \frac{\partial (1)}{\partial \lambda_i^j} = 0 $
后半部分的线性修正项严格恒等于 0，因此梯度仅取决于测度导数与对数概率比（Log-Likelihood Ratio）的加权内积：
$ \frac{\partial I_\Lambda(H : \mathcal{E})}{\partial \lambda_i^j} = \sum_{H, \mathcal{E}} \left( \sum_{\mathcal{V}} P(\mathcal{V}, \mathcal{E}) \frac{\partial P_\Lambda(H \mid \mathcal{V})}{\partial \lambda_i^j} \right) \log \left( \frac{P_\Lambda(\mathcal{E}, H)}{P_\Lambda(H) P(\mathcal{E})} \right) $

* **数值采样估计**：利用蒙特卡洛配置样本评估期望值，将联合测度 $ P(\mathcal{V}, \mathcal{E}) $ 与边际测度项分别转化为由预训练自由能 $ \mathcal{F}_{\Theta(\mathcal{V}, \mathcal{E})} $ 和 $ \mathcal{F}_{\Theta(\mathcal{V})} $ 导出的无偏局部估计量；
* **参数演化**：采用随机梯度迭代步进：
  $ \Lambda_{t+1} = \Lambda_t + \eta \nabla_\Lambda I_\Lambda(H : \mathcal{E}) $
  促使连接权重的谱结构在鞍点收敛，直接提取出流形上的主特征模式。

---

### 五、 粗粒化半群迭代与标度律提取

当求得局域最优映射算子 $ P_{\Lambda^*}(H \mid \mathcal{V}) $ 后，系统完成一步离散半群重整化映射：
$ \mathbb{R}_b : P_k(X) \longrightarrow P_{k+1}(X') $
其中空间线度按照空间缩放因子 $ b $ 收缩（如 $ L \to L/b $）。

#### 1. 有效热力学参量的自洽重构
在迭代第 $ k $ 步，利用粗粒化构型 $ H^{(k)} $ 重新训练无偏统计模型，由两点关联张量或隐层有效自由能导出其有效偶合常数（或有效无量纲参数 $ \tau \equiv |T - T_c| / T_c $）：
$ \mathcal{G}^{(k)}(r) = \langle h_x^{(k)} h_{x+r}^{(k)} \rangle - \langle h_x^{(k)} \rangle \langle h_{x+r}^{(k)} \rangle $

#### 2. 有限尺寸标度假设（Finite-Size Scaling）与特征指数解耦
在不动点（Fixed Point）邻近区域，物理关联长度 $ \xi $ 遵循通用齐次标度方程：
$ \xi(\tau) \propto \tau^{-\nu} $
由于离散 RG 步骤 $ n $ 对应物理关联长度的对数收缩算子：
$ n = \log_b \left( \frac{\xi_0}{\xi_n} \right) $
在有效参数平面绘制 RG 轨线流向并执行有限尺寸数据崩塌（Data collapse），对数流动方程的渐近导数直接确定了关联长度临界指数 $ \nu $：
$ \frac{d \log \xi}{d n} = -\log b \implies \nu \approx -\left( \left. \frac{d \log \tau}{d n} \right|_{T_c} \right)^{-1} $
由此建立了一条**完全摆脱模型具体微观细节，完全从无监督互信息动力学中闭式解析提取重整化群临界指数**的理论闭环。