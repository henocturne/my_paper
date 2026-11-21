[第1页，第1段]
超越无限宽度极限的贝叶斯深度神经网络统计力学框架

[第1页，第2段]
收稿日期：2022年10月21日
接受日期：2023年10月30日

[第1页，第3段]
在线发布日期：2023年12月18日

[第1页，第4段]
查看更新

[第1页，第5段]
尽管深度神经网络在实践中取得了成功，但目前仍缺乏一个全面的理论框架，能够根据训练数据的知识来预测实际相关的评分（如测试准确率）。在无限宽度极限下会出现巨大的简化，即每个隐藏层（$ \ell = 1, \ldots, L $，其中$ L $为网络深度）中的单元数$ N_f $远超训练样本数$ P $。然而，这种理想化明显偏离了深度学习实践的现实。本文利用统计力学的工具集来克服这些局限，并为全连接深度神经架构推导出一个近似配分函数，该函数编码了关于训练模型的信息。该计算在热力学极限下成立，其中$ N_f $和$ P $都很大，且它们的比值$ \alpha_f = P/N_f $是有限的。这一进展使我们能够获得：(1) 与具有有限$ \alpha_f $的单隐藏层网络中回归任务相关的泛化误差的闭式公式；(2) 深度架构配分函数的近似表达式（通过依赖于有限数量序参量的有效作用量）；以及(3) 比例渐近极限下的深度神经网络与Student's $ t $-过程之间的联系。

[第1页，第6段]
深度学习的兴起，由计算技术的进步所驱动并由数十年的研究所预示，已经超出了我们建立坚实理论基础的能力。在基本层面上填补我们对深度学习理解的空白是一项长期的集体努力，涉及多个社区。统计物理学在这方面取得了深远的成果，并且仍然是新视角和突破的源泉。最近一个值得注意的进展是通过考虑无限宽度极限获得的，其中训练数据数量$ P $是固定的，而隐藏层的大小趋于无穷。此类深度模型等价于高斯过程（Gaussian processes, GPs）这一观察建立了深度学习与核方法之间的联系，并提供了该区域的统计物理学描述。

[第1页，第7段]
然而，人们一致认为一个更完整的理论应当处理超越无限宽度极限的深度学习：事实上，现实的神经网络运行在一个性质不同的区域中，其中训练样本的数量超过最大层的宽度。在热力学极限下对有限宽度区域进行建模——其中自由度数量发散且统计力学工具最为有效——相当于取渐近极限

[第1页，第8段]
1 都灵理工大学应用科学与技术系，意大利都灵。2 博科尼大学人工智能实验室，意大利米兰。3 因苏布里亚大学科学与高技术系及非线性与复杂系统中心，意大利科莫。4 意大利国家核物理研究所米兰分部，意大利米兰。5 巴黎-萨克雷大学，法国国家科学研究中心，理论物理与统计力学实验室，法国奥赛。6 巴黎高等师范学院物理实验室，法国国家科学研究中心，PSL大学，索邦大学，巴黎西岱大学，法国巴黎。7 米兰大学，意大利米兰。8 帕尔马大学数学、物理与信息科学系，科学园区，意大利帕尔马。9 电子邮件：pietro.rotondo@unipr.it

[第2页，第1段]
其中训练集大小 $P$ 和每个隐藏层中的单元数 $N_{\ell}$ 都趋于无穷大，且它们的比率固定，正如我们在本工作中所考虑的那样：

[第2页，第2段]
$$P, N_{\ell} \to \infty, \alpha_{\ell} = \frac{P}{N_{\ell}} \text{ finite } \forall \ell = 1, \ldots, L$$  \hspace{1cm} (1)

[第2页，第3段]
其中 $L$ 是网络的（有限）深度（$P$ 随输入大小 $N_0$ 的缩放需要特别关注，在方法部分的“缩放约束……”一节中讨论）。这一选择保证了此类网络在过参数化区域中工作。

[第2页，第4段]
另一条富有成果的研究方向是克服无限宽度极限的局限性，它通过考虑深度线性输入-输出映射来牺牲网络的非线性本质：即使所得架构缺乏与具有非线性的相同模型一样的表达能力$^{30-37}$，多层结构仍保持学习问题的非凸性，同时便于分析研究$^{38,39}$。Li 和 Sompolinsky$^{7}$最近提出了一种方法，用于分析评估在一般固定训练集上训练的深度有限宽度线性网络的性质（例如其泛化误差）；然而，更相关的一般非线性 DNN（深度神经网络）情形仍然是一个开放问题，尽管最近有一些值得注意的尝试来解决它$^{3,26-29,40-42}$。

[第2页，第5段]
在统计力学中，配分函数是编码系统在热力学极限下性质的核心对象。在本工作中，我们处理全连接、多层、非线性神经网络的配分函数的解析计算，作为训练集的函数，在方程 (1) 定义的渐近极限下。技术上，该计算相当于对大量自由度（网络的权重）进行积分消除，从而得到一个仅涉及有限数量（与深度 $L$ 成正比）积分的表达式，通过鞍点方法进行评估。在单隐藏层（1HL）情形中，唯一的關鍵近似由 Bardet 和 Surgailis$^{43}$ 的广义中心极限定理证明（该定理属于源自开创性论文$^{45}$的一类称为 Breuer–Major 定理$^{44}$的结果）。

[第2页，第6段]
在具有 $L$ 个隐藏全连接层的架构的一般情形中，我们表明每一层 $\ell$ 的预激活分布是依赖于 $\ell$ 个参数的高斯混合。值得注意的是，一旦向模型添加非线性，参考文献 5 中执行的反向传播积分就不再是可行选项。我们引入一种前向传播方法，从输入层开始执行嵌套积分。这一结果依赖于一个假设，该假设至少在精神上类似于用于随机和一般特征模型的高斯等价原理$^{46-52}$。

[第2页，第7段]
从这些进展中，我们能够获得网络在插值阈值以下的泛化误差的定量预测。此外，我们的结果从随机过程的角度具有有趣的解释：我们表明，在有限 $\alpha_{\ell}$ 的情形下，贝叶斯神经网络$^{15}$的无限宽度极限中出现的 GP（高斯过程）应推广为 Student's t 随机过程$^{53}$。

[第2页，第8段]
作为该理论的第一个应用，我们建立了一个简单的准则（等价于线性情形$^{5,42}$和有限 P 扰动理论$^{40,54}$中的准则），用于预测在泛化性能方面，采用有限宽度深度神经网络是否比其无限宽度版本更有利。

[第2页，第9段]
**问题设定**

[第2页，第10段]
我们考虑一个监督学习问题，训练集为 $\mathcal{F} = \{\mathbf{x}^\mu, \mathbf{y}^\mu\}_{\mu=1}^P$，其中每个 $\mathbf{x}^\mu \in \mathbb{R}^{N_0}$ 且对应标签 $\mathbf{y}^\mu \in \mathbb{R}$。架构是一个深度神经网络 $f_{\text{DNN}}(\mathbf{x})$，具有 $(L-1)$ 个全连接隐藏层和最终线性读出层，如方程 (22) 所定义。我们分析具有二次损失函数的回归问题：

[第2页，第11段]
$$\mathcal{L} = \frac{1}{2} \sum_{\mu=1}^P \left[ \mathbf{y}^\mu - f_{\text{DNN}}(\mathbf{x}^\mu) \right]^2 + \mathcal{L}_{\text{reg}},$$  \hspace{1cm} (2)

[第2页，第12段]
其中对损失函数的每一层添加了 $L^2$ 正则化，$\|\cdot\|$ 是为权重矩阵 $\mathbf{W}^\ell$ 定义的标准 Frobenius 范数，$\beta = 1/T$ 是逆温度参数。

[第2页，第13段]
作为深度学习统计力学中的标准做法，我们将问题的配分函数定义为：

[第2页，第14段]
$$Z = \int \mathcal{D} \theta e^{-\beta \mathcal{L}(\theta)}.$$  \hspace{1cm} (3)

[第2页，第15段]
其中符号 $\int \mathcal{D} \theta$ 表示对网络权重的集体积分，$\theta = \{\mathbf{W}^\ell, \mathbf{v}\}$。这一选择在 $\beta \to \infty$ 时强制最小化训练误差。我们注意到，将 $\mathcal{L}_{\text{reg}}$ 按 $1/\beta$ 缩放具有自然的贝叶斯学习解释：与方程 (4) 中配分函数相关的 Gibbs 概率 $P_{\beta}(\theta) = Z^{-1} e^{-\beta \mathcal{L}(\theta)}$ 是训练后权重的后验分布，而高斯正则化是一个先验，等价于假设初始化时的权重是从高斯分布中抽取的。

[第2页，第16段]
在此框架中，新（未见）样本 $(\mathbf{x}^0, \mathbf{y}^0)$ 上的平均测试误差由下式给出：

[第2页，第17段]
$$\langle \epsilon_g(\mathbf{x}^0, \mathbf{y}^0) \rangle = \int \mathcal{D} \theta [\mathbf{y}^0 - f_{\text{DNN}}(\mathbf{x}^0)]^2 e^{-\beta \mathcal{L}(\theta)}.$$  \hspace{1cm} (5)

[第2页，第18段]
**结果**

[第2页，第19段]
**1HL NN 的渐近贝叶斯有效作用量。** 在 1HL 架构的情形中，我们能够将配分函数（方程 (4)）在方程 (1) 描述的热力学极限下简化为以下二变量积分：

[第2页，第20段]
$$Z = \int dQ \int dQ \exp \left[ -\frac{N_1}{2} S(Q, \bar{Q}) \right]$$  \hspace{1cm} (6)

[第2页，第21段]
其中我们定义了一个有效作用量 $S$，由下式给出：

[第2页，第22段]
$$S = -Q\bar{Q} + \log(1 + Q) + \frac{\alpha_1}{p} \text{Tr} \log \beta \left[ \frac{1}{\beta} + \frac{\alpha_K}{\lambda_1} \right] + \frac{\alpha_1}{p} \mathbf{y}^\top \left[ \frac{1}{\beta} + \frac{\alpha_K}{\lambda_1} \right]^{-1} \mathbf{y}$$  \hspace{1cm} (7)

[第2页，第23段]
并且我们为输出引入了向量记号 $\mathbf{y}^\top = (\mathbf{y}^1, \mathbf{y}^2, \ldots, \mathbf{y}^P)$。$P \times P$ 的输入依赖核 $K/\lambda_1$ 是在无限宽度极限中出现的神经网络高斯过程（NNGP）核$^{15}$，其以输入协方差矩阵（由第一层的高斯先验 $\lambda_0$ 重新缩放）$C_{\mu\nu} = \mathbf{x}^\mu \cdot \mathbf{x}^\nu / (\lambda_0 N_0)$ 表示的精确定义在方法部分方程 (44) 中给出。另请注意，方程 (7) 对零均值激活函数成立，即其在中心化高斯上的平均值为零的函数（见方程 (43)）；一般有限均值情形的有效作用量在补充第 4 节中报告，并且该推导对许多合理的非线性和输入数据分布都适用，至少在 $P = O(N_0)$ 的区域中（我们在方法部分讨论这一关键的技术点）。这是我们工作的第一个主要结果，我们推测它是精确的，因为我们执行的唯一关键高斯近似由参考文献 43 中 Breuer–Major 定理的扩展所证明，正如方法部分所论证的那样。

