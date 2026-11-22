[第1页，第1段]
从动力系统视角分析神经网络

[第1页，第2段]
Dennis Chemnitz, Maximilian Engel, Christian Kuehn, Sara-Viola Kuntz

[第1页，第3段]
1 柏林自由大学数学系，Arnimallee 6，14195 柏林，德国
2 阿姆斯特丹大学Korteweg de-Vries数学研究所，Science Park 105-107，1098 XG 阿姆斯特丹，荷兰
3 慕尼黑工业大学计算、信息与技术学院数学系，Boltzmannstraße 3，85748 加兴，德国
4 慕尼黑数据科学研究所（MDSI），加兴，德国
5 慕尼黑机器学习中心（MCML），慕尼黑，德国

[第1页，第4段]
2026年6月16日

[第1页，第5段]
摘要

[第1页，第6段]
在本章中，我们利用动力系统来分析机器学习算法的若干方面。作为一项阐述性贡献，我们展示了如何将深度神经网络、（随机）梯度下降及相关主题中的各种挑战重新表述为动力学命题。我们还处理了三个具体挑战。首先，我们考虑信息通过神经网络传播的过程，即研究不同架构下的输入-输出映射。我们解释了增广神经常微分方程（neural ODEs）表示给定正则性任意函数的通用嵌入性质，按合适函数类对多层感知机和神经常微分方程进行分类，以及神经延迟方程中的记忆依赖性。其次，我们从动力学角度考虑神经网络的训练方面。我们描述了梯度下降的动力系统视角，并研究超定问题的稳定性。然后我们将此分析扩展到过参数化设置，并描述稳定性边缘现象，同时结合对隐式偏差的可能解释进行讨论。对于随机梯度下降，我们通过插值解的Lyapunov指数给出过参数化设置的稳定性结果。第三，我们解释关于神经网络平均场极限的几个结果。我们描述了一个结果，该结果通过有向图测度将现有技术扩展到涉及图极限的异质神经网络。这表明大类神经网络如何自然地落入图上Kuramoto型模型及其大图极限的框架。最后，我们指出，使用动力学研究可解释和可靠AI的类似策略也可应用于生成模型或梯度训练方法中的基本问题等设置，例如反向传播或梯度消失/爆炸。

[第1页，第7段]
1 引言

[第1页，第8段]
鉴于近年来人工智能的巨大成功及其对我们社会许多方面不可避免的影响，机器学习的实际应用与我们对其的理论理解之间出现了令人担忧的差距。由于所涉及任务和算法的动态性质，机器学习（ML）和人工智能（AI）与成熟的动力系统数学理论深度关联。这种丰富的相互作用为理论分析和理解开辟了许多可能性。广义上，出现了两个主要方向：（a）我们使用ML/AI技术来更好地理解给定的动力系统；（b）我们将ML算法本身视为动力系统，并尝试使用动力学技术理解ML/AI能力。这两个方向已经活跃了数十年[40, 80]，但最近重新获得了显著关注[20, 38]。关于（a）已有许多有趣的途径，这些

[第2页，第1段]
通常更直接一些，因为机器学习往往可以作为一个几乎黑箱的工具，从数据中插值或外推动力学。在本章中，我们完全聚焦于第二个方向 (b)。这一视角往往极具挑战性，并且在可预见的未来很可能依然如此。其中一些挑战是：

[第2页，第2段]
(C1) 何时才可能真正将关于可解释/可靠人工智能的问题重新表述为动力学框架？

[第2页，第3段]
(C2) 在动力学背景下，与其他非线性系统相比，机器学习算法在其分析中会带来哪些额外挑战？

[第2页，第4段]
(C3) 人们可以期望通过严格证明来完全证成多少分析结果？

[第2页，第5段]
我们将在本章中通过指出若干具体重新表述关于人工智能/机器学习问题的实例，来肯定地回答 (C1)。以动力学方式重新解释几乎任何机器学习算法，都可以为数学/理论分析提供一个非常有效的切入角度。这种重新表述是完全自然的，例如，任何人工神经网络都作为网络上的动力系统动态地处理信息，而训练权重通常是迭代进行的，从而形成一个网络的动力系统。神经网络的这一视角也可以很好地嵌入到结合了两种动力学方面的自适应（或协同进化）网络框架中 [15]。事实上，动力系统中的许多经典结果可以立即用于理解机器学习算法的动力学 [120, 122]。然而，(C2) 的一个关键方面是，在实践中系统通常具有如此高的维度和异质性，以至于必须对动力学进行初步约化。我们将在此遵循这一范式，首先尝试将神经网络设计的问题（即网络上的动力学）与训练给定架构权重的问题（即网络的动力学）分开。此外，我们将指出，当人们仅隔离算法的单个方面时，许多解释机器学习/人工智能的挑战通常可以显著简化。只有在进行适当的约化之后，我们才有希望针对挑战 (C3) 获得完整的分析证明。

[第2页，第6段]
本章的一个关键主题是，我们自始至终强调并解释为什么将人工智能/机器学习重新视为动力学问题是自然且有利的。我们没有直接以完全一般性来处理挑战 (C2) 和 (C3)，而是聚焦于通过我们自己近期工作中的结果来说明它们。这展示了动力系统方法如何能够有助于理解人工智能。当然，结果的选择提供了有偏见的视角，而且肯定有许多有趣的结果可以讨论。然而，正如本书引言中所述，本书也作为德国研究基金会优先项目（SPP2298 深度学习基础）第一阶段的最终报告，本章的所有四位作者都参与了该项目。因此，我们通过选择在参与优先项目期间产生的近期工作来兼顾这一双重目的。

[第2页，第7段]
1.1 基本框架

[第2页，第8段]
一个一般的神经网络是一个函数

[第2页，第9段]
$ 
\Phi : \mathbb{R}^D \times \mathbb{R}^d \to \mathbb{R}^q, \quad (\theta, x) \mapsto \Phi(\theta, x),
 $

[第2页，第10段]
它依赖于输入数据 $  x  $ 和参数 $  \theta  $。一个典型的神经网络模型定义在图/网络上，由两个主要过程组成：信息传播和学习。信息传播过程描述网络上的动力学，即数据通过网络流动，而学习过程描述网络的动力学，即其权重和偏置的演化。由于网络的动力学影响网络上的动力学，反之亦然，因此神经网络是一个自适应动力网络。

[第2页，第11段]
网络上的动力学：信息传播

[第2页，第12段]
对于固定权重，神经网络将输入 $  x \in \mathbb{R}^d  $ 的状态映射到输出 $  \Phi(\theta, x)  $ 的状态，并由此定义了一个映射

[第2页，第13段]
$ 
\Phi_\theta : \mathbb{R}^d \to \mathbb{R}^q, \quad x \mapsto \Phi_\theta(x) := \Phi(\theta, x).
 $

[第2页，第14段]
由于信息传播描述的是固定参数上的过程，我们将其称为网络上的动力学。

[第3页，第1段]
网络的动力学：学习过程

[第3页，第2段]
为了使用神经网络的输入-输出映射 $\Phi_\theta$ 来近似给定数据，可以调整参数 $\theta$。通常，对于监督学习，训练数据由输入-输出对 $(x, y) \in \mathbb{R}^d \times \mathbb{R}^q$ 组成，这些数据用于通过（随机）基于梯度的方法最小化预定义的损失函数。梯度下降定义了一个更新映射

[第3页，第3段]
$$\varphi : \mathbb{R}^D \to \mathbb{R}^D, \quad \theta \mapsto \varphi(\theta) := \theta - \eta \nabla \mathcal{L}(\theta),$$

[第3页，第4段]
其中 $\eta > 0$ 是学习率，$\mathcal{L}$ 是损失函数。对于随机梯度下降，这个更新映射被替换为一个随机更新映射

[第3页，第5段]
$$\varphi : \Omega \times \mathbb{R}^D \to \mathbb{R}^D, \quad (\omega, \theta) \mapsto \varphi_\omega(\theta),$$

[第3页，第6段]
其中 $(\Omega, \mathbb{P})$ 是一个概率空间。由于学习过程迭代地修改底层图，我们将其称为网络的动力学，即学习过程修改底层网络边的权重（或链接）。

[第3页，第7段]
1.2 本章结构

[第3页，第8段]
第2节将信息通过网络传播的过程，即如方程(2)中的输入-输出映射 $\Phi_\theta$，作为一个动力系统进行研究。在介绍前馈神经网络（第2.1节）之后，将神经常微分方程（ODEs）和延迟微分方程（DDEs）视为深度神经网络对应的无限深度极限（第2.2节）。接下来，给出并讨论了文献[88, 89, 90]中的主要结果：表示给定正则性任意函数的增广神经常微分方程的通用嵌入（第2.3节），多层感知机和神经常微分方程在 $C^k$-函数类方面的分类（第2.4节），以及神经延迟微分方程中的记忆依赖性（第2.5节）。

[第3页，第9段]
第3节将神经网络的训练过程作为一个动力系统进行研究，刻画极小值的动力学稳定性，并讨论稳定性对从训练数据到测试数据的泛化问题的影响。在形式化优化任务并区分超定和超参数化情形（第3.1节）之后，我们引入梯度下降的动力系统视角，并研究超定问题的稳定性（第3.2节）。然后我们将此分析扩展到超参数化设置，并描述稳定性边缘现象，同时结合隐式偏差的可能解释（第3.3节）。在引入随机梯度下降的随机动力系统框架，并简要讨论超定设置（第3.4节）之后，我们呈现文献[25]中的关键结果，该结果通过插值解的Lyapunov指数刻画了超参数化设置下随机梯度下降的稳定性（第3.5节）。

[第3页，第10段]
第4节讨论机器学习中其他一些能被动力学视角很好地描述的重要主题。首先，我们简要讨论玻尔兹曼机和Hopfield网络（第4.1节），它们可以在相互作用粒子系统（IPS）的一般框架内理解。对于IPS，我们接着考虑平均场极限，这有助于部署动力学严谨工具进行分析（第4.2节）。我们陈述一个结果，证明相当一般图上的Kuramoto型（随机）IPS具有平均场极限[83]，使用了有向图测度和图算子理论[82, 86]。许多深度神经网络属于这一类别，包括循环神经网络和Transformer（第4.3节）。最后，我们还想说明机器学习中的许多其他问题也能从动力学视角中极大受益。我们涵盖生成模型及其各种形式，允许马尔可夫链理论、演化博弈论或随机微分方程的定性性质的应用和进一步发展（第4.4节）。作为最后一步，我们强调甚至反向传播的概念也只是在反向时间沿轨迹使用变分方程，这是一个非常经典的动力学概念（第4.5节）。

[第3页，第11段]
2 神经网络作为动力系统

[第3页，第12段]
在本节中，我们关注通过网络的信息传播过程，由固定权重 $\theta \in \mathbb{R}^D$ 的输入-输出映射 $\Phi_\theta$ 给出，如第1.1节所定义。所考虑的动力学

[第4页，第1段]
网络上的动力学可以在离散或连续时间尺度上定义。在接下来的两节中，我们介绍不同的神经网络架构。在第2.1节中，我们关注离散时间尺度上的前馈神经网络（FNNs），例如多层感知机（MLPs）、残差神经网络（ResNets）和密集连接残差网络（DenseResNets）。在第2.2节中，我们介绍神经常微分方程（neural ODEs）和神经延迟微分方程（neural DDEs），它们可以解释为ResNets和DenseResNets的无限深度极限。

[第4页，第2段]
将神经网络的输入-输出映射$\Phi_\theta$作为动力系统来研究，与哪些函数可以被映射$\Phi_\theta$表示和逼近的问题相关联。在第2.3节中，介绍了通用嵌入和通用逼近的概念。随后，陈述了近期工作[88]、[89]和[90]的主要结果。在第2.4节中，通过Morse函数分析了MLPs和neural ODEs情况下$\Phi_\theta$的几何结构。这些性质被用于在第2.5节中研究神经DDEs的记忆容量与其逼近能力之间的相互作用。总体而言，我们强调了神经网络的结构设计与动力学性质之间的相互作用，这有助于对网络上的动力学有更深刻和理论化的理解。

[第4页，第3段]
### 2.1 前馈神经网络

[第4页，第4段]
在大多数被研究的神经网络架构中，神经元被组织成层$h_l \in \mathbb{R}^{d_l}$，其中$l \in \{0, \ldots, L\}$，构建一个前馈神经网络。层数$L$称为网络的深度，每层最大神经元数$\max_{l \in \{0, \ldots, L\}} \{d_l\}$称为网络的宽度。所得的神经网络是一个映射$\Phi_\theta : \mathcal{X} \to \mathbb{R}^q$，其输入层为$h_0 = x \in \mathcal{X}$，$\mathcal{X} \subset \mathbb{R}^d = \mathbb{R}^{d_0}$，输出层为$h_L \in \mathbb{R}^q = \mathbb{R}^{d_L}$，隐藏层为$h_1, \ldots, h_{L-1}$。

[第4页，第5段]
最著名的前馈神经网络模型是多层感知机（MLP），Rosenblatt在1957年就已对其进行了研究[117]。一般MLP的更新规则由下式给出

[第4页，第6段]
$$h_{l+1} = f_l(h_l, \theta_l) := \tilde{W}_l \sigma_l(W_l h_l + b_l) + \tilde{b}_l$$  \hspace{1cm} (3)

[第4页，第7段]
其中$l \in \{0, \ldots, L-1\}$，激活函数为$\sigma_l : \mathbb{R}^{m_l} \to \mathbb{R}^{m_l}$，$W_l, \tilde{W}_l$是适当维度的权重矩阵，$b_l, \tilde{b}_l$是偏置。我们将层$h_l$的参数简记为$\theta_l := (W_l, \tilde{W}_l, b_l, \tilde{b}_l)$，所有参数记为$\theta = (\theta_0, \ldots, \theta_{L-1})$。激活函数$\sigma_l$按分量应用，通常选择为tanh、soft-plus、sigmoid或（普通、泄漏或参数化）ReLU。更新规则(3)既包括外部非线性的情况（若$\tilde{W}_l = \text{Id}$，$\tilde{b}_l = 0$），也包括内部非线性的情况（若$W_l = \text{Id}$且$b_l = 0$）。对于第2.4节中MLPs的分析，我们需要额外假设激活函数的每个分量$[\sigma_l]_i, i \in \{1, \ldots, m_l\}$都是严格单调的。

[第4页，第8段]
**定义2.1**（多层感知机（MLP））。所有MLPs $\Phi_\theta : \mathcal{X} \to \mathbb{R}^q$，$\mathcal{X} \subset \mathbb{R}^d$为开集，具有更新规则(3)和按分量应用的严格单调激活函数$[\sigma_l]_i \in C^k(\mathbb{R}, \mathbb{R})$，$k \geq 0$，的集合记为$\Xi^k(\mathcal{X}, \mathbb{R}^q) \subset C^k(\mathcal{X}, \mathbb{R}^q)$。

[第4页，第9段]
根据层$h_l$的维度$d_l$和激活函数$\sigma_l$的维度$m_l$，每个前馈神经网络可以被归类为三种不同的架构类型。为表述方便，我们在下文中假设对所有$l \in \{0, \ldots, L-1\}$有$d_l = m_l$，一般情况在[89]中讨论。

[第4页，第10段]
- **非增广FNN：** 层的维度从$h_0$到$h_L$单调递减，即对所有$l \in \{1, \ldots, L\}$有$d_{l-1} \geq d_l$。
- **增广FNN：** 最大维度层$h_{l_{\text{max}}}$比输入层$h_0$更宽，即$d_{l_{\text{max}}} > d_0$，且对所有$l \in \{1, \ldots, l_{\text{max}}\}$有$d_{l-1} \leq d_l$，对所有$l \in \{l_{\text{max}} + 1, \ldots, L\}$有$d_{l-1} \geq d_l$。
- **带瓶颈的FNN：** 存在一个称为瓶颈的层$h_{l_{\text{B}}}$，以及两个层$h_i$和$h_j$，使得$0 \leq i < l_{\text{B}} < j \leq L$且$d_i > d_{l_{\text{B}}}$，$d_{l_{\text{B}}} < d_j$。

[第4页，第11段]
这三种不同的架构类型构成了所有以层$h_l \in \mathbb{R}^{d_l}$结构化的前馈神经网络的完整不相交划分。在MLPs的情况下，我们将非增广的、

[第5页，第1段]
图1：当 $ q = 1 $ 时，非增强、增强和瓶颈标量前馈神经网络的结构。通常，前馈神经网络的输出可以是多维的。图1(a)-(c)改编自[89, 图3.2(a)-(c)]。

[第5页，第2段]
增强和瓶颈架构分别记为 $ \Xi_{\mathrm{B}}^{k}(\mathcal{X}, \mathbb{R}^{q}) $、$ \Xi_{\mathrm{A}}^{k}(\mathcal{X}, \mathbb{R}^{q}) $ 和 $ \Xi_{\mathrm{B}}^{k}(\mathcal{X}, \mathbb{R}^{q}) $。在图1中，展示了 $ q = 1 $ 时非增强、增强以及带瓶颈的FNN示例。在第2.4节对MLP的分析中，我们主要关注单个输出分量，对应于标量情形 $ q = 1 $。

[第5页，第3段]
一类更先进的前馈神经网络是残差神经网络（ResNets）[59]。在ResNet架构中，所有层具有相同的宽度 $ d = d_l $，$ l \in \{0, \ldots, L\} $，更新规则形式为

[第5页，第4段]
$ 
h_{l+1} = h_l + f_l(h_l, \theta_l)
 $

[第5页，第5段]
其中 $ l \in \{0, \ldots, L-1\} $。与MLP的更新规则(3)相比，ResNet更新规则(4)通过加项 $ h_l $ 允许额外的捷径/跳跃连接。额外的跳跃连接对于层数 $ L \gg 1 $ 的深度神经网络的基于梯度的训练方法是有利的[59]。此外，如果更新规则与层无关，即对所有 $ l \in \{0, \ldots, L-1\} $ 有 $ f_{\mathrm{ResNet}}(\cdot, \cdot) = f_l(\cdot, \cdot) $，则ResNet更新规则(4)激发了对神经常微分方程的研究，这将在第2.2节中介绍。

[第5页，第6段]
更为演进的前馈架构例如U-Nets（参见[116]）和DenseNets（参见[70]），它们允许额外的层间连接。通过这种方式，信息或特征

[第6页，第1段]
先前层的信息可以在后续层中被重新引入。此外，层间连接可以缓解训练过程中的问题，例如梯度消失 [70]。在本工作中，我们聚焦于神经延迟微分方程（neural DDEs），它可以被解释为具有 ResNet 结构的稠密连接前馈神经网络（DenseResNets）的连续时间类比。在 DenseResNet 架构中，所有层具有相同的宽度 $d = d_l$，$l \in \{0, \ldots, L\}$，且层 $h_{l+1}$ 可以依赖于所有先前层，从而得到更新规则

[第6页，第2段]
$$h_{l+1} = h_l + f_{\text{Dense},l}(h_l, h_{l-1}, \ldots, h_0, \theta_{\text{Dense},l})$$  \hspace{1cm} (5)

[第6页，第3段]
其中 $l \in \{0, \ldots, L-1\}$。这里 $\theta_{\text{Dense},l}$ 存储了层 $h_{l+1}$ 与 $h_{l+1-i}$ 之间对于每个 $i \in \{1, \ldots, l+1\}$ 的所有权重和偏置。需要注意的是，DenseResNet 在结构上不同于具有全连接层的 FNN 或 ResNet，后者的所有权重矩阵仅包含非零元素。在图 2 中，展示了具有更新规则 (5) 的 DenseResNet 的所有可能的层间连接。

[第6页，第4段]
![图 2：稠密连接残差神经网络（DenseResNet）的结构。与图 1 不同，每个由方块表示的顶点对应于一个层 $h_l \in \mathbb{R}^{d_l}$。该图改编自 [90, 图 1.1(b)]。](image)

[第6页，第5段]
### 2.2 神经 ODE 与神经 DDE

[第6页，第6段]
除了离散时间尺度上的神经网络（如第 2.1 节介绍的前馈神经网络）之外，还存在连续时间尺度上的架构。首先，我们介绍神经常微分方程（neural ODEs），它可以被解释为残差神经网络的无限深度极限 [26, 38, 59, 88]。一方面，像神经 ODE 这样的连续时间模型在训练过程中具有恒定内存开销的优势；另一方面，它们为深度神经网络的动力学提供了洞见，如下文所启发 [26]。对于所有 $l \in \{0, \ldots, L-1\}$，当 $f_{\text{ResNet}}(\cdot, \cdot) = f_l(\cdot, \cdot)$ 时，ResNet 的迭代更新规则 (4) 可以作为初值问题（IVP）的欧拉离散化得到

