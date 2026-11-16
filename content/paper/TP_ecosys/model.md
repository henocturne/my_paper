从**动力系统理论（Dynamical Systems Theory）**、**随机微分方程（SDEs）**以及**泛函分析与转移算子理论（Transfer Operator Theory）**的角度，该论文建立了一套将临界点（Tipping Points）由经典的低维确定性分叉拓展到非自治、高维非梯度及随机网络系统的完整数学与理论推导框架：

---

### **1. 动力系统结构与势函数/准势能（Quasi-potential）推广**

#### **(1) 梯度自治系统与分叉（B-tipping）**
论文首先定义一维及高维梯度动力系统：
$ \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \nu) = -\nabla V(\mathbf{x}, \nu), \quad \mathbf{x} \in \mathbb{R}^N $
其中 $ \nu $ 为控制参数，$ V(\mathbf{x}, \nu) $ 为势函数。鞍结分叉（Saddle-node bifurcation）发生在平衡点局部极小值与鞍点相互碰撞湮灭的临界参数 $ \nu = h $ 处：
$ \det(D\mathbf{f}(\mathbf{x}^*, h)) = 0 $
此时该局域吸引子消失，系统失去渐近稳定性，状态轨线被释放至其他吸引盆（Basin of attraction）。

#### **(2) 高维非梯度与混沌边界危机**
对于非梯度系统（不存在全局势函数 $ V $），论文将其推广为**准势能（Quasi-potential）** $ \Phi(\mathbf{x}, \nu) $。在高维多稳态或混沌吸引子情形下，B-tipping 在数学上表现为**吸引子边界危机（Basin crisis）**：
* 状态所在的参考吸引子与吸引盆边界上的**边缘态（Edge state）**发生接触。
* 边缘态是位于吸引盆分界面内部的鞍型不变集（Dynamical saddle），具有一维横截不稳定方向。在临界点处，两者的融合将产生**幽灵态（Ghost state）**，相空间局域流速在此处极度缓慢，诱发长暂态（Long transients）。

---

### **2. 非自治动力系统与速率诱导倾覆（R-tipping）**

当参数随时间演化 $ \nu = \nu(t) $ 时，系统退化为非自治常微分方程：
$ \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \nu(t)) $
设参数在时间区间 $ \Delta t $ 内变化率平均为 $ R = |\Delta \nu / \Delta t| $。

* **拉回吸引子（Pullback Attractor）与分叉**：
  为描述非自治系统的时变吸引集合，论文引入了拉回吸引子理论：即在给定的固定观测时间 $ t $，从极久远的过去（$ t_0 \to -\infty $）演化而来的时变紧集。
* **临界速率判据**：
  当参数的时间变化率 $ R $ 超出临界速率 $ R_{cr} $ 时，时变势能景观的移动速度超过了系统状态轨线的自弛豫时间尺度（Relaxation timescale），即使参数值在任何瞬时均未跨越确定性分叉阈值，系统轨线亦会脱离时变吸引盆边界，发生**吸引盆失稳（Basin instability）**。
* **紧致化（Compactification）与奇异微扰法**：
  针对渐近恒定外力情景（$ t \to \pm\infty $ 时 $ \nu(t) $ 存在有限极限），通过将时间 $ t $ 变换为有界辅助动力学变量，将非自治系统映射为高维自治**增广系统（Augmented system）**，随后运用快–慢几何奇异微扰理论（Fast-slow geometric singular perturbation theory）及类似 Melnikov 方法进行临界速率解析估计。

---

### **3. 随机微分方程与大偏差理论（N-tipping 与 AN-tipping）**

#### **(1) 高斯白噪声下的 Ito 随机微分方程**
论文将外界扰动表述为伊藤（Itô）形式随机动力系统：
$ \mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x}, \nu)\mathrm{d}t + \sigma \Sigma(\mathbf{x})\mathrm{d}\mathbf{W} \quad \text{--- (式 1)} $
其中 $ \mathbf{x} \in \mathbb{R}^N $，$ \sigma > 0 $ 为噪声强度，$ \mathbf{W} $ 为维纳过程，扩散张量 $ \mathbf{D}(\mathbf{x}) = \Sigma(\mathbf{x})\Sigma(\mathbf{x})^T $ 处处可逆（非退化噪声）。

