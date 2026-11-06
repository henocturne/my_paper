在当前选中的论文 **《Local kernel renormalization as a mechanism for feature learning in overparametrized convolutional neural networks》**（*Nature Communications*, 2025）中，正文共包含 **3 幅核心图像（Fig. 1 至 Fig. 3）**。以下为您系统梳理各图的具体内容与核心结论：

---

### **Fig. 1 | 全连接网络与卷积神经网络中的全局核与局部核对比示意图（Global and local kernels in FC and convolutional one hidden layer networks）**
* **图像布局与构成**：
  * **左侧（单隐层全连接网络 1HL FCN）**：展示了标准的 NNGP 核矩阵 $ K_{\mu\nu} $。其行与列仅对应不同的训练样本模式 $ \mu, \nu) $（如飞机与汽车图像）。在比例热力学极限下，FCN 只能通过训练数据微调**单一标量参数 $ Q $**，对整个核矩阵进行全局等比例缩放（Global kernel renormalization）。
  * **右侧（单隐层卷积网络 1HL CNN）**：展示了带有两个额外空间切块索引 $ i, j) $ 的**局部核矩阵 $ K_{\mu\nu}^{ij} $**。图中采用多重索引记号 $ K_{(\mu,i),(\nu,j)} $ 将其展开显示为包含图像不同局部区域相互作用的大矩阵。
* **实验参数与计算细节**：
  * 使用降采样至 $ N_0 = 784 $ 的灰度化 CIFAR-10 图像子集（$ P = 10 $ 张图像）进行实证计算。
  * 局部核采用二维卷积评估，卷积核尺寸为 $ M = 14 $，步长为 $ S = 14 $（无重叠滤波器）。
* **核心物理结论**：
  * FCN 的全局核仅能捕捉样本之间的整体相关性，无法进行细粒度的空间特征选择；
  * CNN 由于具备局部连接与权重共享，能够自适应优化一个完整的**特征参数矩阵 $ Q_{ij} $**，以数据驱动的方式对局部切块 $ i $ 和 $ j $ 之间的相关性权重进行精细调控（即局部核重整化 Local kernel renormalization）。

---

### **Fig. 2 | 局部核重整化在泛化性能上超越最优无限宽核（Local kernel renormalization can in principle outperform the best infinite-width generalization performance）**
* **坐标轴与曲线**：
  * **横坐标**：训练样本数量 $ P $。
  * **纵坐标**：预测的测试集泛化偏差（Generalization bias，在偏差主导机制下）。
  * **紫色圆点（Dots）**：最优无限宽核的泛化性能，对应于无重整化的平凡解 $ Q_{\text{IW}} = \mathbf{1} $。针对每个样本量 $ P $，在超参数空间进行了网格搜索以寻找最优温度 $ T^* $ 和读出层先验 $ \lambda_1^* $（搜索范围 $ \lambda_1 \in [0.1, 10], T \in [0.001, 0.02] $）。
  * **橙色方块（Squares）与插图矩阵**：在保持最优无限宽超参数不变的条件下，允许 $ Q \neq \mathbf{1} $（通过基于梯度的局部核重整化优化流程求解特征矩阵 $ Q_{ij} $，在 $ P=500 $ 和 $ P=1000 $ 处展示）。插图直观展示了优化得到的非平庸矩阵 $ Q_{ij} $ 的热图。
* **任务设置**：基于灰度化 CIFAR-10 数据集中的“汽车（cars）”与“飞机（planes）”构建的二分类监督学习任务。
* **核心物理结论**：
  * 在偏差主导的机制下，局部核重整化通过引入非平庸的自适应特征矩阵 $ Q \neq \mathbf{1} $，**成功突破了由最优无限宽 NNGP 核界定的泛化误差下界**，理论证实了有限通道 CNN 优于无限宽核的机制。

---

### **Fig. 3 | 全连接网络与卷积网络内部表征变化的有限尺寸标度分析（Predicting the effect of global and local kernel renormalization on the internal representations of FC and CNNs. A finite-size scaling analysis）**
系统检验了训练前后网络内部表征相似度矩阵变化量 $ \Delta K_{\mu\nu} \equiv \langle \mathcal{O}_{\mu\nu} \rangle - K_{\mu\nu} $ 的缩放行为（在固定比例比值 $ \alpha_1 = P/N_1 = 1 $ 下增大 $ P $ 和 $ N_1 $）：

* **(a, b) 单隐层全连接网络（1HL FCN）**：
  * **(a) 0-1 类别子块 $ \Delta K_{\mu\nu}^{\text{FC}}\vert_{01} $ 的方差**：上方子图显示采样矩阵热图，中下方显示其经验分布的方差随 $ N_1 $ 增加以 $ \sim 1/N_1^2 $ 的速率迅速衰减并向零收缩。
  * **(b) 1-1 类别子块 $ \Delta K_{\mu\nu}^{\text{FC}}\vert_{11} $ 的均值漂移**：显示其经验分布的直方图在保持狭窄的同时，以 $ \sim 1/N_1 $ 的速率向零漂移。
  * **结论**：表明在全连接网络中，内部表征在训练过程中的改变纯粹是一种**有限尺寸效应（Finite-size effect）**，在比例热力学极限下完全消失。
* **(c, d) 单隐层卷积网络（1HL CNN，采用 1D 卷积）**：
  * **(c, d) 0-1 与 1-1 类别子块的分布行为**：与 FCN 形成鲜明对比，CNN 内部表征变化量 $ \Delta K_{\mu\nu}^{\text{CNN}} $ 的矩阵元素方差在 $ N_c $ 和 $ P $ 增大（固定 $ \alpha_c = 1 $）时**并未衰减归零**，矩阵热图中清晰保留了显著的非零模式。
  * **结论**：定量印证了理论预测——CNN 中由局部核重整化引入的双重求和项使得表征演化保持有限阶 $ \Delta K^{\text{CNN}} \propto \mathcal{O}(P/N_1) $，证实卷积网络在热力学极限下依然发生**真实的特征学习（Genuine feature learning）**。