[第6页，第7段]
$$\frac{dh}{dt} = f_{\text{ODE}}(h(t), \theta(t)), \quad h(0) = x,$$  \hspace{1cm} (6)

[第6页，第8段]
在时间区间 $[0, T]$ 上，步长为 $\delta = \frac{T}{L}$，向量场为 $f_{\text{ODE}}(\cdot, \cdot) := \frac{1}{3} f_{\text{ResNet}}(\cdot, \cdot)$。这里，IVP 的解 $h$ 可以被解释为隐藏层，函数 $\theta$ 为权重。ODE 的初始条件是第一层 $h_0 = x \in \mathbb{R}^d$，输出层 $h_L$ 对应于 IVP 的时间-$T$ 映射 $h(T) \in \mathbb{R}^d$（参见 [57]）。典型的学习算法应用于神经网络的平稳参数，而非参数函数。为了能够针对平稳参数进行优化，IVP (6) 可以重写为如下形式

[第6页，第9段]
$$\frac{dh}{dt} = f(t, h(t)), \quad h(0) = x,$$  \hspace{1cm} (7)

[第6页，第10段]
其中 $f$ 是依赖于参数的非自治向量场。由于欧拉离散化的离散化误差取决于步长 $\delta = \frac{T}{L}$，ResNet 越深，神经 ODE 动力学对 ResNet 动力学的近似就越好。

[第6页，第11段]
类似于神经 ODE，我们定义神经延迟微分方程（neural DDEs），它可以被解释为 DenseResNet 的无限深度极限。在关于向量

[第7页，第1段]
在域上（如[90]中所指定），更新规则(5)可以通过延迟微分方程（DDE）的欧拉离散化获得

[第7页，第2段]
$ 
\frac{dh(t)}{dt} = F(t, h_t), \quad h(s) = c_x(s) \quad \text{for } s \in [-\tau, 0],
 $

[第7页，第3段]
其中延迟为 $ \tau \geq 0 $，延迟函数 $ h_t \in C([-\tau, 0], \mathbb{R}^d) $ 定义为 $ h_t(s) = h(t + s) $ 对于 $ s \in [-\tau, 0] $，参数依赖的非自治向量场 $ F $ 和常数初始数据 $ c_x : [-\tau, 0] \to \mathbb{R}^d $ 满足 $ c_x(t) = x $。神经DDE的输入函数 $ c_x $ 由相应DenseResNet的输入数据 $ h_0 = x $ 指定，输出由时间-$ T $映射 $ h(T) $ 给出[90, 142]。由于DDE (8)生成的动力系统的状态空间 $ C([-\tau, 0], \mathbb{R}^d) $ 是无限维的，因此有必要在时间区间 $ [-\tau, 0] $ 上指定一个初始函数，而不是像ODE那样在 $ t = 0 $ 处指定一个初始值。

[第7页，第4段]
由(7)和(8)定义的神经ODE和神经DDE仅限于建模具有相同输入和输出维度 $ d $ 的数据。为了克服这一限制，两个仿射线性层

[第7页，第5段]
$ 
\lambda : \mathbb{R}^d \to \mathbb{R}^m, \quad \lambda(x) = Wx + b, \quad \tilde{\lambda} : \mathbb{R}^m \to \mathbb{R}^q, \quad \tilde{\lambda}(x) = \tilde{W}x + \tilde{b},
 $

[第7页，第6段]
可以添加在 $ m $ 维神经ODE或DDE的解之前和之后。神经网络 $ \Phi_\theta : \mathcal{X} \to \mathbb{R}^q $ 现在定义如下：给定一些初始数据 $ x \in \mathcal{X} \subset \mathbb{R}^d $，变换后的状态 $ \lambda(x) \in \mathbb{R}^m $ 用作ODE (7)的点初始条件，$ c_{\lambda(x)} \in C([-\tau, 0], \mathbb{R}^m) $ 用作DDE (8)的常数初始函数。然后，ODE/DDE在时间区间 $ [0, T] $ 上求解。神经ODE/DDE架构的输出定义为

[第7页，第7段]
$ 
\Phi_\theta(x) = \tilde{\lambda}(h(T)) \in \mathbb{R}^q,
 $

[第7页，第8段]
这是第二个线性变换 $ \tilde{\lambda} $ 应用于时间-$ T $映射 $ h(T) $。具有两个额外仿射线性层的神经ODE/DDE的结构如图3所示。连续时间神经网络(10)的参数 $ \theta $ 由权重和偏置 $ W, \tilde{W}, b, \tilde{b} $ 以及向量场 $ f $ 或 $ F $ 的参数给出。

[第7页，第9段]
在下文中，我们不将分析限制在向量场的固定参数化上，而是考虑一般的、非参数化的神经ODE/DDE架构。为此，对于神经ODE，我们考虑空间 $ C^{0,k}([0, T] \times \mathbb{R}^m, \mathbb{R}^m) $，$ k \geq 1 $，它由所有在第一个变量上连续且在第二个变量上 $ k $ 次连续可微的函数组成。对于神经DDE，我们考虑空间 $ C^{0,k}_b([0, T] \times C([-\tau, 0], \mathbb{R}^m), \mathbb{R}^m) $，$ k \geq 1 $，由在第一个变量上连续且关于第二个变量具有直到 $ k $ 阶有界连续导数的函数组成。

[第7页，第10段]
**定义2.2**（神经ODE）。对于 $ k \geq 1 $，所有神经ODE架构 $ \Phi_\theta : \mathcal{X} \to \mathbb{R}^q $ 的集合，其中 $ \mathcal{X} \subset \mathbb{R}^d $ 是开集，由(10)定义并基于具有非参数化向量场 $ f \in C^{0,k}([0, T] \times \mathbb{R}^m, \mathbb{R}^m) $ 的初值问题(7)，记为 $ \text{NODE}^k(\mathcal{X}, \mathbb{R}^q) \subset C^k(\mathcal{X}, \mathbb{R}^q) $。

[第7页，第11段]
**定义2.3**（神经DDE）。对于 $ k \geq 1 $，所有神经DDE架构 $ \Phi_\theta : \mathcal{X} \to \mathbb{R}^q $ 的集合，其中 $ \mathcal{X} \subset \mathbb{R}^d $ 是开集，由(10)定义并基于具有非参数化向量场 $ F \in C^{0,k}_b([0, T] \times C([-\tau, 0], \mathbb{R}^m), \mathbb{R}^m) $ 的DDE (8)，记为 $ \text{NDDE}^k(\mathcal{X}, \mathbb{R}^q) \subset C^k(\mathcal{X}, \mathbb{R}^q) $。

[第7页，第12段]
根据(7)和(8)中向量场的定义，可以得出每个延迟为 $ \tau = 0 $ 的神经DDE都是神经ODE。如[88, 90]所示，神经ODE和神经DDE也可以在比定义2.2和2.3中对向量场的更弱正则性假设下良好定义。根据维度 $ d $ 和 $ m $，我们可以区分不同类型的神经ODE和神经DDE架构：

[第7页，第13段]
- **非增广神经ODE/DDE：** 满足 $ m \leq d $ 且权重矩阵 $ W, \tilde{W} $ 具有满秩。

[第7页，第14段]
- **增广神经ODE/DDE：** 满足 $ m > d $ 且权重矩阵 $ W, \tilde{W} $ 具有满秩。

[第7页，第15段]
- **退化神经ODE/DDE：** 权重矩阵 $ W, \tilde{W} $ 中的一个是奇异的。

[第8页，第1段]
图3：具有两个仿射线性层的通用神经常微分方程/时滞微分方程（neural ODE/DDE）架构结构。图3(a)改编自[89, 图4.1(a)]，图3(b)改编自[90, 图2.4(b)]。

[第8页，第2段]
我们分别将非增广架构记为 $NODE^K_A(\mathcal{X}, \mathbb{R}^q)$ / $NDDE^K_{\tau, A}(\mathcal{X}, \mathbb{R}^q)$，将增广架构记为 $NODE^K_D(\mathcal{X}, \mathbb{R}^q)$ / $NDDE^K_{\tau, D}(\mathcal{X}, \mathbb{R}^q)$。图3中可视化了非增广神经常微分方程和增广神经常时滞微分方程的结构。通过利用连续时间动力系统理论，我们可以更好地理解神经常微分方程和神经常时滞微分方程的理论性质。借助近似结果，这些见解可以迁移到(4)中定义的深度ResNet和(5)中定义的深度DenseResNet。总之，我们可以直接使用常微分方程和时滞微分方程的动力系统方法来理解无限深度极限下的神经网络架构类别。

[第8页，第3段]
2.3 通用嵌入与通用近似

[第8页，第4段]
在监督学习中，神经网络被用于学习给定的真实数据

[第8页，第5段]
$$ \Psi : \mathcal{X} \to \mathcal{Y}, \quad x \mapsto y := \Psi(x), \tag{11} $$

[第8页，第6段]
其中 $\mathcal{X}$ 和 $\mathcal{Y}$ 为拓扑空间。因此，神经网络 $\Phi_\theta : \mathcal{X} \to \mathcal{Y}$ 的一个理想性质是通用近似，即能够以任意精度近似给定函数空间中的任意函数 $\Psi$。在从 $\mathcal{X}$ 映射到 $\mathcal{Y}$ 的 $k$ 次连续可微函数类 $C^k(\mathcal{X}, \mathcal{Y})$ 的背景下，通用近似的定义如下。

[第8页，第7段]
**定义2.4**（通用近似[88]）。设神经网络 $\Phi_\theta : \mathcal{X} \to \mathcal{Y}$ 具有参数 $\theta$、拓扑空间 $\mathcal{X}$ 和度量空间 $\mathcal{Y}$，若对于任意 $\varepsilon > 0$ 和每个函数 $\Psi \in C^k(\mathcal{X}, \mathcal{Y})$，存在参数 $\theta$ 的选择，使得对所有 $x \in \mathcal{X}$ 都有 $\text{dist}_\mathcal{Y}(\Phi_\theta(x), \Psi(x)) < \varepsilon$，则该网络关于空间 $C^k(\mathcal{X}, \mathcal{Y})$（$k \geq 0$）具有通用近似性质。

[第8页，第8段]
对于许多前馈神经网络架构，通用近似性质可以通过增加网络的宽度、深度或参数数量来获得[33, 69, 95, 110, 121]。事实上，早在20世纪50年代和60年代就已证明，映射的叠加和/或迭代可以使用非常简单的构建模块来近似函数和序列

[第9页，第1段]
块 [79, 122]。此外，对于神经 ODE，可以证明通用逼近定理，特别是通过增广相空间 [37, 78, 88, 119, 141]。除了通用逼近之外，在数学上研究通用嵌入（即通过神经网络精确表示函数）通常更为透明。分析神经网络精确输出的几何结构，取决于其结构，可以提供对某些架构为何优于其他架构的基本理解。

[第9页，第2段]
**定义 2.5**（通用嵌入 [88]）。一个神经网络 $\Phi_\theta : \mathcal{X} \to \mathcal{Y}$，参数为 $\theta$，拓扑空间为 $\mathcal{X}$ 和 $\mathcal{Y}$，如果对于每个函数 $\Psi \in C^k(\mathcal{X}, \mathcal{Y})$，都存在参数 $\theta$ 的选择，使得对于所有 $x \in \mathcal{X}$ 有 $\Phi_\theta(x) = \Psi(x)$，则称其关于空间 $C^k(\mathcal{X}, \mathcal{Y})$，$k \geq 0$，具有通用嵌入性质。

[第9页，第3段]
根据定义，每个具有通用嵌入性质的神经网络 $\Phi_\theta$ 也具有通用逼近性质。在接下来的第 2.4 节和第 2.5 节中，我们介绍近期工作 [89] 和 [90] 关于 MLP、神经 ODE 和神经 DDE 的输入-输出映射的几何结构及其对通用嵌入和通用逼近的影响的主要结果。在 [88] 中，通过迭代函数方程、微分几何、悬浮流和动力系统理论研究了神经 ODE 的嵌入能力。与 MLP 相比，如果向量场的维数足够大，则可以证明具有一般非自治向量场 $f$ 的神经 ODE 的通用嵌入结果。

[第9页，第4段]
**定理 2.6**（增广神经 ODE 的通用嵌入 [88]）。神经 ODE 架构 $NODE_A^k(\mathcal{X}, \mathbb{R}^q)$，$\mathcal{X} \subset \mathbb{R}^d$ 开，$k \geq 1$，对于 $m \geq d + q$ 具有关于空间 $C^k(\mathcal{X}, \mathbb{R}^q)$ 的通用嵌入性质。

[第9页，第5段]
在标量神经 ODE 的情况下，即 $q = 1$ 的神经 ODE，定理 2.6 对所有增广神经 ODE 成立，因为条件 $m \geq d + q = d + 1$ 等价于第 2.2 节中由 $m > d$ 给出的增广神经 ODE 的定义。

[第9页，第6段]
### 2.4 通过 Morse 函数分析几何结构

[第9页，第7段]
在本节中，我们将分析限制在标量 MLP 和标量神经 ODE 上，即输出维数为 $q = 1$。在 $q > 1$ 的神经网络情况下，我们的结果适用于输出的单个分量。我们旨在分析标量 MLP 和标量神经 ODE 的输入-输出映射 $\Phi_\theta : \mathcal{X} \to \mathbb{R}$，$\mathcal{X} \subset \mathbb{R}^d$，关于临界点的存在性和正则性性质，这通常通过 Morse 函数来刻画。

[第9页，第8段]
**定义 2.7**（Morse 函数 [63, 102]）。一个映射 $\Psi \in C^2(\mathcal{X}, \mathbb{R})$，$\mathcal{X} \subset \mathbb{R}^d$ 开，如果 $\Psi$ 的所有临界点都是非退化的，即对于每个由零梯度 $\nabla \Psi(p) = 0 \in \mathbb{R}^d$ 定义的临界点 $p \in \mathcal{X}$，Hessian 矩阵 $H_\Psi(p) \in \mathbb{R}^{d \times d}$ 是非奇异的，则称为 Morse 函数。

[第9页，第9段]
在光滑标量有界函数的 Banach 空间中，Morse 函数是稠密的，即光滑函数是 Morse 函数是一个通用性质。为了不仅区分一个函数是否为 Morse 函数，而且对临界点的存在性进行分类，我们定义了函数空间 $C^k(\mathcal{X}, \mathbb{R})$，$\mathcal{X} \subset \mathbb{R}^d$ 的三个不同子空间。

[第9页，第10段]
**定义 2.8**（$C^k$-函数类）。对于 $k \geq 2$，根据临界点的存在性和正则性，我们定义 $C^k(\mathcal{X}, \mathbb{R})$，$\mathcal{X} \subset \mathbb{R}^d$ 开的三个子空间：

[第9页，第11段]
$$(C^1)^k(\mathcal{X}, \mathbb{R}) := \{ \Psi \in C^k(\mathcal{X}, \mathbb{R}) : \nabla \Psi(x) \neq 0 \ \forall x \in \mathcal{X} \},$$

[第9页，第12段]
$$(C^2)^k(\mathcal{X}, \mathbb{R}) := \{ \Psi \in C^k(\mathcal{X}, \mathbb{R}) : (\exists p : \nabla \Psi(p) = 0) \ \text{and} \ (\nabla \Psi(q) = 0 \Rightarrow H_\Psi(q) \ \text{is non-singular}) \},$$

[第9页，第13段]
$$(C^3)^k(\mathcal{X}, \mathbb{R}) := \{ \Psi \in C^k(\mathcal{X}, \mathbb{R}) : \exists p : (\nabla \Psi(p) = 0 \ \text{and} \ H_\Psi(p) \ \text{is singular}) \}.$$

[第9页，第14段]
所定义的子空间是非空的，并构成 $C^k(\mathcal{X}, \mathbb{R})$ 的不相交细分，即 $C^k(\mathcal{X}, \mathbb{R}) = (C^1)^k(\mathcal{X}, \mathbb{R}) \cup (C^2)^k(\mathcal{X}, \mathbb{R}) \cup (C^3)^k(\mathcal{X}, \mathbb{R})$。

[第10页，第1段]
根据定义，类 $(C1)^k(\mathcal{X}, \mathbb{R})$ 和 $(C2)^k(\mathcal{X}, \mathbb{R})$ 中的所有函数都是 Morse 函数，而类 $(C3)^k(\mathcal{X}, \mathbb{R})$ 中的任何函数都不是 Morse 函数。所定义函数类的一维示例如下：$(C1)^k(\mathbb{R}, \mathbb{R})$ 包含所有严格单调函数，$(C2)^k(\mathbb{R}, \mathbb{R})$ 包含二次函数 $x \mapsto x^2$，而 $(C3)^k(\mathbb{R}, \mathbb{R})$ 包含所有阶数 $n \geq 3$ 的高阶单项式 $x^n$。对于 $d = 2$，类 $(C2)^k(\mathbb{R}^2, \mathbb{R})$ 中两个 Morse 函数的示例（分别由圆形和 XOR 数据集表示）在图 4 中可视化。

[第10页，第2段]
![图 4：具有底层 Morse 函数 $\Psi(x) = x_1^2 + x_2^2 - 1$ 的二维数据集。](image)

[第10页，第3段]
(a) 具有底层 Morse 函数 $\Psi(x) = x_1^2 + x_2^2 - 1$ 的圆形数据集。

[第10页，第4段]
(b) 具有底层 Morse 函数 $\Psi(x) = x_2^2 - x_1^2$ 的 XOR 数据集。

[第10页，第5段]
在标量 MLP 和标量神经 ODE 的背景下，Morse 函数起着至关重要的作用。这是因为，根据第 2.1 节和第 2.2 节中定义的架构类型（非增广、增广、瓶颈/退化），关于临界点的存在性和正则性会得到不同的结果。接下来的定理聚焦于 MLP，其中所有权重矩阵均为满秩。如果一个 MLP 具有奇异权重矩阵，我们可以通过显式构造识别出一个等价的 MLP，称为范式，它具有相同的输入-输出映射 $\Phi_\theta$，但所有权重矩阵均为满秩 [89]。通过应用算法获得仅含满秩权重矩阵的范式，底层结构以及因此的分类（非增广、增广、瓶颈）可能会发生变化。

[第10页，第6段]
**定理 2.9**（标量 MLP 和标量神经 ODE 的分类 [89]）。设 $\mathcal{X} \subset \mathbb{R}^d$ 为开集，考虑仅含满秩矩阵且权重空间为 $\mathbb{W} = (W_0, \overline{W}_0, \ldots, W_{L-1}, \overline{W}_{L-1})$ 的标量 MLP $\Phi_\theta \in \Xi^k(\mathcal{X}, \mathbb{R})$，以及权重空间为 $\mathbb{V} = (W, \overline{W})$ 的标量神经 ODE $\Phi_\theta \in \text{NODE}^k(\mathcal{X}, \mathbb{R})$。那么，根据网络的底层结构（非增广、增广、瓶颈/退化），表 1 中的分类结果成立。

[第10页，第7段]
从表 1 的结果中，我们得出结论：MLP 和神经 ODE 在非增广和增广情况下，关于临界点的存在性和正则性表现出相同的几何性质。这些结果与 MLP 激活函数 $\sigma$ 和神经 ODE 的向量场 $f$ 无关。对于非增广架构和退化神经 ODE，我们可以直接推断它们不可能具有通用嵌入性质，因为并非所有函数类 $(C1)^k(\mathcal{X}, \mathbb{R})$、$(C2)^k(\mathcal{X}, \mathbb{R})$ 和 $(C3)^k(\mathcal{X}, \mathbb{R})$ 都能被表示。借助扰动结果可知，非增广 MLP 和神经 ODE 也不可能具有通用逼近性质 [89]。非通用逼近的结果直接转移到具有多维输出 $q > 1$ 的架构，因为通用逼近需要对所考虑网络的每个单独分量都成立。在增广情况下，我们的结果与现有文献一致，因为已建立的 MLP 和神经 ODE 通用逼近定理使用的是增广架构 [69, 78, 88, 110]。在具有瓶颈的 MLP 情况下，[89] 中的结果显示了根据底层图中瓶颈位置而定的更详细分类。此外，还讨论了为什么这些结果


[第11页，第2段]
在瓶颈/退化情形下也具有可比性。主要原因是神经常微分方程在隐藏层中不能存在瓶颈，因为底层初值问题的维数随时间保持不变。