#### **(2) 福克–普朗克方程与不变测度**
概率密度演化由 Fokker–Planck 方程控制：
$ \frac{\partial p(\mathbf{x}, t)}{\partial t} = \mathcal{L}_\nu p(\mathbf{x}, t) \quad \text{--- (式 2)} $
其中微分算子定义为：
$ \mathcal{L}_\nu(\cdot) = -\sum_{i} \frac{\partial}{\partial x_i}[f_i(\mathbf{x}, \nu)(\cdot)] + \frac{\sigma^2}{2} \sum_{i, j} \frac{\partial^2}{\partial x_i \partial x_j}[D_{ij}(\mathbf{x})(\cdot)] $
平稳统计由不变测度 $ \rho(\mathbf{x}, \nu) $ 满足 $ \mathcal{L}_\nu \rho(\mathbf{x}, \nu) = 0 $ 给出。

#### **(3) 弱噪声极限（Freidlin–Wentzell 大偏差理论）**
在弱噪声渐近极限 $ \sigma \to 0 $ 下，不变测度满足 WKB 近似展开：
$ \rho(\mathbf{x}, \nu) \sim Z(\mathbf{x}, \nu) \exp\left(-\frac{2\Phi(\mathbf{x}, \nu)}{\sigma^2}\right) $
其中 $ \Phi(\mathbf{x}, \nu) $ 为非平衡准势能。
* **逃逸路径（Instantons）**：跨越亚稳态势垒的最概然逃逸路径对应于 **Freidlin–Wentzell 作用量泛函**的变分极小解（有限噪声下则对应 Onsager–Machlup 泛函）。
* **克莱默斯逃逸时间（Kramers-type scaling）**：系统在参考稳态邻域的平均停留时间 $ \tau $ 满足指数缩放律：
  $ \log(\tau) \sim \frac{2\Delta\Phi}{\sigma^2} $
  其中 $ \Delta\Phi $ 为通往边缘态的最低准势垒高度。

#### **(4) 异常/重尾噪声（AN-tipping）**
若驱动噪声替换为非高斯、跳跃–扩散的柯西/莱维过程（Lévy process），由于厚尾分布在有限时间内产生大脉冲位移的概率不为零，准势能泛函描述失效；系统倾覆机制转变为泊松复合跳跃过程直接击穿确定性吸引盆边界（Shock/Jump tipping）。

---

### **4. 耦合网络子系统与级联倾覆（Cascading Tipping）模型**

考虑单向或双向耦合的子系统链/网络结构（例如 Leader–Follower 系统模型）：
$ \begin{cases}
\mathrm{d}\mathbf{x}_1 = \mathbf{f}_1(\mathbf{x}_1, \nu)\mathrm{d}t + \sigma_1 \Sigma_1(\mathbf{x}_1)\mathrm{d}\mathbf{W}_1 \\
\mathrm{d}\mathbf{x}_2 = \mathbf{f}_2(\mathbf{x}_1, \mathbf{x}_2)\mathrm{d}t + \sigma_2 \Sigma_2(\mathbf{x}_2)\mathrm{d}\mathbf{W}_2
\end{cases} \quad \text{--- (式 5)} $
* **时间尺度分离与传播模态**：
  设子系统 $ k $ 具有特征内禀弛豫时间 $ \tau_k $。
  * 若各跟随子系统的内部时间尺度较长（$ \tau_2 \gg \tau_1 $），系统出现阶段性的亚稳态瞬态，呈现离散的时间分离多相多米诺效应（Domino cascading）。
  * 若跟随子系统的内部时间尺度极短，各子系统状态迅速级联，发生联合级联倾覆（Joint cascading / 快速同步多米诺）。
* **间接倾覆（Indirect Tipping）与级联跳跃（Cascading Hopping）**：
  若耦合矩阵使得参数漂移 $ \nu $ 仅直接作用于主导系统 $ \mathbf{x}_1 $，可能出现主导系统并未越过分叉点，但跟随子系统 $ \mathbf{x}_2 $ 率先失稳的“间接倾覆”现象；或中继节点具有高阈值不发生状态跳跃，却将扰动传递至下游节点的“级联跳跃”动力学。

