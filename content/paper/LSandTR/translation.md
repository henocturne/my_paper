[第1页，第1段]
深度学习中的景观与训练机制

[第1页，第2段]
Mario Geiger, Leonardo Petrini, Matthieu Wyart *

[第1页，第3段]
洛桑联邦理工学院物理研究所，1015 洛桑，瑞士

[第1页，第4段]
文章信息 摘要

[第1页，第5段]
文章历史：
收稿日期：2021年2月8日
收到修改稿日期：2021年3月25日
接受日期：2021年4月3日
在线发布日期：2021年4月16日
编辑：Massimo Vergassola

[第1页，第6段]
关键词：
深度学习
阻塞（Jamming）
惰性训练（Lazy training）
特征学习（Feature learning）
神经网络
损失景观（Loss landscape）
维数灾难（Curse of dimensionality）
神经正切核（Neural tangent kernel）

[第1页，第7段]
深度学习算法在图像识别或围棋对弈等多种任务中引发了技术革命。然而，它们为何有效尚不清楚。归根结底，它们成功地对高维数据进行分类——由于高维空间的几何特性以及相关的维数灾难（curse of dimensionality），这通常是不可能实现的。理解何种结构、对称性或不变性使得图像等数据变得可学习，是一项根本性挑战。其他谜题包括：(i) 学习对应于最小化高维损失，该损失通常非凸，很可能陷入不良极小值。(ii) 深度学习的预测能力随拟合参数数量的增加而提高，即使在数据被完美拟合的情况下也是如此。在本手稿中，我们综述了阐明 (i, ii) 的最新结果，以及它们对（仍未解释的）维数灾难悖论所提供的视角。我们的理论讨论基于 $ h, \alpha) $ 平面，其中 $ h $ 控制参数数量，$ \alpha $ 控制网络初始化时输出的尺度，并在该平面上为两个常见图像分类数据集提供了新的系统性性能度量。我们认为不同的学习机制可以组织成相图。一条临界点线将欠参数化相与过参数化相 sharply 分隔开来。在过参数化网络中，学习可以在由平滑交叉（cross-over）分隔的两种机制下运行。在较大初始化下，它对应于核方法（kernel method），而在较小初始化下，特征可以与数据中的不变量一起被学习。我们综述了这些不同相的性质、分隔它们的转变以及一些开放问题。我们的处理强调与物理系统的类比、标度论证（scaling arguments）以及数值可观测量（numerical observables）的发展，以在经验上定量检验这些结果。还讨论了实际意义，包括对具有不同初始权重的网络进行平均的好处，或选择参数 $ h, \alpha) $ 以优化性能。

[第1页，第8段]
© 2021 作者。由 Elsevier B.V. 出版。这是一篇根据 CC BY 许可（http://creativecommons.org/licenses/by/4.0/）发布的开放获取文章。

[第1页，第9段]
目录

[第1页，第10段]
1. 引言...................................................................................................................................................... 2
   1.1. 深度学习的介绍及其成功的量化.............................................................. 2
   1.2. 深度学习为何不应有效................................................................................................................ 4
   1.3. 关于这些悖论的当前见解............................................................................................................ 5
   1.4. 手稿的组织结构.................................................................................................................... 6
2. 损失景观与阻塞转变................................................................................................................ 8
3. 双下降与过参数化的好处....................................................................................... 11
4. 解耦 NTK 与特征学习机制......................................................................................... 12

[第1页，第11段]
* 通讯作者。
电子邮件地址：matthieu.wyart@epfl.ch (M. Wyart)。

[第1页，第12段]
https://doi.org/10.1016/j.physrep.2021.04.001
0370-1573/© 2021 作者。由 Elsevier B.V. 出版。这是一篇根据 CC BY 许可（http://creativecommons.org/licenses/by/4.0/）发布的开放获取文章。

[第2页，第1段]
通过压缩无关输入维度学习简单不变量。13
结论。14
竞争利益声明。15
致谢。15
参考文献。15

[第2页，第2段]
1. 引言

[第2页，第3段]
人类或人工智能的先决条件之一是理解通常位于高维空间中的数据。一个经典案例是计算机视觉，其目标是分类一张图片的内容[1]，而图片的维度是像素的数量。在本综述所考虑的有监督设置中，算法从已知的、带标签的数据中进行训练。例如，给定一百万张猫和狗图片的训练集，并且知道哪张是哪张。目标是构建一个算法，能够从这些示例中学习规则，并预测一张新图片是猫还是狗。经过六十年相当温和的进展之后，机器学习正在经历一场革命。深度学习算法[2]受我们视觉皮层组织的启发，如今在广泛的任务中取得了显著成功，包括语音[3]和文本识别[4]、自动驾驶汽车[5]，以及在围棋[6]或电子游戏[7]中击败最优秀的人类。然而，对于这些算法为何有效，人们的理解仍然非常有限。如下文所解释的，有若干原因说明为什么深度学习特别是、以及有监督学习一般而言本不应有效。最突出的是与高维空间几何相关的维数灾难，它阻碍了在一般设置下的学习。如果高维数据可以被学习，那么它们必定具有大量结构、不变性和对称性。理解这种结构的本质是什么，以及如何通过具有合适架构的神经网络来利用它，是我们时代的一项挑战。

[第2页，第4段]
在本引言的1.1节中，我们回顾使用深度网络进行有监督学习的基本流程，以及通过学习曲线指数对其成功进行量化。在1.2节中，我们讨论使这一成功令人惊讶的若干原因。这包括上文提到的维数灾难、损失景观中据称存在的坏极小值，以及深度学习通常在一个过参数化（over-parametrized）区域中工作这一事实，在该区域中拟合参数的数量远大于数据的数量。在1.3节中，我们回顾两个试图解决这些悖论的近期想法。首先，在网络参数数量发散的极限下，深度学习收敛到两个不同的、定义良好的算法（惰性训练（lazy training）和特征学习（feature learning）），具体取决于初始化的尺度。在每个区域中，都能找到损失的全局最小值。其次，在图像分类的背景下，有人假设深度学习能够有效应对维数灾难，因为神经网络学会了变得对图像的平滑变形不敏感。

[第2页，第5段]
这两类工作提出了各种问题，详见下文。简而言之：(i) 是否存在一个临界参数数量，一旦进入过参数化区域，损失中的坏极小值就消失？这种转变的本质是什么，其附近损失景观的几何结构如何？(ii) 为什么即使超过这一转变，性能仍倾向于随参数数量渐近改善？(iii) 一旦进入过参数化区域，惰性训练和特征学习之间的交叉发生在何处？哪个区域表现更好，以及它如何依赖于数据结构和网络架构？(iv) 在特征学习区域中，简单不变量是如何被学习的，以及它如何影响学习曲线指数？本手稿的目标在本引言1.4节中阐述，既回顾在深度网络分类背景下针对这些问题的近期结果，也提供新的系统性经验数据，将这些结果统一到一个相图中。

[第2页，第6段]
1.1. 深度学习的介绍及其成功的量化

[第2页，第7段]
某些架构中的信号传播。深度学习是一种拟合过程，其中用于插值数据的函数形式依赖于许多参数，并且可以迭代地表示。表征这种函数形式的最先进（SOTA）架构可能极其复杂，这里我们仅限于本质属性。我们用$\tilde{f}_\theta(x)$表示网络对应于输入$x$的输出，由$\theta$参数化。我们将记号$f_\theta(x)$保留给预测模型，两者之间的关系将在式(9)中定义。对于全连接网络（FC）——从理论角度来看，这是研究最多的架构——输出函数可以递归地写为：

[第2页，第8段]
$$\tilde{f}_\theta(x) = a^{(L+1)},$$

[第2页，第9段]
$$a_\beta^{(i)} = \sum_\alpha \frac{1}{\sqrt{h}} W_{\alpha, \beta}^{(i)} \sigma \left( a_\alpha^{(i-1)} + B_\beta^{(i)} \right),$$

[第2页，第10段]
$$a_\beta^{(1)} = \sum_\alpha \frac{1}{\sqrt{d}} W_{\alpha, \beta}^{(1)} x_\alpha + B_\beta^{(1)},$$

[第2页，第11段]
其中$a_\alpha^{(i)}$是位于深度$i$的神经元$\alpha$的预激活，$L$是总层数。我们考虑具有固定数量隐藏层$L$的网络，每层大小为$h$，即网络宽度。在下文中，鉴于参数总数遵循$N \sim Lh^2$，我们将同时使用$h$和$N$来指代网络规模。在我们的记号中，集合

[第3页，第1段]
参数 $\theta$ 包括权重 $W_{\alpha,\beta}^{(i)}$ 和偏置 $B_{\alpha}^{(i)}$。$\sigma(z)$ 是非线性激活函数，例如 ReLU $\sigma(z) = \max(z, 0)$。按照通常做法，我们对权重使用“LeCun 初始化”，即将其按因子 $1/\sqrt{h}$ 缩放。这确保了无限宽度的极限不是平凡的，参见例如 [10] 中的讨论。我们在图 1 中表示该网络。

[第3页，第2段]
卷积神经网络 (Convolutional neural nets, CNNs) 受灵长类大脑启发，在包括图像分类在内的各种任务上表现远优于全连接网络 (FCs)。每个隐藏层由若干通道组成，每个通道将数据表示为一个特征图——本身也是一幅图像。CNNs 在图像的不同位置执行相同的操作，并强制这些操作是局部的。因此，CNNs 比 FCs 受到更多约束，它们可以通过强制某些权重相同（以实现平移不变性）而另一些为零（以实现局部性）从后者获得。

[第3页，第3段]
学习动力学。权重通过拟合训练集来学习，这是通过最小化损失或代价函数 $\mathcal{L}$ 来完成的。为简化符号，我们考虑一个二分类问题，其中包含 $P$ 个不同的训练数据，记为 $\{(\mathbf{x}_\mu, y_\mu)\}_{\mu=1}^P$。向量 $\mathbf{x}_\mu$ 是输入，位于 $d$ 维空间中，$y_\mu = \pm 1$ 是其标签。$\mathcal{L}$ 是对整个训练集的求和，表示每个数据的拟合程度：

[第3页，第4段]
$$\mathcal{L}(\theta) = \frac{1}{P} \sum_{\mu=1}^P \ell(y_\mu f(\mathbf{x}_\mu)),$$  \hspace{1cm} (4)

[第3页，第5段]
其中 $f$ 是模型，$\ell$ 是其参数的递减函数。常见选择包括线性（$\gamma = 1$）或二次（$\gamma = 2$）合页损失 $\ell(y_\mu f(\mathbf{x}_\mu)) = \max(0, \Delta_\mu)^\gamma$，其中 $\Delta_\mu \equiv 1 - y_\mu f(\mathbf{x}_\mu)$，或交叉熵 $\ell(y_\mu f(\mathbf{x}_\mu)) = \log(1 + \exp(-y_\mu f(\mathbf{x}_\mu)))$。合页损失的优点是，将损失方程 (4) 降为零等价于满足一组约束 $\Delta_\mu < 0$，对应于以单位间隔拟合数据。这一事实是与物理学中遇到的其他可满足性问题进行类比的基础，如下文所述。然而，对于 SOTA 架构在常规基准上的性能，这一选择并不会产生显著影响 [8]。