[第2页，第24段]
在补充信息中，我们获得了若干因篇幅限制未在此处录入的额外结果：(1) 在线性激活函数情形下有效作用量的重新推导，在固定 $P, N_1, N_0$ 下有效，并与参考文献 5,55 中给出的结果进行比较；(2) 二次激活函数情形下有效作用量的具体推导，该推导不使用 Breuer–Major

[第3页，第1段]
定理；(3) 将方程 (7) 中的有效作用推广到多路（但有限）输出的情形。

[第3页，第2段]
我们现在可以使用鞍点法求解方程(7)，当$  N_1 \to \infty  $时，这相当于寻找方程组$  \partial_Q S = 0  $、$  \partial_Q S = 0  $的解$  Q^*  $、$  \tilde{Q}^*  $（当$  a_1 \to 0  $时重新得到无限宽度极限，对应于特解$  Q^*  $、$  \tilde{Q}^* = 1  $）。在零温度极限下，我们可以找到鞍点方程的解析解（见方法部分）。直接计算表明，泛化误差可以用通常的偏差-方差分解表示为：

[第3页，第3段]
$ 
\langle \epsilon_g(\mathbf{x}^0, y^0) \rangle = (y^0 - \Gamma_1)^2 + \sigma_1^2,
 $

[第3页，第4段]
$ 
\Gamma_1 = \sum_{\mu, \nu} \kappa_{\mu}(\mathbf{x}^0) K_{\mu \nu}^{-1} y_{\nu},
 $

[第3页，第5段]
$ 
\sigma_1^2 = \frac{\tilde{Q}^*}{\lambda_1} \left[ \kappa_0(\mathbf{x}^0) - \sum_{\mu, \nu} \kappa_{\mu}(\mathbf{x}^0) K_{\mu \nu}^{-1} \kappa_{\nu}(\mathbf{x}^0) \right],
 $

[第3页，第6段]
其中 $ \kappa_{\mu}(\mathbf{x}^0), \kappa_0(\mathbf{x}^0) $ 可以使用新的未见输入 $ \mathbf{x}^0 $，从 NNGP 核（NNGP kernel）的函数定义中计算得到，如方法部分所示。

[第3页，第7段]
我们可以直接利用公式(8)获得在贝叶斯学习设置下训练的有限宽度1HL架构的泛化误差的可检验预测，正如我们在图1a中对定义在CIFAR10和MNIST数据集上的两个特定回归任务所做的那样（进一步细节请参阅方法部分的“数值实验”章节以及补充信息）。我们发现，这两个回归任务的泛化曲线作为$  N_1  $的函数是单调递增（递减）的，这取决于可观测值$  y^T (K/\lambda_1)^{-1} y/P  $是小于（大于）1。这一量在控制泛化性能方面的重要性已在线性网络$ ^{5,42} $以及非线性网络在有限$  P  $下的直接微扰理论$ ^{40,54} $中被注意到。

[第3页，第8段]
我们还指出，仅通过观察方程（8）对隐藏层规模 $  N_1  $ 和最后一层高斯先验 $  \lambda_1  $ 的依赖关系，即可对泛化误差的一般行为作出两个半定量预测。在 $  T = 0  $ 时，偏置作为 $  N_1  $ 的函数是常数（正如参考文献5中线性情形所明确观察到的那样），并且与 $  \lambda_1  $ 无关。相比之下，方差依赖于 $  N_1  $，并在大 $  \lambda_1  $ 极限下按 $  1/\sqrt{\lambda_1}  $ 减小。这些观察引出以下两个可检验的预测：（1）增大高斯先验 $  \lambda_1  $ 的幅度应在任意 $  N_1  $ 下系统性地改善泛化性能；（2）对于大 $  \lambda_1  $，泛化误差对 $  N_1  $ 的依赖性应消失（另见图1b中进行的数值实验）。

[第3页，第9段]
**学生 $  t  $ 过程与浅层神经网络之间的联系。** 在获得上一节报告的结果时，我们的理论可以表述为关于输出变量概率分布的陈述。

[第3页，第10段]
$ 
s^\mu = \frac{1}{\sqrt{N_1}} \sum_{i=1}^{N_1} v_{i1} \sigma(h_i^\mu),
 $

[第3页，第11段]
其中 $  h \approx N(0, C \otimes \mathbb{I}_{N_1})  $，$  v \approx N(0, \lambda_1^{-1} \mathbb{I}_{N_1})  $。按照方法部分中配分函数推导的过程，这些变量的概率密度函数可以写成重加权傅里叶变换，

[第3页，第12段]
$ 
P(s| \mathcal{F}_P) = \frac{e^{-\frac{\beta}{2} \sum_{\mu} (y^\mu - s^\mu)^2}}{Z} \int \prod_{\mu} \frac{ds^\mu}{2\pi} e^{i s^\mu \tau} s^\mu \Xi(s),
 $

[第3页，第13段]
的函数

[第3页，第14段]
$ 
\Xi(s) = \left( 1 + \frac{1}{\lambda_1 N_1} \sum_{\mu, \nu} s^\mu K_{\mu \nu}(C) s^\nu \right)^{-\frac{N_1}{2}}.
 $

[第3页，第15段]
**图1 | 1HL网络的学习曲线。** a. 采用Erf激活函数的1HL架构（通过离散化Langevin动力学训练；更多细节见方法部分）的学习曲线，作为隐藏层大小 $  N_1  $ 的函数，针对CIFAR10（上图）和MNIST（下图）数据集上的两个回归任务。两种情况下均选择了零/一标签，CIFAR10数据集的图像已被灰度化并降采样至 $  N_0 = 28 \times 28  $。不同训练集大小 $  P  $ 下的实验测试损失（点及表示一个标准差的误差棒）与由公式(8)计算的理论值（实线）进行比较。柱状中心计算为 $  S = 450  $ 个平衡构型集合的平均值。每 $  10^4  $ 个Langevin步采样一次（在动力学热化之后）。b.c. 实验学习曲线作为 $  N_1  $ 的函数，对应最后一层高斯先验 $  \lambda_1  $ 递增的取值。误差棒在点内，虚线用于引导视线。网络在CIFAR10数据集的 $  P = 3,000  $ 个样本（b）和MNIST的 $  P = 500  $ 个样本（c）上训练。验证了零温度下理论的两个定性预测：(1) 当 $  \lambda_1  $ 增大时，泛化损失应对任何 $  N_1  $ 都减小；(2) 学习曲线对 $  N_1  $ 的依赖性在大 $  \lambda_1  $ 极限下消失，因为偏置为常数（另见正文）。

[第3页，第16段]
很容易注意到，只要 $  N_1 \to \infty  $ 且 $  N_1 \gg P  $，对 $  N_1  $ 的依赖就会消失，我们便得到：

[第3页，第17段]
$ 
\Xi(s) \to e^{-\frac{1}{2\lambda_1} \sum_{\mu, \nu} s^\mu K_{\mu \nu}(C) s^\nu}.
 $

[第4页，第1段]
方程 (11) 是在比例渐近极限 $  P/N_1 \approx O(1)  $ 下，利用基于 Breuer–Major 定理的高斯等价性推导得到的，这表明变量 $  s^H  $ 服从多元 Student's $  t  $-分布 $  ^{53,56-58}  $。

[第4页，第2段]
将 Student's $  t  $-过程视为 NNPGs 的推广这一需求，在最后一层权重分布采用不同先验的情形下已被注意到 $  ^{59}  $。与方程 (11) 形式相似的后验非高斯性也出现在文献 60–62 中。在我们此处考虑的情形下出现这类过程的原因可以通过一个启发式论证来理解：当 $  N_1  $ 和 $  P  $ 处于同一量级时，我们不能在 $  P \to \infty  $ 之前取极限 $  N_1 \to \infty  $，因此在估计输出变量 $  s^H  $ 的概率分布时，需要使用其经验协方差而非真实协方差。对这些神经网络 Student's $  t  $-过程（NNTPs）及其出现机制的更精确刻画，是未来工作中值得研究的有趣课题。

[第4页，第3段]
**深度神经网络（DNNs）的渐近贝叶斯有效作用量。** 在具有有限层数 $  L  $ 和零均值激活函数的深度全连接架构的一般情形下，我们将配分函数表示为 $  2L  $ 维积分（见方法部分）：

[第4页，第4段]
$ 
Z_{\text{DNN}} = \int \prod_{\ell=1}^{L} dQ_\ell d\bar{Q}_\ell e^{-\frac{N_L}{2} S_{\text{DNN}}([Q_\ell, \bar{Q}_\ell])},
 $

[第4页，第5段]
其中有效作用量由下式给出：

[第4页，第6段]
$ 
S_{\text{DNN}} = \sum_{\ell=1}^{L} \frac{\alpha_\ell}{\alpha_\ell} [-Q_\ell \bar{Q}_\ell + \log(1 + Q_\ell)] + \frac{\alpha_\ell}{p} \text{Tr} \log \beta \left( \frac{1}{\beta} + K_L^{(R)} ([Q_\ell]) \right) - \frac{\alpha_\ell}{p} y^T \left( \frac{1}{\beta} + K_L^{(R)} ([Q_\ell]) \right)^{-1} y
 $

[第4页，第7段]
并且我们引入了一个重整化核 $  K^{(R)}  $，它推广了 $  L  $ 层 NNPG 核的递推关系：

[第4页，第8段]
$ 
K_\ell^{(R)} ([Q_\ell]) = \bar{Q}_\ell / \Lambda_\ell K_0 \left[ K_\ell^{(R)} ([Q_\ell]) \right], \quad K_0^{(R)} = C,
 $

[第4页，第9段]
其中 $  C  $ 是上文定义的输入协方差矩阵，我们强调每个 $  K_\ell^{(R)}  $ 仅依赖于变量 $  \bar{Q}_1, \ldots, \bar{Q}_{\ell-1}  $。为完整起见，我们注意到无限宽度核 $  K_L  $ 的递推关系由方程 (15) 给出，其中 $  \bar{Q}_\ell = 1 \forall \ell = 1, \ldots, L  $。

[第4页，第10段]
该作用量与上文针对 IHL 特殊情形所得到的作用量具有相同的结构，区别在于对于 $  L  $ 个隐藏层，推导的递归性质引入了额外的序参量，这些序参量嵌套在核 $  K_L  $ 的定义中。此外，由于我们的推导适用于任意大小 $  N_\ell  $ 的层，该作用量还依赖于纵横比 $  \alpha_\ell  $。在补充信息中我们推导了一系列额外结果：(1) 我们将该有效作用量推广到有限均值激活函数；(2) 我们展示了如何在各向同性极限 $  \alpha_\ell = \alpha \forall \ell = 1, \ldots, L  $ 下恢复线性情形；(3) 利用 (1)，我们演示了如何修正文献 5 中针对 ReLU 激活提出的启发式理论。