---

### **5. 泛函算子谱分析理论与早期预警信号（EWS）推导**

论文超越了经典临界慢化（CSD）标量经验统计量（自相关、方差发散），从**库普曼–柯尔莫哥洛夫算子（Koopman–Kolmogorov Operator）**与**佩龙–弗罗贝尼乌斯转移算子（Perron–Frobenius Operator）**的泛函谱分析层面给出了普适数学推导：

#### **(1) 转移算子的本征谱分解**
Fokker–Planck 生成元算子 $ \mathcal{L}_\nu $（对应概率测度演化的 Perron–Frobenius 视角）及其共轭伴随算子 $ \mathcal{L}_\nu^T $（对应可观测量演化的 Koopman–Kolmogorov 视角）满足对偶特征值问题：
$ \mathcal{L}_\nu \rho_j = \lambda_j \rho_j, \quad \mathcal{L}_\nu^T \phi_j = \lambda_j \phi_j $
特征值按其实部降序排列：
$ \lambda_0 = 0 > \mathrm{Re}(\lambda_1) \ge \mathrm{Re}(\lambda_2) \ge \dots $
其中 $ \lambda_0 = 0 $ 对应不变平稳测度，离散孤立谱 $ \{\lambda_j\} $ 被称为**（随机）Ruelle–Pollicott 共振（Resonances）**，连续谱则表征极快衰减模态。

#### **(2) 可观测量滞后自相关与谱隙坍缩**
对于相空间中的任意可观测量标量泛函 $ \Psi(\mathbf{x}) $，其时间滞后自相关函数 $ C_{\Psi, \Psi}(t) $ 严格展开为指数衰减基函数的线性组合：
$ C_{\Psi, \Psi}(t) = \sum_{j=1}^{N} \alpha_j(\Psi) e^{\lambda_j t} \quad \text{--- (式 3)} $
积分相关时间（Integrated correlation time）推导为：
$ \int_0^\infty C_{\Psi, \Psi}(\tau)\mathrm{d}\tau = \sum_{j=1}^N \frac{\alpha_j(\Psi)}{-\lambda_j} \quad \text{--- (式 4)} $
* **临界预警的本质（谱隙 $ \tau \to 0 $）**：
  当系统接近临界点 $ \nu \to h $ 时，**谱隙（Spectral gap）**定义为次主导特征值的实部模长：
  $ \tau = |\mathrm{Re}(\lambda_1)| \to 0 $
  导致主导衰减时间尺度 $ \tau_d = 1/\tau \to \infty $，系统内禀弛豫急剧恶化。
* **霍夫型临界振荡（Critical Oscillation）**：
  若趋于虚轴的是一对共轭复特征值 $ \lambda_{1,2} = -\tau \pm i\omega $，则临界慢化伴随高维临界振荡现象。
* **退化指纹与可观测量投影条件**：
  自相关函数发散能作为有效预警信号的**充分必要条件**是：可观测量 $ \Psi $ 在临界本征模（Critical mode $ \rho_1 $ 或 $ \phi_1 $）上的投影展开系数 $ \alpha_1(\Psi) \ne 0 $。若可观测量选取不当（如间接倾覆中仅观测主导系统 $ \Psi(\mathbf{x}_1) $），其在网络临界模上的投影为零，传统自相关预警将完全失效。

---

### **总结**
整篇论文的理论主线是以**动力系统极限行为与泛函算子谱论**为核心，将临界点从单纯的“低维参数点微扰（$ \dot{x} = -\mathrm{d}V/\mathrm{d}x $）”，严格推导扩展为涵盖“**相空间几何结构突变（Edge States / Long Transients）**”、“**非自治外力轨迹拓扑失稳（Pullback Attractors / Rate Tipping）**”、“**大偏差非平衡流泛函极小化（Instantons / Quasi-potentials）**”以及“**转移算子 Ruelle–Pollicott 谱隙向零收敛（Operator Spectrum Gap Shrinking）**”的现代物理与泛函数学体系。