[第11页，第3段]
2.5 记忆容量对通用逼近性的影响

[第11页，第4段]
在上一节2.4中，我们已经看到非增广神经常微分方程不具有通用嵌入性质。如果相空间足够大，定理2.6表明增广神经常微分方程具有通用嵌入性质。自然地，问题随之而来：是否也可以通过向网络架构中添加记忆而非增加相空间的宽度或维数来实现通用逼近？对于具有更新规则(5)的DenseResNets，记忆通过层间连接引入；对于神经时滞微分方程，记忆通过DDE (8)的时滞参数$\tau$引入。在本节中，我们聚焦于定义2.3中的神经时滞微分方程，并证明：取决于记忆容量$K\tau$（由Lipschitz常数$K$与时滞$\tau$的乘积给出），类$\text{NDDE}_\tau^k(\mathcal{X}, \mathbb{R}^q)$关于空间$C^j(\mathcal{X}, \mathbb{R}^q)$具有或不具有通用逼近性质。

[第11页，第5段]
定理2.10（神经时滞微分方程中的记忆依赖性[90]）。设$\Phi_\theta \in \text{NDDE}_\tau^k(\mathcal{X}, \mathbb{R}^q)$，$\mathcal{X} \subset \mathbb{R}^d$为开集，$k \geq 1$，是一个时滞为$\tau \geq 0$的神经时滞微分方程。设底层向量场$F$关于第二变量全局Lipschitz连续，Lipschitz常数为$K$。固定常数$w, \tilde{w} \in (0, \infty)$和$A \geq 0$。则以下结论成立：

[第11页，第6段]
(a) 若$m = d$，存在连续函数$\tau_0((0, \infty), [0, T])$，使得对于$K \in (0, \infty)$有$K\tau_0(K\epsilon) < 1$，从而若$\tau \in [0, \tau_0(K))$，则神经时滞微分方程类$\text{NDDE}_{\tau, N}^k(\mathcal{X}, \mathbb{R}^q)$（其中对所有$t \in [0, T]$有$||F(t, 0)||_\infty \leq A$，且权重矩阵$W, \tilde{W}$满足$||W||_\infty \leq w$，$||\tilde{W}||_\infty \leq \tilde{w}$）关于空间$C^j(\mathcal{X}, \mathbb{R}^q)$，$j \geq 0$，不具有通用逼近性质。

[第11页，第7段]
(b) 设$\Psi \in C_b^k(\mathcal{X}, \mathbb{R}^q)$，$k \geq 1$，全局Lipschitz常数为$K_\Psi$。则若

[第11页，第8段]
$$K\tau \geq 2 \left(1 + \frac{K_\Psi}{w\tilde{w}}\right),$$

[第11页，第9段]
且$m = \max\{d, q\}$，则映射$\Psi$可由神经时滞微分方程$\Phi_\theta \in \text{NDDE}_\tau^k(\mathcal{X}, \mathbb{R}^q)$表示，其权重矩阵$W, \tilde{W}$满足$||W||_\infty = w$，$||\tilde{W}||_\infty = \tilde{w}$，时滞为$\tau$，关于第二变量的全局Lipschitz常数为$K$。

[第11页，第10段]
由(a)部分可知，通过删除向量场的任意分量可得：对于$m \leq d$，神经时滞微分方程不能具有通用逼近性质。(b)部分的结论可通过向向量场添加额外的零分量推广至所有$m \geq \max\{d, q\}$。对于$m \geq d + q$，它

[第12页，第1段]
与定理2.6类似，神经DDEs $\Phi_\theta \in \text{NDDE}^k_{\tau, A}(\mathcal{X}, \mathbb{R}^q)$ 也具有关于空间 $C^k(\mathcal{X}, \mathbb{R}^q)$ 的通用嵌入性质，其中 $\mathcal{X} \subset \mathbb{R}^d$ 为开集 [90]。关于神经DDEs记忆依赖性的所有结果均在图5中可视化。当输出维度不大于输入维度时，即 $d \geq q$，有 $\max\{d, q\} = d$，因此对于 $m = d$，定理2.10的(a)和(b)两个结果均适用。总之，定理2.10就记忆在网络架构中的作用——即增加记忆如何实现通用逼近和通用嵌入——给出了数学上精确的陈述。

[第12页，第2段]
![图5：定理2.6和定理2.10关于神经DDEs记忆依赖性的结果在三维参数空间 $(K, \tau, m) \in [0, \infty) \times [0, T] \times \mathbb{N}$ 中的联合可视化，其中 $K$ 为Lipschitz常数，$\tau$ 为延迟，$m$ 为DDE向量场的维度。无法实现通用逼近的参数区域以橙色显示，具有通用嵌入性质的参数区域以蓝色显示。该图改编自[90, 图3.4]。(图像)](image)

[第12页，第3段]
### 3 作为动力系统的优化算法

[第12页，第4段]
在上一节中，我们展示了如何利用动力系统来研究固定网络上的动力学。接下来，我们将讨论如何将神经网络的训练过程解释为一个动力系统。我们特别关注刻画极小值的动力学稳定性以及稳定性对泛化的影响。在第3.1节中，我们介绍优化任务以及超定问题与超参数化问题之间的区别。在第3.2节中，我们引入梯度下降的动力系统视角，并研究超定问题的稳定性。在第3.3节中，我们将这一分析推广到超参数化情形，并讨论稳定性边缘（edge of stability）现象以及隐式偏差（implicit bias）的可能解释。在第3.4节中，我们为随机梯度下降引入随机动力系统框架，并简要讨论超定情形。最后，在第3.5节中，我们将超参数化情形的稳定性分析推广到随机梯度下降。

[第12页，第5段]
#### 3.1 机器学习中的优化任务

[第12页，第6段]
训练神经网络 $\Phi : \mathbb{R}^D \times \mathbb{R}^d \to \mathbb{R}^q$，$(\theta, x) \mapsto \Phi_\theta(x) = \Phi(\theta, x)$（参见(2)）的目标是找到参数 $\theta$，使得在适当意义下 $\Phi_\theta \approx \Psi$，其中 $\Psi$ 为真实函数（ground-truth function）。在实践中，真实函数 $\Psi$ 是未知的，因此必须从 $N$ 个训练样本 $(x_i, y_i)_{i=1,\ldots,N}$ 中推断出合适的参数 $\theta$，其中对每个 $i$ 有 $y_i = \Psi(x_i)$。为此，我们引入函数 $\ell : \mathbb{R}^q \times \mathbb{R}^q \to [0, \infty)$，$(y', y) \mapsto \ell(y', y)$，用于度量预测值 $y'$ 与真实答案 $y$ 之间的距离。当然，这样的距离函数应满足 $\ell(y', y) = 0$ 当且仅当 $y' = y$。然后我们可以通过下式定义损失函数（loss function）$\mathcal{L} : \mathbb{R}^D \to [0, \infty)$：

[第12页，第7段]
$$\mathcal{L}(\theta) := \frac{1}{N} \sum_{i=1}^{N} \ell(\Phi(\theta, x_i), y_i).$$  (12)

[第13页，第1段]
值 $L(\theta)$，也称为经验误差，衡量神经网络 $\Phi_\theta$ 在训练数据集 $\{x_1, \ldots, x_N\}$ 上逼近真实函数 $\Psi$ 的程度。对于我们这里考虑的回归问题，$\ell$ 的一个自然选择由 $\ell(y', y) := \frac{1}{2} \|y' - y\|_2^2$ 给出，其中 $\|\cdot\|_2$ 表示欧几里得范数。在这种情况下，损失函数 $L$ 就是所谓的均方误差（MSE）。

[第13页，第2段]
我们不是直接寻找使 $\Phi_\theta \approx \Psi$ 的参数 $\theta$，而是寻找使 $L(\theta) \approx 0$ 的 $\theta$，这意味着至少对于所有 $x \in \{x_1, \ldots, x_N\}$，有 $\Phi_\theta(x) \approx \Psi(x)$。理想情况下，我们希望找到损失函数 $L$ 的全局最小值 $\theta^*$，即

[第13页，第3段]
$$\theta^* \in \arg\min_{\theta \in \mathbb{R}^D} L(\theta). \tag{13}$$

[第13页，第4段]
在研究这样的优化任务时，区分问题是超定还是超参数化至关重要。形式为 (13) 的优化任务如果 $D < qN$ 则称为超定的，如果 $D > qN$ 则称为超参数化的。根据著名的双下降曲线 [13, 图 1]，超定模型和超参数化模型都能表现良好，而“中间地带” $D \approx qN$ 往往表现不佳。两种情形之间的主要区别可以通过询问是否存在满足 $L(\theta) = 0$ 的参数 $\theta$ 来看出。由 (12)，这样的参数 $\theta$ 必须插值训练数据，即它必须满足

[第13页，第5段]
$$\Phi(\theta, x_i) = y_i, \quad \text{for all } i \in [N]. \tag{14}$$

[第13页，第6段]
在超定情形 $D < qN$ 下，(14) 中方程的数量超过 $\theta$ 的维数，并且一般不存在满足 $L(\theta) = 0$ 的 $\theta \in \mathbb{R}^D$。此外，$L$ 的全局最小值一般是唯一的。因此，训练过程关注的主要问题是算法是否收敛到该全局最小值。

[第13页，第7段]
另一方面，在超参数化情形 $D > qN$ 下，$\theta$ 的维数超过 (14) 中方程的数量，并且 $L(\theta) = 0$ 可能有无限多个解。特别地，假设 $D > qN$，以下陈述由 Sard 定理（参见例如 [101]）得出：

[第13页，第8段]
**定理 3.1**（插值解集作为嵌入子流形 [30]）。对于每个连续可微的网络函数 $\Phi : \mathbb{R}^D \times \mathbb{R}^d \to \mathbb{R}^q$ 和每个位于 Lebesgue 零集（可能依赖于 $\Phi$）之外的训练数据集 $((x_1, y_1), \ldots, (x_N, y_N)) \in (\mathbb{R}^d \times \mathbb{R}^q)^N$，插值解集 $M := \{\theta \in \mathbb{R}^D : L(\theta) = 0\}$ 要么为空，要么是 $\mathbb{R}^D$ 的 $(D - qN)$ 维嵌入子流形。

[第13页，第9段]
如果网络函数具有足够的表达能力，我们期望存在插值参数，这意味着 $M$ 是一个非空的 $(D - qN)$ 维流形。在这种情况下，每个 $\theta \in M$ 都是 $L$ 的全局最小值，并且 (13) 不能唯一地定义 $\theta^*$。因此，不仅询问优化算法是否收敛到全局最小值是有意义的，而且询问收敛到哪一个也是有意义的。后一个问题对于理解隐式偏差尤为重要。这里，隐式偏差指的是优化算法倾向于找到泛化良好的全局最小值 $\theta^*$，这意味着即使对于 $x \notin \{x_1, \ldots, x_N\}$，也有 $\Phi_{\theta^*}(x) \approx \Psi(x)$。

[第13页，第10段]
### 3.2 梯度下降与 Milnor 稳定性

[第13页，第11段]
可用于训练神经网络的最简单算法称为梯度下降（GD）。在确定性地选择一些初始参数 $\theta_0$（例如 $\theta_0 = 0$）或随机地选择（例如 $\theta_0 \sim \mathcal{N}(0, \Sigma)$）之后，参数根据递推关系依次更新

[第13页，第12段]
$$\theta_{n+1} := \varphi(\theta_n) := \theta_n - \eta \nabla L(\theta_n). \tag{15}$$

[第13页，第13段]
这里 $\eta$ 是一个称为学习率的正实数，$\nabla L$ 表示损失函数 $L$ 的梯度。如上文所启发，我们关注 $\theta_n$ 当 $n \to \infty$ 时的行为。递推 (15) 可以解释为离散时间动力系统，并且容易看出对于所有 $n \in \mathbb{N}$，我们有 $\theta_n = \varphi^n(\theta_0)$。这允许我们采取动力学的视角，即将焦点从考虑单个轨迹转移到考虑映射 $\varphi$ 在整个参数空间上的几何性质。如果 $\theta^* \in \mathbb{R}^D$ 是 $L$ 的局部最小值，那么 $\nabla L(\theta^*) = 0$，因此 $\theta^*$ 是 $\varphi$ 的不动点，即我们有 $\varphi(\theta^*) = \theta^*$。梯度下降算法是否能够实际收敛到局部最小值 $\theta^*$ 取决于其动力学稳定性。

[第13页，第14段]
目前，考虑超定情形 $D < qN$。我们引入以下关于孤立不动点（即具有不包含其他不动点的非空邻域的不动点）的稳定性定义。

[第14页，第1段]
图6：二维参数空间中，超定（左）和过参数化（右）情形下损失景观的典型几何形态。损失 $\mathcal{L}$ 在蓝色区域较低，在橙色区域较高。细黑线显示 $\mathcal{L}$ 的等值集。在左图中，两个黑点表示局部极小值，空心点表示鞍点。在右图中，插值解的流形 $\mathcal{M}$（参见定理3.1）显示为粗黑线。

[第14页，第2段]
**定义3.2**（孤立不动点的Milnor稳定性）。

[第14页，第3段]
(i) 若存在正Lebesgue测度的可能初始化集合 $\theta_0 \in \mathbb{R}^D$，使得梯度下降迭代序列 $\theta_n$ 收敛到 $\theta^*$，则称孤立不动点 $\theta^* = \varphi(\theta^*)$ 为Milnor稳定的，即

[第14页，第4段]
$$\text{Vol} \left\{ \theta \in \mathbb{R}^D : \lim_{n \to \infty} \varphi^n(\theta) = \theta^* \right\} > 0.$$

[第14页，第5段]
(ii) 若对于 $\theta^*$ 的每个开邻域 $U \subset \mathbb{R}^D$，存在正Lebesgue测度的可能初始化集合 $\theta_0 \in U$，使得梯度下降迭代序列 $\theta_n$ 永远停留在 $U$ 中并收敛到 $\theta^*$，则称孤立不动点 $\theta^* = \varphi(\theta^*)$ 为局部Milnor稳定的，即

[第14页，第6段]
$$\text{Vol} \left\{ \theta \in U : \varphi^n(\theta) \in U, \forall n \in \mathbb{N} \text{ and } \lim_{n \to \infty} \varphi^n(\theta) = \theta^* \right\} > 0.$$

[第14页，第7段]
Milnor稳定性这一名称的动机在于：不动点 $\theta^*$ 是Milnor稳定的当且仅当单点集 $\{\theta^*\}$ 是Milnor吸引子[100]。由于以下事实（它是定义的直接推论），Milnor稳定性对于优化任务而言是一个有趣的概念。

[第14页，第8段]
**命题3.3.** 设 $\theta^*$ 为局部极小值。对于参数空间 $\mathbb{R}^D$ 上的概率测度 $\nu$，设 $\theta_0$ 为服从分布 $\nu$ 的 $\mathbb{R}^D$ 值随机变量，并设 $\theta^n = \varphi^n(\theta_0)$ 为梯度下降的迭代。假设 $\nu$ 与Lebesgue测度等价，即

[第14页，第9段]
$$\nu(A) = 0 \Leftrightarrow \text{Vol}(A) = 0, \text{ for each Borel set } A \subset \mathbb{R}^D.$$

[第14页，第10段]
则 $\nu(\lim_{n \to \infty} \theta^n = \theta^*) > 0$，即以正概率到达 $\theta^*$，当且仅当 $\theta^*$ 是Milnor稳定的。

[第14页，第11段]
注意，局部Milnor稳定性的概念强于Milnor稳定性的概念。然而，如果映射 $\varphi$ 是非奇异的，即Lebesgue零集的原像也是Lebesgue零集，则这两个定义是等价的。

[第15页，第1段]
命题3.4. 设$  \theta^*  $为$  \mathcal{L}  $的一个局部极小值点，并假设映射$  \varphi  $是非奇异的。那么$  \theta^*  $是局部Milnor稳定的当且仅当它是Milnor稳定的。

[第15页，第2段]
证明. 由定义3.2可直接得出，每个局部Milnor稳定点都是Milnor稳定的。只需证明反之亦然。假设$  \varphi  $是非奇异的，且$  \theta^*  $不是局部Milnor稳定的，令$  U \subset \mathbb{R}^D  $为$  \theta^*  $的一个邻域，使得集合

[第15页，第3段]
$ 
N := \left\{ \theta \in U : \varphi^n(\theta) \in U, \forall n \in \mathbb{N}, \text{ 且 } \lim_{n \to \infty} \varphi^n(\theta) = \theta^* \right\}
 $

[第15页，第4段]
是Lebesgue零测集。通过反复应用$  \varphi  $的非奇异性，我们得到

[第15页，第5段]
$ 
\operatorname{Vol} \left( \varphi^{-m}(N) \right) = 0, \forall m \in \mathbb{N}.
 $

[第15页，第6段]
由收敛的定义，我们有

[第15页，第7段]
$ 
\left\{ \theta \in \mathbb{R}^D : \lim_{n \to \infty} \varphi^n(\theta) = \theta^* \right\} = \bigcup_{m=1}^{\infty} \varphi^{-m}(N)
 $

[第15页，第8段]
因此

[第15页，第9段]
$ 
\operatorname{Vol} \left\{ \theta \in \mathbb{R}^D : \lim_{n \to \infty} \varphi^n(\theta) = \theta^* \right\} = 0
 $

[第15页，第10段]
这意味着$  \theta^*  $不是Milnor稳定的。

[第15页，第11段]
文献[31, 定理12]中已证明，梯度下降更新映射$  \varphi  $确实是通有非奇异的，这使得这两个定义在实际应用中几乎等价。尽管局部Milnor稳定性严格弱于经典的渐近稳定性概念，但局部Milnor稳定性——更重要的是其缺失——可以使用相同的技术来证明。

[第15页，第12段]
设$  \theta^*  $为严格局部极小值点，即Hessian矩阵$  \operatorname{Hess} \mathcal{L}(\theta^*)  $是正定的。特别地，$  \theta^*  $是一个孤立局部极小值点，其稳定性由$  \varphi  $在$  \theta^*  $附近的线性化决定。

[第15页，第13段]
定理3.5（谱稳定性与Milnor稳定性）. 对于严格局部极小值点$  \theta^*  $，令$  \rho(\operatorname{D} \varphi(\theta^*))  $表示$  \varphi  $在$  \theta^*  $处的Jacobian矩阵的谱半径。那么，若$  \rho(\operatorname{D} \varphi(\theta^*)) < 1  $，则$  \theta^*  $是局部Milnor稳定的；仅当$  \rho(\operatorname{D} \varphi(\theta^*)) \leq 1  $时，$  \theta^*  $才是局部Milnor稳定的。

[第15页，第14段]
证明概要. 在$  \rho(\operatorname{D} \varphi(\theta^*)) < 1  $的情形下，局部稳定性由稳定流形定理[77, 第6.2节]得出。在$  \rho(\operatorname{D} \varphi(\theta^*)) > 1  $的情形下，局部稳定性的缺失由中心不稳定流形定理[77, 第6.2节]得出。

[第15页，第15段]
由于$  \operatorname{D} \varphi(\theta^*) = \mathbb{I}_D - \eta \operatorname{Hess} \mathcal{L}(\theta^*)  $（参见(15)），且$  \operatorname{Hess} \mathcal{L}(\theta^*)  $是正定的，$  \operatorname{D} \varphi(\theta^*)  $的谱半径小于1当且仅当

[第15页，第16段]
$ 
2 > \eta \rho(\operatorname{Hess} \mathcal{L}(\theta^*)) = \eta \| \operatorname{Hess} \mathcal{L}(\theta^*) \|,
 $

[第15页，第17段]
其中等号利用了Hessian矩阵是对称的这一事实，且右端的矩阵范数是由$  \mathbb{R}^D  $上的欧几里得范数导出的算子范数。

[第15页，第18段]
注3.6. $  \varphi  $在局部极小值点$  \theta^*  $附近的线性近似

[第15页，第19段]
$ 
\varphi(x) = x^* + \operatorname{D} \varphi(x^*)(x - x^*) + o(|x - x^*|)
 $

[第15页，第20段]
是损失函数$  \mathcal{L}  $的二次近似

[第15页，第21段]
$ 
\mathcal{L}(\theta) = \mathcal{L}(\theta^*) + \langle \theta - \theta^*, \operatorname{Hess} \mathcal{L}(\theta^*)(\theta - \theta^*) \rangle + o\left(|\theta - \theta^*|^2\right)
 $

[第15页，第22段]
的动力学类比，后者更常用于研究局部极小值点的稳定性。稳定性条件(17)也可以通过考虑损失函数的二次近似同样快速地推导出来，在这种情况下，收敛结果通常被称为下降引理[16, 命题1.2.3]。我们提倡动力学视角，因为它更适合将以下稳定性分析推广到随机优化算法（参见下文第3.5节）。

[第16页，第1段]
3.3 过参数化设置下梯度下降的稳定性

[第16页，第2段]
将注意力转向过参数化设置 $D > qN$，严格的局部极小值不再存在。事实上，很容易看出损失函数 $L$ 的 Hessian 矩阵的秩至多为 $qN$，因此当 $D > qN$ 时其核空间总是非平凡的。取而代之，作为一项基本假设，我们假定插值参数集合 $M := \{ \theta \in \mathbb{R}^D : L(\theta) = 0 \}$ 非空，并构成 $\mathbb{R}^D$ 的一个 $(D - qN)$ 维嵌入子流形（参见定理 3.1）。尽管局部极小值可能仍然存在，但在过参数化设置下我们将仅关注这些全局极小值。如前所述，每个 $\theta^* \in M$ 都是 $\varphi$ 的不动点。与超定设置不同，我们不应再期望能够证明对于任意固定的 $\theta^* \in M$ 有 $\mathbb{P}(\theta_n \to \theta^*) > 0$，因为 $M$ 是不可数的。相反，我们试图刻画对于哪些极小值 $\theta^*$，算法具有正概率收敛到接近 $\theta^*$ 的极小值。这引导我们调整稳定性的概念。

[第16页，第3段]
**定义 3.7**（过参数化设置下 GD 的稳定性）。

[第16页，第4段]
(i) 全局极小值 $\theta^* \in M$ 称为稳定的，如果对于 $\theta^*$ 在 $M$ 的子流形拓扑中的每个开邻域 $V \subset M$，使得梯度下降收敛到某个全局极小值 $\theta' \in V$ 的可能初始化 $\theta_0$ 的集合具有正 Lebesgue 测度，即

[第16页，第5段]
$$ \text{Vol} \{ \theta \in \mathbb{R}^D : \exists \theta' \in V, \text{ s.t. } \lim_{n \to \infty} \varphi^n(\theta) = \theta' \} > 0. $$

[第16页，第6段]
(ii) 全局极小值 $\theta^* \in M$ 称为局部稳定的，如果存在 $\theta^*$ 的一个开邻域 $U$，使得对于 $\theta^*$ 在 $M$ 的流形拓扑中的每个开邻域 $V \subset M$，使得梯度下降永远停留在 $U$ 中并收敛到某个全局极小值 $\theta' \in V$ 的可能初始化 $\theta_0$ 的集合具有正 Lebesgue 测度，即

[第16页，第7段]
$$ \text{Vol} \{ \theta \in \mathbb{R}^D : \forall n \in \mathbb{N}, \varphi^n(\theta) \in U \text{ and } \exists \theta' \in V, \text{ s.t. } \lim_{n \to \infty} \varphi^n(\theta) = \theta' \} > 0. $$

[第16页，第8段]
与命题 3.3 类似，这种稳定性概念具有如下解释，该解释同样直接由定义得出。

[第16页，第9段]
**命题 3.8.** 设 $\theta^* \in M$ 为全局极小值。对于参数空间 $\mathbb{R}^D$ 上的概率测度 $\nu$，设 $\theta_0$ 为服从分布 $\nu$ 的 $\mathbb{R}^D$ 值随机变量，并设 $\theta^n = \varphi^n(\theta_0)$ 为梯度下降的迭代。我们定义 $(M \cup \{ \emptyset \})$ 值随机变量 $\theta_{\text{lim}}$ 为

[第16页，第10段]
$$ \theta_{\text{lim}} := \begin{cases} \lim_{n \to \infty} \theta_n, & \text{if } \exists \theta \in M, \lim_{n \to \infty} \theta_n = \theta, \\ \emptyset, & \text{otherwise.} \end{cases} $$

[第16页，第11段]
这里 $\emptyset$ 应被视为一个异常状态，用于考虑梯度下降不收敛到 $M$ 的可能性。假设 $\nu$ 与 Lebesgue 测度等价（参见 (16)），并定义

[第16页，第12段]
$$ \text{supp}(\theta_{\text{lim}}) = \text{supp}(\text{law}(\theta_{\text{lim}})) = \{ \theta \in M : \forall U \in \mathcal{U}_{\theta,M}, \nu(\{ \theta_0 : \theta_{\text{lim}} \in U \}) > 0 \}, $$

[第16页，第13段]
其中 $\mathcal{U}_{\theta,M}$ 表示 $\theta$ 在 $M$ 的流形拓扑中的开邻域族。

[第16页，第14段]
则 $\theta^* \in \text{supp}(\theta_{\text{lim}})$ 当且仅当 $\theta^*$ 在定义 3.7(i) 的意义下是稳定的。

[第16页，第15段]
如果映射 $\varphi$ 是非奇异的，则可以证明定义 3.7(i) 中的稳定性概念与定义 3.7(ii) 中的局部稳定性概念是等价的，这与命题 3.4 的证明类似。我们同样旨在刻画局部稳定的极小值。

[第16页，第16段]
对于全局极小值 $\theta^* \in M$，设 $\mathcal{T}(\theta^*)$ 表示流形 $M$ 在 $\theta^*$ 处的切空间，$\mathcal{N}(\theta^*) = \mathcal{T}(\theta^*)^\perp$ 表示法空间。容易验证

[第16页，第17段]
$$ \mathcal{T}(\theta^*) = \ker(\text{Hess } L(\theta^*)) \quad \text{and} \quad \mathcal{N}(\theta^*) = \text{im}(\text{Hess } L(\theta^*)). $$

[第16页，第18段]
因此，Jacobian 矩阵 $\text{D}\varphi(\theta^*) = \mathbb{1}_D - \eta \text{Hess } L(\theta^*)$ 尊重分解 $\mathbb{R}^D = \mathcal{T}(\theta^*) \otimes \mathcal{N}(\theta^*)$，且对于每个 $\partial \in \mathcal{T}(\theta^*)$ 有 $\text{D}\varphi(\theta^*) \partial = \partial$。特别地，1 是 $\text{D}\varphi(\theta^*)$ 的特征值，其几何重数至少为 $D - qN$。因此，上一节中的稳定性条件 $\rho(\text{D}\varphi(\theta^*)) < 1$ 永远不会被满足，取而代之我们应考虑 $\text{D}\varphi(\theta^*)$ 在法空间 $\mathcal{N}(\theta^*)$ 上的限制，它定义了一个线性自同构 $\text{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)} : \mathcal{N}(\theta^*) \to \mathcal{N}(\theta^*)$。该线性映射决定了 $M$ 在 $\theta^*$ 处的横截稳定性。