[第4页，第11段]
在新样本 $  (x^0, y^0)  $ 上计算泛化误差得到：

[第4页，第12段]
$ 
\langle \epsilon_g(x^0, y^0) \rangle = (y^0 - \Gamma_L)^2 + \sigma_L^2
 $

[第4页，第13段]
其中

[第4页，第14段]
$ 
\Gamma_L = \sum_{\mu\nu} K_L^{(R)} \left( \frac{1}{\beta} + K_L^{(R)} ([Q_\ell]) \right)^{-1} y_\nu,
 $

[第4页，第15段]
$ 
\sigma_L^2 = K_L^{(R)} - \sum_{\mu\nu} K_L^{(R)} \left( \frac{1}{\beta} + K_L^{(R)} ([Q_\ell]) \right)^{-1} K_L^{(R)}
 $

[第4页，第16段]
且 $  K_L^{(R)}, K_L^{(R)}  $ 是由方程 (15) 中给出的递推关系、以输入 $  x^0  $ 作为初始条件计算得到的递归核。

[第4页，第17段]
注意，在此情形下我们同样可以对泛化误差对最后一层高斯先验 $  \Lambda_\ell  $ 的依赖性进行相同的标度分析（在零温极限下）。结果表明，偏置不依赖于它，而方差 $  \sigma_\ell^2  $ 在 $  \Lambda_\ell  $ 趋于无穷时以 $  1/\sqrt{\Lambda_\ell}  $ 的速度趋近于零。这意味着，在有限深度 $  L > 1  $ 的情形下，在最后一层高斯先验取较大值时进行训练，应当在网络的任意纵横比下都能改善泛化性能。我们在图 2c,f 中用数值实验证实了这一普遍观察。然而，与 IHL 情形不同，我们观察到即使在零温极限下偏置也依赖于纵横比，并且我们不能再期望网络纵横比 $  \alpha_\ell  $ 的依赖性在 $  \Lambda_\ell \to \infty  $ 极限下消失。

[第4页，第18段]
通过考虑 ReLU 激活下的有效作用量，我们可以获得 $  L  $ 层理论的另一个预测（这再次证实了先前关于线性网络的结果以及关于非线性网络的微扰计算 $  ^{54,42,54}  $）。在无限宽度极限 $  \alpha_\ell = \alpha = 0 \forall \ell = 1, \ldots, L  $ 附近进行直接的泰勒展开表明，对测试损失的第一个修正 $  \Delta \epsilon_g  $ 正比于：

[第4页，第19段]
$ 
\Delta \epsilon_g \propto \alpha \left( \frac{1}{\beta} y^T K_L^{-1} y - 1 \right).
 $

[第4页，第20段]
其中 $  K_\ell  $ 是方程 (15) 中递推关系在 $  \bar{Q}_\ell = 1 \forall \ell = 1, \ldots, L  $ 及 ReLU 激活下的解。这意味着存在一个简单的标量可观测量，它决定了有限宽度深度神经网络是否会优于其无限宽度对应物，该量推广了在 IHL 中发现的量：

[第4页，第21段]
$ 
s_L = \frac{1}{\beta} y^T K_L^{-1} y.
 $

[第4页，第22段]
特别地，我们预期当 $  s_L < 1  $ 时，有限宽度网络将优于其无限宽度对应物。在图 2a,c 中，我们在 IHL 情形所用的相同回归任务上，对采用 ReLU 激活的深度架构检验了这一预测。注意，随着隐藏层数 $  L  $ 的增长，$  s_L  $ 会迅速发散到无穷大。其原因很简单：当 $  L \to \infty  $ 时，ReLU NNPG 核 $  K_L  $ 至少发展出一个零特征值。这最终发生是因为矩阵 $  K_\ell  $ 的每个元素随着 $  L  $ 的增长都收敛到零（见图 2b,c），这一点通过查看 NNPG ReLU 核的显式递推关系 $  ^{15,63}  $ 便可轻易验证。我们注意到，这种奇异性可以等价地视为由 NNPG 核递推关系所定义的离散动力映射的不动点，因此研究我们渐近极限下的泛化性能与随机神经网络混沌边缘相关工作 $  ^{64,65}  $ 之间的关系可能是值得的。

[第4页，第23段]
方程 (18) 提供了与 Student's $  t  $-推断的另一联系。事实上，Tracey 和 Wolpert $  ^{66}  $ 在研究基于 Student's $  t  $-过程的贝叶斯优化时发现了相同的判据。作者表明，$  s_\ell  $ 的值决定了他们所考虑的 Student's $  t  $-过程是否比具有相同核的相应 GP 具有更大/更小的方差。

[第4页，第24段]
**讨论**

[第4页，第25段]
在我们的工作中，我们描述了一种研究深度神经网络统计力学的策略，它超越了无限宽度极限，即在有限渐近区域 $  P, N_\ell \to \infty  $ 且 $  \alpha_\ell = P/N_\ell > 0  $ 下，而非无限宽度 $  \alpha_\ell = 0  $。在 IHL 情形下，我们推测我们的评估在上述热力学极限下是精确的。因此，我们预期结果不会有进一步的修正，至少在渐近区域内如此。特别地，我们找到了泛化误差的闭式表达式，它原则上为全连接架构的泛化能力提供了贝叶斯估计量，适用于

[第5页，第1段]
对于任何给定的经验数据集，只要所选的架构能够完美拟合训练集。

[第5页，第2段]
对于有限深度 $ L > 1 $ 网络的情况，至少原则上应该可以系统地考虑对鞍点作用量的非高斯修正，以检查这些修正是否对有限宽度下的理论相关，因为我们推导结果时所做的假设是清晰的（另见方法）。

[第5页，第3段]
从数学角度来看，我们发现与Student's $ t $-processes（学生t过程）的联系非常有前景。这种映射的精确刻画及其有效性限制代表了未来研究的一个方向。

[第5页，第4段]
**图2 | 深度网络 $ L > 1 $ 的实验 a,d，具有ReLU激活的LHL神经网络的测试损失，作为深度 $ L $ 的函数，对于 $ P = 100 $（a显示CIFAR10的结果，d显示MNIST的结果）。该网络在小 $ \alpha $ 区域（$ \alpha = 0.1 $）的回归任务上训练，接近无限宽度极限。有限宽度网络只有在 $ s_t < 1 $ 时（阴影区域）才能超越无限宽度预测，也就是说，仅在MNIST任务和深度 $ L < 3 $ 时。b,e，网络不同层处无限宽度NNGP核元素的 visualization（可视化）（b中为CIFAR10，e中为MNIST）。ReLU NNGP核在重复迭代后收敛到零。这产生了几乎消失的特征值，使得 $ s_t $ 最终总是大于一。c,f，在 $ P = 1,000 $ 个样本上训练的4HL网络的测试损失，具有不同的正则化强度（其中 $ N_t = N = 1,000 $；c中为CIFAR10，f中为MNIST）。尽管增加最后一层高斯先验的幅度对所有 $ N $ 仍然改善泛化，但已经不清楚（如1HL网络那样）大 $ \lambda_t $ 处的曲线是否是作为 $ N $ 的函数的常数。虚线用于引导视线。在所有面板中，误差棒位于点内。**

[第5页，第5段]
**图3 | 随机数据和序参量的普适行为作为深度 $ L $ 的函数。a，不同1HL架构在完全随机任务上训练的训练损失（即，输入 $ \mathbf{x} \in \mathbb{R}^{N_0} $ 其中 $ N_0 = 50 $ 和标量输出 $ y $ 都是从零均值和单位方差的 normal distribution（正态分布）中采样的独立同分布随机变量）作为 $ \alpha_t $ 的函数。误差棒位于点内。目前我们无法用我们的理论捕捉这种普适现象，该理论只描述了训练误差恰好为零的超参数化极限。b，在ReLU激活函数和各向同性网络 $ \alpha_t = \alpha \forall \ell $ 的情况下，对于不同深度 $ L $，展示了解 $ \hat{Q} $ 的数值评估。随着 $ L $ 增大（$ \ell = 30 $），参数 $ \hat{Q} $ 对所有 $ \alpha $ 快速接近1，这表明在顺序极限中（深度 $ L $ 在 $ P, N $ 之后趋于无穷），渐近区域中的DNN也收敛到核极限。**

[第5页，第6段]
值得注意的是，我们的理论预测，当深度 $ L $ 趋于无穷时，核极限也应出现在渐近区域中。例如，可以通过考虑各向同性极限 $ \alpha_t = \alpha \forall \ell $ 和ReLU激活来验证这一点。这里可以数值求解大 $ L $ 时 $ \hat{Q} $ 的鞍点方程，并验证对所有 $ \alpha $ 有 $ \hat{Q} \to 1 $，如图3b所示。因此，在这个极限中，我们也期望与核理论等价，其核由 $ K_\alpha(C) $ 给出。注意，从我们的框架中可以清楚地看到，我们仅在 $ P, N $ 之后取深度 $ L $ 趋于无穷。因此，我们不对固定 $ L/N $ 时具有挑战性的同时极限 $ L, N \to \infty $ 做出断言，例如参考文献27、28、55、67中所做的那样。

[第5页，第7段]
应该强调，我们的理论只描述了零训练损失的平衡区域，因此我们的分析不应适用于 $ P/N_t \gg 1 $ 的区域。然而，使用不同宽度的1HL架构和随机训练标签进行的数值模拟表明，训练损失关于 $ \alpha_t $ 遵循普适行为42,68（见图3a），包括DNN无法完美拟合数据的区域。开发一个也能捕捉这一相的理论将是可取的。

[第5页，第8段]
另一个需要理解的有趣方面是这种平均场静态分析可以在多大程度上扩展到平衡之外，以评估完整的训练动力学；这样的理论确实将使研究用于训练深度神经网络的许多（通常是启发式的）学习算法的性能成为可能。

[第5页，第9段]
最后我们指出，将我们在固定数据下的理论与参考文献42、69中研究的数据平均情况进行比较，并将我们的结果扩展到卷积层（如参考文献17中在无限宽度情况下所做的那样），将是很有趣的。

[第5页，第10段]
**方法**

[第5页，第11段]
**学习问题的设定和符号**

[第5页，第12段]
我们考虑具有 $ L $ 个全连接隐藏层的深度神经网络 $ f_{\text{DNN}}(\mathbf{x}) $，其中每一层的预激活 $ h_{i\ell}^{(\ell)} $（$ i_\ell = 1, \ldots, N_\ell $；$ \ell = 1, \ldots, L $）递归地表示为前一层预激活 $ h_{i\ell}^{(\ell-1)} $（$ i_\ell = 1, \ldots, N_\ell $）的非线性函数：

[第5页，第13段]
$ 
h_{i\ell}^{(\ell)} = \frac{1}{\sqrt{N_{\ell-1}}} \sum_{i_{\ell-1}=1}^{N_{\ell-1}} W_{i_{\ell}i_{\ell-1}}^{(\ell)} \sigma \left( h_{i\ell-1}^{(\ell-1)} \right) + b_{i\ell}^{(\ell)}, \tag{20}
 $

