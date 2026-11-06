在当前选中的论文 **《Mutual information, neural networks and the renormalization group》**（发表于 *Nature Physics*）中，正文共包含 **5 幅核心图像（Fig. 1 至 Fig. 5）**。以下为您系统梳理各图像的具体内容与物理意义：

---

### **Fig. 1 | RSMI 算法架构与工作流程图（The RSMI algorithm）**
* **a. RSMI 神经网络架构**：
  * 展示了输入空间划分为：小局域“可见区域” $ \mathcal{V} $（灰色深区）、包围可见区域的“缓冲区” $ \mathcal{B} $（黄色区域，用于滤除局域短程关联），以及剩余的环境系统 $ \mathcal{E} $（紫色外层区域）。
  * 隐藏神经元层 $ H $（红色方块）仅通过权重矩阵 $ \lambda_i^j $（红色箭头）与可见区域 $ \mathcal{V} $ 直接耦合。
  * 训练目标为优化这些权重，使得隐藏变量 $ H $ 与环境 $ \mathcal{E} $ 之间的**实空间互信息（Real-Space Mutual Information, RSMI）** $ I_\Lambda(H:\mathcal{E}) $ 最大化。
* **b. 算法工作流程**：
  * 使用两个受限玻尔兹曼机（RBM）通过对比散度（Contrastive Divergence, CD）算法分别学习联合概率分布 $ P(\mathcal{V}, \mathcal{E}) $ 和边际分布 $ P(\mathcal{V}) $，其训练参数分别记为 $ \Theta(\mathcal{V}, \mathcal{E}) $ 和 $ \Theta(\mathcal{V}) $。
  * 这两组参数作为主 RSMI 网络的输入，主网络通过随机梯度上升法最大化互信息 $ I_\Lambda $，最终求解出条件分布 $ P_\Lambda(H \mid \mathcal{V}) $ 的权重 $ \lambda_i^j $，从而提取出系统的重整化群“相关自由度”。

---

### **Fig. 2 | 在 Ising 模型上训练的 RSMI 网络权重可视化（The weights of the RSMI network trained on the Ising model）**
展示了可见区域为 $ 2 \times 2 $ 个自旋（共 4 个自旋）时训练得到的网络权重矩阵：
* **a. 单个隐藏神经元（$ N_h = 1 $）**：
  * 该隐藏神经元以均等的权重与 $ 2 \times 2 $ 的 4 个自旋耦合，隐藏单元的状态完全由区域内的平均磁化强度决定。
  * **物理结论**：神经网络在无任何物理先验知识的情况下，**自主重新发现了凝聚态物理中著名的卡达诺夫块自旋（Kadanoff block spins）粗粒化方案**。
* **b. 四个隐藏神经元（$ N_h = 4 $）**：
  * 作为合理性校验（Sanity check），当分配 4 个隐藏神经元来表示 4 个可见自旋时，每个隐藏神经元各自单独追踪并耦合到一个原始自旋上，未发生粗粒化压缩。

---

### **Fig. 3 | 二聚体模型（The dimer model）与电场映射示意**
* **a. 两种典型的二聚体构型（样本数据）**：
  * 蓝色椭圆表示晶格边上的二聚体，分别对应具有宏观垂直电场 $ E_y $ 和水平电场 $ E_x $ 的构型。
  * 晶格顶点与面心之间绘制的粉紫色波浪线表示人工添加的**短程自旋对**；这些自旋对与二聚体完全解耦，构成纯粹的**局域无关噪声（Irrelevant noise）**，用于检验算法抗噪能力。
* **b. 二聚体构型到局域电场的映射**：
  * 左图交错排列（Staggered）的二聚体构型映射为非零平均垂直电场（$ \langle E_y \rangle \neq 0 $）。
  * 右图柱状排列（Columnar）的二聚体构型则映射为平均电场为零（$ \langle E_x \rangle = \langle E_y \rangle = 0 $）的状态。

---

### **Fig. 4 | 在二聚体模型数据上训练的 RSMI 网络权重（The weights of the RSMI network trained on dimer model data）**
展示网络对 $ 8 \times 8 $ 可见区域提取二聚体模型特征时的权重矩阵热图：
* **a. 两个隐藏神经元（$ N_h = 2 $）**：
  * 两个神经元的权重模式分别提取出均匀垂直电场 $ E_y $ 以及叠加电场 $ E_x + E_y $。大负权重（深蓝）与大正权重（亮黄）分别捕捉局域电场的方向交替。
* **b. 四个隐藏神经元（$ N_h = 4 $）**：
  * 四个滤波器分别对应局域电场分量及其不同线性叠加 $ E_x + E_y $ 或 $ E_x - E_y $。
* **抗噪鲁棒性验证**：在放置人工噪声自旋对的格点位置，网络学到的权重全部归零（呈现浅绿色的背景色），证明算法能自动识别并滤除与长程宏观物理无关的短程高频噪声。

---

### **Fig. 5 | 二维 Ising 模型的重整化群流动图（RG flow for the 2D Ising model）**
* **坐标轴定义**：
  * **横坐标**：有效温度 $ T / T_c $（以真实临界温度 $ T_c $ 为单位）。
  * **纵坐标**：RG 迭代步数（即相关长度的收缩对数 $ \log_2(\xi_{128} / \xi) $）。
* **流动曲线与物理结论**：
  * 初始温度低于临界点（$ T < T_c $）的系统（蓝紫色曲线）在迭代 coarse-graining 下流向更低的有效温度（有序铁磁相，Ferromagnet）。
  * 初始温度高于临界点（$ T > T_c $）的系统（红橙色曲线）随 RG 步骤流向更高有效温度（无序顺磁相，Paramagnet）。
  * **定量提取物理量**：仅利用流线的分流发散点，算法识别出临界温度 $ T_c $ 的误差小于 1%；通过有限尺寸数据崩塌（Data collapse），提取出关联长度临界指数 $ \nu \approx 1.0 \pm 0.15 $，与二维 Ising 模型的精确解析解 $ \nu = 1 $ 高度吻合。