[第3页，第6段]
然后可以使用不同的过程来最小化 $\mathcal{L}$，从权重的随机初始化开始（这是一个需要牢记的重要事实）。特别是，梯度下降 (GD) 或随机梯度下降 (SGD) 常被使用。在 GD 的每一步中，计算 $\mathcal{L}$，并按照损失景观中负梯度的方向更新参数：

[第3页，第7段]
$$\theta^{(t+1)} = \theta^{(t)} - \eta \nabla_\theta \mathcal{L}(\theta^{(t)}),$$  \hspace{1cm} (5)

[第3页，第8段]
其中学习率 $\eta$ 控制步长。对于 SGD，在每个最小化时间步，不是像方程 (4) 中定义的那样在整个训练集上计算损失，而是只考虑进入求和的项的一个随机子集。根据所考虑的数据，各种技巧可以提高性能，包括早停（在损失触底之前停止最小化）或权重衰减（然后向损失中添加项以防止权重变得过大）。

[第4页，第1段]
[P1/1]
1 将讨论扩展到多类分类问题以及回归问题是直接的。

[第5页，第1段]
性能。学习完成后，可以通过计算误分类一个新数据的概率（即所谓的测试误差 $\epsilon$）来从测试集（未用于训练但分布与训练集相同的数据）估计泛化性能。学习一个任务需要多少数据由学习曲线 $\epsilon(P)$ 来刻画。通常观察到，在可用的训练集大小 $P$ 范围内，测试误差可以很好地用幂律衰减 $P^{-\beta}$ 来描述$^3$，其指数 $\beta$ 共同取决于数据和所选择的算法。在 [11] 中，报告了 SOTA 架构在几个任务上的 $\beta$：在神经机器翻译中 $\beta \approx 0.3-0.36$；在语言建模中 $\beta \approx 0.06-0.09$；在语音识别中 $\beta \approx 0.3$，在图像分类（ImageNet）中 $\beta \approx 0.3-0.5$。

[第5页，第2段]
深度网络学习数据的层次化表示。一旦学习发生，就可以分析神经元主要对数据中的哪些特征做出响应 [9,12]。引人注目的是，这些发现与在灵长类动物视觉皮层中所发现的情况非常相似：随着信号在网络中推进，神经元学会对数据越来越抽象的方面做出响应，如图 1 所示。这一观察被认为是深度学习为何有效的一个重要方面，然而理解抽象特征是如何动态学习的，以及它对性能的贡献有多大，仍然是一个挑战。

[第5页，第3段]
1.2. 为什么深度学习本不应奏效

[第5页，第4段]
维度灾难。一般性论证表明，当数据的维度 $d$ 很大时（这在实践中通常是这种情况），$\beta$ 应该非常小——因此学习本质上是不可能的。例如在一个回归任务中，如果对目标函数的唯一假设是其满足 Lipschitz 连续（Lipschitz continuity），那么测试误差的衰减速度无法保证快于指数 $\beta \sim 1/d$ [13]。这一维度灾难（curse of dimensionality）[14] 源于一个几何事实：最近邻数据点之间的距离 $\delta$ 在大 $d$ 下衰减极慢，为 $\delta \sim P^{-1/d}$，如图 2.A 所示。因此，基于距离的插值或分类方法对于一般数据预期会非常不精确。

[第5页，第5段]
损失景观中的坏极小值。另一个在 90 年代使深度学习不太受欢迎的问题涉及学习。损失函数没有凸性的保证，且参数空间是高维的。那么是什么阻止了学习动态陷入性能不佳、损失很高的极小值中，如图 2.B 所示？换句话说，在什么条件下可以保证训练数据被很好地拟合？损失景观是否类似于物理学中玻璃态系统的能量景观，其中极小值的数量随自由度数量呈指数增长 [15,16]？

[第5页，第6段]
过参数化。最后，神经网络通常在过参数化（over-parametrized）机制下训练，其中参数数量 $N$ 显著大于数据点数量 $P$。在这种机制下，它们的容量非常大：即使标签被随机化，它们也能拟合训练集 [17]。统计学习理论因此无法保证不会发生过拟合，也无法保证所学模型具有任何预测能力。事实上，从统计学教科书中，人们预期测试误差与模型参数数量之间呈钟形学习曲线关系，如图 2.C 所示。在这种观点下，当 $N$ 较小时，学习算法的假设类太小，导致所学预测器存在偏差。当 $N$ 较大时，由于对数据中噪声的过拟合而呈现大方差。深度学习一个非常令人困惑的方面是，增加 $N$ 超过所有数据被完美拟合的点并不会破坏预测能力，反而会改善它 [18–21]，如图 2 所示。

[第6页，第1段]
2 对于每个 $P$，都会训练一个不同的网络。

[第6页，第2段]
3 对于训练集中有有限比例被错误标记的数据集，人们预期测试误差最终会趋于一个有限值并保持平稳。然而，在各种基准测试中，实践中并未观察到测试误差的这种饱和现象，这表明此类噪声的幅度很小。

[第7页，第1段]
图3. A：有限宽度网络在函数空间中动力学的示意图。随着权重变化，函数沿着可表达函数的黑色流形演化，该流形是弯曲的。B：在无限宽度极限下，即使函数演化量为$  \mathcal{O}(1)  $，该流形也变得平坦：函数与权重之间的关系变为线性。C：势场中的相互作用粒子。当粒子数量很大时，描述其密度而非个体运动变得更为有利（图片由Eric Vanden-Eijnden慷慨分享）。

[第7页，第2段]
1.3. 关于这些悖论的当前见解

[第7页，第3段]
过参数化网络中不存在糟糕的极小值。最近，人们认识到，如果参数数量足够，深度学习的损失景观终究不是玻璃态的。关注具有大量参数（且只有一个隐藏层）的网络的理论工作，以及使用更现实架构的经验工作[22–25]，支持损失函数具有连通水平集的特性：参数空间中任何两个具有相同损失的点都可以通过一条损失恒定的路径相连。此外，对损失景观曲率（由Hessian矩阵的谱捕获）[26–28]和SGD动力学的经验研究[29,30]揭示，景观即使在底部也显示出大量平坦方向。对于欠参数化网络则并非如此[30]。

[第7页，第4段]
这些观察提出了关键问题。随着参数数量的增长，景观几何中是否存在相变？如果存在，其普适类是什么？它如何影响性能？

[第7页，第5段]
隐式正则化与无限宽度网络。如果过参数化网络可以拟合任何数据，它们如何能具有预测性？这必然意味着GD或SGD动力学导致损失景观的特定极小值，在这些极小值处函数比一般极小值更规则——这一现象被称为隐式正则化[18,19]。如图2所示，当$  N \to \infty  $时性能最佳，引发了对该极限的巨大兴趣。在这种情况下，GD对应于哪些算法？

[第7页，第6段]
NTK：输入信号在初始化时通过无限宽度全连接网络的传播现在已被充分理解。如果权重——在公式(3)中定义——被初始化为零均值、方差为1的独立同分布随机变量（这是我们在本工作中始终考虑的设定），输出函数$  \tilde{f}(x)  $是一个高斯随机过程。其协方差可以递归计算[31–36]。

[第7页，第7段]
最近人们认识到，学习动力学在此极限下也得到简化[10,37–41]。[10]的关键见解是，输出此时成为权重的线性函数，如图3A、B所示。从物理上讲，权重的极小变化可以正向干涉并将输出改变$  \mathcal{O}(1)  $，这足以学习，但不足以改变梯度$  \nabla_{\theta} \tilde{f}  $。

[第7页，第8段]
更形式化地说，有限时间下的梯度流动力学（GD的连续时间极限）总是可以用神经正切核（NTK）来描述，其定义为：

[第7页，第9段]
$ 
\Theta(\theta, x, y) = \nabla_{\theta} \tilde{f}_{\theta}(x) \cdot \nabla_{\theta} \tilde{f}_{\theta}(y),
 $

[第7页，第10段]
其中$  x, y  $是两个输入，$  \nabla_{\theta}  $是关于参数$  \theta  $的梯度。具体而言，$  \partial \tilde{f}(x)/\partial t  $可以表示为$  \Theta(\theta, x, x_i)  $的线性组合；即$  \tilde{f}  $在一个维度为$  P  $的空间中演化。一般来说，$  \Theta  $依赖于$  \theta  $，因而依赖于时间和初始化的随机性。然而当$  h \to \infty  $时，$  \Theta(\theta, x, y)  $收敛到一个与初始化无关的明确定义的极限，并且不随时间变化[10]：因此该极限下的深度学习本质上是一种核方法。⁴

[第7页，第11段]
特征学习（流体动力学）区域：无限宽度极限可以通过在输出定义中添加因子$  1/\sqrt{h}  $而以不同方式取得。此时权重必须显著变化才能使输出变为$  \mathcal{O}(1)  $并拟合数据。这一最近发现的极限在文献中被称为“平均场”、“丰富”但也称为“特征学习区域”，因为神经元学会如何响应输入数据的不同方面，如图1所示——而在NTK极限中，神经元的响应演化是无穷小的。这一区域已在多项工作中被研究，主要集中于单隐藏层网络[43–49]，最近也有对更深网络的发展，参见例如[50]。在此设定下，单隐藏层的输出函数为：

[第7页，第12段]
$ 
\tilde{f}_{\theta}(x) = \frac{1}{h} \sum_{i=1}^{h} W_{i}^{(2)} \sigma \left( \frac{1}{\sqrt{d}} W_{i}^{(1)} \cdot x + B_{i} \right),
 $