[第5页，第14段]
$ 
h_{i1}^{(1)} = \frac{1}{\sqrt{N_0}} \sum_{i_1=1}^{N_0} W_{i_1i_0}^{(1)} x_{i_0} + b_{i1}^{(1)} \tag{21}
 $

[第6页，第1段]
其中 $W^{(i)}$ 和 $b^{(i)}$ 分别是第 $i$ 层的权重和偏置，而输入层的维度为 $N_0$（输入数据维度）；$\sigma$ 是非线性激活函数，且各层共用同一激活函数。我们添加最后一个读出层，并将深度神经网络实现的函数定义为：

[第6页，第2段]
$$f_{DNN}(x) = \frac{1}{\sqrt{N}} \sum_{i=1}^{N} v_i \sigma \left[ h_i^{(L)}(x) \right],$$  (22)

[第6页，第3段]
其中 $v$ 是最后一层的权重向量。

[第6页，第4段]
在给定逆温度 $\beta$ 下的平均训练误差为：

[第6页，第5段]
$$\langle \epsilon_t \rangle = \frac{1}{P} \int \mathcal{D} \theta [\mathcal{L}(\theta) - \mathcal{L}_{reg}(\theta)] \frac{e^{-\beta \mathcal{L}(\theta)}}{Z},$$  (23)

[第6页，第6段]
该量连同公式 (5) 中定义的测试误差，代表两个特殊的可观测量，但更一般地，对于任意可观测量 $O$，我们有：

[第6页，第7段]
$$\langle O \rangle = \int \mathcal{D} \theta O(\theta) \frac{e^{-\beta \mathcal{L}(\theta)}}{Z}.$$  (24)

[第6页，第8段]
Breuer–Major 定理作为浅层网络中高斯等价性的依据

[第6页，第9段]
Breuer–Major 定理及其扩展处理以下随机变量序列：

[第6页，第10段]
$$S_N = \frac{1}{\sqrt{N}} \sum_{i=1}^{N} c_i f(x_i) N \geq 1.$$  (25)

[第6页，第11段]
显然，如果向量 $x = (x_1, \ldots, x_N)$ 的分布在其坐标上可分解（即 $p(x) = \prod_i p(x_i)$ 且 $f(x) = x$），则只要均值 $\mathbb{E}(x_i) = 0$、方差 $\mathbb{E}(x_i^2)$ 有限，且 $c_i$ 的值满足所谓的 Lindeberg 条件，随机变量 $S = \lim_{N \to \infty} S_N$ 就是正态分布的。只要 $F$ 是性质良好的非线性函数，这一点同样成立。

[第6页，第12段]
Breuer–Major 定理本质上将该结果推广到一般高斯过程（GP），给出了高斯过程协方差矩阵以及非线性函数 $F$ 的充分条件，以保证 $S_N$ 收敛到正态分布。我们在此报告参考文献 44 中给出的该定理的现代表述。

[第6页，第13段]
我们首先考虑一个平稳的（一维）高斯过程 $x = (x_k)_{k \in \mathbb{Z}}$。平稳性——并非本质要求，下文将用更弱的条件替代——要求该过程的协方差 $C_\theta = \mathbb{E}(x_k x_l)$ 是差值 $i - j$ 的函数，即 $C_\theta = C(i - j)$。对非线性函数 $F$ 唯一需要施加的技术条件是它具有定义良好的 Hermite 秩 $R$。Hermite 秩是 $F$ 在 Hermite 多项式展开中出现的最小正整数：

[第6页，第14段]
$$F(x) = \sum_{k=R}^{\infty} f_k H_k(x),$$  (26)

[第6页，第15段]
其中 $H_k(x)$ 是第 $k$ 个 Hermite 多项式，$f_k$ 是展开系数。对于许多合理的激活函数 $F$，$R = 1$。

[第6页，第16段]
**定理 1.** 本节基于参考文献 45 中的 Breuer–Major 定理。设 $x = (x_k)_{k \in \mathbb{Z}}$ 是一个协方差为 $C(i - j)$ 的平稳一维高斯过程。设 $\mathbb{E}[F(x_i)] = 0$ 且 $\mathbb{E}[F^2(x_i)] < \infty$，并假设函数 $F$ 具有 Hermite 秩 $R \geq 1$。假设：

[第6页，第17段]
$$\sum_{j \in \mathbb{Z}} |C_{ij}|^R < \infty.$$  (27)

[第6页，第18段]
则 $\sigma^2 := \mathbb{E}[F(x_i)^2] + 2 \sum_{j=1}^{\infty} \mathbb{E}[F(x_i) F(x_j)]$ 是有限的。此外，随机变量序列

[第6页，第19段]
$$S_N = \frac{1}{\sqrt{N}} \sum_{i=1}^{N} f(x_i) N \geq 1$$  (28)

[第6页，第20段]
依分布收敛到 $\mathcal{N}(0, \sigma^2)$，即均值为零、方差为 $\sigma^2$ 的高斯分布。

[第6页，第21段]
就本工作的范围而言，我们需要比上述结论稍强的陈述，因为：(1) 在我们的计算中协方差不是平稳的；(2) 我们需要考虑更一般的非线性函数序列 $c_i f(x_i)$，使得求和（公式 (28)）中的每一项都可以乘以因子 $c_i \neq 1$。

[第6页，第22段]
参考文献 45 已经表明，平稳性假设可以被削弱，并替换为协方差元素一致收敛的要求，即：

[第6页，第23段]
$$\sum_{j \in \mathbb{Z}} |C_{ij}|^R < B_0 \forall i \in \mathbb{Z},$$  (29)

[第6页，第24段]
其中 $B_0$ 是一个正的有限常数。

[第6页，第25段]
上述扩展 (1) 和 (2) 最近已由 Bardet 和 Surgailis 处理，我们报告如下。设 $x^N$ 是一个 $N$ 维高斯向量，满足 $\mathbb{E}[x_i^N] = 0$、$\mathbb{E}[(x_i^N)^2] = 1$。现定义 $C_N^y = \mathbb{E}[x_i^N x_j^N]$。对于给定的整数 $m \geq 1$，假设

[第6页，第26段]
$$\sup_{N \geq 1} \max_{1 \leq i \leq N} \sum_{i=1}^{N} |C_N^y|^m < \infty,$$  (30)

[第6页，第27段]
$$\sup_{N \geq 1} \frac{1}{N} \sum_{1 \leq i, j \leq N} |C_N^y|^m \xrightarrow{K \to \infty} 0.$$  (31)

[第6页，第28段]
同时取 $\mathbb{L}_0^2(x) = \{f : \mathbb{E}f(x) = 0, \mathbb{E}f^2(x) < \infty\}$，其中 $x$ 是标准正态变量。我们随后在下一节继续。

[第6页，第29段]
**定理 2.** 本节基于 Bardet 和 Surgailis 工作中“(1.ii)”节的相关定理。假设公式 (30)、(31) 成立，并设 $f_i^N \in \mathbb{L}_0^2(x) (N \geq 1, 1 \leq i \leq N)$ 是一列函数，均具有至少为 1 的 Hermite 秩 $m$。假设存在一个 $\mathbb{L}_0^2(x)$ 值连续函数 $\phi_r, r \in [0, 1]$，使得

[第6页，第30段]
$$\sup_{r \in (0,1]} \mathbb{E}\left[f_N^m(x) - \phi_r(x)\right]^2 \xrightarrow{N \to \infty} 0.$$  (32)

[第6页，第31段]
此外，令

[第6页，第32段]
$$(\sigma^N)^2 = \mathbb{E}\left[\frac{1}{\sqrt{N}} \sum_{i=1}^{N} f_i^N(x_i^N)\right]^2 \xrightarrow{N \to \infty} \sigma^2,$$  (33)

[第6页，第33段]
其中 $\sigma^2 > 0$。则

[第6页，第34段]
$$\frac{1}{\sqrt{N}} \sum_{i=1}^{N} f_i^N(x_i^N) \xrightarrow{d} \mathcal{N}(0, \sigma^2),$$  (34)

[第6页，第35段]
其中 $\xrightarrow{N \to \infty}$ 表示依分布收敛。

[第6页，第36段]
该定理的假设应被视为对激活函数 $\sigma$、重标度输入协方差矩阵 $C_{iv}$ 以及傅里叶积分（公式 (10)）中的主导构型 $s$ 的条件，以证明我们的高斯假设（见公式 (41)）。

[第6页，第37段]
**贝叶斯框架下 1HL 全连接神经网络有效作用量计算的概要**

[第6页，第38段]
我们现在讨论计算中的关键方面。起点是以下配分函数：

[第7页，第1段]
$ 
Z = \int \prod_{i_1}^{N_1} dv_{i_1} \prod_{i_2}^{N_2} dv_{i_2} \exp \left\{ -\frac{\lambda_1}{2} \sum_{i_1}^{N_1} v_{i_1}^2 - \frac{\lambda_2}{2} \prod_{i_2}^{N_2} w_{i_2}^2 \right\}
\tag{35}
 $

[第7页，第2段]
$ 
-\frac{\beta}{2} \sum_{\mu} \left[ y^{\mu} - \frac{1}{\sqrt{N_1}} \sum_{i_1}^{N_1} v_{i_1} \sigma \left( \sum_{i_2}^{N_2} w_{i_2} \frac{x_{i_2}^p}{\sqrt{N_0}} \right) \right]^2
 $

[第7页，第3段]
其中 $  w = W^{(1)}  $，并且在不失一般性的情况下取 $  b^{(1)} = 0  $。（可以通过将每一层的输入维度和激活维度都增加一维，将带有非零偏置的系统映射到零偏置系统中。原始偏置随后可以简单地映射到增广系统的额外权重中）。第一步是在损失函数中解耦不同层的权重。这可以通过引入基于两族狄拉克δ函数的标准恒等式来实现，一族用于隐藏层的预激活，另一族用于网络的输出：

[第7页，第4段]
$ 
1 = \int \prod_{\mu} ds^{\mu} \delta \left[ s^{\mu} - \frac{1}{\sqrt{N_1}} \sum_{i_1}^{N_1} v_{i_1} \sigma(h_{i_1}^{\mu}) \right],
 $

[第7页，第5段]
$ 
1 = \int \prod_{\mu} \prod_{i_1}^{N_1} dh_{i_1}^{\mu} \delta \left( h_{i_1}^{\mu} - \frac{1}{\sqrt{N_0}} \sum_{i_2}^{N_2} w_{i_2} x_{i_2}^{\mu} \right).
 $

[第7页，第6段]
通过使用这些δ函数的标准傅里叶表示，引入共轭变量 $  h_{i_1}^{\mu}  $ 和 $  s^{\mu}  $，我们可以对内部权重和外部权重执行高斯积分：

[第7页，第7段]
$ 
Z = \int \prod_{\mu} \prod_{i_1}^{P} ds^{\mu} ds^{\mu} e^{-\frac{\beta}{2} \sum_{i_1}^{P} (y^{\mu} - s^{\mu})^2 + i \sum_{\mu} s^{\mu} s^{\mu}}
 $