[第17页，第1段]
图7：过参数化优化问题中梯度下降的轨迹。损失函数由 $  \mathcal{L}(\theta) = (1 - \theta^{(1)}\theta^{(2)})^2  $ 给出，其中 $  \theta = (\theta^{(1)}, \theta^{(2)}) \in \mathbb{R}^2  $。全局极小值流形 $  \mathcal{M} = \{\theta^{(1)}\theta^{(2)} = 1\}  $ 的不稳定部分用虚线表示，稳定部分用实线表示。学习率 $  \eta = \frac{1}{2}  $ 的梯度下降轨迹用粉色表示。其初始化于 $  \theta_0 = (2.5, 0.41)  $，靠近 $  \mathcal{M}  $ 的一个不稳定区域。梯度下降逃离 $  \mathcal{M}  $ 的该区域，转而收敛到稳定区域中的一个点。

[第17页，第2段]
定理3.9（全局极小值的谱稳定性与局部稳定性）。若 $  \rho(\mathcal{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)}) < 1  $，则全局极小值 $  \theta^*  $ 在定义3.7(ii)的意义下是局部稳定的；仅当 $  \rho(\mathcal{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)}) \leq 1  $ 时成立。

[第17页，第3段]
证明概要。在 $  \rho(\mathcal{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)}) < 1  $ 的情形下，局部稳定性由稳定流形定理推出。在 $  \rho(\mathcal{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)}) > 1  $ 的情形下，局部稳定性的缺失由中心不稳定流形定理推出。详见[25, 定理A]或[2, 第2节]。

[第17页，第4段]
利用恒等式 $  \mathcal{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)} = \mathbb{1}_D|_{\mathcal{N}(\theta^*)} - \eta \operatorname{Hess} \mathcal{L}(\theta^*)|_{\mathcal{N}(\theta^*)}  $ 以及算子 $  \mathcal{L}(\theta^*)|_{\mathcal{N}(\theta^*)}: \mathcal{N}(\theta^*) \to \mathcal{N}(\theta^*)  $ 是正定的事实，我们可以看到稳定性条件 $  \rho(\mathcal{D}\varphi(\theta^*)|_{\mathcal{N}(\theta^*)}) < 1  $ 等价于

[第17页，第5段]
$ 
\| \operatorname{Hess} \mathcal{L}(\theta^*)|_{\mathcal{N}(\theta^*)}\| < \frac{2}{\eta}.
 $

[第17页，第6段]
尽管这是超定设定下稳定性条件(17)的直接类比，但在过参数化设定下其内涵相当不同。条件(17)表明学习率 $  \eta  $ 应足够小，以使某个感兴趣的极小值在算法下稳定。相反，条件(19)应被解释为关于所讨论的全局极小值的条件，而非关于学习率的条件。从这个观点看，它表明算法只能收敛到损失函数足够平坦的全局极小值。由于平坦极小值至少在启发式意义上与良好泛化相关联[65]，这为隐式偏差提供了一种可能的解释。对于学习率的选择，这表明更高的学习率应导致更严格的选择、更平坦的极小值和更好的泛化。这一假设确实得到了经验支持[54, 67]。

[第17页，第7段]
最后，我们请读者参阅数值研究[29]。在该研究中观察到，在实际相关场景中，梯度下降收敛到所谓的稳定性边缘，即收敛到一个极小值 $  \theta^*  $，使得

[第17页，第8段]
$ 
\| \operatorname{Hess} \mathcal{L}(\theta^*)|_{\mathcal{N}(\theta^*)}\| \approx \frac{2}{\eta}.
 $

[第18页，第1段]
这表明条件 (19) 并非仅仅是数学上的技术性细节。相反，所选的学习率直接影响梯度下降算法所找到的极小值的平坦性。特别地，它表明在训练的后期阶段，梯度下降的动力学与其连续时间模拟——梯度流 $ \dot{\theta} = -\nabla L(\theta) $——在性质上是不同的，在梯度流下每个严格局部极小值都是稳定的。例如，这可以从梯度下降在训练后期阶段并不单调地减小损失这一事实中看出，如 [29] 所示。

[第18页，第2段]
### 3.4 随机梯度下降作为随机动力系统

[第18页，第3段]
实践中使用的大多数算法都是随机梯度下降（SGD）的变体。这些算法不是每次迭代都直接优化 $ L $，而是为每一步选取一个称为小批量（mini-batch）的随机子集 $ \Xi $，然后针对该子集对应的损失 $ L_{\Xi} $ 进行优化，其定义为

[第18页，第4段]
$ 
L_{\Xi}(\theta) = \frac{1}{|\Xi|} \sum_{i \in \Xi} \ell(\Phi(\theta, x_i), y_i).
 $

[第18页，第5段]
更准确地说，更新规则 (15) 被替换为

[第18页，第6段]
$ 
\theta_{n+1} := \theta_n - \eta \nabla L_{\Xi_{n+1}}(\theta_n).
 $

[第18页，第7段]
这里 $ \Xi_1, \Xi_2, \ldots $ 是 $ [N] $ 的一系列随机独立、均匀分布的 $ B $ 元子集，其中 $ 1 \leq B < N $ 称为小批量大小。

[第18页，第8段]
虽然稳定性条件 (19) 被广泛认为是确定性梯度下降的正确条件，但对于随机梯度下降，人们提出了若干不同的概念 [140, 97, 25, 6]。这里，我们遵循 [25]，将梯度下降的分析推广到随机情形，从而得到一个基于随机矩阵乘积的 Lyapunov 指数（Lyapunov exponent）的稳定性条件。关于该条件与文献中提出的其他稳定性概念之间关系的详细讨论，见 [25, 附录 A]。

[第18页，第9段]
为了将梯度下降的稳定性分析推广到随机梯度下降，我们首先为随机梯度下降引入一个动力系统框架。设 $ \Omega, \mathcal{F}, \mathbb{P}) $ 是定义随机变量 $ \Xi_i) $ 的概率空间，使得对每个 $ i \in \mathbb{N} $，随机变量 $ \Xi_i : \Omega \to \{\Xi \subset [N] : |\Xi| = B\} $ 是 $ \mathcal{F} $-可测的。随机梯度下降定义了一个随机动力系统（random dynamical system）[8]，其构造如下。对每个可能的小批量 $ \Xi \subset [N] $，$ |\Xi| = B $，我们定义一个映射 $ \varphi_{\Xi} : \mathbb{R}^D \to \mathbb{R}^D $ 为

[第18页，第10段]
$ 
\varphi_{\Xi}(\theta) := \theta - \nabla L_{\Xi}(\theta).
 $

[第18页，第11段]
此外，对每个 $ \omega \in \Omega $ 和每个 $ n \in \mathbb{N}_0 $，我们定义一个映射 $ \varphi_{\omega}^{(n)} : \mathbb{R}^D \to \mathbb{R}^D $，其定义为 $ \varphi_{\omega}^{(0)}(x) := x $ 以及

[第18页，第12段]
$ 
\varphi_{\omega}^{(n)} := \varphi_{\Xi_n(\omega)} \circ \cdots \circ \varphi_{\Xi_1(\omega)}.
 $

[第18页，第13段]
同样，我们有 $ \varphi_{\omega}^{(n)}(\theta_0) = \theta_n $。与确定性情形不同，我们不再有关系 $ \varphi_{\omega}^{(n+m)} = \varphi_{\omega}^{(n)} \circ \varphi_{\omega}^{(m)} $。为了表述随机情形下的类似性质，我们首先需要在概率空间上定义一个移位作用。设 $ \zeta : \Omega \to \Omega $ 是一个保持概率测度 $ \mathbb{P} $ 的可测映射，即它满足

[第18页，第14段]
$ 
\mathbb{P}(\zeta^{-1}(E)) = \mathbb{P}(E), \text{ 对每个事件 } E \in \mathcal{F},
 $

[第18页，第15段]
并且满足

[第18页，第16段]
$ 
(\Xi_1(\zeta\omega), \Xi_2(\zeta\omega), \ldots) = (\Xi_2(\omega), \Xi_3(\omega), \ldots).
 $

[第18页，第17段]
有了这些记号，可以验证映射 $ \varphi_{\omega}^{(n)} $ 满足余循环性质（cocycle property）

[第18页，第18段]
$ 
\varphi_{\omega}^{(n+m)} = \varphi_{\zeta^m\omega}^{(n)} \circ \varphi_{\omega}^{(m)},
 $

[第18页，第19段]
从而使对 $ \zeta, \varphi) $ 成为一个随机动力系统。

[第19页，第1段]
与梯度下降不同，局部甚至全局极小值 $\theta^*$ 对于随机梯度下降而言不再必然是固定点。然而，插值参数 $\theta^* \in \mathcal{M}$ 是随机动力系统 $\varphi_\omega^{(n)}$ 的几乎必然固定点，即对于每个小批量 $\Xi \subset [N]$，$|\Xi| = B$，我们有 $\varphi_\Xi(\theta^*) = \theta^*$，因此对于任意 $n \in \mathbb{N}$，$\varphi_\omega^{(n)}(\theta^*) = \theta^*$ 几乎必然成立。由于在超定（overdetermined）设定下 $\mathcal{M}$ 通常是空集，我们只能在超参数化（overparameterized）设定下将稳定性分析推广到随机算法。我们指出，在超定设定下，仍然可以研究 $\theta_n$ 的分布收敛到随机动力学的平稳分布而非收敛到单个参数 [58]。或者，可以考虑使用衰减学习率的随机梯度下降，这确实允许收敛（参见例如 [14, 41]）。这两种方法都超出了我们的讨论范围，在下文中我们仅限于超参数化设定 $D > qN$。

[第19页，第2段]
### 3.5 超参数化问题的 SGD

[第19页，第3段]
与第 3.3 节类似，我们再次作为基本假设假定插值参数集合 $\mathcal{M} := \{\theta \in \mathbb{R}^D : \mathcal{L}(\theta) = 0\}$ 非空，并构成 $\mathbb{R}^D$ 的一个 $(D - qN)$ 维嵌入子流形（参见定理 3.1）。我们通过以下方式将定义 3.7 推广到随机优化算法。

[第19页，第4段]
**定义 3.10**（超参数化设定下 SGD 的稳定性）：

[第19页，第5段]
(i) 全局极小值 $\theta^* \in \mathcal{M}$ 称为稳定的，如果对于 $\theta^*$ 的每个在 $\mathcal{M}$ 的子流形拓扑中开邻域 $V \subset \mathcal{M}$，使得随机梯度下降以正概率收敛到某个全局极小值 $\theta' \in V$ 的可能初始值 $\theta_0$ 的集合具有正 Lebesgue 测度，即

[第19页，第6段]
$$\text{Vol} \left\{ \theta \in \mathbb{R}^D : \mathbb{P} \left( \exists \theta' \in V, s.t. \lim_{n \to \infty} \varphi_\omega^{(n)}(\theta) = \theta' \right) > 0 \right\}$$

[第19页，第7段]
(ii) 全局极小值 $\theta^* \in \mathcal{M}$ 称为局部稳定的，如果存在 $\theta^*$ 的一个开邻域 $U$，使得对于 $\theta^*$ 的每个在 $\mathcal{M}$ 的流形拓扑中开邻域 $V \subset \mathcal{M}$，使得随机梯度下降以正概率永远停留在 $U$ 中同时收敛到某个全局极小值 $\theta' \in V$ 的可能初始值 $\theta_0$ 的集合具有正 Lebesgue 测度，即，

[第19页，第8段]
$$\text{Vol} \left\{ \theta \in \mathbb{R}^D : \mathbb{P} \left( \forall n \in \mathbb{N}, \varphi^n(\theta) \in U \text{ and } \exists \theta' \in V, s.t. \lim_{n \to \infty} \varphi^n(\theta) = \theta' \right) > 0 \right\}$$

[第19页，第9段]
同样，这种稳定性概念可以借助 $\theta_{\text{lim}}$ 的支撑集来解释。假设 $\theta_0$ 根据 $\mathbb{R}^D$ 上与 Lebesgue 测度等价的概率测度 $\nu$ 随机初始化（参见 (16)）。令 $\theta_n = \varphi_\omega^{(n)}(\theta_0)$ 为随机梯度下降的迭代值，并如 (18) 中那样定义随机变量 $\theta_{\text{lim}}$。这一次，$\theta_{\text{lim}}$ 依赖于初始化和训练的随机性。相应地，我们现在将 $\text{supp}(\theta_{\text{lim}})$ 定义为

[第19页，第10段]
$$\text{supp}(\theta_{\text{lim}}) := \{\theta \in \mathcal{M} : \forall U \in \mathcal{U}_\theta, \mathcal{M} : (\mathbb{P} \times \nu)(\{\omega, \theta_0\} : \theta_{\text{lim}} \in U\}) > 0\}.$$

[第19页，第11段]
**命题 3.11.** 对于全局极小值 $\theta^* \in \mathcal{M}$，$\theta^* \in \text{supp}(\theta_{\text{lim}})$ 当且仅当 $\theta^*$ 在定义 3.10(ii) 的意义下是稳定的。

[第19页，第12段]
如果函数 $\varphi_\Xi$ 对于每个小批量 $\Xi \subset [N]$ 都是非奇异的，则可以容易地调整命题 3.3 的证明以表明每个稳定极小值也是局部稳定的。由于 $\varphi_\Xi$ 是约简训练数据集上的梯度下降映射，[31] 的结果仍然表明该条件在一般情况下是满足的。与我们对梯度下降的分析类似，我们可以通过线性化更新映射来确定全局极小值 $\theta \in \mathcal{M}$ 是否局部稳定。然而，对于随机梯度下降，我们对每个小批量 $\Xi$ 得到不同的 Jacobian 矩阵 $D\varphi_\Xi(\theta^*)$。令 $A_\Xi(\theta^*) = D\varphi_\Xi(\theta^*): \mathcal{N}(\theta^*) \to \mathcal{N}(\theta^*)$ 为 $\varphi_\Xi$ 的 Jacobian 矩阵的横截部分。单个矩阵的主特征值在随机矩阵乘积中的正确类比由 Lyapunov 指数（Lyapunov exponent）给出，其存在性由 Furstenberg-Kesten 定理保证。