[第7页，第13段]
⁴ 核方法是一类机器学习算法，它们使用函数$  K(x, x')  $——即核——作为数据点之间的相似性度量。通常，预测函数可以写成形式$  f(x) = \sum_{i=1}^{p} \alpha_{i} K(x, x_{i})  $，其中参数$  \alpha_{i}  $是学习得到的，$  x_{i}  $是训练集中的点。支持向量机就是此类算法的一个例子。我们推荐[42]作为核方法的参考文献。

[第8页，第1段]
于是可以引用大数定律，将式 (7) 替换为一个积分：

[第8页，第2段]
$ 
\tilde{f}_\theta(x) \to \int dW^{(2)} dW^{(1)} dB \rho(W^{(2)}, W^{(1)}, B) W^{(2)} \sigma \left( \frac{1}{\sqrt{d}} W^{(1)} \cdot x + B \right)
 $

[第8页，第3段]
其中 $ \rho $ 是参数的密度。随后可以直接证明，梯度流会导致 $ \rho $ 上出现守恒量通常类型的一种动力学：它是通量的散度 $ \partial \rho / \partial t = -\nabla \cdot J $。这里的散度是相对于与单个神经元相关联的权重集合计算的，而通量遵循 $ J = \rho \Psi(W^{(2)}, W^{(1)}, B; \rho_t) $，其中 $ \Psi $ 是某个可以用损失[43]表示的函数。这种表述等价于处于某种外部势中的相互作用粒子的流体动力学描述。图 3.C 表明，当粒子（或神经元）数量很大时，$ \rho $ 是比追踪所有粒子位置（在此情况下即权重）更合适的描述。

[第8页，第4段]
惰性训练（lazy training）：深度学习在 $ h $ 发散时收敛到定义良好的算法这一事实，解释了为什么性能在该极限下收敛到一个定义良好的值（该值将取决于所考虑的极限），如图 2 所示。然而，这种在 NTK 不变化的区域与 NTK 演化且特征被学习的区域之间的区分，可以在有限 $ h $ 下做出。Chizat 和 Bach 提出了如下形式的模型[51]：

[第8页，第5段]
$ 
f_\theta(x) \equiv \alpha \left[ \tilde{f}_\theta(x) - \tilde{f}_\theta(t=0)(x) \right],
 $

[第8页，第6段]
$ \alpha = \mathcal{O}(1) $ 对应于 NTK 初始化，而 $ \alpha = \mathcal{O}(h^{-1/2}) $ 对应于平均场极限。在数据被拟合的过参数化区域（我们下文将严格定义它）中，当 $ \alpha \to \infty $ 且 $ h $ 有限时，权重的无穷小变化就足以进行学习，并且 NTK 不随时间演化（但在初始化时存在涨落）。这一区域有时被称为惰性训练，在我们的语境中，我们将交替地将其称为 NTK 区域。

[第8页，第7段]
总体而言，这些发现是我们对神经网络理解的最新突破。然而，它们提出了许多对本综述至关重要的问题。如果存在两个极限，哪一个最能刻画实际中使用的神经网络？哪一个极限会带来更好的性能？它如何依赖于架构和数据结构的？随着 $ h $ 增大，是哪种效应导致了性能的提升？

[第8页，第8段]
维数灾难与对微分同胚的不变性。Mallat 和 Bruna [52,53] 提出，对图像的平滑形变（即微分同胚（diffeomorphisms））的不变性，可能使深度网络克服维数灾难。具体而言，考虑输入向量 $ x $ 是一幅图像的情形。它可以被视为一个描述位置 $ s $ 处强度的函数 $ x(s) $，其中 $ s \in [0, 1]^2 $。微分同胚是一种双射形变，它将像素的位置 $ s $ 变为 $ s' = \tau(s) $。在我们下文的综述中，引入像素位移场 $ \xi(s) = \tau(s) - s $ 将会很有用，它类似于弹性力学中的核心位移场。我们用 $ T_\tau[x] $ 表示由 $ \tau $ 形变后的图像，即 $ T_\tau[x](s) = x(\tau^{-1}(s)) $。人们期望平滑的微分同胚不会影响图像的标签：如果 $ \|\nabla_s \xi\| \ll 1 $，则 $ \text{Prob}(y(x) \neq y(T_\tau[x])) \ll 1 $。

[第8页，第9段]
Mallat 和 Bruna 能够手工设计出对平滑微分同胚不敏感且表现良好的 CNN，即“散射变换”（scattering transform）：

[第8页，第10段]
$ 
 $

[第8页，第11段]
他们假设，在训练过程中，CNN 会学习满足式 (10)。在这种观点下，通过变得对数据中许多与任务无关的方面不敏感，CNN 有效地降低了数据维度，并使问题变得可处理。

[第8页，第12段]
这一框架的一个局限在于，它几乎没有说明不变量是如何被动态学习的。然而，这正是问题的核心。全连接网络（FC nets）比 CNN 更具表达能力，并且先验上没有什么能阻止它们学习这些不变量——然而，它们大概并没有做到，因为它们的性能无法与 CNN 相比。沿着这条路线，一个有趣的问题是如何开发可观测量，以经验性地刻画不变量的动态涌现。已经有人尝试使用互信息方法[54]，但这类方法在这种确定性设定中显示出问题[55]；或者使用基于数据神经表示的有效维度的度量[56,57]，这些度量具有信息量，但有时会导致反直觉的结果。在第 5 节中，我们将讨论基于 NTK 的核 PCA 的其他可观测量。

[第8页，第13段]
1.4. 手稿的组织结构

[第8页，第14段]
为了以统一的方式思考上述结果及其提出的问题，考虑图 4 是有用的。它展示了神经网络在平面 $ h, \tilde{\alpha}) $ 中性能的新颖经验数据，其中 $ h $ 是宽度，$ \tilde{\alpha} $ 是重新缩放的初始化幅度 $ \tilde{\alpha} = \sqrt{h\alpha} $。具体而言，图中展示了在 MNIST（一个手写数字数据集[59]）和 CIFAR10（飞机、狗等图像[60]）上使用 GD 训练的全连接网络的集成测试误差——这些数据集的样本报告于图 5 中。该集成测试误差是通过为相图中的每个点准备 $ M = 15 $ 个具有不同初始化的网络来计算的。然后展示的是 15 个训练后网络上的平均预测器 $ \langle f \rangle $ 的测试误差。黑色区域对应于欠参数化区域，在该区域中单个网络的损失不会收敛到

[第9页，第1段]
5 由于像素数量有限，这个空间实际上是离散的，但这并不改变讨论。

[第9页，第2段]
6 有效维度（effective dimension）是根据相邻点之间的距离 $ \delta $ 如何随其数量 $ P $ 变化来定义的，即 $ \delta \sim P^{-1/d_{\text{eff}}} $。其解释可能很微妙，因为观察到它有时会随着信息在网络中传播而增加，而对于表示数据的流形的真实维度来说，这不可能发生。

[第10页，第1段]
学习后为零。如下文所述，其边界对应于一条临界点线，该临界点线对应于一个“阻塞转变”（jamming transition），此时系统不再呈现粗糙的景观。在彩色过参数化区域中，黑线表示一个交叉（cross-over），将懒惰训练（lazy training）区域（其中单个网络在学习过程中NTK的总变化相对较小）与特征学习（feature learning）区域（其中NTK显著演化）分隔开。

[第10页，第2段]
图6显示了当$h$变化时，三个$\tilde{\alpha}$值下的测试误差和集成测试误差曲线。在阻塞转变处，测试误差显示出如[61]中观察到的峰值。类似的峰值出现在回归问题[21]中，其中它的起源更简单，并且发生在参数数量与数据数量匹配时。此后，这种测试误差的形状被称为双下降（double-descent）[62]。有趣的是，如图6所示，这种现象是独立发生的。

[第11页，第1段]
关于 $\tilde{\alpha}$ 的取值（以及由此进入的越过阻塞（jamming）的过参数化区域），并且在取系综平均时消失，正如 [63] 中所观察到并在 [64] 中最近所确认的那样。

[第11页，第2段]
我们的目标是以非技术性的方式回顾那些为该相图提供依据的概念和论证，并讨论在此背景下不变量的学习问题。在第2节中，我们将论证图4中黑色区域的边界是一条临界点线，类似于具有有限程相互作用的排斥粒子中发生的阻塞转变（jamming transition）。对于更宽的网络，能量景观（landscape）不是玻璃态的，并显示出许多平坦方向。我们将提供一个简单的几何论证，说明为什么深度网络中的这一转变属于椭球（而非球）粒子的普适类（universality classes），这确定了转变附近景观的性质（例如 Hessian 的谱）。我们将提及一个类似 Landau 的论证，用以解释该点处测试误差中的尖点（cusp）。在第3节中，我们将定量解释为什么随着宽度增加越过这一转变，测试误差会持续改善。增加宽度最终会消除由于权重随机初始化而产生的噪声，最终导致上文所引入的明确定义的算法。有限宽度下的系综平均有效地消除了这一噪声源以及双下降（double descent），如图6所示。在第4节中，我们将解释为什么懒惰（lazy）区域与特征学习（feature learning）区域之间的交叉在渐近意义上对应于图4中的一条水平线。我们将回顾以下观察：对于全连接架构，懒惰训练在标准图像数据集上优于特征学习，但对于 CNN 架构则不然，这对应于更大的学习曲线指数 $\beta$。在第5节中，我们回顾可以说是最简单的模型，其中神经网络学习数据结构中的不变量，其方式是考虑标签不依赖于输入空间中的某些方向。正如在真实数据中所观察到的那样，随后可以计算出懒惰和特征学习中的两个不同的训练指数 $\beta$。最后我们讨论开放性问题。

[第11页，第3段]
2. 损失景观与阻塞转变

[第11页，第4段]
最小化损失与最小化能量非常相似。描述物理系统的能量景观是一个被广泛研究的问题，尤其是在玻璃的背景下。在过去十五年中，通过考虑有限程相互作用，这一主题取得了进展，对于这类相互作用，将能量降为零等价于满足一组约束。在这种情况下，景观由一个临界点 [65–67] 控制，即所谓的阻塞转变（jamming transition）。它随着粒子密度 $\phi$ 的增加而发生。对于 $\phi > \phi_c$，从粒子随机初始位置开始的梯度下降会陷入众多亚稳态（meta-stable states）之一，对应于如图7B、D所示的玻璃态固体。对于较低的密度，梯度下降达到零能量，如图7E所示：粒子可以自由移动而没有恢复力，并且景观具有许多平坦方向。这对应于图7A、C中所描绘的情形。

[第11页，第5段]
阻塞有两种普适类（universality classes），导致景观曲率（即 Hessian 的谱）[68–73]、所获得的堆积结构 [74–77] 以及对扰动的动力学响应 [78,79] 具有不同的性质。球和椭圆属于不同的类，如图7所示。更一般地，阻塞转变一般地发生在具有连续自由度的可满足性问题中（它也可以用离散自由度来定义 [80]，但那时会有质的差异；特别是，目前的讨论不适用于离散情形）。它发生在感知机（perceptron）[81–83] 中，但也发生在深度网络中 [8,61]。

[第12页，第1段]
图7. 排斥球体和椭球体阻塞转变的示意图。(a, b, c, d) 当密度超过某个阈值时，两种系统都从流体转变为固体，球体的阈值记为$\phi_s$，椭球体的阈值记为$\phi_E$。(e) 对于更密集的堆积，势能$\mathcal{U}$变为有限值。(f) 接触粒子数$N_A$（对应于未满足的约束）与自由度数目$N$之间的比值$N_A/N$不连续地跳跃到一个有限值，对于球体该值为1，而对于椭球体则更小。(g, h) 这一差异对能量景观产生了显著影响，特别是对Hessian矩阵的谱。在两种情况下，谱在阻塞时变为非零，但椭球体的情况显示出一个具有有限权重的delta函数（表明存在严格平坦的方向），随后是一个无特征值的间隙，然后是一个连续谱（h，实线）。对于球体，既没有delta函数也没有间隙（g，实线）。当进入阻塞相时，在两种情况下谱中都会出现一个特征尺度$\lambda \sim \sqrt{\mathcal{U}}$（g和h，虚线）。

[第12页，第2段]
来源：摘自[8]。