[第7页，第8段]
$ 
\times \left\{ \int \prod_{\mu} \prod_{i_1}^{P} dh^{\mu} dh^{\mu} e^{i \sum_{\mu} h^{\mu} h^{\mu} - \frac{1}{2N_1} \sum_{i_1}^{N_1} \sum_{\mu} s^{\mu} \sigma(h^{\mu})^2} \right\}^2 - e^{-\frac{1}{2N_0} \sum_{i_1}^{N_0} \sum_{\mu} \left( \sum_{\mu} h^{\mu} x_{i_2}^{\mu} \right)^2} \right\}^N,
 $

[第7页，第9段]
其中我们利用了 $  h_{i_1}^{\mu}  $ 和 $  h_{i_1}^{\mu}  $ 上的积分可以按指标 $  i_1  $ 分解这一事实。关于 $  h_{i_1}^{\mu}  $ 的积分是高斯型的，可以求解：

[第7页，第10段]
$ 
\int \prod_{\mu} \prod_{i_1}^{P} dh^{\mu} e^{i \sum_{\mu} h^{\mu} h^{\mu} - \frac{1}{2N_1} \sum_{i_1}^{N_1} \sum_{\mu} s^{\mu} \sigma(h^{\mu})^2} = P_1(h^{\mu}),
 $

[第7页，第11段]
其中

[第7页，第12段]
$ 
P_1(h^{\mu}) = \frac{e^{-\frac{1}{2} \sum_{\mu} h^{\mu} C_{1,1}^{\mu} h^{\mu}}}{\sqrt{(2\pi)^P \det C}} \cdot C_{\mu \nu} = \frac{1}{\lambda_0 N_0} \sum_{i_0}^{N_0} x_{i_0}^{\mu} x_{i_0}^{\nu}.
 $

[第7页，第13段]
最后一步要求协方差矩阵 $  C  $ 可逆。注意，一旦 $  P > N_0  $，这一条件就不再成立，但向 $  C  $ 添加一个小的对角项即可解决该问题。可以显式验证最终结果不依赖于这一额外的正则化。

[第7页，第14段]
为了处理关于 $  h^{\mu}  $ 的积分，我们可以为随机变量 $  q = 1/\sqrt{\lambda_1 N_1} \sum_{\mu} s^{\mu} \sigma(h^{\mu})  $ 引入另一个狄拉克δ恒等式。这将问题转化为求概率密度 $  P(q)  $。在公式(1)定义的极限下，这恰好是Breuer-Majer定理$ ^{44,45} $，特别是其扩展$ ^{43} $的相同设定。因此，只要（正则化的）协方差 $  C  $ 和激活函数 $  \sigma  $ 都满足该定理的假设，就能保证概率分布 $  P(q)  $ 依分布收敛到高斯分布：

[第7页，第15段]
$ 
P(q) = \int d^P h P_1(h^{\mu}) \delta \left[ q - \frac{1}{\sqrt{\lambda_1 N_1}} \sum_{\mu} s^{\mu} \sigma(h^{\mu}) \right],
 $

[第7页，第16段]
$ 
P(q) \to \mathcal{N}_q(0, Q).
 $

[第7页，第17段]
其方差为

[第7页，第18段]
$ 
Q(s, C) = \frac{1}{\lambda_1 N_1} \sum_{\mu, \nu} s^{\mu} \sigma(h^{\mu}) \sigma(h^{\nu}) \left[ \int d^P h P_1(h^{\mu}) \sigma(h^{\nu}) \sigma(h^{\nu}) \right] s^{\nu}
 $

[第7页，第19段]
$ 
= \frac{1}{\lambda_1 N_1} \sum_{\mu, \nu} s^{\mu} K_{\mu \nu}(C) s^{\nu}.
 $

[第7页，第20段]
可以证明，在积分域中存在某些特殊配置 $  s  $，对于这些配置我们不能援引高斯等价（例如，参见我们在补充材料第2节末尾的讨论）。在我们的推导中，我们假设这些特殊配置对有效作用的贡献在热力学极限下可以忽略不计。这里我们还假设变量 $  q  $ 的均值为零，只要满足以下条件即可验证：

[第7页，第21段]
$ 
\int d^P h P_1(h^{\mu}) \sigma(h^{\nu}) = 0,
 $

[第7页，第22段]
即只要 $  \sigma  $ 是零均值的；对于有限均值激活函数（如ReLU），请参见补充材料第4节中更一般的推导。

[第7页，第23段]
核矩阵 $  K_{\mu \nu}(C)  $ 的每个元素都可以很容易地从 $  P  $ 维积分简化为更简单的二维积分：

[第7页，第24段]
$ 
K_{\mu \nu}(C) = \int \frac{d t_1 d t_2}{\sqrt{(2 \pi)^2 \det C}} e^{-\frac{1}{2} t_1^T C^{-1} t_1} \sigma(t_1) \sigma(t_2),
 $

[第7页，第25段]
其中 $  t = (t_1, t_2)^T  $，且

[第7页，第26段]
$ 
C = \begin{pmatrix} C_{\mu \nu} & C_{\mu \nu} \\ C_{\mu \nu} & C_{\nu \nu} \end{pmatrix}.
 $

[第7页，第27段]
是简化的 $  2 \times 2  $ 输入协方差矩阵。值得指出的是，我们这里得到的核是所谓的NNGP核。它不同于在梯度下降训练网络的无限宽度极限中发现的神经正切核$ ^{70} $。贝叶斯神经网络的无限宽度极限与梯度下降得到的极限不同这一事实确实是已知的，并在文献$ ^{20} $中讨论过。

[第7页，第28段]
现在我们可以对变量 $  q  $ 积分并得到：

[第7页，第29段]
$ 
\int \frac{d q e^{-\frac{q^2}{2} \sum_{i_1}^{N_1} \sum_{i_2}^{N_2} \sigma(q, C)}}{\sqrt{2 \pi Q(s, C)}} = [Q(s, C) + 1]^{-\frac{N_1}{2}}.
 $

[第7页，第30段]
在有限 $  \alpha_1 = P/N_1  $ 的一般情况下，我们只剩下关于 $  s^{\mu}  $ 和 $  s^{\mu}  $ 的积分。为了求解它们，方便引入最后一个狄拉克δ恒等式：

[第7页，第31段]
$ 
1 = \int d Q \delta \left[ Q - \frac{1}{\lambda_1 N_1} \sum_{\mu, \nu} s^{\mu} K(C)_{\mu \nu} s^{\nu} \right],
 $

[第7页，第32段]
其中 $  Q \geq -1  $ 现在是积分变量而不是 $  s  $ 的函数，因此我们消除了配分函数中对 $  \sqrt{Q(s, C) + 1}  $ 的显式依赖。最后，一旦通过共轭变量 $  \tilde{Q}  $ 插入δ函数的另一种积分表示，关于 $  s^{\mu}  $ 和 $  s^{\mu}  $ 的积分就是高斯型的。这使我们能够得到公式(7)中获得的最终有效作用。

[第7页，第33段]
### 零温度极限下鞍点方程的精确解

[第7页，第34段]
从公式(7)得到的鞍点方程在零温度极限（$  \beta \to \infty  $）下大大简化。特别地，利用核 $  K  $ 只有正特征值这一事实（在渐近

[第8页，第1段]
在正则化参数 $ \alpha_1, \alpha_0 $ 有限的情况下，我们得到：

[第8页，第2段]
$ \hat{Q} = \frac{1}{1+\alpha_1} \cdot Q = \alpha_1 \cdot \frac{\alpha_1}{\alpha_0} \cdot \frac{1}{\rho} \cdot \frac{1}{\lambda_1} \cdot y. $

[第8页，第3段]
给定条件 $ Q \geq -1 $，$ \hat{Q} $ 的唯一精确解为正，其表达式为：

[第8页，第4段]
$ \hat{Q}^* = \frac{\sqrt{(\alpha_1 - 1)^2 + 4\alpha_1 \cdot \frac{1}{\rho} \cdot \frac{1}{\lambda_1} \cdot y - (\alpha_1 - 1)}}{2}. $

[第8页，第5段]
### 预测器统计量

[第8页，第6段]
我们关注的主要可观测量是泛化误差（公式 (5)）。我们可以沿着上一节中计算相同的思路进行，除了由公式 (36) 和 (37) 定义的变量 $ s^\mu, h^\mu_i $ 之外，引入描述新测试样本的输出和预激活的额外变量 $ s^0, h^0_i $。由此得到：

[第8页，第7段]
$ \langle \epsilon_g(\mathbf{x}^0, y^0) \rangle = \frac{1}{2} \int \frac{ds^0 d\hat{s}^0}{2\pi} \int \frac{ds^\mu d\hat{s}^\mu}{2\pi} \cdot (y^0 - s^0)^2 $

[第8页，第8段]
$ \times e^{-\frac{\rho}{2} \sum_{\mu=1}^{P} (y^\mu - s^\mu)^2 + i \sum_{\mu=1}^{P} s^\mu \hat{s}^\mu + i s^0 \hat{s}^0} $

[第8页，第9段]
$ \times \left[ 1 + \frac{1}{\lambda_1 N_1} \left( \sum_{\mu=1}^{P} s^\mu K_{\mu \nu} s^\nu + 2s^0 \sum_{\mu=1}^{P} s^\mu K_{\mu \nu} (\mathbf{x}^0) + (s^0)^2 K_0 (\mathbf{x}^0) \right) \right]^{-\frac{N_1}{2}}, $

[第8页，第10段]
其中 $ K_\mu $ 和 $ K_0 $ 分别是训练-测试和测试-测试核积分，如公式 (42) 所定义，此时协方差矩阵涉及测试输入，即：

[第8页，第11段]
$ K_\mu = \int \frac{dt_1 dt_2}{\sqrt{(2\pi)^2 \det \hat{C}_\mu}} e^{-\frac{1}{2} t^T \hat{C}_\mu^{-1} t} \sigma(t_1) \sigma(t_2), $

[第8页，第12段]
$ K_0 = \int \frac{dt}{2\pi C_{00}} e^{-\frac{t^2}{2 C_{00}}} \sigma(t)^2, $

[第8页，第13段]
其中

[第8页，第14段]
$ \hat{C}_\mu = \begin{pmatrix} C_{\mu \mu} & C_{\mu 0} \\ C_{00} & C_{00} \end{pmatrix}, \quad C_{\mu 0} = \frac{1}{\lambda_0 N_0} \sum_{i=1}^{N_0} x_i^0 x_{i 0}^0, $

[第8页，第15段]
$ C_{00} = \frac{1}{\lambda_0 N_0} \sum_{i=1}^{N_0} (x_{i 0}^0)^2. $

[第8页，第16段]
现在我们可以通过公式 (47) 及其傅里叶表示引入序参量 $ Q $ 和 $ \hat{Q} $，并对所有 $ s^\mu, \hat{s}^\mu $ 以及 $ \hat{s}^0 $ 执行积分。这样做得到关于 $ s^0 $ 的单一积分以及关于 $ Q $ 和 $ \hat{Q} $ 的积分。