[第20页，第1段]
定理3.12（Furstenberg-Kesten定理[45]）。设$\theta^* \in \mathcal{M}$为全局最小值。存在一个（确定性的）实数$\lambda(\theta^*)$，称为Lyapunov指数（Lyapunov exponent），使得对于几乎所有的$\omega \in \Omega$，我们有

[第20页，第2段]
$$\lambda(\theta^*) = \lim_{n \to \infty} \frac{1}{n} \log \left\| D \left( \varphi_{\omega}^{(n)} \right) (\theta^*) \right\|_{\mathcal{N}(\theta^*)} = \lim_{n \to \infty} \frac{1}{n} \log \left\| A_{\Xi_n(\omega)} \cdot \ldots \cdot A_{\Xi_1(\omega)} \right\|.$$

[第20页，第3段]
条件$\lambda(\theta^*) < 0$是将梯度下降的稳定性条件$\rho(D\varphi(\theta^*))_{\mathcal{N}(\theta^*)} < 1$正确推广到随机梯度下降的情形。事实上，如果$\rho(D\varphi(\theta^*))_{\mathcal{N}(\theta^*)} < 1$，根据Gelfand公式，我们有

[第20页，第4段]
$$\lim_{n \to \infty} \frac{1}{n} \log \left\| D \left( \varphi^n \right) (\theta^*) \right\|_{\mathcal{N}(\theta^*)} = \lim_{n \to \infty} \frac{1}{n} \log \left\| \left( D\varphi(\theta^*) \right)_{\mathcal{N}(\theta^*)}^n \right\| = \log(\rho(D\varphi(\theta^*))_{\mathcal{N}(\theta^*)}),$$

[第20页，第5段]
从而建立了这一联系。因此，有理由假设：若$\lambda(\theta^*) < 0$则$\theta^*$局部稳定，且仅当$\lambda(\theta^*) \leq 0$时$\theta^*$局部稳定。然而，由于可能出现非一致双曲性（non-uniform hyperbolicity），其证明比确定性情形要困难得多。为克服这一障碍，需要对所讨论的全局最小值施加额外假设。

[第20页，第6段]
**定义3.13（正则最小值）。** 全局最小值$\theta^* \in \mathcal{M}$称为正则的，如果

[第20页，第7段]
(i) 对每个小批量（mini-batch）$\Xi$，算子$A_{\Xi}(\theta^*) \text{ and } Id - A_{\Xi}(\theta^*)$均可逆，且

[第20页，第8段]
(ii) 由$\{A_{\Xi}(\theta^*) : \Xi \subset [N], |\Xi| = B \}$生成的半群（semigroup）$S(\theta^*)$是强不可约的，即不存在$\mathcal{N}(\theta^*)$的有限个真子空间构成的集合在$S(\theta^*)$下不变。

[第20页，第9段]
注意，一般的全局最小值都是正则的。有了这一定义，文献[25]已经证明，对于正则全局最小值$\theta^*$，Lyapunov指数$\lambda(\theta^*)$确实决定了$\theta^*$的局部稳定性。

[第20页，第10段]
**定理3.14（SGD正则最小值的局部稳定性[25，定理B]）。** 设$\theta^* \in \mathcal{M}$为正则全局最小值。则若$\lambda(\theta^*) < 0$则$\theta^*$局部稳定，且仅当$\lambda(\theta^*) \leq 0$时$\theta^*$局部稳定。

[第20页，第11段]
文献[25]中给出的定理3.14的证明受到Baxendale和Stroock[12]为研究随机过程不变流形的稳定性而发展的一种技巧的启发。定理3.14的可能推广在[25，第2.6节]中进行了讨论。

[第20页，第12段]
总之，我们在本节中看到，（随机）梯度下降可以用（随机）动力系统来分析。选择一个适当的稳定性概念至关重要。特别地，在过参数化（overparameterized）情形下，要将定理3.14中的主导Lyapunov指数概念更全局地（即超越局部稳定性）用于具体给定的SGD，实际上是非常不平凡的。从动力学的角度来看，这并不令人意外，因为在诸如估计混沌系统中Lyapunov指数的背景下也会出现类似的挑战。我们所考虑的设定是对使用先进优化算法和学习率调度（learning rate schedules）的真实机器学习应用的极大简化。尽管如此，本节引入的许多概念也适用于更复杂的设定。我们结果的可能推广在[25，第2.7节]中进行了详细讨论。

[第20页，第13段]
## 4 平均场极限、生成模型与优化

[第20页，第14段]
在第2节和第3节中，我们已经看到了两个关键例子，说明机器学习中的问题如何被动力系统理论深刻支撑。因此，一个自然的问题是：动力学方法的普适性如何？我们通常能否将机器学习问题转化为可以用非线性动力学技术来处理的形式？在这里我们将表明，这个问题的答案是压倒性地肯定的，因为几乎总是存在动力学视角并且它是有帮助的。在本节中，我们将针对几个示例性主题（不分重要性顺序）来说明动力学视角，以展示该方法的普适性。

[第21页，第1段]
4.1 作为特例的玻尔兹曼机与霍普菲尔德网络

[第21页，第2段]
玻尔兹曼机实际上是经典 Ising [72] 和 Sherrington-Kirkpatrick [123] 模型的网络变体。反过来，所有这些系统都是具有马尔可夫随机场性质 [71] 的哈密顿粒子系统的特例。这些系统与一般接触过程理论 [94] 密切相关。总体而言，所有这些先前的类别又只是网络上的相互作用粒子系统（interacting particle systems, IPS）[105, 111] 的特例。如果考虑学习，所有这些系统都成为自适应（或协同进化网络）[15] 的特例。大型 IPS 领域至少可以追溯到 Boltzmann [17, 23, 52] 对气体动力学的研究。

[第21页，第3段]
更具体地说，考虑一个简单图 $  G = (V, E)  $，其顶点集为 $  V  $，边集为 $  E  $，并固定基数 $  |V| = M  $。将 $  E  $ 的邻接矩阵记为 $  A = (a_{ij})_{i,j=1}^M \in \mathbb{R}^{M \times M}  $，并令 $  b \in \mathbb{R}^M  $ 为参数向量。考虑相空间 $  X = \{0, 1\}^M  $，时间域 $  T = \mathbb{N}  $，使得每个顶点满足 $  v_i = v_i(k) \in \{0, 1\}  $，其中 $  k \in \mathbb{N}  $ 且 $  i \in [M] = \{0, 1, 2, \ldots, M\}  $。特别地，我们认为每个顶点（或粒子、节点或代理）具有可以取值 0 或 1 的动力学。在 $  G  $ 上定义一个随机动力系统如下

[第21页，第4段]
$ 
v_i(k+1) = \begin{cases} 1 & \text{以概率 } p_{ik} := f(v_i(k); A, b), \\ 0 & \text{以概率 } 1 - p_{ik}, \end{cases}
 $

[第21页，第5段]
其中需要选择一个通常为非线性的函数 $  f  $。随机动力系统 (20) 是 Ising-Sherrington-Kirkpatrick 型经典 IPS 的变体。对于 $  f  $ 的一种常见选择被称为玻尔兹曼机 [1]，即

[第21页，第6段]
$ 
f(v_i(k)) = \frac{1}{1 + \exp(b_i + \sum_{j=1}^M a_{ij}v_j(k))}.
 $

[第21页，第7段]
与经典统计力学的联系可以通过注意到 (21) 与一个能量（或哈密顿量）相关来观察到

[第21页，第8段]
$ 
\mathcal{H}(v) := \sum_{i=1}^M v_i b_i - \frac{1}{2} \sum_{i,j=1}^M v_i v_j a_{ij}.
 $

[第21页，第9段]
事实上，稍早发展的 Hopfield 模型 [68] 具有相同的能量 (22)，只是它使用确定性的极限更新规则

[第21页，第10段]
$ 
v_i(k+1) = \begin{cases} 1 & \text{若 } p_{ik} := f(v_i(k); A, b) > 0, \\ 0 & \text{否则.} \end{cases}
 $

[第21页，第11段]
在这类 Ising 型模型中会出现各种各样的动力学现象，包括收敛到平稳分布（玻尔兹曼分布），或者在参数变化时存在相变 [51]，这通常可以与平均场或连续极限中的分岔 [56, 92] 相关联。在机器学习背景下增加的额外复杂性是通过给定数据和优化算法来训练权重 $  a_{ij}  $ 和/或 $  b  $ 的元素。这解释了将动力系统中的经典参数（如 $  A  $ 和 $  b  $）重命名为“超参数”的趋势。不幸的是，这种约定具有误导性。如果将超参数也称为相/状态空间变量，将会更加合乎逻辑、更加清晰、更加一致，因为它们在训练过程中也会动态演化；参见第 3 节。

[第21页，第12段]
与第 2 节类似，回顾将顶点分为输入或可见集 $  V_{\text{in}}  $ 和隐藏集 $  V_{\text{hid}}  $。让我们将 $  V_{\text{in}}  $ 中的索引记为 $  \{1, 2, \ldots, d\}  $，其中 $  d \leq M  $。训练数据由一族二值向量 $  \tilde{v} \in \{0, 1\}^M  $ 组成。将训练集上的概率分布记为 $  P^+(\tilde{V}_{\text{in}})  $。假设玻尔兹曼机达到其平衡分布 $  P^*(V)  $，并将其在 $  V_{\text{hid}}  $ 上的边缘化记为 $  P^-(\tilde{V}_{\text{in}})  $。学习应使这两个分布接近。当然，一般来说，抽象和简化这种情况是有利的，即我们有两个概率分布 $  P^+  $ 和 $  P^-  $，比如具有相关的概率测度 $  \mu^+  $ 和 $  \mu^-  $，我们希望通过学习使它们的距离接近。一种选择是在概率测度空间上选取一个度量 $  d  $ 并考虑问题

[第21页，第13段]
$ 
\min_{A, b} d(\mu^+, \mu^-).
 $

[第22页，第1段]
最经典的情况并不完全考虑度量，而是使用Kullback-Leibler散度或相对熵，例如，在玻尔兹曼机或Hopfield模型的情况下，人们经常发现最小化问题

[第22页，第2段]
$$
\min_{A, b} \sum_{V} P^{+}(V) \ln \left( \frac{P^{+}(V)}{P^{-}(V)} \right),
$$

[第22页，第3段]
其中我们对所有可能的配置 $V \in \{0, 1\}^M$ 求和。显然，(24)-(25) 此时只是标准的优化问题，可以使用第3节中讨论的梯度下降或随机梯度下降来解决。这再次导致一个（随机）动力系统，其相空间或状态空间变量为 $A, b$。我们强调，与其考虑离散时间 $T = \mathbb{N}$ 和离散状态空间 $X$，总是存在自然的连续时间和连续空间类比（反之亦然）。例如，考虑 $x_i = x_i(t) \in \mathbb{R}$ 并定义经典的连续时间连续状态空间Hopfield模型为

[第22页，第4段]
$$
x_i' := \frac{dx_i}{dt} = -\alpha x_i + \sum_{j=1}^{M} a_{ij} h(x_j) + b_i, \quad i \in [M],
$$

[第22页，第5段]
其中 $\alpha > 0$ 是每个独立神经元的松弛参数。显然，系统 (26) 只是网络上的一个微分方程组。神经网络相互作用的通用网络模型类别已在许多其他背景下发展起来，并且在Hopfield将其应用于机器学习之前就已存在，例如，我们参考Amari和Wilson/Cowan在生物物理学中的开创性工作 [3, 4, 137, 138]。

[第22页，第6段]
为了进一步说明网络动力学的科学普遍性，再次考虑一个一般网络/图 $G = (V, E)$。假设每个顶点有一个 $d$ 维光滑流形 $X$ 作为其相空间，即 $x_j = x_j(t) \in X$，其中 $t \in \mathbb{R}$ 且 $\dim(X) = d$。常见的情况是 $X = \mathbb{R}^d$、球面 $X = S^d$ 或环面 $\mathbb{T}^d$。假设每个独立顶点/节点 $i$ 具有动力学

[第22页，第7段]
$$
x_i' := \frac{dx_i}{dt} = f_i(x_i), \quad x_i(0) = x_{i,0}, \quad i \in [M],
$$

[第22页，第8段]
对于足够光滑的截面 $f_i$ 映射到切丛 $TX$。我们假设 (27) 产生一个对所有 $t \in \mathbb{R}$ 定义的光滑流 $\phi_t(x_{i,0}) = x_i(t)$。作为我们最抽象的连续时间连续空间网络动力系统（NDS）类别，我们将考虑常微分方程

[第22页，第9段]
$$
x_i' = f_i(x_i) + \sum_{j=1}^{M} a_{ij} g(x_i, x_j), \quad i \in [M], \quad x_i = x_i(t) \in X,
$$

[第22页，第10段]
对于耦合映射 $g : X \times X \to TX$。NDS (28) 在复杂系统中非常常见，包括

[第22页，第11段]
（玻尔兹曼）
$$
X = \mathbb{R}^6, \quad f_i(x_i) = (x_{i,1}, x_{i,2}, x_{i,3}, 0, 0, 0)^T, \\
a_{ij} = \frac{1}{M}, \quad g_{4,5,6}(x_i, x_j) = \gamma \frac{(x_i - x_j)}{\|x_i - x_j\|^3}
$$

[第22页，第12段]
（Kuramoto）
$$
X = S^1 := \mathbb{R}/(2\pi\mathbb{Z}), \quad f_i(x_i) \equiv \omega_i \in \mathbb{R}, \\
a_{ij} \equiv \frac{K}{M}, \quad g(x_i, x_j) = \sin(x_j - x_i)
$$

[第22页，第13段]
（Desai-Zwanzig）
$$
X = \mathbb{R}, \quad f_i(x_i) = -V'(x_i), \\
a_{ij} \equiv \frac{K}{M}, \quad g(x_i, x_j) = x_j - x_i,
$$

[第22页，第14段]
（耦合vdP/FHN）
$$
X = \mathbb{R}^2, \quad f_i(x_i) = (x_{i,2} - \frac{1}{3} x_{i,1}^3 + x_{i,1}, -\varepsilon x_{i,1})^T, \\
a_{ij} \equiv \frac{K}{M}, \quad g_{1}(x_i, x_j) = x_j - x_i,
$$

[第22页，第15段]
（Hopfield）
$$
X = \mathbb{R}, \quad f_i(x_i) \equiv -\alpha x_i - b_i, \\
a_{ij} \equiv \frac{K}{M}, \quad g(x_i, x_j) = \frac{1}{1 + e^{-x_j}}
$$

[第23页，第1段]
其中 $  i \neq j  $，$  a_{ij}^M = 0  $，$  \gamma \in \mathbb{R}  $ 的符号决定了在无碰撞玻尔兹曼气体动力学情形中我们考虑的是库仑相互作用还是引力相互作用 [104]，$  K > 0  $ 是控制耦合强度的参数，Kuramoto 振子的固定频率 $  \omega_i  $ 通常从给定的概率分布中采样 [91, 128]，$  V  $ 是 Desai-Zwanzig 模型中粒子的给定约束势 [34]，$  \epsilon > 0  $ 是扩散耦合 van-der-Pol/FitzHugh-Nagumo [42, 103, 131] 振子情形中时间尺度分离的小参数 [139, 126]，$  \alpha > 0  $ 和 $  b_i \in \mathbb{R}  $ 是 Hopfield [68] 情形中控制各个神经元向静息态衰减及外部输入的参数对，$  c_i, d_i > 0  $ 是 Hegselmann-Krause [60] 观点动力学中每个智能体指示函数的慷慨阈值和竞争阈值，最后 $  \alpha > 0  $ 是 Cucker-Smale [32] 群集/集群模型中控制非线性的参数。事实上，形式为 (28) 的模型列表远不完整，还有更多例子，例如在生态学中（如食物网）、在神经科学中（如脉冲神经网络），以及实际上在所有其他科学中。相当常见的是，不同的科学共同体发展出了各自独立的名称和术语来研究 NDS (28) 这一类别。事实上，这使得重复发现的可能性相当大，而只要认识到抽象数学结构是相同的，就可以避免这种情况。

[第23页，第2段]
### 4.2 相互作用粒子系统的平均场极限

[第23页，第3段]
从动力系统的角度来看，将 NDS (28) 这一类别作为一个共同的研究领域来处理要实用和有效得多。目前已有大量结果可用，尽管对于有限固定但较大的 $  M  $，除了哈密顿/可积结构、对称性或多尺度约化等特殊情况外，通常难以严格证明相关命题。有时可以缓解这一困难的一种手段是过渡到平均场或连续极限 $  M \to \infty  $，我们将在接下来讨论。这里我们将不讨论连续极限，即把顶点排列在离散结构上然后考虑极限。

[第23页，第4段]
#### 全连接耦合系统

[第23页，第5段]
为了教学上的简便，首先考虑全连接耦合系统的情形 [52]

[第23页，第6段]
$ 
a_{ij}^M = 1 \quad \text{if } i \neq j \quad \text{and} \quad a_{ii}^M = 0 \quad \text{if } i \in [M],
 $

[第23页，第7段]
其中我们引入了指标 $  M  $ 来表示邻接矩阵依赖于粒子/神经元的数量。为简单起见，考虑 (28) 中 $  f_i \equiv 0  $ 且对于 $  i \neq j  $ 有 $  a_{ij}^M \equiv 1/M  $，$  \mathcal{X} = \mathbb{R}^d  $，于是

[第23页，第8段]
$ 
x_i' = \frac{1}{M} \sum_{j=1}^{M} g(x_i, x_j),
 $

[第23页，第9段]
其中 $  a_{ii}^M = 0  $ 通过假设 $  g(x, \tilde{x}) = -g(\tilde{x}, x)  $ 来纳入。假设我们有

[第23页，第10段]
$ 
\frac{1}{M} \sum_{j=1}^{M} g(x_i(t), x_j(t)) \to \int_{\mathbb{R}^d} g(x_i(t), \tilde{x}) \mu(t, \mathrm{d}\tilde{x}), \quad \text{for } M \to \infty,
 $

[第23页，第11段]
对于测度 $  \mu(t, x)  $，或者更好的情况是对于具有密度 $  \mu(t, x) = u(t, x) \mathrm{d}x  $ 的测度。那么可以用特征 ODE 替换 (36)

[第23页，第12段]
$ 
x' = \int_{\mathbb{R}^d} g(x, \tilde{x}) \mu(t, \mathrm{d}\tilde{x}).
 $

[第24页，第1段]
方程 (37) 是一阶偏微分方程的特征常微分方程

[第24页，第2段]
$ 
\partial_t \mu = -\nabla_x \cdot (\mu \mathcal{V}[\mu]), \quad \mathcal{V}[\mu](t, x) := \int_{\mathbb{R}^d} g(x, \tilde{x}) \mu(t, \mathrm{d}\tilde{x}).
 $

[第24页，第3段]
如果 $ \mu $ 具有密度 $ u $，则偏微分方程 (38) 可进一步简化，得到一个更经典的 Vlasov 方程

[第24页，第4段]
$ 
\partial_t u = -\nabla_x \cdot (u \mathcal{V}[u]), \quad \mathcal{V}[u](t, x) := \int_{\mathbb{R}^d} g(x, \tilde{x}) u(t, \tilde{x}) \mathrm{d}\tilde{x}.
 $

[第24页，第5段]
研究 (39) 与 (36) 之间的近似性质需要用到经验测度

[第24页，第6段]
$ 
\delta_M(t) := \frac{1}{M} \sum_{j=1}^M \delta_{x_j(t)},
 $

[第24页，第7段]
其中 $ \delta_{x_j(t)} $ 是通常的在 $ x_j = x_j(t) $ 处的 Dirac 测度。注意 $ \delta_M(t) $ 是一个概率测度，它追踪有限个相互作用个体/粒子的平均状态。将其与概率密度 $ u $ 及其关联测度 $ \mu $ 进行比较是自然的。问题在于是否存在概率测度上的度量 $ \mathbf{d} $，使得

[第24页，第8段]
$ 
\lim_{M \to \infty} \sup_{t \in [0, T]} \mathbf{d}(\delta_M, \mu) = 0.
 $

[第24页，第9段]
$ \mathbf{d} $ 的经典选择是 Wasserstein(-Monge-Kantorovich-Rubinstein) [52, 133] 度量