[第12页，第3段]
图8. 相图，显示在训练结束时 hinge loss（铰链损失）是否达到零（蓝色）或未达到零（白色），随参数数量$N$和训练点数$P$变化，使用上述讨论的MNIST数据集（二分类，10个主成分），通过具有3个隐藏层的全连接网络进行训练。B 未满足模式数$N_A/N$作为训练结束时损失的函数，沿面板A中箭头所示方向。此处$N$固定，$P = 1, \ldots 70k$。C 阻塞附近Hessian矩阵中主导项$H_0$的谱（在B的矩形区域内对阻塞时的运行取平均）在零处呈现一个delta函数，在高频处呈现一个有间隙的连续谱，这是亚稳态阻塞（hypostatic jamming）的普遍特征。D 沿A中所示箭头的输出函数的涨落，对20个初始条件取平均。对于MNIST数据集，它渐近地以幂律$N^{-1/4}$衰减。在阻塞时，这些涨落急剧增大，与二次奇异性一致。

[第12页，第4段]
来源：摘自[8,63]。

[第12页，第5段]
下面我们将回顾[8]中引入的一个几何论证，该论证确定了阻塞转变的普适类。对于深度网络，阻塞属于椭球体的普适类[8,61]。阻塞转变附近损失的谱显示出零模、一个间隙和一个连续部分，如图8.C所测量。这一类比另一个含义是学习后边际小于1的数据数量$N_A$，这些数据对损失有贡献。这些数据在概念上类似于SVM算法中核心的支持向量。对于粒子，$N_A$对应于能量最小化后仍然重叠的粒子对数量。如图8.B所示，$N_A/N$在阻塞时从零跳跃到一个严格小于1的值，此时损失变为正值，正如椭球体所做的那样。

[第12页，第6段]
确定普适类的几何论证。在此我们试图对[8]的结果给出一个简单的直观解释（更严格的论证可在该文献中找到）。我们考虑连续可满足性问题，其中人们寻求最小化能量或

[第13页，第1段]
损失函数类型如下：

[第13页，第2段]
$ 
\mathcal{U} = \sum_{\mu \in m} \frac{1}{2} \Delta_{\mu}^{2}.
 $

[第13页，第3段]
其中求和是对所有未满足的约束进行的，对应于 $ \Delta_{\mu} > 0 $。量 $ \Delta_{\mu} $ 通常可以依赖于系统的 $ N $ 个自由度。对于粒子系统，$ \mathcal{U} $ 是能量，$ \Delta_{\mu} $ 是粒子对 $ \mu = (i, j) $ 之间的重叠量。对于球体，其表达式为 $ \Delta_{ij} = 2R - r_{ij} $，其中 $ R $ 是粒子半径，$ r_{ij} = \| \mathbf{r}_i - \mathbf{r}_j \| $ 是粒子 $ i $ 和 $ j $ 之间的距离。在这种情况下，$ N $ 是粒子数乘以空间维度。对于感知机或深度网络，$ \mathcal{U} $ 对应于通常在公式 (4) 中定义的二次铰链损失（记为 $ \mathcal{L} $）（将这些论证直接推广到 $ \gamma > 1 $ 的其他铰链损失是直接的 [8,65]，线性铰链的 $ \gamma = 1 $ 情况与这些有许多相似之处，但也表现出有趣的差异 [84]）。如引言中所定义，在这种情况下 $ \Delta_{\mu} = 1 - f(\mathbf{x}_\mu) \mathcal{Y}_{\mu} $。

[第13页，第4段]
由于阻塞转变是一个奇异点，因此从玻璃态（大密度 $ \phi $ 或欠参数化）相逼近是有用的——但并非严格必要$ ^8 $。这对应于 $ \mathcal{U} \to 0 $，如图 7E, F 所示，意味着 $ \Delta_{\mu} \to 0 \forall \mu \in m $。如 [85] 中所论证的，对于每个 $ \mu \in m $，约束 $ \Delta_{\mu} = 0 $ 定义了一个维度为 $ N - 1 $ 的流形。因此，满足 $ N_{\Delta} $ 个这样的方程通常会导致一个维度为 $ N - N_{\Delta} $ 的解流形。因此，要求解存在意味着在阻塞时，有：

[第13页，第5段]
$ 
N_{\Delta} \leq N.
 $

[第13页，第6段]
注意，这个论证隐含地假设了 $ N_{\Delta} $ 个约束是独立的，更多讨论见 [8]。

[第13页，第7段]
通过稳定性考虑，可以施加一个相反的界限，即要求在稳定最小值中 Hessian 矩阵必须是正定的 [68]。Hessian 是一个 $ N \times N $ 矩阵，可以写成：

[第13页，第8段]
$ 
\mathcal{H}_{\mathcal{U}} = \sum_{\mu \in m} \nabla \Delta_{\mu} \otimes \nabla \Delta_{\mu} + \sum_{\mu \in m} \Delta_{\mu} \mathcal{H}_{\Delta_{\mu}} \equiv \mathcal{H}_0 + \mathcal{H}_p,
 $

[第13页，第9段]
其中 $ \mathcal{H}_{\Delta_{\mu}} $ 是 $ \Delta_{\mu} $ 的 Hessian 矩阵，$ \mathcal{H}_0 $ 和 $ \mathcal{H}_p $ 分别对应于第一个和第二个求和。$ \mathcal{H}_0 $ 是半正定的，因为它是 $ N_{\Delta} $ 个秩为 1 的半正定矩阵之和；因此 $ \text{rk}(\mathcal{H}_0) \leq N_{\Delta} $，这意味着 $ \mathcal{H}_0 $ 的零空间维度至少为 $ N - N_{\Delta} $。当逼近阻塞时，由于 $ \Delta_{\mu} $ 趋于零，$ \mathcal{H}_p $ 变得非常小。让我们用 $ N^{-} $ 表示 $ \mathcal{H}_p $ 的负特征值数量。因此，要求 $ \mathcal{H}_{\mathcal{U}} $ 没有负特征值意味着：

[第13页，第10段]
$ 
N_{\Delta} \geq N^{-}.
 $

[第13页，第11段]
对于球体 [66]（以及对于感知机，如果在约束权重向量范数的同时使用负间隔），$ \mathcal{H}_p $ 是负定的且 $ N^{-} = N $。这个结果源于 $ \mathcal{H}_{\Delta_{\mu}} $ 是半负定的这一事实。实际上，$ \mathcal{H}_{\Delta_{\mu}} $ 表征了粒子间重叠量的二阶变化，并且是负的，因为根据勾股定理，横向于其相对方向运动的球体之间的距离总是增加。在这种情况下，我们有 $ N_{\Delta} \geq N $。结合公式 (12)，这导致 $ N_{\Delta} = N $：当球体阻塞时，自由度的数量与（源于接触的）约束数量相等，正如经验观察到的 [65]。这个性质通常被称为等静定性。

[第13页，第12段]
然而，在诸如椭圆和深度网络等其他问题中，$ \mathcal{H}_{\Delta_{\mu}} $ 以及因此 $ \mathcal{H}_p $ 具有正特征值。实际上，如果其中一个椭圆旋转，两个椭圆之间的重叠量可以增加。同样，对于全连接 Relu 网络和初始化时的随机数据，$ \mathcal{H}_p $ 具有对称谱且 $ N^{-} \approx N/2 $。通常预期阻塞会以 $ N_{\Delta} < N $ 发生，如图 7 中对椭圆的示意以及图 8 中对神经网络学习 MNIST 的经验所示。阻塞因此被称为“亚静定”。在 [70,71,86] 中针对特定情况推导了同图中所示的 Hessian 谱的相关后果：它总是在零处呈现一个 delta 函数，并在阻塞时出现一个间隙。

[第13页，第13段]
训练数据数量 $ P $ 的影响。阻塞转变的位置 $ N^{*}(P) $ 取决于 $ P $。这种依赖性对于随机数据是线性的，但对于结构化数据是亚线性的 [8]，如图 8A 所示。记 $ N^{-} = C_0N $，并使用公式 (14) 以及 $ N_{\Delta} \leq P $，我们得到 $ N^{*}(P) \leq P/C_0 $，保证如果 $ C_0 > 0 $，则在参数数量与 $ P $ 成线性关系时收敛到零损失。我们推测，对于实践中使用的通用数据和架构，$ C_0 $ 在 $ N $ 很大时保持有界于一个严格正值。$ ^9 $ $ C_0 $ 可以事后测量，得到的界限对应于图 8A 中的虚线。$ C_0 $ 先验地取决于架构、动力学和数据集的选择。先验地控制其值尚不可行，$ ^{10} $ 并且这将导致对收敛到损失全局最小值的相当严格的保证。

[第13页，第14段]
$ ^8 $ 如果对系统施加无穷小的压力，粒子总是可以恰好处于阻塞状态。在神经网络的背景下，也可以通过引入一个额外项来实现，例如 $ \lambda \| \theta(t) - \theta(t = 0) \|^2 $ 类型的损失项，惩罚权重的平方演化（称为“权重衰减”），其幅度 $ \lambda \to 0^+ $ 消失。
$ ^9 $ 这个事实对于线性或多项式激活函数不成立，讨论见 [8]。
$ ^{10} $ 在学习过程中控制 $ H_0 $ 和 $ H_p $ 仅在 $ N \to \infty $ 极限下进行，这不适用于阻塞附近 [87]。

[第14页，第1段]
初始化尺度 $\tilde{\alpha}$ 的影响。从图 4 中可以明显看出，阻塞转变（jamming transition）的位置取决于初始化尺度 $\tilde{\alpha}$。从该图可以观察到以下总体趋势：当集成平均预测器的测试误差较小时，阻塞转变在参数较少时发生。这符合直觉：一个更容易学习的规则应该对应更少的参数来拟合数据。

[第14页，第2段]
阻塞转变对性能的影响。随着阻塞转变的逼近，预测器的范数 $\|f_N\|$ 发散 [8]，这导致了图 6 中测试误差所显示的双下降（double descent）中的尖点。这种发散最早是在回归问题中被指出的 [21]。然而对于分类问题，这种发散在定量上有所不同，并且与逆幂律相容，如图 8.D 所示。这可以用类似于 Landau 的论证来理解，其灵感来自感知机（perceptron）的相关结果 [81,83]。直观的想法是，通过增加预测器的范数，可以有效地减小 hinge 损失拟合数据所需的单位间隔（margin）。对于 $N < N^*$，即使间隔趋于零也无法拟合数据。

[第14页，第3段]
具体而言，考虑预测器的范数 $\|f_N\|$ 在训练期间固定，并记 $N^*(\epsilon)$ 为作为间隔 $\epsilon$ 函数的阻塞转变。假设（如感知机中所发生的那样）$N^*(\epsilon)$ 是 $\epsilon$ 的光滑函数，使得 $N^*(\epsilon) \approx N^*(0) + N^*(0)\epsilon$。对于略大于 $N^*(0)$ 的 $N$，在预测器范数固定的情况下，量级为单位的间隔无法被拟合，但如果允许该范数增加一个因子 $N^*(0)/(N - N^*(0))$，则可以拟合。事实上，这有效地将间隔减小了该量，达到某个有效值 $\tilde{\epsilon} \equiv \epsilon(N - N^*(0))/N^*(0)$。根据构造，$\tilde{\epsilon}$ 满足 $N^*(\tilde{\epsilon}) = N$。这一论证为观察到的逆幂律提供了依据。