[第8页，第17段]
$ \langle \epsilon_g(\mathbf{x}^0, y^0) \rangle = \frac{1}{2} \int \frac{dQ d\hat{Q}}{2\pi} e^{-\frac{N_1}{2} S(Q, \hat{Q})} \times \int \frac{ds^0 (y^0 - s^0)^2}{\sqrt{2\pi \sigma^2}} e^{-\frac{(\sigma^0 + \tau_1)^2}{2 \sigma^2}}, $

[第8页，第18段]
其中

[第8页，第19段]
$ \Gamma_1 = \frac{\hat{Q}}{\lambda_1} \sum_{\mu} K_{\mu} (\mathbf{x}^0) \left( \frac{1}{\beta} + \frac{\hat{Q}}{\lambda_1} K_1 \right)^{-1} y_\nu, $

[第8页，第20段]
$ \sigma_1^2 = \frac{\hat{Q}}{\lambda_1} \left[ K_0 (\mathbf{x}^0) - \frac{\hat{Q}}{\lambda_1} \sum_{\mu} K_{\mu} (\mathbf{x}^0) \left( \frac{1}{\beta} + \frac{\hat{Q}}{\lambda_1} K_1 \right)^{-1} K_\nu (\mathbf{x}^0) \right] $

[第8页，第21段]
然后我们可以展开关于 $ s^0 $ 的简单积分，并在鞍点解上计算结果。泛化误差用 $ \Gamma_1 $ 和 $ \sigma_1^2 $ 表示，如公式 (8) 所示。在公式 (54) 中取 $ \beta \to \infty $ 极限即可得到公式 (8) 中的表达式。

[第8页，第22段]
### 数据集规模 $ P $ 与输入维度 $ N_0 $ 之间标度关系的约束

[第8页，第23段]
在本节中，我们讨论热力学标度（$ P, N_1 \to \infty $，且 $ \alpha_1 = P/N_1 $ 有限）可能受到的额外约束，这些约束可能来自关于协方差矩阵 $ C $ 的 Breuer–Major 定理的假设。唯一需要验证的严格条件是公式 (29)，即

[第8页，第24段]
$ \sum_{\mu=1}^{P} |C_{\mu \nu}|^R < B_0 \forall \nu = 1, \ldots, P, $

[第8页，第25段]
其中 $ B_0 $ 是给定的有限常数，$ R $ 是激活函数 $ \sigma $ 的 Hermite 秩。在输入 $ \mathbf{x} $ 具有独立同分布的标准高斯坐标的情况下，$ C_{\mu \nu} $ 是一个 Wishart 随机矩阵，其非对角元素量级为 $ 1/\sqrt{N_0} $ 且符号随机：取绝对值后，公式 (55) 中的求和量级为 $ P(N_0)^{-R/2} $。注意这提供了一类无限的激活函数（那些 Hermite 秩 $ R \geq 2 $ 的），我们至少可以在有限 $ \alpha_0 = P/N_0 $ 下安全地工作。对于 Hermite 秩 $ R = 1 $ 的激活函数（如 Erf 或 ReLU），我们仅通过查看 Breuer–Major 定理的假设无法提供这样的保证。还值得强调的是，给定任何 Hermite 秩 $ R = 1 $ 的奇（非奇）激活函数 $ \sigma(x) $，很容易构造一个新的合理的 Hermite 秩 $ R = 3 $（$ R = 2 $）的激活函数，只需将奇激活函数替换为新的 $ \sigma_1(x) = \sigma(x) - g_1 x $，其中系数 $ g_1 = (\sigma(x) \text{He}_1(x)) $，平均值是在零均值单位方差的 normal 分布上取的。

[第8页，第26段]
我们观察到至少存在一个 $ R = 1 $ 的激活函数案例，其推导在有限 $ \alpha_0 $ 下成立，即线性函数 $ \sigma(x) = x $（在这种情况下，我们可以在有限 $ P, N_1, N_0 $ 下获得结果，如参考文献 55 所做）。在补充材料第 2 节中，我们研究了二次激活 $ \sigma(x) = x + x^2 $（其 $ R = 1 $）的具体情况，在不使用 Breuer–Major 定理的情况下推导了最终的有效作用量。与线性情况一样，该推导在有限 $ \alpha_0 $ 下成立。因此我们认为，对于 $ R = 1 $ 所建议的标度 $ P = O(\sqrt{N_0}) $ 过于悲观。

[第8页，第27段]
### 推广到具有有限隐藏层数 $ L > 1 $ 和零均值激活的深度神经网络

[第8页，第28段]
按照与单隐藏层（1HL）计算相同的思路，我们引入 $ L $ 组辅助变量 $ h^\mu_{i \nu} $（其中 $ i, \nu = 1, \ldots, N_\nu $），它们等于每一层的预激活。执行计算的策略是证明每一层预激活的概率分布 $ P_c(h^\mu_{i \nu}) $ 可以从输入层开始递归计算。我们注意到这在概念上不同于参考文献 5 中引入的反向传播核重整化群。它仍然是一个核重整化群，但是前向传播的，并且代表了 NNPGP 中出现的核递推关系向 NNTP 的推广。在实践中，我们的方法相当于用 Student's $ t $-分布（该分布在 1HL 情况下出现）对预激活统计量进行系统的逐层描述。这可以看作是对无限宽度极限下恢复的标准高斯统计量的定量修正。目前我们无法使用参考文献 5 中引入的反向传播方法重新推导相同的结果。

[第8页，第29段]
让我们从对第一层权重进行积分开始。这通过以下方式定义了第一层预激活上的概率分布：

[第8页，第30段]
$ P_1(h^\mu_{i \nu}) = \int \mathcal{D}W^{(1)} \prod_{i, \mu} \delta \left( h^\mu_{i \nu} - \frac{1}{\sqrt{N_0}} \sum_{i=1}^{N_0} W^{(1)}_{i \nu} x^\mu_{i \nu} \right) $

[第8页，第31段]
$ = \prod_{i=1}^{N_1} \frac{e^{-\frac{1}{2} \sum_{\mu=1}^{P} \hat{\sigma}_1^2 \hat{\sigma}_1^2 x^\mu_{i \nu}}}{\sqrt{(2\pi)^P \det C}}. $

[第9页，第1段]
其中 $  C  $ 在方程 (40) 中定义。该结果是直接的，并且对任意 $  N_0, P  $ 和 $  N_t  $ 都成立，因为权重的先验是高斯分布。在第二层我们有：

[第9页，第2段]
$ 
P_2(h_{t_1}^{H}) = \int \mathcal{D}W^{(2)} \mathcal{D}h_1 P_1(h_{t_1}^{H}) \\
\times \prod_{i, \mu} \delta \left( h_{t_1}^{H} - \frac{1}{\sqrt{N_i}} \sum_{i=1}^{N_t} W_{i, t_1}^{(2)} \sigma(h_{t_1}^{H}) \right)
 $

[第9页，第3段]
我们现在为第二层的激活引入共轭变量 $  \tilde{h}_{t_1}^{H}  $，计算过程与 1HL 架构的情形相同。为了取得分析上的进展，我们需要做出两个基本近似：(1) 我们假设随机变量集合 $  q_{i, s} = 1/(\sqrt{N_i} \Lambda_i) \sum_{\mu} \tilde{h}_{t_1, s}^{H} \sigma(h^{H})  $（其中 $  h \approx N(0, C)  $）服从高斯分布；(2) 我们忽略第二隐藏层不同预激活之间的相关性。总之，我们得到：

[第9页，第4段]
$ 
P_2(h_{t_1}^{H}) = \int dQ_1 d\tilde{Q}_1 e^{-\frac{N_1}{2} (-Q_1 \tilde{Q}_1 + \log(1 + Q_1))} \\
\times \prod_{i, \mu} \frac{e^{-\frac{1}{2} \sum_{\mu} h_{t_1, \mu}^{H} (\tilde{Q}_1 K(C)/\Lambda_i)} e^{\frac{1}{2} \sum_{\mu} h_{t_1, \mu}^{H} (\tilde{Q}_1 K(C)/\Lambda_i)}}{\sqrt{(2\pi)^d \det(\tilde{Q}_1 K(C)/\Lambda_i)}},
 $

[第9页，第5段]
其中 $  K(C)  $ 由方程 (42) 定义。注意，除了对两个变量 $  Q_1  $ 和 $  \tilde{Q}_1  $ 的积分之外，如果我们将 $  C  $ 替换为 $  \tilde{Q}_1 K(C)/\Lambda_i  $，这与 1HL 系统的概率分布（方程 (40)）相同。这一推理可以很容易地逐层迭代，得到：

[第9页，第6段]
$ 
P_L(h_{t_1}^{H}) = \int \prod_{\ell=1}^{L-1} dQ_\ell d\tilde{Q}_\ell e^{-\sum_{\ell=1}^{L-1} \sum_{\mu} \frac{1}{2} \sum_{\mu} \left[ -Q_\ell \tilde{Q}_\ell + \log(1 + Q_\ell) \right]} \\
\times \prod_{i, \mu} \frac{e^{-\frac{1}{2} \sum_{\mu} h_{t_1, \mu}^{H} (\tilde{Q}_1 K(C)/\Lambda_i)} e^{\frac{1}{2} \sum_{\mu} h_{t_1, \mu}^{H} (\tilde{Q}_1 K(C)/\Lambda_i)}}{\sqrt{(2\pi)^d \det(\tilde{Q}_1 K(C)/\Lambda_i)}},
 $

[第9页，第7段]
其中 $  K_\ell^{(R)} (\tilde{Q}_\ell)  $ 是一个重整化核（renormalized kernel），满足方程 (15) 中的递推关系。

[第9页，第8段]
在一个新样本 $  (x^0, y^0)  $ 上的泛化误差计算给出：

[第9页，第9段]
$ 
\langle \epsilon_g(x^0, y^0) \rangle = (y^0 - \Gamma_L)^2 + \sigma_\ell^2
 $

[第9页，第10段]
其中 $  \Gamma_L  $ 和 $  \sigma_\ell^2  $ 在方程 (17) 中定义。注意 $  k_{t_1, \mu}^{(R)}  $、$  k_{t_1, \mu}^{(R)}  $ 是递归核（recursive kernels），它们推广了训练–测试核与测试–测试核（方程 (51)）。它们从方程 (15) 出发定义，其中核 $  K  $ 现在用涉及训练–测试点或测试–测试点的协方差矩阵 $  C  $ 来求值。注意，$  L  $ 个隐藏层的泛化误差是通过将 1HL 核替换为其递归推广（方程 (15)）得到的。

[第9页，第11段]
### 数值实验

[第9页，第12段]
**网络架构。** 我们使用深度全连接架构进行数值实验，在计算机视觉中的两个回归任务上进行训练。具体而言，我们使用 MNIST 和 CIFAR10 数据集的 0 类和 1 类，对于后者，它们对应于标签“汽车”和“飞机”（图 1a）。CIFAR10 的样本被粗粒化为 $  N_0 = 28 \times 28  $ 像素并转换为灰度。