[第24页，第10段]
$ 
\mathcal{W}_p(\nu, \mu) := \inf_{\pi \in \Pi(\mu, \nu)} \left( \int_{\mathbb{R}^d \times \mathbb{R}^d} \|x - y\|^p \pi(\mathrm{d}x \mathrm{d}y) \right)^{1/p},
 $

[第24页，第11段]
其中 $ \Pi(\mu, \nu) $ 是 $ \mu $ 与 $ \nu $ 之间所有耦合构成的空间，即 $ \mu $ 和 $ \nu $ 分别是 $ \Pi(\mu, \nu) $ 中测度在第一和第二个参数上的边缘分布。证明 (40) 的一种方法是首先研究 Vlasov 方程 (38) 和/或 (39) 的存在性与唯一性。一旦证明这一点，就研究解关于初始条件在 $ \mathbf{d} $ 下的连续依赖性。如果这一性质成立，例如

[第24页，第12段]
$ 
\lim_{M \to \infty} \sup_{t \in [0, T]} \mathbf{d}(\delta_M(t), \mu(t)) = 0 \quad \text{if} \quad \lim_{M \to \infty} \mathbf{d}(\delta_M(0), \mu(0)) = 0,
 $

[第24页，第13段]
那么通过有限维常微分方程组 (36) 演化经验测度就能很好地近似平均场极限 Vlasov 方程，反之亦然；这也称为 Vlasov 方程在 $ [0, T] $ 上是严格可导出的 [19, 52, 81, 104]。

[第24页，第14段]
对于具有 Lipschitz 耦合函数 $ g $ 的全连接耦合系统，关于形如 (36) 的连续依赖性，在 1-Wasserstein（或有界 Lipschitz）度量下的一个典型结果是针对两个解 $ \mu_{1,2}(t) $ 的 Dobrushin 型估计 [35, 36]，其形式为

[第24页，第15段]
$ 
\mathcal{W}_1(\mu_1(t), \mu_2(t)) \leq e^{2L|t|} \mathcal{W}_1(\mu_1(0), \mu_2(0)),
 $

[第24页，第16段]
其中 $ L > 0 $ 是 $ g $ 的 Lipschitz 常数。由 (43) 可以得出结论：Vlasov 方程在 $ [0, T] $ 上是严格可导出的。

[第24页，第17段]
我们还要指出，机器学习中最常见的极限是将在下一节研究的一般异构网络的深度神经网络。然而，也存在全连接耦合已经出现的经典情形。例如，训练一个具有单层 $ M $ 个神经元的前馈神经网络（见第 2.1 节）可以解释为具有全连接耦合的 IPS [28, 125, 46]。这里，每个神经元被视为一个独立粒子，其状态由输入和输出边的权重及其偏置给出。相互作用来自梯度下降更新规则 (15)。因此，极限 $ M \to \infty $ 描述了无限宽单层神经网络的训练，这与第 2.2 节研究的无限深神经网络是相反的极限。

[第25页，第1段]
奇异耦合系统、图算子与有向图测度

[第25页，第2段]
在动力学理论中更为抽象的工作[104, 52, 73]基础之上，人们实际上可以针对特定模型进行专门化，以获得具体且适用的结果。作为例证，考虑 Kuramoto 情形[93]，其中对于 Vlasov 方程可得

[第25页，第3段]
$ 
\partial_t u = -\partial_x (uV[u]), \quad V[u](x, t, \omega) = \omega + K \int_0^{2\pi} \int_{\mathbb{R}} \sin(\tilde{x} - x)u(\tilde{x}, t; \tilde{\omega})\zeta(\tilde{\omega}) d\tilde{\omega} d\tilde{x},
 $

[第25页，第4段]
其中 $ \zeta $ 是振子固有频率 $ \omega_i $ 的给定固定概率分布，即指定固有动力学 $ f_i(x_i) = \omega_i $ 的分布。对于 Kuramoto（及合适的变体），最近已证明可以考虑通过图极限（graphon）$ G $ 建模的图 $ G^M $ [96]，即邻接矩阵由核导出

[第25页，第5段]
$ 
a_{ij}^M = \int_{\mathcal{I}_i^M \times \mathcal{I}_j^M} G(x, y) dx dy, \quad G : \mathcal{I} \times \mathcal{I} \to \mathbb{R},
 $

[第25页，第6段]
其中 $ \{\mathcal{I}_i^M\}_{i=1}^M $ 是单位区间 $ \mathcal{I} = [0, 1] $ 的一个划分。在关于 $ G $ 和 $ \zeta $ 的技术性假设下，对于 $ u = u(x, t, \omega, z) $ 可得到修正的 Vlasov 方程[10, 27, 76]

[第25页，第7段]
$ 
\partial_t u = -\partial_x (uV[u]),
 $

[第25页，第8段]
$ 
V[u](x, t, \omega, z) = \omega + K \int_{\mathcal{I}} \int_0^{2\pi} \int_{\mathbb{R}} \sin(\tilde{x} - x)u(\tilde{x}, t, \tilde{\omega}, \tilde{z})\zeta(\tilde{\omega})G(z, \tilde{z}) d\tilde{\omega} d\tilde{x} d\tilde{z},
 $

[第25页，第9段]
其中 $ z \in \mathcal{I} $ 追踪图/网络的异质性。除了平均场 Vlasov 方程之外，类似的方法也可以用于包含图极限的连续极限偏微分方程[98, 99, 75, 85]。然而，请注意 (44) 做出了一个强假设，即图 $ G $ 的极限是一个定义良好的图极限 $ G \in L^p(\mathcal{I} \times \mathcal{I}, \mathcal{I}) $（对于 $ p \in [1, \infty) $），而对于大类图极限而言并非如此[11]。然而，即使在更一般的情形下，也可以推广到图算子（graphops），如[82, 47, 86, 48, 49]中所讨论的。考虑为常微分方程添加额外的随机强迫项而得到随机微分方程，会引出（Vlasov-）Fokker-Planck-Kolmogorov (FPK) 方程[113, 44, 109, 129]。在促成本章的研究项目中，我们证明了平均场极限的一种特定变体，其中通过所谓的有向图测度（digraph measures, DGM）[86] 包含了图极限的推广。

[第25页，第10段]
在此，我们出于例证目的简要概述[83]中的这一结果。我们考虑由下式给出的 NDS (28) 的随机变体

[第25页，第11段]
$ 
dx_i = f(x_i)dt + \frac{1}{M} \sum_{j=1}^{M} a_{ij}^M g(x_i, x_j)dt + \frac{1}{M} \sum_{j=1}^{M} \hat{a}_{ij}^M h(x_i, x_j)dW^i
 $

[第25页，第12段]
其初始条件为 $ x_i(0) = x_i^0 $（对于 $ i \in [M] $），$ a_{ij}^M)_{i,j=1}^M $ 是系统的通常邻接矩阵，表示顶点 $ i $ 与 $ j $ 之间的基本确定性网络交互，$ \hat{a}_{ij}^M $ 是表示噪声如何受 $ i $ 与 $ j $ 之间交互影响的邻接矩阵，最后 $ W^i = W^i(t) $（对于 $ i \in [M] $）是独立同分布的布朗运动。我们将始终再次假设 $ f, g, h $ 是 Lipschitz 的。为了刻画图的异质性，我们再次引入区间 $ \mathcal{I} = [0, 1] $，它将通过变量 $ u \in \mathcal{I} $ 构成每种顶点类型的位置。由于我们处理的是 DGM，且在我们的问题中有一个由矩阵表示的图，我们需要用 DGM 来近似这个图。考虑区间 $ \mathcal{I} = [0, 1] $ 的如下划分：对于 $ 1 < i \leq M $，$ I_i^M = \left[ \frac{i-1}{M}, \frac{i}{M} \right] $，以及 $ I_1^M = [0, \frac{1}{M}] $。然后我们引入与 $ a_{ij}^M $ 和 $ \hat{a}_{ij}^M $ 相关联的有向图测度，由下式给出

[第25页，第13段]
$ 
\eta_{A^M}^u(v) := \sum_{i=1}^{M} 1_{I_i^M}(u) \sum_{j=1}^{M} \frac{a_{ij}^M}{M} \delta_{\frac{i}{M}}(v),
 $

[第25页，第14段]
$ 
\eta_{A^M}^u(v) := \sum_{i=1}^{M} 1_{I_i^M}(u) \sum_{j=1}^{M} \frac{\hat{a}_{ij}^M}{M} \delta_{\frac{i}{M}}(v),
 $

[第26页，第1段]
其中 $ 1_{\frac{j}{M}}(x) $ 表示指示函数，$ \frac{j}{M} $ 作为细分 $ \mathcal{I} $ 的集合 $ I_M^J := \left(\frac{j-1}{M}, \frac{j}{M}\right] $ 的代表元。我们将假设两个交互图序列在以下意义下具有极限：若当 $ M \to \infty $ 时 $ \mathbf{d}_{\infty}(\eta_{AM}, \eta) \to 0 $，则图 $ \{A^M\}_{M \geq 1} $ 收敛到极限测度 $ \eta $，其中 $ \mathbf{d}_{\infty} $ 是测度上的有界 Lipschitz 距离。类似地，$ \hat{A}^M $ 将收敛到一个有向图测度 $ \hat{\eta} $。与确定性 IPS（交互粒子系统）情形下的 ODE 特征方程不同，我们考虑以下独立过程：

[第26页，第2段]
$ 
X_u(t) = X_u(0) + \int_0^t f(X_u(s)) \, ds + \int_0^t \int_{\mathcal{I}} g(X_u(s), y) \, \mu_{v,s}(dy) \eta^u(dv) \, ds
 $

[第26页，第3段]
$ 
+ \int_0^t \int_{\mathcal{I}} \int_{\mathbb{X}} h(X_u(s), y) \, \mu_{v,s}(dy) \hat{\eta}^u(dv) \, dW_u^s,
 $

[第26页，第4段]
其中我们定义 $ \mu_{u,t} = \mathcal{L}(X_u(t)) $ 为 $ X_u(t) $ 在 $ u \in \mathcal{I} $ 时的分布律。初始条件 $ X_u(0) = X_u^0 $ 在概率测度 $ \hat{\mu}^0 \in \mathcal{P}(\mathcal{X}) $ 下是独立同分布的。两个测度 $ \eta, \hat{\eta} $ 可分解为测度族 $ \{\eta^u\} $（$ u \in \mathcal{I} $）和 $ \{\hat{\eta}^u\} $（$ u \in \mathcal{I} $）。这些被称为纤维测度（fiber measures）[11]，直接类比于图算子（graphops）理论 [82]。实际上，这些测度表示邻接矩阵 $ a_{i,j}^M $ 和 $ \hat{a}_{i,j}^M $，每个纤维测度描述了给定标签 $ u \in \mathcal{I} $ 的顶点的局部连通性。最低阶平均场近似通过在图异质性上取平均获得，即取异质经验测度的平均

[第26页，第5段]
$ 
\hat{\mu} := \int_{\mathcal{I}} \mu_{u,t} \, du.
 $

[第26页，第6段]
文献 [83] 的主要定理指出，我们随后再次收敛（在一种相当技术性的度量下）到一个非局部 Vlasov-Fokker-Planck 方程

[第26页，第7段]
$ 
\partial_t \hat{\mu}_t + \partial_x \left( \hat{\mu}_t f(x) + \int_{\mathcal{I}} \mu_{u,t} \int_{\mathbb{X}} g(x, y) \, \mu_{v,t}(dy) \eta^u(dv) \, du \right)
 $

[第26页，第8段]
$ 
+ \frac{1}{2} \partial_x^2 \left( \int_{\mathcal{I}} \mu_{u,t} \left[ \int_{\mathcal{I}} \int_{\mathbb{X}} h(x, y) \, \mu_{v,t}(dy) \hat{\eta}^u(dv) \right]^2 \, du \right) = 0.
 $

[第26页，第9段]
当然，人们可以将这类结果进一步推广到超越图异质性和领头阶平均场极限的范围。例如，可以相对直接地将这一理论与平均场介观 PDE 层面的随机修正相结合。这样将得到随机 PDE。此外，如果将粒子间的相互作用半径从长程相互作用缩放到中等范围，则可以在宏观层面得到反应-扩散或流体型 PDE。如果考虑宏观可观测量并推导其微分方程，这些类别也会在极限 $ M \to \infty $ 下出现。

[第26页，第10段]
总之，人们应当将经典的机器学习网络模型视为 NDS（网络动力系统）领域的非常特殊的情形，将动力系统视为其特例，并在大网络极限下将其视为重要的偏积分微分方程的特例。这使得这些领域的所有经典工具可以立即应用于 ML/AI。我们还参考本书中由 PI Herty 及其合作者撰写的关于 SPP2298 项目“通过平均场理论评估深度学习”的章节，其中讨论了在 ML 问题中利用 IPS 平均场极限的相同通用策略。

[第26页，第11段]
### 4.3 循环神经网络、Transformer 及超越

[第26页，第12段]
现在有人可能会争辩说，ML/AI 中近期持续涌现的网络架构和算法改进可能需要重新思考上述讨论的 NDS 模型类（28）。更仔细的数学审视表明，一个非常温和的推广已经足够。

[第26页，第13段]
例如，考虑循环神经网络（RNN）及其各种变体。RNN 动态更新规则的一个典型表述为

[第26页，第14段]
$ 
x_{k+1} = Ax_k + B\tilde{G}(x_{k-1}) + Cx_k + b_k
 $

[第26页，第15段]
其中 $ x_k \in \mathbb{R}^n $，$ A, B, C $ 为矩阵，$ b_k $ 为偏置，$ \tilde{G} : \mathbb{R}^n \to \mathbb{R}^n $ 为给定的非线性（或激活函数），$ X $ 表示输入数据。方程 (49) 作为具有适当固定延迟的延迟微分方程的时间离散化而出现。显然 (49) 定义了一个动力

[第27页，第1段]
具有记忆的系统，这实际上是一个古老的想法 [115, 5]，其出现时间显著早于更现代的时间延迟神经网络的使用 [135]；关于延迟对于嵌入/逼近性质的重要性，另见第2.5节。

[第27页，第2段]
与(49)相关的主要变体之一是长短期记忆（LSTM）架构 [64]。尽管技术上较为繁琐，LSTM也可以与带延迟的动力系统相关联 [124]。实际上，任何循环网络都可以从网络动力学的视角被视为具有更长程连接的NDS。事实上，我们已经在上文看到了Hopfield和Boltzmann机的例子，它们在一般情况下是全连接的。其他有直接联系的例子是回声状态网络（ESN）和储备池计算机 [74, 108, 7]。

[第27页，第3段]
与其更详细地深入这些经典架构思想，人们可能会试图反驳说，转换为动力学视角不适用于“更近期的”机器学习/人工智能架构和算法。通常，这种反对意见仅仅是由于在使系统在数学上更加精确方面存在现实中的实际时间延迟而产生的。为了说明这一点，让我们考虑“transformers”（或注意力网络），它们通常被归功于 [132]。为了说明目的，我们将使用连续时间（“深度transformers”），但非常类似的评论也适用于离散时间。令 $ x_i = x_i(t) \in \mathbb{R}^d $，并通过ODEs的流来定义transformer

[第27页，第4段]
$ 
x_i' = \sum_{j=1}^{M} \frac{\exp(\mathcal{M}_1(t)x_i \cdot \mathcal{M}_2(t)x_j)}{\sum_{l=1}^{M} \exp(\mathcal{M}_1(t)x_i \cdot \mathcal{M}_2(t)x_j)} \mathcal{M}_3(t)x_j, \quad i \in [M],
 $

[第27页，第5段]
其对 $ \mathcal{M}_1(t), \mathcal{M}_2(t) \in \mathbb{R}^{M_0 \times M} $（对于 $ M_0 \leq M $）和 $ \mathcal{M}_3(t) \in \mathbb{R}^{M \times M} $ 为给定矩阵使用了“soft-max”或“自注意力”机制。当然，非线性项的许多变体是可能的。显然，我们将(50)识别为标准NDS (28)的另一个变体。事实上，所有transformer类型的模型又都只是IPS的形式。我们现在也习惯了系数可能是时间相关的这一事实，因为这联系到第2节中讨论的结构网络性质以及第3节中讨论的训练。关于训练，我们还提到一个由于篇幅限制在此不涉及的领域：即，人们也可以使用上文讨论的IPS视角的动力学来处理训练背景下的节点极限。确实，如果将边权重和偏置视为训练期间的独立动态变量，人们又可以取IPS的平均场极限。这方面在许多近期工作中有所涉及，参见例如 [43, 118, 125]。网络动力学的主要挑战仍然类似于第4.2节中讨论的网络上的动力学，即证明当边/参数数量趋于无穷时的平均场或连续极限。

[第27页，第6段]
### 4.4 生成模型

[第27页，第7段]
到目前为止，我们通常假设我们的网络在某个给定数据集 $ x_i, y_i)_{i \in \mathbb{N}} $ 上训练，然后在某种意义上估计条件概率 $ \mathbb{P}(Y|X = x) $，将我们的输入/可观测 $ X $ 和目标/输出 $ Y $ 视为随机变量。这通常被称为判别建模。相比之下，在生成模型中，输入/可观测数据是根据对 $ \mathbb{P}(X|Y = y) $ 的估计结合 $ \mathbb{P}(Y) $ 生成的，从而产生可观测和目标联合概率分布的估计量，特别是通过贝叶斯规则得到 $ \mathbb{P}(Y|X = x) $；关于这两类的区别参见 [106]。生成模型对于选择特征、促进分类和提高模型准确性，或生成新的真实数据样本以继续学习过程高度相关。

[第27页，第8段]
在（深度）学习的背景下，生成模型有几种重要的变体（参见例如 [50] 的综述），包括高斯混合模型、隐马尔可夫模型、潜在狄利克雷分配、Boltzmann机、变分自编码器、生成对抗网络或生成扩散模型。Boltzmann机已在第4.1节中讨论。从动力学的角度来看，其他最有趣的类别是隐马尔可夫模型（HMMs）、生成对抗网络（GANs）和生成扩散模型（GDMs）。

[第27页，第9段]
HMMs [22] 将观测的时间序列视为具有转移核 $ Q $ 的马尔可夫链 $ \{X_k\}_{k \geq 0} $，即

[第27页，第10段]
$ 
\mathbb{P}(X_{k+1} \in A|F_k) = Q(X_k, A)
 $

[第27页，第11段]
对于可测集 $ A $ 和相应的滤波 $ F_k $。完整的HMM现在添加从观测变量 $ X $ 到目标变量 $ Y $ 的转移核 $ G $，以获得联合马尔可夫的核

[第28页，第1段]
其中 $  C  $ 是乘积空间中的可测集。现在，这个联合马尔可夫链可用于生成输入可观测量 $  X  $ 和输出目标 $  Y  $ 所期望的联合分布。动力学的视角变得相关，因为人们希望存在一个不变、遍历的概率分布 $  \pi(x, y)  $，它可以通过从具有适当核 $  T  $ 的马尔可夫链中采样来近似（该核应基于一些首次观察到的时间序列来估计，从而诱导出对 $  Q  $ 和 $  G  $ 的猜测）。现在，可以应用几种蒙特卡洛算法，如接受-拒绝或 Metropolis-Hastings 方案来完成此任务；这些方法的理论基础已得到充分研究，包括经典的细致平衡条件/可逆马尔可夫链 [114]，以及包括不可逆性在内的较新方法 [107]。

[第28页，第2段]
生成对抗网络（GANs）已在 [53] 中提出，此后在理论和应用方面产生了巨大影响。在这种方法中，训练两个模型：一个捕获数据分布的生成模型，以及一个估计某个数据样本属于实际训练数据集而非生成模型所产生样本的概率的判别模型。该框架将训练过程理解为一个两人博弈，其中生成模型试图战胜真实训练数据。这种方法不部署底层马尔可夫链，而是可以与迭代博弈相关联，直接联系到动力系统理论。

[第28页，第3段]
研究零和博弈中相应的最小化遗憾学习动力学的一个起点是复制者动力学模型，可以说是进化博弈论中研究最充分的结构 [136]。复制者结构是乘法权重更新（MWU）的连续时间模拟，后者是一种以其遗憾保证而闻名的元算法 [9]。在两人零和博弈的具体情况下，复制者方程由常微分方程给出

[第28页，第4段]
$ 
\dot{x}_i = x_i \left( \{Ay\}_i - x^\top Ay \right), \\
\dot{y}_j = y_j \left( \{Bx\}_j - y^\top Bx \right),
 $