[第14页，第4段]
注意，对梯度流的任何扰动（如早停、使用随机梯度下降或权重衰减）都会破坏这种发散。11 因此，此类正则化在阻塞转变附近最为有效 [61]。

[第14页，第5段]
3. 双下降与过参数化的益处

[第14页，第6段]
因此，为了避免损失景观中的不良极小值，只需将 $N$ 增大到超过 $N^*$ 即可。但这样一来，人们会天真地预期性能下降并出现过拟合，如图 2 右面板所示。对于分类问题和深度网络而言并非如此，如图 6 所示：性能非常差，并在阻塞转变点 $N^*$ 处显示出一个尖点，然后随着 $N \to \infty$ 持续改善！

[第14页，第7段]
可以建立一个标度理论（scaling theory）来定量解释为什么性能在超过该点后随着 $N$ 持续改善，以及测试误差以多快的速度达到其渐近行为 [63]。本质上，在无限宽度下，学习对应于引言中讨论的明确定义的算法，但当宽度有限时，这些算法会变得更有噪声。事实上，随着 $N \sim h^2$ 的增加，由权重的随机初始化所引起的已学习输出函数的涨落会减小 [88]。由此可得 $\|f_N - (f_N)\| \sim N^{-1/4}$，如图 8.D 所示，其中 $(f_N)$ 是通过对使用不同随机初始化训练的输出进行集成平均得到的。这一结果在惰性训练（lazy training）[63] 和特征学习（feature learning）[58] 两种机制下都成立，如下文所论证。相关的测试误差增加与涨落的平方成正比（对于均方误差损失这是显然的，但在合理假设下对分类问题也成立 [63]），导致 $\langle \epsilon(f_N) - \epsilon(f_N) \rangle \sim N^{-1/2}$，正如所观察到的那样 [63]。这一效应是双下降的原因，可以通过考虑图 6 中集成平均函数 $(f_N)$ 的训练曲线 $\epsilon((f_N))$ 来直接验证，该曲线不显示第二次下降。更一般地，如图 4 所示，在固定 $\tilde{\alpha} = \sqrt{h\alpha}$ 的情况下，一旦进入过参数化区域，集成平均测试误差随 $h$ 的变化很微弱。

[第14页，第8段]
在惰性训练机制下，涨落 $\langle \|f_N - (f_N)\| \rangle \sim N^{-1/4}$ 简单地反映了由初始化引起的 NTK 的涨落，文献 [63] 论证其遵循 $\| \Theta_N - (\Theta_N)\| \sim N^{-1/4} \sim h^{-1/2}$，此后已得到分析上的证实 [89,90]。对于简单的损失和梯度下降，预测器 $f_N$ 必须获得相同的涨落 [63]，正如所观察到的那样。

[第14页，第9段]
由初始条件引起的类似涨落 $\langle \|f_N - (f_N)\| \rangle \sim N^{-1/4}$ 及其相同的后果也出现在神经网络的特性学习机制中 [58]。对于单隐藏层，这种涨落在初始化时当然是预期的，因为式 (8) 中引入的神经元参数密度 $\rho$ 必须具有量级为 $\delta\rho \sim 1/\sqrt{h} \sim N^{-1/4}$ 的有限采样涨落，这正如中心极限定理所预期的那样。由于在渐近区域 $N \to \infty$ 中，初始化时 $\rho$ 的值会影响已学习的函数，因此由随机初始化引起的涨落 $\delta\rho$（以及由此引起的已学习函数 $f_N$ 的涨落）的幅度在学习之后仍将以 $N^{-1/4}$ 标度，这已在文献 [91] 中对单隐藏层严格证明。

[第14页，第10段]
总体而言，这一标度理论支持以下观点：对于一般数据集和深层架构，第二次下降源于有限 $N$ 效应和初始化对 $N \to \infty$ 时达到的极限算法所诱导的噪声。换言之，已学习预测器的方差在该极限下减小，因为其对初始化的依赖性消失了。这一结果的一个有趣的实践意义（在图 4 和图 6 中显而易见）是，最佳性能可以通过对超过阻塞转变的有限宽度网络进行集成平均来获得。

[第14页，第11段]
自这些论证提出以来，双下降曲线已在无限维极限下线性数据和随机特征机（random features machines）的简单情形中被解析计算 [47,92]，其中还证明了 [93,94] 它源于随神经元数量增加而消失的核的涨落，从而证实了目前的解释。

[第14页，第12段]
11 它们是在临界现象意义下的相关扰动。

[第15页，第1段]
图 9. 左、中：集成平均测试误差与缩放参数 $\tilde{\alpha} = \sqrt{h\alpha}$ 的关系。该图表明，对于全连接（FC）架构（左图），NTK（神经正切核）机制（较大的 $\sqrt{h\alpha}$）往往优于特征学习机制（较小的 $\sqrt{h\alpha}$），但在卷积神经网络（CNN）中并非如此（中图）。在后一种情况下，特征学习机制（蓝色曲线，$\beta \approx 1/2$）的训练曲线指数 $\beta$ 大于 NTK 机制（橙色曲线，$\beta \approx 1/3$）。

[第15页，第2段]
来源：取自 [58]。

[第15页，第3段]
4. 解耦 NTK 与特征学习机制

[第15页，第4段]
如上一节所述，更宽的网络具有更强的预测能力。然而，通过对多次权重初始化下的输出进行集成平均，在中等宽度下就已经可以获得相当的性能提升。如图 4 所示，初始化的缩放幅度 $\tilde{\alpha} = \alpha \sqrt{h}$ 允许在惰性训练与特征学习机制之间发生交叉过渡，它确实会影响性能。哪种机制最能刻画实际使用的深度网络？哪一种表现更好？NTK 机制的一些预测似乎在现实架构中成立 [39]，并且在 NTK 极限下训练的网络可以在真实数据集上取得良好性能 [40,95,96]。然而，在若干情况下，特征学习机制优于 NTK [51,97]，这与图 1 中所描绘的构建数据抽象表示是有用的这一常见观点相一致。若干理论工作表明，对于特定的简单数据模型，NTK 表现不佳 [14,98–101]。

[第15页，第5段]
在 [58] 中，该问题在 ($\alpha, h$) 平面上对深度网络进行了系统研究，其中 $\alpha$ 是 [51] 中引入的初始化尺度，如式 (9) 所定义。该研究发展了自适应学习率的数值方法，以在将 $\alpha$ 改变十个数量级的同时跟随梯度流。主要结果如下：

[第15页，第6段]
(i) 两种机制之间的交叉过渡发生在 $\alpha \sqrt{h} = O(1)$ 时，如图 4 所示，这将 [51] 中仅限于单隐藏层网络的结果进行了推广。当 $\alpha \sqrt{h} \ll 1$ 时，$\|\Delta \Theta\|/\|\Theta\| \gg 1$，而当 $\alpha \sqrt{h} \gg 1$ 时则相反。这里 $\Delta \Theta = \Theta(t) - \Theta(t = 0)$ 刻画了切核的演化，$t$ 是学习时间。将损失除以 $\alpha^2$ 并考虑 $\tilde{\mathcal{L}} \equiv \mathcal{L}/\alpha^2$ 是方便的，可以证明这确保了在大的 $\alpha$ 极限下动力学发生在与 $\alpha$ 无关的时间尺度上 [51,58]。该结果对于通常选择的损失（交叉熵、合页损失等）在任何有限时间下都成立。如果使用合页损失，该结果对于 $t \to \infty$ 也成立，因为在这种情况下，收敛到零损失在有限时间内发生，且与 $h$ 和 $\alpha$ 无关。

[第15页，第7段]
这里我们提供一个示意性论证来证明该结果，更详细的分析见 [58]。给定神经元的输出 $f$ 相对于预激活 $a$（在初始化时为一阶量）的变化量约为 $\partial f/\partial a \sim \alpha/\sqrt{h}$。这一结果对于最后一个隐藏层是显然的（利用最后权重为 $1/\sqrt{h}$ 量级这一事实），但可以递归地在所有层上加以论证，如 [58] 所讨论并在 NTK 研究 [10] 中隐式推导的那样。对于梯度流，由偏置演化（考虑前一层权重会得到类似的缩放）引起的预激活变化量 $\Delta a$ 必须为 $\Delta a \sim t(\partial \tilde{\mathcal{L}}/\partial f)(\partial f/\partial a) \sim t/\alpha\sqrt{h}$ 量级，这里利用了 $\partial \tilde{\mathcal{L}}/\partial f \sim 1/\alpha^2$。因此，在训练结束时 $\Delta a$ 为 $1/\alpha\sqrt{h}$ 量级（因为零合页损失在 $t = O(1)$ 的时间尺度上达到）。因此，当 $\Delta a \sim 1$ 时，NTK 机制必然失效，此时权重与输出之间的关系必须变为非线性，这对应于大 $h$ 下 $\alpha^* \sim 1/\sqrt{h}$ 的交叉过渡。

[第15页，第8段]
类似的思路可用于中等宽度。当减小 $h$ 以从过参数化相接近阻塞（jamming）转变时，输出的范数——因而权重和预激活——会爆炸，如第 2 节所综述的那样。此时永远不会处于惰性训练机制，权重变化与输出之间的关系必须变为非线性。因此，在阻塞转变附近，网络总是处于特征学习机制。 consequently，分隔惰性与特征学习的交叉过渡线必须向上弯曲，并且永远不会与图 4 中的阻塞线相交。我们确实观察到曲线如预期那样定性地向上弯曲（然而在非常接近阻塞处很难进行精确测量）。

[第15页，第9段]
(ii) 对于全连接网络和梯度下降，NTK 往往优于特征学习机制，如图 9 左图所示。这一结果在多种数据集（MNIST、Fashion-MNIST、CIFAR10 等）上均被发现，但 MNIST 10 PCA 除外。这在图 4 中很明显，其中 MNIST 10 PCA 的最佳性能似乎出现在交叉过渡区域 $\tilde{\alpha} \sim 1$。

[第15页，第10段]
(iii) 对于 CNN 架构，特征学习优于 NTK 机制，如图 9 中图所示。这对应于更大的训练曲线指数 $\beta$，如图 9 右图所示。(ii, iii) 最近被 Google 团队所证实 [64]。

[第16页，第1段]
这些观察引发了各种问题。特征学习（feature learning）的优点和缺点是什么，为什么后者在FC而非CNN架构中更为明显？对于现代CNN架构，特征学习机制中学习曲线指数$\beta$的改善是否是理解如何克服维度灾难的关键？这是否与学习数据中的不变量有关？我们认为，这些问题的答案尚不清楚。为了开始解决这些问题，在下一节中，我们研究一个简单的不变数据模型，对于该模型，可以计算特征学习机制中学习曲线指数$\beta$的改善。

[第16页，第2段]
5. 通过压缩无关输入维度来学习简单不变量