[第9页，第13段]
为了在零均值激活函数的情形下检验我们的理论，我们使用了 Erf 函数，其 NNGP 核可以解析计算：

[第9页，第14段]
$ 
K_{f}^{Erf}(C) = \frac{2}{\pi} \arcsin \left( \frac{2C_{\mu\nu}}{\sqrt{(1 + 2C_{\mu\nu})(1 + 2C_{\nu\nu})}} \right).
 $

[第9页，第15段]
在图 2 中，我们训练了使用 $  \sigma = \text{ReLU}  $ 的网络。在这种情况下核也可以解析计算，其形式为：

[第9页，第16段]
$ 
K_{f}^{ReLU}(C) = \sqrt{C_{\mu\nu} C_{\nu\nu}} K \left( \frac{C_{\mu\nu}}{\sqrt{C_{\mu\nu} C_{\nu\nu}}} \right),
 $

[第9页，第17段]
$ 
K(x) = \frac{1}{2\pi} \left[ x(\pi - \arccos(x)) + \sqrt{1 - x^2} \right].
 $

[第9页，第18段]
**从贝叶斯后验中采样。** 为确保后验权重分布收敛到吉布斯系综（Gibbs ensemble），我们使用离散化朗之万动力学（Langevin dynamics）训练网络，与文献 3、5 中的做法类似。在每个训练步 $  t  $，参数 $  \theta = \{W^t, \nu\}  $ 按如下方式更新：

[第9页，第19段]
$ 
\theta(t+1) = \theta(t) - \eta \nabla_\theta \mathcal{L}(\theta(t)) + \sqrt{2T \eta} \epsilon(t)
 $

[第9页，第20段]
其中 $  T = 1/\beta  $ 是温度，$  \eta  $ 是学习率，$  \epsilon(t)  $ 是白高斯噪声向量，其分量取自标准正态分布，损失为方程 (3) 中定义的损失。我们在所有实验中都采用 $  T = \eta = 10^{-3}  $。这足以在我们所考虑的区域中近似 $  T = 0  $ 的动力学。该动力学需要 $  10^5/10^6  $ 步才能达到热化，具体取决于数据集和网络的规模。我们在单次运行中提取泛化损失：在训练误差达到最小值且测试损失热化之后，我们每隔 $  10^3/10^4  $ 个 epoch（同样取决于 $  P, N_t  $ 的大小）对测试损失值取平均。为完整起见，我们报告 1HL 架构在两个数据集上取得的最佳测试准确率：在 CIFAR10 上为 0.86（$  P = 3,000  $，$  \Lambda_1 = 1,000  $），在 MNIST 上为 0.999（相同的高斯先验，$  P = 1,000  $）。训练准确率始终为 1。关于模拟贝叶斯动力学时遇到的技术问题的进一步讨论见补充第 5 节。

[第9页，第21段]
### 数据可用性

[第9页，第22段]
我们所有实验使用的 CIFAR10 和 MNIST 数据集均可在网上公开获取，分别位于 https://www.cs.toronto.edu/~kriz/cifar.html 和 http://yann.lecun.com/exdb/mnist/。

[第9页，第23段]
### 代码可用性

[第9页，第24段]
用于执行实验、计算理论预测和分析数据的代码可在以下地址获取：https://github.com/rpacelli/FC_deep_bayesian_networks（文献 74）。

[第9页，第25段]
### 参考文献

[第9页，第26段]
1. Goodfellow, J., Bengio, Y. & Courville, A. Deep Learning (MIT Press, 2016).
2. Engel, A. & Van den Broeck, C. Statistical Mechanics of Learning (Cambridge Univ. Press, 2001).
3. Seroussi, I., Naveh, G. & Ringel, Z. Separation of scales and a thermodynamic description of feature learning in some CNNs. Nat. Commun. 14, 908 (2023).
4. Wakhloo, A. J., Sussman, T. J. & Chung, S. Linear classification of neural manifolds with correlated variability. Phys. Rev. Lett. 131, 027301 (2023).
5. Li, Q. & Sompolinsky, H. Statistical mechanics of deep linear neural networks: the backpropagating kernel renormalization. Phys. Rev. X 11, 031059 (2021).
6. Baldassi, C. et al. Learning through atypical phase transitions in overparameterized neural networks. Phys. Rev. E 106, 014116 (2022).
7. Canatar, A., Bordelon, B. & Pehlevan, C. Spectral bias and task-model alignment explain generalization in kernel regression and infinitely wide neural networks. Nat. Commun. 12, 2914 (2021).
8. Mozeika, A., Li, B. & Saad, D. Space of functions computed by deep-layered machines. Phys. Rev. Lett. 125, 168301 (2020).

[第10页，第1段]
9. Goldt, S., Mézard, M., Krzakala, F. & Zdeborová, L. 建模数据结构对神经网络学习的影响：隐藏流形模型 (hidden manifold model)。*Phys. Rev. X* **10**, 041044 (2020)。

[第10页，第2段]
10. Bahri, Y. 等。深度学习的统计力学。*Ann. Rev. Condensed Matter Phys.* **11**, 501–528 (2020)。

[第10页，第3段]
11. Li, B. & Saad, D. 探索深度学习机器的函数空间。*Phys. Rev. Lett.* **120**, 248301 (2018)。

[第10页，第4段]
12. Neal, R. M. 在 *Bayesian Learning for Neural Networks* 中，29–53 (Springer, 1996)。

[第10页，第5段]
13. Williams, C. 用无限网络进行计算。在 *Proc. 9th International Conference on Neural Information Processing Systems* 中 (eds Jordan, M. I. & Petsche, T.) 295–301 (MIT Press, 1996)。

[第10页，第6段]
14. de G. Matthews, A. G., Hron, J., Rowland, M., Turner, R. E. & Ghahramani, Z. 宽深度神经网络中的高斯过程行为 (Gaussian process behaviour)。在 *International Conference on Learning Representations* 中 (ICLR, 2018)。

[第10页，第7段]
15. Lee, J. 等。深度神经网络作为高斯过程 (Gaussian processes)。在 *International Conference on Learning Representations* 中 (ICLR, 2018)。

[第10页，第8段]
16. Garriga-Alonso, A., Rasmussen, C. E. & Aitchison, L. 深度卷积网络作为浅层高斯过程 (shallow Gaussian processes)。在 *International Conference on Learning Representations* 中 (ICLR, 2019)。

[第10页，第9段]
17. Novak, R. 等。具有多通道的贝叶斯深度卷积网络是高斯过程 (Gaussian processes)。在 *International Conference on Learning Representations* 中 (ICLR, 2019)。

[第10页，第10段]
18. Jacot, A., Gabriel, F. & Hongler, C. 神经正切核 (Neural tangent kernel)：神经网络中的收敛与泛化。在 *Proc. 32nd International Conference on Neural Information Processing Systems* 中 (eds. Bengio, S. 等) 8580–8589 (Curran Associates, 2018)。

[第10页，第11段]
19. Chizat, L., Oyallon, E. & Bach, F. 关于可微编程中的惰性训练 (lazy training)。在 *Proc. 33rd International Conference on Neural Information Processing Systems* 中 (eds. Wallach, H. 等) 2937–2947 (Curran Associates, 2019)。

[第10页，第12段]
20. Lee, J. 等。任意深度的宽神经网络在梯度下降下演化为线性模型 (linear models)。在 *Proc. 33rd International Conference on Neural Information Processing Systems* 中 (eds Wallach, H. 等) 8572–8583 (Curran Associates, 2019)。

[第10页，第13段]
21. Cortes, C. & Vapnik, V. 支持向量网络 (Support-vector networks)。*Mach. Learn.* **20**, 273–297 (1995)。

[第10页，第14段]
22. Bordelon, B., Canatar, A. & Pehlevan, C. 核回归和宽神经网络中谱依赖的学习曲线 (Spectrum dependent learning curves)。在 *Proc. 37th International Conference on Machine Learning* 中 (eds Daumé, H. III & Singh, A.) 1024–1034 (PMLR, 2020)。

[第10页，第15段]
23. Dietrich, R., Opper, M. & Sompolinsky, H. 支持向量网络的统计力学。*Phys. Rev. Lett.* **82**, 2975–2978 (1999)。

[第10页，第16段]
24. Seleznova, M. & Kutyniok, G. 超越无限宽度极限的神经正切核 (Neural tangent kernel)：深度和初始化的影响。预印本见 https://arxiv.org/abs/2202.00553 (2022)。

[第10页，第17段]
25. Vyas, N., Bansal, Y. & Preetum, N. NTK 在理解深度学习泛化方面的局限性。预印本见 https://arxiv.org/abs/2206.10012 (2022)。

[第10页，第18段]
26. Antognini, J. M. 神经网络高斯过程的有限尺寸修正 (Finite size corrections)。预印本见 https://arxiv.org/abs/1908.10030 (2019)。

[第10页，第19段]
27. Yaida, S. 有限宽度下的非高斯过程 (Non-Gaussian processes) 和神经网络。在 *Proc. 1st Mathematical and Scientific Machine Learning Conference* 中 (eds Lu, J. & Ward, R.) 165–192 (PMLR, 2020)。

[第10页，第20段]
28. Hanin, B. 随机全连接神经网络作为微扰可解层级 (perturbatively solvable hierarchies)。预印本见 https://arxiv.org/abs/2204.01058 (2023)。

[第10页，第21段]
29. Zavatone-Veth, J. & Pehlevan, C. 有限贝叶斯神经网络的精确边缘先验分布 (Exact marginal prior distributions)。在 *Advances in Neural Information Processing Systems* 中 (eds Vaughan, J. 等) 3364–3375 (Curran Associates, 2021)。

[第10页，第22段]
30. Bengio, Y. & Delalleau, O. 在 *Algorithmic Learning Theory* 中 (eds Kivinen, J. 等) 18–36 (Springer, 2011)。

[第10页，第23段]
31. Bartlett, P. L., Harvey, N., Liaw, C. & Mehrabian, A. 分段线性神经网络的近乎紧的 VC 维和伪维界 (Nearly-tight VC-dimension and pseudodimension bounds)。*J. Mach. Learn. Res.* **20**, 2285–2301 (2019)。

[第10页，第24段]
32. Rotondo, P., Lagomarsino, M. C. & Gherardi, M. 计算几何结构化数据的可学习函数。*Phys. Rev. Res.* **2**, 023169 (2020)。

[第10页，第25段]
33. Rotondo, P., Pastore, M. & Gherardi, M. 超越存储容量：数据驱动的可满足性转变 (data-driven satisfiability transition)。*Phys. Rev. Lett.* **125**, 120601 (2020)。

[第10页，第26段]
34. Pastore, M., Rotondo, P., Erba, V. & Gherardi, M. 结构化数据的统计学习理论。*Phys. Rev. E* **102**, 032119 (2020)。

[第10页，第27段]
35. Gherardi, M. 结构化数据线性可分性的可解模型。*Entropy* **23**, 305 (2021)。

[第10页，第28段]
36. Pastore, M. 结构化数据分类问题中 SAT/UNSAT 转变的临界性质。*J. Stat. Mech.* **2021**, 113301 (2021)。