[第28页，第5段]
其中 $  (x, y) \in \Delta_n \times \Delta_m  $，分别表示 $  n  $ 维和 $  m  $ 维单纯形，$  A  $ 和 $  B  $ 是收益矩阵。（混合）纳什均衡是博弈动力学中的关键对象，它正是常微分方程 (51) 的（内部）均衡，通常是椭圆的，即只能平均达到（参见，例如，[66]）。随机噪声对此类模型的影响，显然也与 GANs 的算法情形相关，已在 [39] 中研究，这也是我们 SPP2298 研究项目期间发表的一篇出版物。结果表明，噪声的选择对于是否观察到内部纳什均衡至关重要，即对于算法至少平均收敛到有利解至关重要。

[第28页，第6段]
类似地（也与前面的小节类似），旨在学习概率分布的生成模型的离散时间问题可以与更容易研究的连续时间模型相关联，在这种情况下，是形式如下的随机微分方程

[第28页，第7段]
$ 
dX_t = b(X_t, t)dt + \sigma(X_t, t)dW_t,
 $

[第28页，第8段]
其中 $  b  $ 是漂移向量场，$  W_t  $ 是独立布朗运动的向量，其缩放参数 $  \epsilon  $ 控制噪声水平。此类模型可以理解为生成扩散模型（GDMs）[21]。遍历、不变概率分布的存在性，给出了生成时间序列的典型行为，现在可以围绕寻找平稳 Fokker-Planck 方程的（可能唯一的）解来研究

[第28页，第9段]
其中 $  L^*  $ 是与随机微分方程 (52) 相关的前向 Kolmogorov 算子。在这里，可以参考随机动力学中一个研究极为充分的问题，以理解和控制生成过程的结果。最近的一项研究 [62] 通过 Morse-Smale 流的扰动，取 (52) 中的 $  \epsilon  $ 很小，将此类生成扩散模型与联想记忆模型联系起来。在此背景下，广泛研究的亚稳态问题 [18] 进入了生成建模的领域，通过（随机）动力系统中另一个完善的理论，允许许多新的见解。

[第28页，第10段]
GDMs 的一个特别有趣的变体是基于分数的生成模型（SGMs），它将数据 $  X(0)  $ 的分布 $  p_0(x)  $ 沿随机微分方程 (52) 的动力学转移到分布 $  p_T(x)  $

[第29页，第1段]
可以从中高效采样。相应的反向 SDE（reverse SDE）包含一个得分项 $\nabla_x \log p_t(x)$，并诱导出解过程 $Y_t = X_{T-t}$，随后可用于生成新样本（参见，例如，[127]）。最近，此类模型的鲁棒性已通过将（反向）SDE 的马尔可夫解过程理解为随机动力系统（RDS）来研究，即通过我们在第 3.4 节中引入的相同形式体系来研究随机梯度下降的稳定性。在 [24] 中，作者表明，如果与 RDS 解的最大 Lyapunov 指数相关联的首个 Oseledets 空间与数据流形的边界对齐，那么该模型的生成方案在小误差下是鲁棒的。在这里，鲁棒性是根据生成分布的支撑集来理解的：对于足够小的扰动，预测目标仅在实际目标密度有支撑的地方有支撑。所提出理论的动力学条件关键包括 SDE (52) 中向量场 $b$ 对支撑集的吸引，以及应用乘性遍历理论的一般正则性假设（参见 [8]）。因此，这是遍历理论和动力系统与理解学习过程稳定性高度相关的又一个例子。

[第29页，第2段]
4.5 反向传播、优化与梯度

[第29页，第3段]
我们已经看到，机器学习中的信息传播和学习概念基本上总是可以被解释为动力学现象的特例。然而，人们可能会想，该领域中看起来更静态的概念是否也可以被转换。为了说明这一点，让我们仅举一个例子，看看非常经典的反向传播（backpropagation）思想。反向传播在算法上最清晰的描述可能是在自动微分（automatic differentiation）领域给出的 [55]。假设我们有一个可微标量函数的简单复合

[第29页，第4段]
$$F(x_0) = f_1(f_0(x_0)), \quad x_0 \in \mathbb{R}, \quad x_1 := f_0(x_0) \in \mathbb{R}, \quad x_2 := f_1(x_1) \in \mathbb{R}.$$

[第29页，第5段]
计算导数通过链式法则完成，因此

[第29页，第6段]
$$\frac{\partial F}{\partial x_0} = \frac{\partial f_1(x_1)}{\partial x_1} \frac{\partial f_0(x_0)}{\partial x_0} = \frac{\partial x_2}{\partial x_1} \frac{\partial x_1}{\partial x_0}.$$

[第29页，第7段]
如何计算该表达式存在选择。我们可以“由内向外”计算链式法则，从最内层部分 $\frac{\partial x_1}{\partial x_0}$ 开始，然后计算下一个外层部分 $\frac{\partial x_2}{\partial x_1}$。这在自动微分中称为前向累积（forward accumulation）。或者，可以通过反向累积（reverse accumulation）进行，先计算 $\frac{\partial x_2}{\partial x_1}$，然后计算 $\frac{\partial x_1}{\partial x_0}$，即“由外向内”计算链式法则。众所周知，反向累积是反向传播的关键步骤。原因在于，对于多维函数 $F : \mathbb{R}^{N_1} \to \mathbb{R}^{N_2}$ 且 $N_1 \gg N_2$ 的情况，反向累积比前向累积高效得多。$N_1 \gg N_2$ 的情况正是机器学习训练中遇到的情况。乍看之下，反向传播背后似乎没有动力学原理，但事实并非如此。有助于更一般地思考，并考虑函数的任意复合

[第29页，第8段]
$$x_{k+1} = f_k(f_{k-1}(f_{k-2}(\cdots f_0(x_0)))) =: f(x_0, k).$$

[第29页，第9段]
很明显，最后一个方程只是描述了一个非自治离散时间动力系统 $x \mapsto f(x, k)$ 的时间 $k$ 映射；关于离散时间非自治动力学的更广泛背景，参见 [112]。与标准自治迭代映射的区别在于，我们必须允许迭代映射也依赖于时间步 $k$。当然，如果它与 $k$ 无关，那么我们只是有一个更经典的自治迭代映射。让我们更一般地将初始条件 $x_0$ 视为参数 $p$ 的一种可能实例，从而得到

[第29页，第10段]
$$x \mapsto f(x, k; p).$$

[第29页，第11段]
关键的是，我们随后可以问，计算迭代映射关于参数 $p$ 的导数，即沿映射迭代 $x_j = f_{j-1}(x_{j-1}; p)$ 的 $D_p f$，在动力学上意味着什么。这在动力系统中被称为关于 $p$ 的变分方程（variational equation）。它相当于沿解轨迹的局部线性化。为了计算它，应该计算

[第29页，第12段]
$$D_p f_k(f_{k-1}(f_{k-2}(\cdots f_0(x_0); p)); p),$$

[第30页，第1段]
如果在机器学习中把参数 $p$ 等同于未知的权重和偏置，这本质上与标准反向传播问题相同。前向累积这一术语现在变得更加直观，因为从内向外计算链式法则恰好对应于沿轨迹前向计算变分方程，而反向累积则对应于沿轨迹后向（或“反向”）计算变分方程。特别地，反向传播的关键洞见实际上在于：对于一个可以沿两个时间方向考虑的对象，反向时间地看待它是等价的，有时是有益的。在动力学中，这是一个极其古老的观念，已被多次使用。仅作说明，前向和后向传播小扰动的等价性的重要性已在亥姆霍兹1887年关于最小作用量原理的工作中出现[134]（很可能类似的观念在更早时期就已出现在各种其他情境中，因为比较前向/后向运动并利用沿解的局部线性化是一个通用的动力学原理）$ ^1 $。

[第30页，第2段]
更一般地，训练机器学习算法的几乎所有技术实际上都依赖于某种形式的优化。在第3节中，我们已经看到如何使用随机动力系统来理解随机梯度下降的收敛性。类似原理适用于几乎所有优化算法，因为它们通常利用迭代动力学，即我们将算法定义为一个依赖于待优化函数的时间相关动力系统。这一转换原理适用于所有经典优化方法，如梯度下降、随机梯度下降、非线性规划技术、牛顿型方法等，它们绝大多数采用迭代技术。此外，许多元启发式方法只是使用更复杂的动力系统，如模拟退火、Metropolis-Hastings、基于共识的优化等。有人可能会反对说，引入动力系统视角似乎没有必要，因为大多数算法“在实践中效果良好”。这一论点在一定程度上确实成立，但这种观点排除了我们对优化为何以及何时失败的理解。即使对于标准牛顿型方法，众所周知，为牛顿法收敛寻找良好初值的动力学可能极其复杂，即使对于极其简单的问题也是如此。在机器学习背景下，另一个说明这一点的好问题是梯度爆炸或消失。假设我们有一个损失函数 $\mathcal{L} : \mathbb{R}^D \to \mathbb{R}$，并考虑相关的离散时间或连续时间梯度动力学

[第30页，第3段]
$$p_{k+1} = p_k - \alpha \nabla (\mathcal{L}_k) \quad \text{或} \quad p' = -\nabla \mathcal{L}(p).$$

[第30页，第4段]
为教学简便，我们仅使用连续时间并使用梯度流ODE（离散时间情形下同样的论证成立）。我们甚至假设存在唯一的全局最小值，且优化问题是凸的、二次的，且 $D = 2$。这产生一个线性ODE系统

[第30页，第5段]
$$\frac{dp}{dt} = p' = Ap, \quad p(0) = p_0,$$  \tag{53}

[第30页，第6段]
其中 $p_0$ 是我们的初始猜测。事实上，我们甚至可以选择 $A$ 为对角矩阵 $A = \text{diag}(-1, -\varepsilon)$，其中 $0 < \varepsilon \ll 1$ 是一个小参数。很容易看出，当 $t \to 0$ 时 $p(t) \to 0$，即我们确实收敛到损失函数 $\mathcal{L}(p) = \frac{1}{2} p_1^2 + \frac{1}{2} \varepsilon p_2^2$ 的全局最小值 $p = 0$，它是ODE (53)的平衡点。然而，由于 $\varepsilon$ 很小，我们只看到第一个分量 $p_1$ 的快速收敛。当 $p_1$ 很小时，我们得到 $Ap$ 也很小，因此由于几乎消失的梯度，收敛极其缓慢。更准确地说，ODE (53)具有多时间尺度结构，导致几乎消失的梯度；注意，在实际中，由于数值误差和/或随机优化方案，我们从未有精确消失的梯度，而是面临梯度非常接近零的问题。同样的多尺度效应在许多更复杂的问题中可能更加明显。事实上，架构的选择、激活函数、前馈情形的层深度以及许多其他因素可以隐式地产生多尺度结构。即使优化问题原则上适定，如在我们平凡的例子中，消失的梯度也可能使实际计算非常困难。当然，简单地将参数 $\varepsilon$ 反转为 $1/\varepsilon$ 会给出极大的梯度。在我们的例子中，这甚至可以通过简单地重新缩放来实现

[第30页，第7段]
$ ^1 $实际上有趣的是，看看与[134]同期发表的其他论文，包括英语、法语、德语和拉丁语的作品，以及玻尔兹曼、凯莱、弗罗贝尼乌斯、富克斯、汉堡、埃尔米特、克罗内克、库默尔、利普希茨、闵可夫斯基、皮卡、龙格、塞格雷、西尔维斯特、托梅和魏因加滕等作者，他们有许多以他们命名的数学概念。

[第31页，第1段]
时间并定义 $s := t\varepsilon$。科学和工程中的许多经典问题自然会引出多尺度结构，例如化学反应、生物神经元动力学、激光系统以及进化过程等，仅举几例 [87]。因此，许多可以重新表述为动力系统的机器学习（ML）挑战也遇到这个问题，这并不令人意外。总之，期望梯度消失/爆炸在机器学习中频繁出现是相当自然的，这可以进一步使用动力学技术进行分析，例如在混沌系统 [61] 的背景下。

[第31页，第2段]
5 结论

[第31页，第3段]
基于我们之前的讨论，人们可以为人工智能/机器学习（AI/ML）中出现的其他（已知甚至未知的）主题确定一个通用策略。任何纯粹与“学习”相关的方面都必须本质上与动力学视角相联系。事实上，训练过程通常是一个序列化或时间依赖的过程，不断精炼机器学习模型的参数化。例如，我们不断收集新数据，因此通常需要训练新模型或重新训练现有模型，这两者都是动力学过程。关于结构性的“信息处理”，例如通过深度神经网络，总是存在一个将输入映射到输出的序列化转换步骤，这可以视为一个（有限时间）动力学过程的结果。将这两个过程结合起来会导致非自治动力学、自适应/协同进化网络动力学、最优控制挑战或其变体，这些又可以从动力系统的角度来审视。为了严格理解一个 AI/ML 问题的基本难度水平，并弄清楚有哪些技术工具可用于解决它，我们建议首先提取动力学核心问题可以带来巨大的收益。例如，众所周知为什么某些粒子系统比其他系统更难研究，为什么非自治系统中的分岔在结构上与自治系统非常不同，或者为什么随机动力学系统可以诱导新的效应。

[第31页，第4段]
当然，在 AI 背景下存在来自更复杂非线性系统的挑战，这些挑战无法仅通过纸笔动力学技术在数学上证明。对于许多相当低维的经典动力系统来说，这已经是一个众所周知的问题 [130]。然而，即使在这些情况下，也有严格的方法可用于计算验证观察到的动力学现象。例如，在我们的 SPP2298 项目中，这促成了与其他研究人员的各种合作，专注于计算机辅助证明 [84]，即使用计算机辅助证明来证明神经网络生成某些动力学模式。尽管本综述不会进一步追求这个方向，但它很好地说明了 AI/ML 中的新兴方向通常与因动力系统挑战而产生的技术相耦合。

[第31页，第5段]
参考文献

[第31页，第6段]
[1] D. Ackley, G. Hinton, and T. Sejnowski. A learning algorithm for Boltzmann machines. *Cognitive Science*, 9(1):147–169, 1985.

[第31页，第7段]
[2] Kwangjun Ahn, Jingzhao Zhang, and Suvrit Sra. Understanding the unstable convergence of gradient descent. In *Proceedings of the 39th International Conference on Machine Learning*, volume 162 of *Proceedings of Machine Learning Research*, pages 247–257. PMLR, 17–23 Jul 2022.

[第31页，第8段]
[3] S.I. Amari. Characteristics of randomly connected threshold-element networks and network systems. *Proceedings of the IEEE*, 59:35–47, 1971.

[第31页，第9段]
[4] S.I. Amari. Learning patterns and pattern sequences by self-organizing nets of threshold elements. *IEEE Trans. Computers C*, 21:1197–1206, 1972.

[第31页，第10段]
[5] J.A. Anderson. A simple neural network generating an interactive memory. *Math. Biosci.*, 14(3):197–220, 1972.

[第31页，第11段]
[6] Arseniy Andreyev and Pierfrancesco Beneventano. Edge of stochastic stability: Revisiting the edge of stability for sgd, 2025.

[第32页，第1段]
[7] L. Appeltant, M.C. Soriano, G. Van der Sande, J. Danckaert, S. Massar, J. Dambre, B. Schrauwen, C.R. Mirasso, 和 I. Fischer。使用单个动力学节点作为复杂系统的信息处理。*Nature Communications*，2(1):468，2011。

[第32页，第2段]
[8] Ludwig Arnold。*随机动力系统*。Springer数学专著系列。Springer-Verlag，柏林，1998。

[第32页，第3段]
[9] Sanjeev Arora, Elad Hazan, 和 Satyen Kale。乘法权重更新方法：一种元算法及其应用。*计算理论*，8(1):121–164，2012。

[第32页，第4段]
[10] N. Ayi 和 N.P. Duteil。具有时变权重的集体动力学模型的平均场与图极限。*微分方程杂志*，299:65–110，2021。

[第32页，第5段]
[11] A. Backhausz 和 B. Szegedy。算子与图的行动收敛。*加拿大数学杂志*，74(1):72–121，2022。

[第32页，第6段]
[12] P. H. Baxendale 和 D. W. Stroock。微分同胚的大偏差与随机流。*概率论及相关领域*，80(2):169–215，1988。

[第32页，第7段]
[13] Mikhail Belkin, Daniel Hsu, Siyuan Ma, 和 Soumik Mandal。调和现代机器学习实践与经典偏差-方差权衡。*美国国家科学院院刊*，116(32):15849–15854，2019。

[第32页，第8段]
[14] Michel Benaim。随机逼近的动力系统方法。*SIAM控制与优化杂志*，34(2):437–472，1996。

[第32页，第9段]
[15] R. Berner, T. Gross, C. Kuehn, J. Kurths, 和 S. Yanchuk。自适应动态网络。*物理学报告*，103:1–59，2023。

[第32页，第10段]
[16] Dimitri Bertsekas。非线性规划。*运筹学学会杂志*，48(3):334–334，1997。

[第32页，第11段]
[17] L. Boltzmann。关于气体分子热平衡的进一步研究。*帝国科学院会议报告。数学-自然科学类*，66:262–349，1872。

[第32页，第12段]
[18] Anton Bovier 和 Frank den Hollander。*亚稳态*，第351卷，*数学科学基础教程[数学科学基本原理]*。Springer，Cham，2015。一种势论方法。

[第32页，第13段]
[19] W. Braun 和 K. Hepp。Vlasov动力学及其在相互作用经典粒子1/N极限中的涨落。*数学物理通讯*，56(2):101–113，1977。

[第32页，第14段]
[20] S.L. Brunton 和 J.N. Kutz。*数据驱动的科学与工程：机器学习、动力系统与控制*。剑桥大学出版社，2022。

[第32页，第15段]
[21] Hanqun Cao, Cheng Tan, Zhangyang Gao, Yilun Xu, Guangyong Chen, Pheng-Ann Heng, 和 Stan Z. Li。生成扩散模型综述。*IEEE知识与数据工程汇刊*，36:2814–2830，2022。

[第32页，第16段]
[22] Olivier Cappé, Eric Moulines, 和 Tobias Rydén。*隐马尔可夫模型中的推断*。Springer统计学系列。Springer，纽约，2005。Randal Douc对第9章的贡献和Christian P. Robert对第6、7和13章的贡献，第14章由Gersende Fort、Philippe Soulier和Moulines撰写，第15章由Stéphane Boucheron和Elisabeth Gassiat撰写。

[第32页，第17段]
[23] C. Cercignani。*玻尔兹曼方程及其应用*。Springer，1988。

[第32页，第18段]
[24] Nisha Chandramoorthy 和 Adriaan de Clercq。不精确生成模型何时以及如何仍能从数据流形中采样？，2025。

[第32页，第19段]
[25] Dennis Chemnitz 和 Maximilian Engel。刻画过参数化学习中随机梯度下降的动力学稳定性。*arXiv预印本arXiv:2407.20209*，2024。

[第33页，第1段]
[26] Ricky T. Q. Chen、Yulia Rubanova、Jesse Bettencourt 和 David Duvenaud。神经常微分方程。*NeurIPS*，2018。

[第33页，第2段]
[27] H. Chiba 和 G. Medvedev。图上 Kuramoto 模型的平均场分析 I：平均场方程与转捩点公式。*Discr. Cont. Dyn. Syst. A*，39(1)：131–155，2019。

[第33页，第3段]
[28] Lenaic Chizat 和 Francis Bach。关于使用最优传输（optimal transport）对过参数化模型进行梯度下降的全局收敛性。*Advances in neural information processing systems*，31，2018。

[第33页，第4段]
[29] Jeremy Cohen、Simran Kaur、Yuanzhi Li、J Zico Kolter 和 Ameet Talwalkar。神经网络上的梯度下降通常发生在稳定性边缘。载于 *International Conference on Learning Representations*，2020。

[第33页，第5段]
[30] Yaim Cooper。过参数化神经网络的全局极小值。*SIAM J. Math. Data Sci.*，3(2)：676–691，2021。

[第33页，第6段]
[31] Alexandru Crăciun 和 Debarghya Ghoshdastidar。关于大学习率下梯度下降的收敛性。*arXiv preprint arXiv:2402.13108*，2024。

[第33页，第7段]
[32] F. Cucker 和 S. Smale。鸟群中的涌现行为。*IEEE Transactions on Automatic Control*，52(5)：852–862，2007。