[第16页，第3段]
如何克服维度灾难？图像等各种数据集的一个有利方面是数据分布$P(x)$具有高度各向异性，这与数据位于较低维流形上的概念一致。在这种情况下，相邻数据之间的距离随着$P$的增长而更快地减小，从而改善了核方法（kernel methods）[102]。适度的各向异性对核分类[103]和回归[101,104]也有积极影响。然而，即使在MNIST或CIFAR10这样的简单数据集中，内在维度仍然很大（分别为$d_{int} \approx 14$和$d_{int} \approx 30$[102]）。这种效应有帮助，但无法解决复杂数据集的维度灾难：事实上，使用拉普拉斯或高斯核[12]（它们与全连接网络的NTK非常相似）对MNIST得到$\beta \approx 0.4$（这还不错），但对CIFAR10得到$\beta \approx 0.1$，这意味着随着数据数量的增加，学习速度非常慢。

[第16页，第4段]
如引言中所讨论的，另一个流行的观点是，像图像这样的数据集之所以可学习，是因为它们表现出许多保持标签不变的变换。通过对这些变换变得不敏感，网络本质上降低了数据的维度。这一观点与深度学习导致数据的抽象神经表示的概念一致，如图1所示。这种效应可能是我们在图9右侧面板中观察到的训练曲线指数$\beta$在特征学习机制中更有利的原因。然而，理解不变量如何动态构建以及它如何影响性能和$\beta$仍然是一个挑战。

[第16页，第5段]
可以构建特定的数据模型[44,92,101,105]，其中惰性训练（lazy training）完全无法学习，而在特征学习机制中训练的神经网络则成功。然而，这些考虑$d \to \infty$、$P \to \infty$且$P/d$固定的模型无法捕捉在两种机制中观察到的两个有限且不同的学习曲线指数$\beta$。

[第16页，第6段]
条纹模型（stripe model）。在[98,103,106]中，考虑了一个简单的不变量模型。标签不依赖于输入空间的$d_{\perp} = d - d_{\parallel}$个方向，因此$y(x) = y(x_{\parallel})$，其中$x = (x_{\perp}, x_{\parallel})$。例如，$x_{\perp}$可以对应于图片边界附近的无信息像素。显然，核函数仅依赖于$x_{\parallel}$的核方法在这些数据上会比各向同性核表现更好，因为它们将在$d_{\parallel}$（而非$d$）个维度上操作，参见例如[101]。神经网络如何自行发现这种不变性？

[第16页，第7段]
对于梯度下降，使用逻辑损失（logistic loss），可以证明单隐藏层对应于某个非希尔伯特函数空间中的最大间隔分类器[98]。如果数据在投影到低维空间后可以分离，则可以获得与维度无关的性能保证。该分析是严格且通用的，但需要达到实践中未使用的极长时间，并且不能预测$\beta$的值。

[第16页，第8段]
在[103,106]中，考虑了铰链损失（hinge loss）。在这种情况下，动力学在合理的时间后停止。如果数据点的密度在标签之间的界面处不消失，并且后者足够光滑（例如平面或圆柱面），则发现测试误差在两种机制中都按幂律衰减。对于惰性训练机制，受静电学启发的标度论证得出$\beta_{lazy} = d/(3d - 2)$。特征学习表现更好，因为发现$\beta_{feature} = (d + d_{\perp}/2)/(3d - 2)$。导致特征学习机制改善的关键效应在图10中对$d_{\parallel} = 1$（称为条纹模型）进行了说明：由于正交方向上没有梯度，权重仅沿$d_{\parallel}$维度增长。因此，对于权重的无穷小初始化（$\alpha \to 0$），神经元沿数据中的信息坐标对齐。相应地，相对而言，它们对$x_{\perp}$变得不那么敏感，后者仅作为噪声源起作用。这种去噪受限于训练集的有限大小。具体而言，发现$\Lambda \equiv W_{\parallel}/W_{\perp} \sim \sqrt{P}$，其中$W_{\parallel}$和$W_{\perp}$分别是第一层权重在信息方向和无信息方向上的特征尺度。这种效应等价于在无信息方向上对输入进行幅度为$\Lambda$的几何压缩。事实上，通过考虑变换后的数据$(x_{\parallel}, x_{\perp}/\Lambda)$进行这种压缩，并在NTK机制中学习这些数据，其性能与在特征机制中学习原始数据非常相似，参见图10的右侧面板。

[第16页，第9段]
NTK的核PCA揭示了不变量的几何压缩。条纹模型说明，特征学习机制中的神经网络可以学会对数据中不影响标签的变换变得不敏感。这种不敏感性受限于与有限数据集相关的采样噪声。这种现象是否也发生在更现代的架构和表征图像的更微妙的不变量中？对数据神经表示的内在维度的测量[56,57]或互信息估计[54]表明可能如此，但如引言中所述，这些可观测量有一些局限性。

[第16页，第10段]
在特征学习机制中，NTK随时间演化。这种演化导致对所考虑任务的更好的核。事实上，使用基于训练结束时获得的NTK的核方法，其性能与神经网络本身基本相同的性能[106]。这一观察与之前的观察一致，即NTK在

[第16页，第11段]
12 拉普拉斯核的函数形式为$K(x, x') = K(\|x - x'\|) \propto e^{-\|x - x'\|/\sigma}$，高斯核为$K(x, x') = K(\|x - x'\|) \propto e^{-\|x - x'\|^2/(2\sigma^2)}$。带宽$\sigma$控制$K$随其参数增加的衰减速度。

[第17页，第1段]
时间 [107,108]，在以下意义上。对于核，我们总是可以写成 $\Theta(x, y) = \psi(x) \cdot \psi(y)$，其中 $\psi(x)$ 是特征向量。在 NTK 的情况下，$\psi(x)$ 可以选择为输出 $f$ 关于权重的梯度——见式 (6)。如果标签向量 $\{y(x_i)\}_{i=1,\ldots,p}$ 在特征向量 $\{\psi(x_i)\}_{i=1,\ldots,p}$ 的前几个主成分上具有较大的系数（这一操作称为核 PCA [110]），核往往表现更好 [109]。在学习过程中，观察到 NTK 的特征向量的前几个主成分与标签向量之间存在这种对齐 [107,108]。

[第17页，第2段]
尽管关于这种对齐为何发生尚无一般理论，但条纹模型为这一效应提供了合理的解释。在这种情况下，这种改进必然发生，因为系统从各向同性核演化为对各向无信息方向 $x_1$ 敏感性降低的各向异性核。结果，顶部核 PCA 在标签上变得更具信息性（图 11.A），并且它们在其上投影更多（图 11.C）。对于在 MNIST 上训练的 CNN，如图 11.B、D 所示，也观察到相同的结果。总体而言，这一观点支持 NTK 的改进揭示了数据中无信息方向的几何压缩。

[第17页，第3段]
6. 结论

[第17页，第4段]
不要害怕坏的极小值！只需增加参数数量，直到你通过堵塞转变。超过该点后，就不会遇到坏的极小值，你可以将损失降为零。根据网络宽度以及初始化时函数值的缩放方式，深度学习可以表现为核方法，或者可以学习特征。简单的缩放论证界定了相应的相图，并且似乎适用于基准数据集。值得注意的是，这些论证很少依赖于所考虑的具体数据。它们的实际意义在于，在堵塞转变之后，对不同初始化网络进行集成平均可以是一种有效的程序，正如不同研究组所发现的那样 [58,63,64]。

[第17页，第5段]
考虑你在这个相图中的位置，可以说是理解深度学习中未解决问题的关键。例如，对于动力学中随机性的作用来说确实如此，它似乎能提高性能。使用随机梯度下降而不是梯度流在接近堵塞时会有帮助，这是很自然的，因为噪声会正则化预测器范数的发散——这一效应已经可以通过早停 [61] 获得。同样，对于排斥粒子，温度会正则化堵塞转变附近的奇异性 [111]。然而，研究其对相图不同区域性能的影响将是有用的。特别有趣的是，了解在过参数化极限下随机性的主要效应之一是否是将图 4 中懒惰与特征学习机制之间的交叉点向上推，从而在特征学习优于懒惰训练的 CNN 中提高性能。

[第18页，第1段]
最终，仍需理解的核心问题是性能，以及深度网络如何克服维数灾难。即使在经验层面，关于对微分同胚的不变性是这一成功背后的核心现象的观点也尚未确立。在理论层面，这一观点尚未与近期我们对学习理解的改进相结合，而后者主要集中于全连接网络。相比之下，对卷积神经网络（CNN）如何学习特征的建模努力则较为有限，尽管只有这些架构在实践中往往表现良好。此类研究可以说需要设计呈现复杂不变性的简单规范数据模型，而目前这类模型还很稀缺。

[第18页，第2段]
利益冲突声明

[第18页，第3段]
作者声明，他们没有已知的可能影响本文所报告工作的竞争性经济利益或个人关系。

[第18页，第4段]
致谢

[第18页，第5段]
我们感谢 G. Biroli、S. d'Ascoli、F. Cagnetta、A. Favero、F. Gabriel、C. Hongler、A. Jacot、J. Paccolat、L. Pillaud-Vivien、S. Spigler、L. Sagun、U. Tomasini、K. Tyloo 以及 PCSL 小组的所有成员参与讨论。本工作部分得到了西蒙斯基金会（Simons Foundation）资助（#454953 Matthieu Wyart）的支持。M.W. 感谢瑞士国家科学基金会（Swiss National Science Foundation）在资助号 200021-165509 下的支持。

[第18页，第6段]
参考文献