[第10页，第29段]
37. Aguirre-López, F., Pastore, M. & Franz, S. 非对称神经网络中的可满足性转变 (Satisfiability transition)。*J. Phys. A* **55**, 305001 (2022)。

[第10页，第30段]
38. Saxe, A. M., McClelland, J. L. & Ganguli, S. 深度线性神经网络中学习非线性动力学的精确解。在 *Proc. 2nd International Conference on Learning Representations* 中 (eds. Bengio, Y. & LeCun, Y.) (ICLR, 2014)。

[第10页，第31段]
39. Saxe, A. M., McClelland, J. L. & Ganguli, S. 深度神经网络中语义发展的数学理论。*Proc. Natl Acad. Sci. USA* **116**, 11537–11546 (2019)。

[第10页，第32段]
40. Zavatone-Veth, J., Canatar, A., Ruben, B. & Pehlevan, C. 有限贝叶斯神经网络中表示学习的渐近性 (Asymptotics of representation learning)。在 *Advances in Neural Information Processing Systems* 中 (eds Vaughan, J. W. 等) 24765–24777 (Curran Associates, 2021)。

[第10页，第33段]
41. Naveh, G. & Ringel, Z. 高斯过程的自洽理论捕捉有限 CNN 中的特征学习效应。在 *Advances in Neural Information Processing Systems* 中 (eds Vaughan, J. W. 等) 21352–21364 (Curran Associates, 2021)。

[第10页，第34段]
42. Zavatone-Veth, J. A., Tong, W. L. & Pehlevan, C. 深度贝叶斯线性回归中随机特征与学习特征的对比。*Phys. Rev. E* **105**, 064118 (2022)。

[第10页，第35段]
43. Bardet, J.-M. & Surgailis, D. 高斯从属数组的矩界和中心极限定理 (Moment bounds and central limit theorems)。*J. Multivariate Anal.* **114**, 457–473 (2013)。

[第10页，第36段]
44. Nourdin, I., Peccati, G. & Podolskij, M. 定量 Breuer–Major 定理。*Stochastic Process. Appl.* **121**, 793–812 (2011)。

[第10页，第37段]
45. Breuer, P. & Major, P. 高斯场非线性泛函的中心极限定理。*J. Multivariate Anal.* **13**, 425–441 (1983)。

[第10页，第38段]
46. Gerace, F., Loureiro, B., Krzakala, F., Mezard, M. & Zdeborova, L. 使用随机特征和隐藏流形模型学习中的泛化误差。在 *Proc. 37th International Conference on Machine Learning* 中 (eds Daumé, H. III & Singh, A.) 3452–3462 (PMLR, 2020)。

[第10页，第39段]
47. Loureiro, B. 等。使用教师-学生模型对现实数据集的通用特征映射的学习曲线。*J. Stat. Mech.* https://doi.org/10.1088/1742-5468/ac9825 (2021)。

[第10页，第40段]
48. Goldt, S. 等。浅层神经网络学习中生成模型的高斯等价性 (gaussian equivalence)。在 *Proc. 2nd Mathematical and Scientific Machine Learning Conference* 中 (eds. Bruna, J. 等) 426–471 (PMLR, 2022)。

[第10页，第41段]
49. Dobriban, E. & Wager, S. 预测的高维渐近性：岭回归和分类。*Ann. Stat.* **46**, 247–279 (2018)。

[第11页，第1段]
50. Mei, S. & Montanari, A. 随机特征回归的泛化误差：精确渐近与双下降曲线。*Commun. Pure Appl. Math.* **75**, 667–766 (2019)。

[第11页，第2段]
51. Ghorbani, B., Mei, S., Misiakiewicz, T. & Montanari, A. 高维线性化两层神经网络。*Ann. Stat.* **49**, 1029–1054 (2021)。

[第11页，第3段]
52. Ariosto, S., Pacelli, R., Ginelli, F., Gherardi, M. & Rotondo, P. 深度神经网络泛化差距的通用平均场上界。*Phys. Rev. E* **105**, 064309 (2022)。

[第11页，第4段]
53. Shah, A., Wilson, A. & Ghahramani, Z. Student-t过程作为高斯过程的替代方案。载于*第17届人工智能与统计国际会议论文集*（编 Kaski, S. & Corander, J.）877–885（PMLR，2014）。

[第11页，第5段]
54. Zavatone-Veth, J. A., Canatar, A., Ruben, B. S. & Pehlevan, C. 有限贝叶斯神经网络中表示学习的渐近性。*J. Stat. Mech.* 2022, 114008 (2022)。

[第11页，第6段]
55. Hanin, B. & Zlokapa, A. 深度线性网络的贝叶斯插值。*Proc. Natl Acad. Sci.* 120, e2301345120 (2023)。

[第11页，第7段]
56. Coolen, A. C. C., Sheikh, M., Mozeika, A., Aguirre-López, F. & Antenucci, F. 广义线性回归模型中过拟合的复本分析。*J. Phys. A* **53**, 365001 (2020)。

[第11页，第8段]
57. Mozeika, A., Sheikh, M., Aguirre-López, F., Antenucci, F. & Coolen, A. C. C. 通过统计物理得到高维线性回归的精确结果。*Phys. Rev. E* **103**, 042142 (2021)。

[第11页，第9段]
58. Uchiyama, Y., Oka, H. & Nono, A. 概率密度函数空间上的Student t过程回归。*Proc. ISCIE International Symposium on Stochastic Systems Theory and its Applications* **2021**, 1–5 (2021)。

[第11页，第10段]
59. Lee, H., Yun, E., Yang, H. & Lee, J. 神经网络高斯过程的尺度混合。载于*国际学习表示会议*（ICLR，2022）。

[第11页，第11段]
60. Aitchison, L. 为什么更大并不总是更好：论有限与无限神经网络。载于*第37届国际机器学习会议论文集*（编 Daumé, H. III & Singh, A.）156–164（PMLR，2020）。

[第11页，第12段]
61. Zavatone-Veth, J. A. & Pehlevan, C. 深度在过参数化线性贝叶斯神经网络中诱导尺度平均。载于*2021年第55届Asilomar信号、系统与计算机会议* 600–607（IEEE，2021）。

[第11页，第13段]
62. Yang, A. X., Robeyns, M., Milsom, E., Schoots, N. & Aitchison, L. 深度神经网络中表示学习理论给出核方法的深度泛化。预印本见 https://arxiv.org/abs/2108.13097 (2023)。

[第11页，第14段]
63. Cho, Y. & Saul, L. 深度学习的核方法。载于*神经信息处理系统进展*（编 Bengio, Y. 等）第22卷（Curran Associates，2009）。

[第11页，第15段]
64. Poole, B., Lahiri, S., Raghu, M., Sohl-Dickstein, J. & Ganguli, S. 通过瞬态混沌在深度神经网络中的指数表达性。载于*神经信息处理系统进展*（编 Garnett, R. 等）第29卷（Curran Associates，2016）。

[第11页，第16段]
65. Yang, G. & Schoenholz, S. 平均场残差网络：在混沌边缘。载于*神经信息处理系统进展*（编 Guyon, I. 等）第30卷（Curran Associates，2017）。

[第11页，第17段]
66. Tracey, B. D. & Wolpert, D. 从高斯过程升级到Student-t过程。载于*2018年AIAA非确定性方法会议* 1659 (2018)。

[第11页，第18段]
67. Roberts, D. A., Yaida, S. & Hanin, B. *深度学习理论原理*（剑桥大学出版社，2022）。

[第11页，第19段]
68. Gerace, F., Krzakala, F., Loureiro, B., Stephan, L. & Zdeborová, L. 高维随机标签线性分类器的高斯普适性。预印本见 https://arxiv.org/abs/2205.13303 (2022)。

[第11页，第20段]
69. Cui, H., Krzakala, F. & Zdeborová, L. 广泛宽度深度随机网络的贝叶斯最优学习。载于*第40届国际机器学习会议论文集*（编 Krause, A. 等）6468–6521（PMLR，2023）。

[第11页，第21段]
70. Lee, J. 等. 有限与无限神经网络：一项实证研究。载于*神经信息处理系统进展*（编 Lin, H. 等）15156–15172（Curran Associates，2020）。

[第11页，第22段]
71. Pang, G., Yang, L. & Karniadakis, G. E. 神经网络诱导的高斯过程回归用于函数逼近和PDE求解。*J. Comput. Phys.* **384**, 270–288 (2019)。

[第11页，第23段]
72. Krizhevsky, A. *从微小图像学习多层特征*（多伦多大学，2012）。

[第11页，第24段]
73. Lecun, Y., Bottou, L., Bengio, Y. & Haffner, P. 应用于文档识别的基于梯度的学习。*Proc. IEEE* **86**, 2278–2324 (1998)。

[第11页，第25段]
74. Pacelli, R. *rpacelli/FC_deep_bayesian_networks: FC_deep_bayesian_networks* (2023)。

[第11页，第26段]
**致谢**

[第11页，第27段]
M.P. 获得了西蒙斯基金会（Simons Foundation）的资助（资助号454941，S. Franz）。P.R. 感谢Fellini项目在H2020-MSCA-COFUND行动下的资助，资助协议号754496，INFN（意大利）以及#NEXTGENERATIONEU（NGEU）、国家复苏与韧性计划（NRRP）、项目MNESYS（PE0000006）“研究健康和疾病中神经系统的多尺度综合方法”（DN. 1553 11.10.2022）。我们感谢S. Franz、L. Molinari、F. Aguirre-López、R. Burioni、A. Vezzani、R. Aiudi、F. Bassetti、B. Bassetti、P. Baglioni以及米兰博科尼大学计算科学小组的讨论和建议。

[第11页，第28段]
**作者贡献**

[第11页，第29段]
P.R.、S.A.和M.P.在F.G、M.G.和R.P.的支持下进行了分析计算。数值实验、数据分析和数据可视化由R.P.完成。所有作者都参与了结果的讨论和解释以及论文的撰写和编辑。S.A和R.P.对本工作贡献相等。

[第11页，第30段]
**利益冲突**

[第11页，第31段]
作者声明无利益冲突。

[第11页，第32段]
**附加信息**

[第11页，第33段]
**补充信息** 在线版本包含补充材料，可在 https://doi.org/10.1038/s42256-023-00767-6 获取。

[第11页，第34段]
**通讯和材料请求** 应发送至P. Rotondo。

[第11页，第35段]
**同行评审信息** *Nature Machine Intelligence* 感谢匿名审稿人对本工作同行评审的贡献。

[第11页，第36段]
**重印和许可信息** 可在 www.nature.com/reprints 获取。

[第11页，第37段]
**出版商注** Springer Nature对已发表地图和机构隶属关系中的管辖权主张保持中立。

[第11页，第38段]
Springer Nature或其许可方（例如学会或其他合作伙伴）根据与作者或其他权利持有人签订的出版协议对本文拥有专有权；作者对本文接受稿版本的自我存档仅受此类出版协议条款和适用法律的约束。

[第11页，第39段]
© 作者，在Springer Nature Limited的独家许可下，2023