[第33页，第8段]
[33] G. Cybenko。通过 sigmoid 函数（sigmoidal function）的叠加进行逼近。*Mathematics of Control, Signals, and Systems*，2(4)：303–314，1989年12月。

[第33页，第9段]
[34] R.C. Desai 和 R. Zwanzig。非线性随机模型的统计力学。*J. Stat. Phys.*，19：1–24，1978。

[第33页，第10段]
[35] R. Dobrushin。Vlasov 方程。*Funct. Anal. Appl.*，13：115–123，1979。

[第33页，第11段]
[36] R.L. Dobrushin。具有大量局部相互作用分量的马尔可夫过程。*Problems of Transmission of Information*，7(2)：70–87，1971。俄文。

[第33页，第12段]
[37] Emilien Dupont、Arnaud Doucet 和 Yee Whye Teh。增广神经常微分方程。*Advances in Neural Information Processing Systems*，32：3140–3150，2019。

[第33页，第13段]
[38] Weinan E。关于通过动力系统进行机器学习的提议。*Commun. Math. Stat*，5：1–11，2017年3月。

[第33页，第14段]
[39] Maximilian Engel 和 Georgios Piliouras。零和博弈中复制子动力学（replicator dynamics）的随机变体及其不变测度。*Phys. D*，456：论文编号 133940，15，2023。

[第33页，第15段]
[40] J.D. Farmer、N.H. Packard 和 A.S. Perelson。免疫系统、适应与机器学习。*Phys. D*，22(1)：187–204，1986。

[第33页，第16段]
[41] Benjamin Fehrman、Benjamin Gess 和 Arnulf Jentzen。非凸目标函数下随机梯度下降方法的收敛速率。*Journal of Machine Learning Research*，21(136)：1–48，2020。

[第33页，第17段]
[42] R. FitzHugh。神经膜中阈值现象的数学模型。*Bull. Math. Biophysics*，17：257–269，1955。

[第33页，第18段]
[43] M. Fornasier、L. Pareschi、H. Huang 和 P. Sünnen。球面上的基于共识的优化（consensus-based optimization）：收敛到全局极小值与机器学习。*Journal of Machine Learning Research*，22(237)：1–55，2021。

[第33页，第19段]
[44] T.D. Frank。*非线性 Fokker-Planck 方程：基础与应用*。Springer，2005。

[第33页，第20段]
[45] H. Furstenberg 和 H. Kesten。随机矩阵的乘积。*Ann. Math. Statist.*，31：457–469，1960。

[第34页，第1段]
[46] Benjamin Gess, Rishabh S Gvalani, 和 Vitalii Konarovskyi. 保守随机偏微分方程（SPDEs）作为随机梯度下降的涨落平均场极限. *概率论及相关领域*, 页码 1–69, 2025.

[第34页，第2段]
[47] M.A. Gkogkas 和 C. Kuehn. Kuramoto型模型的图算子平均场极限. *SIAM 应用动力系统杂志*, 21(1):248–283, 2022.

[第34页，第3段]
[48] M.A. Gkogkas, C. Kuehn, 和 C. Xu. 自适应网络动力学的连续极限. *数学科学通讯*, 21(1):83–106, 2023.

[第34页，第4段]
[49] M.A. Gkogkas, C. Kuehn, 和 C. Xu. 协同进化符号异质网络的平均场极限. *欧洲应用数学杂志 (已接受/待发表)*, 页码 1–44, 2025.

[第34页，第5段]
[50] Harshvardhan GM, Mahendra Kumar Goursaria, Manjusha Pandey, 和 Siddharth Swarup Rautaray. 机器学习中生成模型的综合调查与分析. *计算机科学评论*, 38:100285, 2020.

[第34页，第6段]
[51] N. Goldenfeld. *相变与重整化群讲义*. Westview 出版社, 1992.

[第34页，第7段]
[52] F. Golse. 平均场极限下大粒子系统的动力学. 载于 *宏观与大尺度现象：粗粒化、平均场极限与遍历性*, 页码 1–144. Springer, 2016.

[第34页，第8段]
[53] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, 和 Yoshua Bengio. 生成对抗网络. 载于 *神经信息处理系统进展*, 页码 2672–2680, 2014.

[第34页，第9段]
[54] Priya Goyal, Piotr Dollár, Ross Girshick, Pieter Noordhuis, Lukasz Wesolowski, Aapo Kyrola, Andrew Tulloch, Yangqing Jia, 和 Kaiming He. 精确的大批量随机梯度下降：1小时内训练ImageNet. *arXiv预印本 arXiv:1706.02677*, 2017.

[第34页，第10段]
[55] A. Griewank. 自动微分的数学视角. *数值分析学报*, 12:321–398, 2003.

[第34页，第11段]
[56] J. Guckenheimer 和 P. Holmes. *非线性振动、动力系统与向量场的分岔*. Springer, 纽约, 1983.

[第34页，第12段]
[57] John Guckenheimer 和 Philip Holmes. *非线性振动、动力系统与向量场的分岔*, 第42卷 *应用数学科学*. Springer 纽约, 第7版, 2002.

[第34页，第13段]
[58] Mert Gurbuzbalaban, Umut Simsekli, 和 Lingjiong Zhu. 随机梯度下降中的重尾现象. 载于 *第38届国际机器学习会议论文集*, 第139卷 *机器学习研究论文集*, 页码 3964–3975. PMLR, 2021年7月18–24日.

[第34页，第14段]
[59] Kaiming He, Xiangyu Zhang, Shaoqing Ren, 和 Jian Sun. 用于图像识别的深度残差学习. *IEEE计算机视觉与模式识别会议*, 页码 770–778, 2016年6月.

[第34页，第15段]
[60] R. Hegselmann 和 U. Krause. 观点动力学与有界置信模型：分析及模拟. *人工社会与社会模拟杂志*, 5(3):1–33, 2002.

[第34页，第16段]
[61] F. Hess 和 Z. Monafred. 用于学习混沌动力学的广义教师强制. *PMLR*, 202:13017–13049, 2023.

[第34页，第17段]
[62] Joshua Hess 和 Quaid Morris. 零噪声极限下的联想记忆与生成扩散, 2025.

[第34页，第18段]
[63] Morris W. Hirsch. *微分拓扑*, 第33卷 *数学研究生教材*. Springer 纽约, 1976.

[第35页，第1段]
[64] S. Hochreiter and J. Schmidhuber. 长短期记忆（Long short-term memory）。*Neural Computation*，9(8)：1735–1780，1997。

[第35页，第2段]
[65] Sepp Hochreiter and Jurgen Schmidhuber. 平坦极小值（Flat minima）。*Neural computation*，9：1–42，02 1997。

[第35页，第3段]
[66] Josef Hofbauer. 双矩阵博弈的演化动力学：一个哈密顿系统（Hamiltonian system）？*J. Math. Biol.*，34(5-6)：675–688，1996。

[第35页，第4段]
[67] Elad Hoffer, Itay Hubara, and Daniel Soudry. 训练更久，泛化更好：弥合神经网络大批量训练中的泛化差距。In I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors，*Advances in Neural Information Processing Systems*，volume 30. Curran Associates, Inc.，2017。

[第35页，第5段]
[68] J.J. Hopfield. 具有涌现集体计算性质的神经网络与物理系统。*Proc. Nat. Acad. Sci. USA*，79：2554–2558，1982。

[第35页，第6段]
[69] Kurt Hornik, Maxwell Stinchcombe, and Halbert White. 多层前馈网络是通用逼近器（universal approximators）。*Neural Networks*，2(5)：359–366，jan 1989。

[第35页，第7段]
[70] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kilian Q. Weinberger. 密集连接卷积网络（Densely connected convolutional networks）。2017。

[第35页，第8段]
[71] V. Isham. 空间点过程与马尔可夫随机场（Markov random fields）导论。*Int. Stat. Rev.*，49(1)：21–43，1981。

[第35页，第9段]
[72] E. Ising. 铁磁性理论贡献。*Zeitschrift für Physik A*，31(1)：253–258，1925。

[第35页，第10段]
[73] P.E. Jabin. Vlasov 方程的平均场极限（mean field limits）综述。*Kinet. Rel. Mod.*，7(4)：661–711，2014。

[第35页，第11段]
[74] H. Jaeger. 训练循环神经网络教程，涵盖 bppt、rtrl、ekf 及“回声状态网络（echo state network）”方法。Technical report，2002。

[第35页，第12段]
[75] D. Kaliuzhnyi-Verbovetskyi and G.S. Medvedev. 稀疏随机图上的半线性热方程。*SIAM J. Math. Analysis*，49(2)：1333–1355，2017。

[第35页，第13段]
[76] D. Kaliuzhnyi-Verbovetskyi and G.S. Medvedev. 具有非 Lipschitz 极限的图序列上 Kuramoto 模型的平均场方程。*SIAM J. Math. Analysis*，50(3)：2441–2465，2018。

[第35页，第14段]
[77] Anatole Katok and Boris Hasselblatt. *现代动力系统理论导论（Introduction to the Modern Theory of Dynamical Systems）*，volume 54 of *Encyclopedia of Mathematics and its Applications*. Cambridge University Press，apr 1995。

[第35页，第15段]
[78] Patrick Kidger. *论神经微分方程（On Neural Differential Equations）*。PhD thesis，Mathematical Institute, University of Oxford，2022。

[第35页，第16段]
[79] A.N. Kolmogorov. 关于将多变量连续函数表示为较少变量连续函数的叠加。*Dokl. Akad. Nauk*，108(2)：179–182，1956。

[第35页，第17段]
[80] B. Kosko. *神经网络与模糊系统：面向机器智能的动力系统方法（Neural networks and fuzzy systems: a dynamical systems approach to machine intelligence）*。Prentice Hall，1992。

[第35页，第18段]
[81] C. Kuehn. *偏微分方程动力学：导论（PDE Dynamics: An Introduction）*。SIAM，2019。

[第35页，第19段]
[82] C. Kuehn. 图算子（graphops）上的网络动力学。*New J. Phys.*，22(5)：053030，2020。

[第35页，第20段]
[83] C. Kuehn and C. Pulido. 有向图测度上随机相互作用粒子的平均场极限。*arXiv:2403.20325*，pages 1–28，2024。

[第36页，第1段]
[84] C. Kuehn 和 E. Queirolo。神经网络动力学的计算机验证：首个案例研究。*离散与连续动力系统*，30(6)：2073–2093，2025。

[第36页，第2段]
[85] C. Kuehn 和 S. Throm。图极限上的电力网络动力学。*SIAM 应用数学杂志*，79(4)：1271–1292，2019。

[第36页，第3段]
[86] C. Kuehn 和 C. Xu。有向图测度上的 Vlasov 方程。*微分方程杂志*，339：261–349，2022。

[第36页，第4段]
[87] Christian Kuehn。*多时间尺度动力学*。应用数学科学丛书。Springer 国际出版，2015。

[第36页，第5段]
[88] Christian Kuehn 和 Sara-Viola Kuntz。神经常微分方程的嵌入能力。*预印本*，2023。

[第36页，第6段]
[89] Christian Kuehn 和 Sara-Viola Kuntz。通过莫尔斯函数分析神经网络和神经常微分方程的几何结构。*预印本*，2024。

[第36页，第7段]
[90] Christian Kuehn 和 Sara-Viola Kuntz。神经时滞微分方程的记忆容量对通用逼近性质的影响。*预印本*，2025。

[第36页，第8段]
[91] Y. Kuramoto。*化学振荡、波与湍流*。Dover，1984。

[第36页，第9段]
[92] Yu.A. Kuznetsov。*应用分岔理论要素*。Springer，纽约，第3版，2004。

[第36页，第10段]
[93] C. Lancellotti。关于无噪声非线性耦合振子系统的 Vlasov 极限。*理论统计物理汇刊*，34(7)：523–535，2005。

[第36页，第11段]
[94] T.M. Liggett。*随机相互作用系统：接触、投票者与排斥过程*。Springer，2013。

[第36页，第12段]
[95] Hongzhou Lin 和 Stefanie Jegelka。具有单神经元隐藏层的 ResNet 是通用逼近器。*神经信息处理系统进展*，31：6169–6178，2018。

[第36页，第13段]
[96] L. Lovász。*大网络与图极限*。AMS，2012。

[第36页，第14段]
[97] Chao Ma 和 Lexing Ying。关于 SGD 的线性稳定性和神经网络的输入光滑性。载于*神经信息处理系统进展*，2021。

[第36页，第15段]
[98] G.S. Medvedev。W-随机图上的非线性热方程。*理性力学与分析档案*，212(3)：781–803，2014。

[第36页，第16段]
[99] G.S. Medvedev。Kuramoto 振子的小世界网络。*物理D*，266：13–22，2014。

[第36页，第17段]
[100] John Milnor。关于吸引子概念。*数学物理通讯*，99(2)：177–195，1985。

[第36页，第18段]
[101] John W. Milnor。*从可微观点看拓扑学*。普林斯顿数学里程碑丛书。普林斯顿大学出版社，新泽西州普林斯顿，1997。基于 David W. Weaver 的笔记，1965年原版的修订重印。

[第36页，第19段]
[102] Marston Morse。*大范围变分法*，*讨论会出版物*第18卷。美国数学学会，1934。

[第36页，第20段]
[103] J. Nagumo、S. Arimoto 和 S. Yoshizawa。模拟神经轴突的主动脉冲传输线。*IRE  Proceedings*，50：2061–2070，1962。

[第36页，第21段]
[104] H. Neunzert。非线性 Boltzmann-Vlasov 方程引论。载于*动理论理论与 Boltzmann 方程*，第60–110页。Springer，1984。

[第36页，第22段]
[105] M.E.J. Newman。复杂网络的结构与功能。*SIAM 评论*，45：167–256，2003。

[第37页，第1段]
[106] Andrew Ng 和 Michael Jordan。关于判别式与生成式分类器：逻辑回归与朴素贝叶斯的比较。载于 T. Dietterich、S. Becker 和 Z. Ghahramani 编，*Advances in Neural Information Processing Systems*，第 14 卷。MIT Press，2001。

[第37页，第2段]
[107] Michela Ottobre。马尔可夫链蒙特卡洛与不可逆性。*Rep. Math. Phys.*，77(3):267–292，2016。

[第37页，第3段]
[108] M. Ozturk、D. Xu 和 J.C. Principe。回声状态网络的分析与设计。*Neural Computation*，19(1):111–138，2007。

[第37页，第4段]
[109] G.A. Pavliotis。*Stochastic Processes and Applications: diffusion processes, the Fokker-Planck and Langevin equations*。Springer，2014。

[第37页，第5段]
[110] Allan Pinkus。神经网络中 MLP 模型的逼近理论。*Acta Numerica*，8:143–195，1999年1月。

[第37页，第6段]
[111] M.A. Porter 和 J.P. Gleeson。*Dynamical Systems on Networks: A Tutorial*。Frontiers in Applied Dynamical Systems: Reviews and Tutorials。Springer，2016。

[第37页，第7段]
[112] C. Pötzsche。*Geometric Theory of Discrete Nonautonomous Dynamical Systems*。Lecture Notes in Mathematics。Springer，2010。

[第37页，第8段]
[113] H. Risken。*The Fokker-Planck Equation*。Springer，1996。

[第37页，第9段]
[114] Christian P. Robert 和 George Casella。*Monte Carlo statistical methods*。Springer Texts in Statistics。Springer-Verlag，纽约，第二版，2004。

[第37页，第10段]
[115] J.B. Roberts。某些神经网络的数学生物物理学。*Bull. Math. Biophys.*，10:1–10，1948。

[第37页，第11段]
[116] Olaf Ronneberger、Philipp Fischer 和 Thomas Brox。U-net：用于生物医学图像分割的卷积网络。第 234–241 页，2015。

[第37页，第12段]
[117] Frank Rosenblatt。感知机——一种感知与识别自动机。*Cornell Aeronautical Laboratory, INC., Buffalo, New York*，(85-460-1)，1957。

[第37页，第13段]
[118] G. Rotskoff 和 E. Vanden-Eijnden。人工神经网络的可训练性与准确性：一种相互作用粒子系统方法。*Comm. Pure Appl. Math.*，75(9):1889–1935，2022。

[第37页，第14段]
[119] Domènec Ruiz-Balet 和 Enrique Zuazua。用于分类、逼近和传输的神经常微分方程控制。*SIAM Review*，65(3):735–773，2023年8月。

[第37页，第15段]
[120] Clayton Sanford 和 Vaggos Chatziafratis。超越 Sharkovsky 定理：通过混沌轨道看神经网络的表达力。2021。

[第37页，第16段]
[121] Anton Maximilian Schäfer 和 Hans Georg Zimmermann。*Recurrent Neural Networks Are Universal Approximators*，第 632–640 页。Springer Berlin Heidelberg，2006。

[第37页，第17段]
[122] A.N. Sharkovskii。关于连续映射的循环与结构。*Ukrainskii Matematicheskii Zhurnal*，17(3):104–111，1965。

[第37页，第18段]
[123] D. Sherrington 和 S. Kirkpatrick。自旋玻璃的可解模型。*Phys. Rev. Lett.*，35:1792–1796，1975。

[第37页，第19段]
[124] A. Sherstinsky。循环神经网络（RNN）与长短期记忆（LSTM）网络基础。*Physica D*，404:132306，2020。

[第37页，第20段]
[125] Justin Sirignano 和 Konstantinos Spiliopoulos。神经网络的平均场分析：大数定律。*SIAM Journal on Applied Mathematics*，80(2):725–752，2020。

[第37页，第21段]
[126] D. Somers 和 N. Kopell。通过快速阈值调制实现快速同步。*Biol. Cybern.*，68(5):393–407，1993。

[第38页，第1段]
[127] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, 和 Ben Poole. 基于随机微分方程的分数生成建模. *CoRR*, abs/2011.13456, 2020.

[第38页，第2段]
[128] S.H. Strogatz. 从 Kuramoto 到 Crawford：探索耦合振子群体中同步的发生. *Physica D*, 143:1–20, 2000.

[第38页，第3段]
[129] A.S. Sznitman. 混沌传播专题. 载于 P.-L. Hennequin 主编, *Ecole d’Été de Probabilités de Saint-Flour XIX - 1989*, *Lecture Notes in Mathematics* 第1464卷, 第165–251页. Springer, 1991.

[第38页，第4段]
[130] W. Tucker. Lorenz 吸引子存在. *C.R. Acad. Sci. Paris*, 328:1197–1202, 1999.

[第38页，第5段]
[131] B. van der Pol. 自由和受迫三极管振动幅度的理论. *Radio Review*, 1:701–710, 1920.

[第38页，第6段]
[132] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L. Kaiser, 和 I. Polosukhin. 注意力就是你所需要的一切. *Advances in Neural Information Processing Systems*, 第30页, 2017.

[第38页，第7段]
[133] C. Villani. *最优传输：旧与新*. Springer, 2008.

[第38页，第8段]
[134] H. von Helmholtz. 论最小作用量原理的物理意义. *J. Reine Angew. Math. (Crelle)*, 100:137–166, 1887.

[第38页，第9段]
[135] A. Waibel. 用于语音识别的时间延迟神经网络的模块化构建. *Neural Computation*, 1(1):39–46, 1989.

[第38页，第10段]
[136] Jörgen W. Weibull. *演化博弈论*. MIT Press, Cambridge, MA, 1995. 由 Ken Binmore 作序.

[第38页，第11段]
[137] H. Wilson 和 J. Cowan. 模型神经元局部群体中的兴奋性和抑制性相互作用. *Biophysical J.*, 12:1–24, 1972.

[第38页，第12段]
[138] H. Wilson 和 J. Cowan. 皮层和丘脑神经组织功能动力学的数学理论. *Biol. Cybern.*, 13(2):55–80, 1973.

[第38页，第13段]
[139] A.T. Winfree. 生物节律与耦合振子群体的行为. *J. Theor. Biol.*, 16(1):15–42, 1967.

[第38页，第14段]
[140] Lei Wu, Chao Ma, 和 Weinan E. SGD 如何在过参数化学习中选择全局最小值：动力稳定性视角. 载于 *Advances in Neural Information Processing Systems*, 第31卷. Curran Associates, Inc., 2018.

[第38页，第15段]
[141] Han Zhang, Xi Gao, Jacob Unterman, 和 Tom Arodz. 神经常微分方程和可逆残差网络的逼近能力. *Proceedings of the 37th International Conference on Machine Learning*, 119:11086–11095, 2020.

[第38页，第16段]
[142] Qunxi Zhu, Yao Guo, 和 Wei Lin. 神经延迟微分方程. *ICLR conference papers*, 2021.