[第18页，第7段]
[1] David Marr, Tomaso Poggio, A computational theory of human stereo vision, Proc. R. Soc. Lond. [Biol.] 204 (1156) (1979) 301–328.
[2] Yann LeCun, Yoshua Bengio, Geoffrey Hinton, Deep learning, Nature 521 (7553) (2015) 436.
[3] Dario Amodei, Sundaram Ananthanarayanan, Rishita Anubhai, Jingliang Bai, Eric Battenberg, Carl Case, Jared Casper, Bryan Catanzaro, Qiang Cheng, Guoliang Chen, et al., Deep speech 2: End-to-end speech recognition in english and mandarin, in: International Conference on Machine Learning, 2016, pp. 173–182.
[4] Baoguang Shi, Xiang Bai, Cong Yao, An end-to-end trainable neural network for image-based sequence recognition and its application to scene text recognition, IEEE Trans. Pattern Anal. Mach. Intell. 39 (11) (2016) 2298–2304.
[5] Brody Huval, Tao Wang, Sameep Tandon, Jeff Kiske, Will Song, Joel Pazhayampalli, Mykhaylo Andriluka, Pranav Rajpurkar, Toki Migimatsu, Royce Cheng-Yue, et al., An empirical evaluation of deep learning on highway driving, 2015, arXiv preprint arXiv:1504.01716.
[6] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, et al., Mastering the game of go without human knowledge, Nature 550 (7676) (2017) 354–359.
[7] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller, Playing atari with deep reinforcement learning, 2013, arXiv preprint arXiv:1312.5602.
[8] Mario Geiger, Stefano Spigler, Stéphane d'Ascoli, Levent Sagun, Marco Baity-Jesi, Giulio Biroli, Matthieu Wyart, Jamming transition as a paradigm to understand the loss landscape of deep neural networks, Phys. Rev. E 100 (1) (2019) 012115, Publisher: American Physical Society.
[9] Quoc V. Le, Building high-level features using large scale unsupervised learning, in: 2013 IEEE International Conference on Acoustics, Speech and Signal Processing, IEEE, 2013, pp. 8595–8598.
[10] Arthur Jacot, Franck Gabriel, Clément Hongler, Neural tangent kernel: Convergence and generalization in neural networks, in: Proceedings of the 32nd International Conference on Neural Information Processing Systems, NIPS'18, Curran Associates Inc., USA, 2018, pp. 8580–8589.
[11] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md Patwary, Mostofa Ali, Yang Yang, Yanqi Zhou, Deep learning scaling is predictable, empirically, 2017, arXiv preprint arXiv:1712.00409.
[12] Bolei Zhou, Aditya Khosla, Agata Lapedriza, Aude Oliva, Antonio Torralba, Object detectors emerge in deep scene cnns, 2014, arXiv preprint arXiv:1412.6856.
[13] Ulrike von Luxburg, Olivier Bousquet, Distance-based classification with Lipschitz functions, J. Mach. Learn. Res. 5 (Jun) (2004) 669–695.
[14] Francis Bach, Breaking the curse of dimensionality with convex neural networks, J. Mach. Learn. Res. 18 (1) (2017) 629–681.
[15] Ludovic Berthier, Giulio Biroli, Theoretical perspective on the glass transition and amorphous materials, Rev. Modern Phys. 83 (2) (2011) 587.
[16] Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, Yann LeCun, The loss surfaces of multilayer networks, in: Artificial Intelligence and Statistics, 2015, pp. 192–204.
[17] Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals, Understanding deep learning requires rethinking generalization, in: 5th International Conference on Learning Representations, ICLR 2017, Toulon, France, April 24-26, 2017, Conference Track Proceedings, 2017.
[18] Behnam Neyshabur, Ryota Tomioka, Ruslan Salakhutdinov, Nathan Srebro, Geometry of optimization and implicit regularization in deep learning, 2017, arXiv preprint arXiv:1705.03071.
[19] Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, Nathan Srebro, Towards understanding the role of over-parametrization in generalization of neural networks, 2018, arXiv preprint arXiv:1805.12076.
[20] Yamini Bansal, Madhu Advani, David D. Cox, Andrew M. Saxe, Minmorn training: An algorithm for training overcomplete deep neural networks, 2018, arXiv preprint arXiv:1806.00730.
[21] Madhu S. Advani, Andrew M. Saxe, Haim Sompolinsky, High-dimensional dynamics of generalization error in neural networks, Neural Netw. (2020).
[22] C. Daniel Freeman, Joan Bruna, Topology and geometry of deep rectified network optimization landscapes, in: International Conference on Learning Representations, 2017.
[23] Elad Hoffer, Itay Hubara, Daniel Soudry, Train longer, generalize better: Closing the generalization gap in large batch training of neural networks, in: Advances in Neural Information Processing Systems, 2017, pp. 1729–1739.
[24] Daniel Soudry, Yair Carmon, No bad local minima: Data independent training error guarantees for multilayer neural networks, 2016, arXiv preprint arXiv:1605.08361.
[25] Yaim Cooper, The loss landscape of overparameterized neural networks, 2018, arXiv preprint arXiv:1804.10200.
[26] Levent Sagun, Léon Bottou, Yann LeCun, Singularity of the Hessian in deep learning, in: International Conference on Learning Representations, 2017.

[第19页，第1段]
[P1/1]
[27] Levent Sagun, Utku Evci, V. Ugur Güney, Yann Dauphin, Léon Bottou，过参数化神经网络Hessian矩阵的经验分析，载于：ICLR 2018研讨会贡献，2017年，arXiv:1706.04454。
[28] Andrew J Ballard, Ritankar Das, Stefano Martiniani, Dhagash Mehta, Levent Sagun, Jacob D Stevenson, David J Wales，机器学习的能量景观，Phys. Chem. Chem. Phys.（2017年）。
[29] Zachary C. Lipton，困在什么之中？权重空间历险记，载于：国际学习表征会议，2016年。
[30] Marco Baity-Jesi, Levent Sagun, Mario Geiger, Stefano Spigler, Gerard Ben Arous, Chiara Cammarota, Yann LeCun, Matthieu Wyart, Giulio Biroli，比较动力学：深度神经网络与玻璃态系统，载于：Jennifer Dy, Andreas Krause（编），第35届国际机器学习会议论文集，机器学习研究论文集，第80卷，PMLR，斯德哥尔摩国际展览中心，瑞典斯德哥尔摩，2018年，第314–323页。
[31] Radford M. Neal，神经网络的贝叶斯学习，Springer-Verlag New York, Inc.，美国新泽西州Secaucus，1996年。
[32] Christopher K.I. Williams，无限网络的计算，载于：神经信息处理系统进展，1997年，第295–301页。
[33] Jae Hoon Lee, Yasaman Bahri, Roman Novak, Samuel S. Schoenholz, Jeffrey Pennington, Jascha Sohl-Dickstein，深度神经网络作为高斯过程，载于：ICLR，2018年。
[34] Alexander G. de G. Matthews, Jiri Hron, Mark Rowland, Richard E. Turner, Zoubin Ghahramani，宽深度神经网络中的高斯过程行为，载于：国际学习表征会议，2018年，https://openreview.net/forum?id=H1-nGgWC-。
[35] Roman Novak, Lechao Xiao, Yasaman Bahri, Jaehoon Lee, Greg Yang, Daniel A. Abolafia, Jeffrey Pennington, Jascha Sohl-dickstein，具有多通道的贝叶斯深度卷积网络是高斯过程，载于：国际学习表征会议，2019年，https://openreview.net/forum?id=B1g30j0qF7。
[36] Greg Yang，权重共享的宽神经网络尺度极限：高斯过程行为、梯度独立性与神经正切核推导，2019年，arXiv预印本arXiv:1902.04760。
[37] Simon S. Du, Xiyu Zhai, Barnabas Poczos, Aarti Singh，梯度下降可证明地优化过参数化神经网络，载于：国际学习表征会议，2019年，https://openreview.net/forum?id=S1eK3i09YQ。
[38] Zeyuan Allen-Zhu, Yuanzhi Li, Zhao Song，通过过参数化的深度学习收敛理论，载于：国际机器学习会议，PMLR，（ISSN: 2640-3498）2019年，第242–252页。
[39] Jaehoon Lee, Lechao Xiao, Samuel Schoenholz, Yasaman Bahri, Roman Novak, Jascha Sohl-Dickstein, Jeffrey Pennington，任意深度的宽神经网络在梯度下降下演化为线性模型，载于：H. Wallach, H. Larochelle, A. Beygelzimer, F. d’ Alché-Buc, E. Fox, R. Garnett（编），神经信息处理系统进展32，Curran Associates, Inc.，2019年，第8572–8583页。
[40] Sanjeev Arora, Simon S Du, Wei Hu, Zhiyuan Li, Russ R Salakhutdinov, Ruosong Wang，关于无限宽神经网络的精确计算，载于：H. Wallach, H. Larochelle, A. Beygelzimer, F. d’ Alché-Buc, E. Fox, R. Garnett（编），神经信息处理系统进展32，Curran Associates, Inc.，2019年，第8141–8150页。
[41] Daniel Park, Jascha Sohl-Dickstein, Quoc Le, Samuel Smith，网络宽度对随机梯度下降与泛化的影响：一项实证研究，载于：国际机器学习会议，PMLR，（ISSN: 2640-3498）2019年，第5042–5051页。
[42] Bernhard Scholkopf, Alexander J. Smola，核学习：支持向量机、正则化、优化及其超越，MIT出版社，2001年。
[43] Song Mei, Andrea Montanari, Phan -Minh Nguyen，两层神经网络景观的平均场视角，Proc. Natl. Acad. Sci. 115 (33) (2018) E7665–E7671。出版商：美国国家科学院 栏目：PNAS Plus。
[44] Grant M. Rotskoff, Eric Vanden-Eijnden，神经网络作为相互作用粒子系统：损失景观的渐近凸性与近似误差的普适标度，2018年，arXiv预印本arXiv:1805.00915。
[45] Lénaïc Chizat, Francis Bach，使用最优传输的过参数化模型梯度下降全局收敛性，载于：神经信息处理系统进展31，Curran Associates, Inc.，2018年，第3040–3050页。
[46] Justin Sirignano, Konstantinos Spiliopoulos，神经网络的平均场分析：大数定律，SIAM J. Appl. Math. 80 (2) (2020) 725–752，出版商：工业与应用数学学会。
[47] Song Mei, Theodor Misiakiewicz, Andrea Montanari，两层神经网络的平均场理论：无维界与核极限，载于：学习理论会议，PMLR，（ISSN: 2640-3498）2019年，第2388–2464页。
[48] Phan -Minh Nguyen，多层神经网络学习动力学的平均场极限，2019年，arXiv预印本arXiv:1902.02880。
[49] Justin Sirignano, Konstantinos Spiliopoulos，神经网络的平均场分析：中心极限定理，Stochastic Process. Appl. 130 (3) (2020) 1820–1852。
[50] Phan -Minh Nguyen, Huy Tuan Pham，多层神经网络平均场极限的严格框架，2020年，arXiv预印本arXiv:2001.11443。
[51] Lenaic Chizat, Edouard Oyallon, Francis Bach，可微编程中的惰性训练，载于：神经信息处理系统进展，2019年，第2937–2947页。
[52] Joan Bruna, Stéphane Mallat，不变散射卷积网络，IEEE Trans. Pattern Anal. Mach. Intell. 35 (8) (2013) 1872–1886。
[53] Stéphane Mallat，理解深度卷积网络，Phil. Trans. R. Soc. A 374 (2065) (2016) 20150203。
[54] Ravid Shwartz-Ziv, Naftali Tishby，通过信息打开深度神经网络的黑箱，2017年，arXiv预印本arXiv:1703.00810。
[55] Andrew M Saxe, Yamini Bansal, Joel Dapello, Madhu Advani, Artemy Kolchinsky, Brendan D Tracey, David D Cox，论深度学习的信息瓶颈理论，J. Stat. Mech. Theory Exp. 2019 (12) (2019) 124020。
[56] Alessio Ansuini, Alessandro Laio, Jakob H Macke, Davide Zoccolan，深度神经网络中数据表示的内在维度，载于：神经信息处理系统进展，2019年，第6111–6122页。
[57] Stefano Recanatesi, Matthew Farrell, Madhu Advani, Timothy Moore, Guillaume Lajoie, Eric Shea-Brown，深度神经网络中的维度压缩与扩展，2019年，arXiv预印本arXiv:1906.00443。
[58] Mario Geiger, Stefano Spigler, Arthur Jacot, Matthieu Wyart，解耦深度神经网络中的特征训练与惰性训练，J. Stat. Mech. Theory Exp. 2020 (11) (2020) 113301，出版商：IOP Publishing。
[59] Yann LeCun, Corinna Cortes，MNIST手写数字数据库，2010年，http://yann.lecun.com/exdb/mnist/。
[60] Alex Krizhevsky，从微小图像中学习多层特征，技术报告，2009年。
[61] S. Spigler, M. Geiger, S. d'Ascoli, L. Sagun, G. Biroli, M. Wyart，从欠参数化到过参数化的阻塞转变影响深度学习中的泛化，J. Phys. A 52 (47) (2019) 474001，出版商：IOP Publishing。
[62] Mikhail Belkin, Daniel Hsu, Siyuan Ma, Soumik Mandal，调和现代机器学习实践与经典偏差-方差权衡，Proc. Natl. Acad. Sci. 116 (32) (2019) 15849–15854。
[63] Mario Geiger, Arthur Jacot, Stefano Spigler, Franck Gabriel, Levent Sagun, Stéphane d'Ascoli, Giulio Biroli, Clément Hongler, Matthieu Wyart，深度学习中泛化随参数数量的标度描述，J. Stat. Mech. Theory Exp. 2020 (2) (2020) 023401，出版商：IOP Publishing。
[64] Jaehoon Lee, Samuel S Schoenholz, Jeffrey Pennington, Ben Adlam, Lechao Xiao, Roman Novak, Jascha Sohl-Dickstein，有限与无限神经网络：一项实证研究，2020年，arXiv预印本arXiv:2007.15801。
[65] Corey S. O'Hern, Leonardo E. Silbert, Andrea J. Liu, Sidney R. Nagel，零温度和零外加应力下的阻塞：无序的典范，Phys. Rev. E 68 (1) (2003) 011306–011324。

[第20页，第1段]
[P1/1]
[66] M. Wyart，论非晶固体的刚性，Ann. Phys. 30 (3) (2005) 1-113。
[67] Andrea J Liu, Sidney R Nagel, W Saarloos, Matthieu Wyart，堵塞场景——导论与展望，OUP Oxford，2010。
[68] Matthieu Wyart, Leonardo E Silbert, Sidney R Nagel, Thomas A Witten，压缩对边缘堵塞固体振动模式的影响，Phys. Rev. E 72 (5) (2005) 051306。
[69] Eric DeGiuli, Adrien Laversanne-Finot, Gustavo Alberto Düring, Edan Lerner, Matthieu Wyart，配位数和压力对非晶固体中声衰减、玻色峰和弹性的影响，Soft Matter 10 (30) (2014) 5628-5644。
[70] Silvio Franz, Giorgio Parisi, Pierfrancesco Urbani, Francesco Zamponi，低温玻璃中简正模式的普适谱，Proc. Natl. Acad. Sci. 112 (47) (2015) 14539-14544。
[71] Carolina Brito, Harukuni Ikeda, Pierfrancesco Urbani, Matthieu Wyart, Francesco Zamponi，非球形颗粒堵塞的普适性，Proc. Natl. Acad. Sci. 115 (46) (2018) 11736-11741，出版方：National Academy of Sciences，栏目：Physical Sciences。
[72] Mitch Mailman, Carl F. Schreck, Corey S. O'Hern, Bulbul Chakraborty，由无摩擦椭球形颗粒组成的系统中的堵塞，Phys. Rev. Lett. 102 (25) (2009) 255501。
[73] Z. Zeravcic, N. Xu, A.J. Liu, S.R. Nagel, W. van Saarloos，接近堵塞时椭球堆积的激发，Europhys. Lett. 87 (2) (2009) 26001。
[74] Matthieu Wyart，边缘稳定性约束随机密堆积中的力和对分布，Phys. Rev. Lett. 109 (12) (2012) 125502。
[75] Edan Lerner, Gustavo During, Matthieu Wyart，球体堆积中的低能非线性激发，Soft Matter 9 (2013) 8252-8263。
[76] Patrick Charbonneau, Jorge Kurchan, Giorgio Parisi, Pierfrancesco Urbani, Francesco Zamponi，结构玻璃中的分形自由能景观，Nature Commun. 5 (3725) (2014)。
[77] Patrick Charbonneau, Jorge Kurchan, Giorgio Parisi, Pierfrancesco Urbani, Francesco Zamponi，高维稠密非晶硬球的精确理论。III. 完全复本对称破缺解，J. Stat. Mech. Theory Exp. 2014 (10) (2014) 10009。
[78] Edan Lerner, Gustavo Düring, Matthieu Wyart，非布朗悬浮液流动与软非晶固体的统一框架，Proc. Natl. Acad. Sci. 109 (13) (2012) 4798-4803。
[79] E. DeGiuli, G. Düring, E. Lerner, M. Wyart，惯性颗粒流与非布朗悬浮液的统一理论，Phys. Rev. E 91 (6) (2015) 062206。
[80] Florent Krzakala, Jorge Kurchan，约束满足问题的景观分析，Phys. Rev. E 76 (2) (2007) 021122。
[81] Silvio Franz, Giorgio Parisi，最简单的堵塞模型，J. Phys. A 49 (14) (2016) 145001。
[82] Silvio Franz, Giorgio Parisi, Maxime Sevelev, Pierfrancesco Urbani, Francesco Zamponi，非凸连续约束满足问题中SAT-UNSAT（堵塞）阈值的普适性，SciPost Phys. 2 (3) (2017) 019。
[83] Silvio Franz, Sungmin Hwang, Pierfrancesco Urbani，多层监督学习模型中的堵塞，Phys. Rev. Lett. 123 (16) (2019) 160602，出版方：American Physical Society。
[84] Silvio Franz, Antonio Sclocchi, Pierfrancesco Urbani，线性感知机的临界堵塞相，Phys. Rev. Lett. 123 (11) (2019) 115702。
[85] Alexei V. Tkachenko, Thomas A. Witten，无摩擦颗粒材料中的应力传播，Phys. Rev. E 60 (1) (1999) 687-696。
[86] Matthieu Wyart，非晶固体中声子输运随连通性的标度，Europhys. Lett. 89 (6) (2010) 64001。
[87] Arthur Jacot, Franck Gabriel, Clément Hongler，训练过程中DNN黑塞矩阵的渐近谱，2019，arXiv预印本arXiv:1910.02875。
[88] Brady Neal, Sarthak Mittal, Aristide Baratin, Vinayak Tantia, Matthew Scicluna, Simon Lacoste-Julien, Ioannis Mitliagkas，神经网络中偏差-方差权衡的现代视角，2018，arXiv预印本arXiv:1810.08591。
[89] Boris Hanin, Mihai Nica，神经正切核的有限深度和宽度修正，2019，arXiv预印本arXiv:1909.05989。
[90] Ethan Dyer, Guy Gur-Ari，从费曼图看宽网络的渐近性质，2019，arXiv预印本arXiv:1909.11304。
[91] Zhengdao Chen, Grant Rotskoff, Joan Bruna, Eric Vanden-Eijnden，浅层神经网络的动态中心极限定理，Adv. Neural Inf. Process. Syst. 33 (2020)。
[92] Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, Andrea Montanari，高维线性化两层神经网络，2019，arXiv预印本arXiv:1904.12191。
[93] Stéphane D'Ascoli, Maria Refinetti, Giulio Biroli, Florent Krzakala，双下降中的双重麻烦：惰性区域中的偏差与方差，载于：International Conference on Machine Learning, PMLR, (ISSN: 2640-3498) 2020, pp. 2280-2290。
[94] Arthur Jacot, Berfin Simsek, Francesco Spadaro, Clement Hongler, Franck Gabriel，随机特征模型的隐式正则化，载于：International Conference on Machine Learning, PMLR, (ISSN: 2640-3498) 2020, pp. 4631-4640。
[95] Sanjeev Arora, Simon S. Du, Zhiyuan Li, Ruslan Salakhutdinov, Ruosong Wang, Dingli Yu，利用无限宽深度网络的力量处理小数据任务，2019，https://openreview.net/forum?id=rkl8sJBYyhV。
[96] Vaishaal Shankar, Alex Fang, Wenshuo Guo, Sara Fridovich-Keil, Jonathan Ragan-Kelley, Ludwig Schmidt, Benjamin Recht，无切线的神经核，载于：International Conference on Machine Learning, PMLR, (ISSN: 2640-3498) 2020, pp. 8614-8623。
[97] Blake Woodworth, Suriya Gunasekar, Jason D. Lee, Edward Moroshko, Pedro Savarese, Itay Golan, Daniel Soudry, Nathan Srebro，过参数化模型中的核区域与丰富区域，载于：Conference on Learning Theory, PMLR, (ISSN: 2640-3498) 2020, pp. 3635-3673。
[98] Lénai c Chizat, Francis Bach，使用逻辑损失训练的宽两层神经网络中梯度下降的隐式偏差，载于：Conference on Learning Theory, PMLR, (ISSN: 2640-3498) 2020, pp. 1305-1338。
[99] Gilad Yehudai, Ohad Shamir，论随机特征在理解神经网络中的能力与局限，载于：Advances in Neural Information Processing Systems, 2019, pp. 6598-6608。
[100] Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, Andrea Montanari，两层神经网络惰性训练的局限性，载于：Advances in Neural Information Processing Systems, 2019, pp. 9111-9121。
[101] Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, Andrea Montanari，神经网络何时优于核方法？Adv. Neural Inf. Process. Syst. 33 (2020)。
[102] Stefano Spigler, Mario Geiger, Matthieu Wyart，核方法的渐近学习曲线：经验数据与教师-学生范式，J. Stat. Mech. Theory Exp. 2020 (12) (2020) 124001，出版方：IOP Publishing。
[103] Jonas Paccolat, Matthieu Wyart, Stefano Spigler，各向同性核在简单不变量上的表现，Mach. Learn. Sci. Technol. (2020)。
[104] Sebastian Goldt, Marc Mézard, Florent Krzakala, Lenka Zdeborová，建模数据结构对神经网络学习的影响：隐藏流形模型，Phys. Rev. X 10 (4) (2020) 041044，出版方：American Physical Society。
[105] Greg Ongie, Rebecca Willett, Daniel Soudry, Nathan Srebro，有界范数无限宽ReLU网络的函数空间视角：多变量情形，载于：8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020, 2020，https://iclr.cc/virtual_2020/poster_H1INPxHKDH.html。
[106] Jonas Paccolat, Leonardo Petrini, Mario Geiger, Kevin Tyloo, Matthieu Wyart，神经网络中不变流形的几何压缩，2020，arXiv预印本arXiv:2007.11471。
[107] Samet Oymak, Zalan Fabian, Mingchen Li, Mahdi Soltanolkotabi，利用雅可比矩阵低秩结构的神经网络泛化保证，2019，arXiv预印本arXiv:1906.05392。
[108] Dmitry Kopitkov, Vadim Indelman，神经谱对齐：实证研究，载于：Artificial Neural Networks and Machine Learning – ICANN 2020, Springer International Publishing, 2020。

[第21页，第1段]
[P1/1]
[109] Blake Bordelon, Abdulkadir Canatar, Cengiz Pehlevan，核回归与宽神经网络中依赖谱的学习曲线，载于：国际机器学习会议，PMLR，（ISSN：2640-3498）2020，第1024–1034页。
[110] Bernhard Scholkopf, Alexander Smola, Klaus-Robert Müller，核主成分分析，载于：核方法进展——支持向量学习，MIT出版社，1999，第327–352页。
[111] Eric Degiuli, E. Lerner, M. Wyart，有限温度下阻塞转变的理论，J. Chem. Phys. 142 (16) (2015) 164503。
