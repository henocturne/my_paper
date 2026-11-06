[第1页，第1段]
局部核重整化作为过参数化卷积神经网络中特征学习的机制

[第1页，第2段]
收稿日期：2024年4月2日
接受日期：2024年12月4日
在线发布日期：2025年1月10日

[第1页，第3段]
检查更新

[第1页，第4段]
R. Aiudi¹,²,⁶, R. Pacelli⁶ ³,⁶, P. Baglioni⁴, A. Vezzani⁶ ¹,²,⁵, R. Burioni⁶ ¹,² &

[第1页，第5段]
P. Rotondo⁶ ¹

[第1页，第6段]
经验证据表明，在大多数计算机视觉任务中，无限宽度极限（惰性训练）下的全连接神经网络最终会优于其有限宽度对应物；另一方面，具有卷积层的现代架构通常在有限宽度区域实现最佳性能。在这项工作中，我们提出了一个理论框架，为单隐藏层网络中的这些差异提供了理论依据；我们推导了具有一个卷积隐藏层的架构在所谓比例极限下的有效作用量，并将其与全连接网络的可用结果进行比较。值得注意的是，我们识别出一种完全不同形式的核重整化：全连接架构的核仅由一个标量参数进行全局重整化，而卷积核则经历局部重整化，这意味着网络可以以数据依赖的方式选择将贡献于最终预测的局部分量。这一发现突显了一种简单的特征学习机制，该机制可以在过参数化的浅层卷积神经网络中发生，但不会在浅层全连接架构或没有权重共享的局部连接神经网络中发生。

[第1页，第7段]
深度学习在从计算机视觉到自然语言处理¹的各种模式识别任务上实现了最先进的性能。一个最小的深度学习理论应该能够（至少）从训练数据的知识中预测实际相关的分数，例如训练和测试准确率。在基本层面上，这意味着解决所谓的特征学习机制²,³，即深度网络从原始数据中自动检测有用表示的能力⁴。

[第1页，第8段]
研究人员已经研究了多种策略来应对这些挑战，包括（i）神经网络的大宽度（无限宽度）极限，即隐藏层大小 $N_\ell$（其中 $\ell = 1...L$，$L$ 为网络深度）趋于无穷大而训练集中示例数量 $P$ 保持有限的状态。这建立了第一个也是唯一一个深度架构的解析可解模型，揭示了一系列丰富的现象学，从所谓的惰性训练⁵-¹⁶到特征学习机制⁷-²⁶，（ii）对无限宽度极限的微扰修正⁷-²⁷，（iii）深度线性模型⁸-³⁵。尽管具有普遍意义，但这些结果并未描述现实状态下的神经网络：无限宽度近似明显偏离神经网络实践，其中训练示例数量 $P$ 在数量级上相当甚至大于层宽度，而线性激活函数的假设则极大地降低了模型的表达能力。

[第1页，第9段]
为了描述逼真的学习设置，在贝叶斯神经网络背景下，在所谓的比例极限中已经取得了进展，该极限定义为热力学极限，其中隐藏层和训练集的大小趋于无穷大，而它们的比率 $\alpha_\ell = P/N_\ell$ 保持有限。在这个框架中，可以构建

[第2页，第1段]
基于尺度分离的热力学描述$ ^{36,37} $，或直接提取一个“有效作用量”，其最小化描述了该机制下训练的全部效果$ ^{38-40} $。深度神经网络（DNNs）的贝叶斯框架在经典文献$ ^{41} $中首次提出，其与平衡态统计力学的联系最近在文献42中进行了综述。高斯过程在无限宽度和比例极限中都是基础性的，标准的入门参考文献是书籍$ ^{43} $。

[第2页，第2段]
上述理论结果所描绘的图景，由一系列近期实证观察所补充，这些观察强调了无限宽度性能在某些情境下是最先进的。例如，文献$ ^{44} $的作者进行的大规模实证研究，他们探索了大量可能的设置以改善有限和无限宽度模型的泛化能力，引发了几个引人注目的观察：在全连接（FC）深度神经网络的情况下，无限宽度核系统地优于其有限宽度对应物；具有有限通道数的卷积神经网络（CNNs）通常优于其相应的无限宽度核性能。文献中已报道了几个类似的观察：文献45的作者最近指出，随着训练集规模的增长，无限宽度深度FC神经网络最终会优于其有限宽度对应物。在处理无限宽度极限的开创性论文之一$ ^{5} $中，作者观察到增加隐藏层大小可以在MNIST和CIFAR10（计算机视觉学习问题的两个基准数据集）上训练的深度FC架构上实现最佳测试准确率。在文献10中，这一观察被扩展到没有权重共享的局部连接网络（LCNs）。有趣的是，文献46,47的作者观察到，具有平均场缩放（在无限宽度极限中显示特征学习）的FC网络系统性地被无限宽度核所超越。

[第2页，第3段]
这些发现表明，CNNs在有限宽度下利用了比FC和LCNs更好的特征学习机制，并引发了至少两个概念性问题：（i）为什么在只有FC层可用时，采用大宽度架构最终是方便的？（ii）为什么在使用卷积层时情况并非如此？以及CNN如何操作性地利用有限宽度机制进行高效的特征学习？

[第2页，第4段]
在这项工作中，我们试图通过核重整化的视角来合理化上述实证观察，这是比例宽度描述的一个物理后果，在文献38中针对非线性网络被识别出来。首先，我们为两个简单的浅层模型（CNN和LCN）推导了一个有效作用量，表明其函数形式在架构之间是共享的，并与FC情况相关。其次，我们表明文献38的理论框架为问题（i）提供了一个简单但非常有启发性的答案：比例宽度浅层网络的性能可以通过相应的无限宽度核和适当选择每层权重上的高斯先验来获得。最后，我们将CNNs获得的结果与FC网络的可用结果进行比较。我们发现在两种架构的核在比例宽度下重整化的方式上存在显著差异：FC核仅由一个标量参数全局重整化，而CNN核经历局部重整化，这意味着在训练期间允许更多自由参数被微调（另见图1）。我们利用这一发现为问题（ii）提供初步见解：我们强调了一种简单的特征学习机制，它可以在有限宽度浅层CNNs中发生，但既不能在浅层FC架构中也不能在没有权重共享的LCNs中发生。

[第2页，第5段]
**结果**

[第2页，第6段]
**比例机制下学习的有效作用量的函数形式在具有局部连接的浅层架构之间是共享的**

[第2页，第7段]
为了解决本手稿引言中提出的问题，我们分析性地研究了两种具有局部连接的单隐藏层（IHL）架构，即CNNs和具有FC读出层的LCNs，其明确定义在本手稿的方法部分给出。

[第2页，第8段]
卷积层的两个基本要素是局部连接和权重共享：FC隐藏层中的给定神经元接收来自前一层所有神经元的输入，而CNN中的神经元排列在一个$d$维数组中，反映了输入数据的相应$d$维排列（例如，对于图像$d = 2$）。这里给定层中的每个神经元仅以平移不变的方式与前一层中神经元的局部邻域交互。

[第2页，第9段]
![图1 | FC和卷积单隐藏层网络中的全局和局部核。](image)

[第2页，第10段]
我们在固定$a_1 = P/N_1$的比例极限$P, N_1 \to \infty$下的计算揭示了FC和CNNs之间的显著差异。在第一种情况下，网络性能与NNGP核$K_{\mu\nu}$相关联，该核仅能够跟踪不同训练模式（$\mu, \nu$）之间的全局相关性（左）。该机制下的FC网络将利用数据集中包含的信息来微调单个参数$Q$，该参数将全局重新缩放核矩阵$K_{\mu\nu}$。另一方面，在CNN情况下，我们识别出一个具有两个额外（空间）索引的局部核。如果我们考虑$2d$图像，局部分量的效果是跟踪（可能）不同图像对（$\mu, \nu$）的不同块$i$和$j$之间的局部相关性（右）。这些相关性中包含的空间信息允许CNN优化参数矩阵$Q_{ij}$，该矩阵将以非平凡的方式重整化核矩阵$K_{\mu\nu}^j$。在图中，我们使用多索引符号$K_{\mu\nu, \lambda(\nu, j)}$并为多索引（$\mu, \lambda$）选择排序，将四索引局部核$K_{\mu\nu}^j$显示为矩阵。全局和局部核是针对$P = 10$张降采样至$N_0 = 784$的灰度CIFAR10图像子集计算的。局部核是针对$2d$卷积经验评估的，滤波器掩码的线性尺寸$M = 14$，步长$S = 14$（非重叠滤波器）。

[第3页，第1段]
text<|/ref|>[[64, 58, 494, 168]]<|/det|>
通过一个共享的（通常较小的）$ d $ 维可学习权重掩码来实现。这些操作定义了一个单一的卷积通道，该通道以 $ d $ 维数组为输入，输出另一个 $ d $ 维数组，其维度由技术细节（如步长、填充和滤波器掩码的维度）决定。通常，许多这样的通道堆叠在一个卷积层中，总体上形成一个 $ d + 1) $ 维数组。LCN 代表 CNN 的一种变体，其中存在局部连接但没有权重共享。

[第3页，第2段]
text<|/ref|>[[64, 168, 494, 236]]<|/det|>
我们的目标是在热力学比例极限下推导有效作用量，其中卷积通道数 $ N_{c} $ 和数据集大小 $ P $ 趋于无穷大，而它们的比值 $ \alpha_{c} = P / N_{c} $ 保持有限。我们通过计算两种架构在温度 $ T = 1 / \beta $ 下的配分函数来实现这一点，即：

[第3页，第3段]
equation<|/ref|>[[192, 247, 492, 275]]<|/det|>
$ Z = \int \mathrm{d}\mu (\theta)\exp \{-\beta \mathcal{L}(\theta)\} , \quad (1) $

[第3页，第4段]
text<|/ref|>[[64, 290, 494, 411]]<|/det|>
其中 $ \theta $ 表示网络权重的集合，$ \mathcal{L} $ 是 Methods 中定义的均方误差损失函数，符号 $ \mathrm{d}\mu (\theta) $ 表示对权重及其先验概率分布 $ \mu (\theta) $ 的集体积分。CNN 和 LCN 所实现函数的明确定义可在 Methods 中找到。正如我们在补充方法 1 和 $ 2^{15} $ 中明确展示的，我们发现 $ Z $ 可以近似为对半正定矩阵 $ Q $ 和 $ Q $ 的系综的积分：$ Z = \int \mathcal{D}Q\mathcal{D}Qe^{- N_{c}S(Q,Q) / 2} $，其中有效作用量由下式给出：

[第3页，第5段]
equation<|/ref|>[[142, 420, 492, 485]]<|/det|>
$ \begin{array}{rl} & S(Q,Q) = -\mathrm{Tr}Q\dot{Q} +\mathrm{Tr}\log (1 + Q)\\ & \qquad +\frac{\alpha_{c}}{\beta}\mathrm{Tr}\log \beta \left(\frac{1}{\beta} +K^{(\mathrm{R})}(X,X;Q)\right)\\ & \qquad +\frac{\alpha_{c}}{\beta}\mathbf{y}^{\top}\left(\frac{1}{\beta} +K^{(\mathrm{R})}(X,X;Q)\right)^{-1}\mathbf{y}. \end{array} \quad (2) $

[第3页，第6段]
text<|/ref|>[[64, 490, 494, 666]]<|/det|>
重整化核 $ K^{(\mathrm{R})}(X,X;Q) $ 是一个 $ P\times P $ 矩阵，它依赖于特定架构（CNN 或 LCN）、$ Q $ 中的序参量，并包含了作用量对训练集 $ X = \{x^{\mu}\}_{\mu = 1}^{P} $ 的依赖性。$ P $ 维向量 $ \mathbf{y} = \{\mathbf{y}^{\mu}\}_{\mu = 1}^{P} $ 包含所有训练集标签。前两项中的迹是对 $ |N_{0} / S|\times |N_{0} / S| $ 算子取的，其中 $ N_{0} $ 是输入维度，$ S $ 是卷积滤波器的步长，$ |x| $ 表示小于或等于 $ x $ 的最大整数（更多细节见 Methods 部分）。第三项中的迹以及与输出标签 $ \mathbf{y} $ 的标量积位于 $ P $ 维向量空间中。此处及下文中，我们将隐含所有核函数 $ K(\cdot ,\cdot ,\cdot) $ 和重整化核 $ K^{(\mathrm{R})}(\cdot ,\cdot ;Q) $ 均为两点函数，并使用以下简写符号来表示矩阵和向量：

[第3页，第7段]
equation<|/ref|>[[178, 677, 492, 730]]<|/det|>
$ \begin{array}{r}K(X,X):[K(X,X)]_{\mu \nu} = K(x^{\mu},x^{\nu}),\\ K(x^{\prime},X):[K(x^{\prime},X)]_{\mu} = K(x^{\prime},x^{\mu}). \end{array} \quad (3) $

[第3页，第8段]
text<|/ref|>[[64, 748, 494, 776]]<|/det|>
CNN 和 LCN 的重整化核表达式分别为：

[第3页，第9段]
equation<|/ref|>[[135, 788, 492, 880]]<|/det|>
$ \begin{array}{r}K_{\mathrm{CNN}}^{(\mathrm{R})}(x^{\mu},x^{\nu};Q) = \frac{1}{\lambda_1|N_0 / S|}\sum_{i = 1}^{|N_0 / S|}Q_{i}\mu^{i}(x^{\mu},x^{\nu}),\\ K_{\mathrm{LCN}}^{(\mathrm{R})}(x^{\mu},x^{\nu};Q) = \frac{1}{\lambda_1|N_0 / S|}\sum_{i = 1}^{|N_0 / S|}Q_{i}K^{i}(x^{\mu},x^{\nu}), \end{array} \quad (5) $

[第3页，第10段]
text<|/ref|>[[64, 897, 494, 938]]<|/det|>
其中 $ \lambda_{1} $ 是读出层的高斯先验。局部核 $ K_{\mu \nu}^{ij} \equiv K^{ij}(x^{\mu},x^{\nu}) $，因其依赖于遍历输入坐标的 $ i,j $ 索引而被称为局部核，由以下局部协方差矩阵 $ C_{\mu \nu}^{ij} $ 的元素给出：

[第3页，第11段]
text<|/ref|>[[513, 58, 761, 73]]<|/det|>
局部协方差矩阵 $ C_{\mu \nu}^{ij} $ 如下：

[第3页，第12段]
equation<|/ref|>[[620, 85, 940, 123]]<|/det|>
$ C_{\mu \nu}^{ij} = \frac{1}{\lambda_0M}\sum_{m = -[M / 2]}^{[M / 2]}x_{\mu}^{ij} + m^{x_{\nu}^{ij}} + m', \quad (7) $

[第3页，第13段]
equation<|/ref|>[[610, 141, 940, 203]]<|/det|>
$ \begin{array}{r}K_{\mu \nu}^{ij} = \int d t_{1}d t_{2}\mathcal{N}_{\epsilon}\left(\pmb {0},\tilde{C}_{\mu \nu}^{ij}\right)\sigma (t_{1})\sigma (t_{2}),\\ \tilde{C}_{\mu \nu}^{ij} = \left( \begin{array}{cc}C_{\mu \mu}^{ij} & C_{\mu \nu}^{ij}\\ C_{\mu \nu}^{ij} & C_{\nu \nu}^{ij} \end{array} \right). \end{array} \quad (8) $

[第3页，第14段]
text<|/ref|>[[513, 211, 941, 266]]<|/det|>
其中 $ \lambda_{0} $ 是隐藏层高斯先验，索引 $ m $ 遍历卷积掩码 $ M $，$ S $ 是步长。我们使用符号 $ \mathcal{N}_{\epsilon}(\pmb {0},\tilde{C}_{\mu \nu}^{ij}) $ 来表示向量 $ \pmb {t} = (t_{1},t_{2}) $ 的归一化高斯分布，其均值为零，协方差矩阵为 $ \tilde{C}_{\mu \nu}^{ij} $。

[第3页，第15段]
text<|/ref|>[[513, 266, 941, 316]]<|/det|>
这种局部核已在关于无限宽 CNN 高斯过程极限的开创性工作中被发现 $ ^{10,11} $。在无限多通道 $ N_{c} \gg P $ 的极限下，可以发现 CNN 和 LCN 按照以下平均核演化：

[第3页，第16段]
equation<|/ref|>[[640, 330, 940, 369]]<|/det|>
$ \bar{K}_{\mu \nu} = \frac{1}{\lambda_1|N_0 / S|}\sum_{i = 1}^{|N_0 / S|}K_{\mu \nu}^{ii}, \quad (9) $

[第3页，第17段]
text<|/ref|>[[513, 376, 941, 468]]<|/det|>
这定义了局部连接模型的无限宽性能。在我们的框架中，我们通过在 $ \alpha_{c} \to 0 $ 极限下求解矩阵 $ Q $ 的鞍点方程来恢复这一结果，其中可得 $ Q_{ij} = \delta_{ij} $，且只有局部核的对角分量对预测有贡献。注意，描述 FC 网络的有效作用量（最初在参考文献 38 中推导，并在 Methods 部分的 Eq. (21) 中报告）可通过在 Eq. (2) 中设置 $ S = N_{0} $ 来恢复。

[第3页，第18段]
text<|/ref|>[[513, 468, 941, 508]]<|/det|>
有效作用量的共享函数形式在所有三种架构（FC、LCN、CNN）中诱导了预测器对未见样本 $ x^{0}, y^{0}) $ 的相同高斯统计量，即：

[第3页，第19段]
equation<|/ref|>[[600, 520, 940, 590]]<|/det|>
$ \begin{array}{rl} & p(f^0 |X,y) = \mathcal{N}(\Gamma ,\sigma^2)\\ & \Gamma \equiv \left\langle f^0 \right\rangle = \left(K^{(\mathrm{R})}(x^0 ,X)\right)^T \left(\frac{1}{\beta} +K^{(\mathrm{R})}(X,X)\right)^{-1}\mathbf{y} \end{array} \quad (10) $

[第3页，第20段]
equation<|/ref|>[[600, 583, 940, 632]]<|/det|>
$ \begin{array}{rl} & \sigma^2 \equiv \left\langle (f^0)^2 \right\rangle - \left\langle f^0 \right\rangle^2 = K^{(\mathrm{R})}(x^0 ,x^0) + \\ & \qquad - \left(K^{(\mathrm{R})}(x^0 ,X)\right)^T \left(\frac{1}{\beta} +K^{(\mathrm{R})}(X,X)\right)^{-1}K^{(\mathrm{R})}(x^0 ,X), \end{array} \quad (11) $

[第3页，第21段]
text<|/ref|>[[513, 647, 941, 728]]<|/det|>
其中 $ f^0 = f_{\mathrm{HL}}(x^0) $ 是对应于输入 $ x^0 $ 的网络输出，尖括号表示对平衡吉布斯分布 $ p_{\beta}(\theta) = e^{-\beta \mathcal{L}(\theta)}\mu (\theta) / Z $ 的平均。该后验统计量的显式推导可在参考文献 38 中找到。同一新样本上的泛化误差由预测器的偏差和方差计算得出：

[第3页，第22段]
equation<|/ref|>[[592, 740, 910, 763]]<|/det|>
$ \left\langle \epsilon_{\mathrm{g}}(x^0 ,y^0) \right\rangle \stackrel {\mathrm{def}}{=} \left\langle (f^0 - y^0)^2 \right\rangle = (y^0 - \Gamma)^2 + \sigma^2. \quad (12) $

[第3页，第23段]
text<|/ref|>[[513, 795, 916, 825]]<|/det|>
在无限宽 1HL FC 网络中调整高斯先验等价于在比例机制下进行训练

[第3页，第24段]
text<|/ref|>[[513, 825, 941, 891]]<|/det|>
参考文献 38 中提出的理论框架（并在 Methods 部分简要总结）的一个物理推论源于对网络预测概率分布的考察，该分布由 Eq. (12) 给出，适用于具有以下重整化核的 FC 1HL 网络：

[第3页，第25段]
equation<|/ref|>[[657, 905, 940, 933]]<|/det|>
$ K_{\mathrm{FC}}^{(\mathrm{R})}(x,x^{\prime}) = \frac{Q}{\lambda_1} K(x,x^{\prime}) \quad (13) $

[第4页，第1段]
其中 $K(x, x')$ 是神经网络高斯过程（Neural Network Gaussian Process, NNGP）核，该核在贝叶斯无限宽度\textsuperscript{89}的背景下被发现，在全连接网络中扮演的角色与式 (8) 在局部连接网络中的角色相同。

[第4页，第2段]
首先，我们注意到重整化核 $K_{\text{FC}}^{(R)}$ 以与 NNGP 核在无限宽度极限下完全相同的方式进入预测器对未见测试元素的统计量，因此一旦求解了参数 $Q$ 的鞍点方程\textsuperscript{38}，它就完全决定了比例宽度下的泛化性能。

[第4页，第3段]
其次，我们观察到标量参数 $Q$ 总是与相应的高斯先验 $\lambda_1$ 以 $Q/\lambda_1$ 的组合形式出现，这意味着一旦在鞍点处求值，$Q$ 就只是高斯先验的一个依赖于数据的标量重整化。这意味着，一旦训练集大小和激活函数 $\sigma$ 固定，总是可以通过仔细微调相应无限宽度核中的高斯先验 $\lambda_1$ 来重新获得任何有限宽度网络的性能。因此，任何有限宽度单隐藏层全连接网络的泛化性能都受限于具有最优高斯先验选择的适当无限宽度核的泛化性能。注意，上述论证可以推广到深度 $L > 1$ 的网络，使用参考文献 38 中发现的重整化 NNGP 核的显式表达式，并注意到每一层 $\epsilon$ 处的 $Q_\epsilon$ 与同一层的高斯先验 $\lambda_\epsilon$ 一一对应。

[第4页，第4段]
无限宽度单隐藏层全连接网络似乎系统性地优于其有限宽度对应物——这一经验观察现在在此框架中找到了可能的解释——指向了一个有些令人失望的结论：在仅含全连接层的比例宽度网络中，特征学习并不是特别有效。

[第4页，第5段]
我们现在转向本手稿引言中提出的第二个问题。与仅含全连接层的深度网络中所发生的情况相反，具有卷积层的深度架构如何利用有限宽度区域进行高效的特征学习？鉴于之前的讨论，一种可能性是比例宽度下的卷积神经网络（CNN）能够以某种方式打破全连接深度网络中出现的无限宽度核的全局（平凡）重整化。这将是下一节中考虑的主题。

[第4页，第6段]
**比例宽度 CNN 中特征学习的简单机制：局部核重整化**

[第4页，第7段]
式 (5) 中展示的核重整化的精确形式就是我们定义的局部核重整化。

[第4页，第8段]
我们的主张是，矩阵 $Q$ 提供了对所考虑的 CNN 模型中特征学习的紧凑描述：训练期间优化的特征矩阵元素 $Q_{ij}$ 实际上与局部协方差矩阵的 $|N_0/S|$ 个块的成对组合一一对应，而这些块又由训练集元素 $x^\epsilon$ 的块定义。从式 (5) 出发，我们现在可以将矩阵 $Q$ 解释为一个特征性的、依赖于数据的矩阵，它告诉我们局部核的给定分量对重整化核 $K_{\text{CNN}}^{(R)}$ 的贡献程度。

[第4页，第9段]
注意，特征矩阵元素 $Q_{ij}$ 还具有自然的物理解释，即对应于块 $(i,j)$ 的读出向量关联的热平均。我们在补充方法 3\textsuperscript{48} 中明确展示了这一点。

[第4页，第10段]
该 CNN 模型在比例极限下发生的局部核重整化与相应的全连接单隐藏层网络中发生的平凡全局重整化完全不同。至此，人们可能会想，CNN 设计中的两个要素——局部连接和权重共享——是否都是观察局部核重整化现象所必需的。答案是肯定的：局部核重整化不会发生在仅具有局部连接的浅层网络中，正如我们在补充方法 1\textsuperscript{48} 中明确验证的那样。在那种情况下，只有局部核的对角分量进入有效作用量，如式 (6) 所示，因此网络对不同块之间的空间关联不敏感（另见表 1 以获取分析结果的总结）。

[第4页，第11段]
为了说明我们的有效理论所预测的局部核重整化机制可能的实际益处，考虑偏置主导区域是有用的，即式 (12) 中方差项收缩至零的极限（注意这可以通过对训练网络的大量不同实现进行集成而在实践中获得）。

[第4页，第12段]
让我们不失一般性地固定 $\lambda_0 = 1$（改变 $\lambda_0$ 相当于对训练模式的单个分量进行全局重缩放）。在偏置主导区域，具有由式 (9) 给出的 NNGP 核 $K$ 的无限宽度 CNN（对应于式 (5) 中 $Q = 1$ 的选择）的泛化损失通过寻找两个参数的最优值来获得下界：温度 $T$ 和最后一层上的高斯先验 $\lambda_1$。

[第4页，第13段]
使用 CIFAR10 数据集的一个子集进行监督学习问题的优化结果（详见补充方法 5\textsuperscript{48}）在图 2 中针对不同的训练集大小 $P$ 值（紫色点）显示。从最优无限宽度值 $T$ 和 $\lambda_1$ 出发，我们可以明确验证局部核重整化，即选择特征矩阵 $Q \neq 1$ 确实可以进一步提高泛化性能（参见图 2 中的橙色标记以及使用补充方法 5\textsuperscript{48} 中概述的数值协议找到的矩阵 $Q_{ij}$ 的两个示例）。用于执行这些实验的代码可在参考文献 49 中作为开源包获取。

[第4页，第14段]
值得强调的是，这只是一个原理验证性分析，我们目前正在致力于我们的有效理论与基于朗之万动力学的贝叶斯实验之间的精确比较，这与我们最近在参考文献 39 中对全连接架构所做的工作精神相同。我们使用具有二维卷积滤波器的贝叶斯 CNN 进行了初步分析，并在补充讨论\textsuperscript{48} 中报告了结果。

[第4页，第15段]
**全局和局部核重整化的经验证据**

[第4页，第16段]
从物理可观测量的测量中提取重整化核并不简单，目前我们无法在数值实验中直接获取它。不同架构中比例宽度下核重整化形式的一种间接实验蓝图由训练前后内部表示的相似性矩阵给出。我们将其定义为

[第5页，第1段]
对于全连接网络（FC）和卷积神经网络（CNN），可观测量为：

[第5页，第2段]
$ 
O_{\mu\nu} \equiv \frac{1}{N_1} \sum_{i=1}^{N_1} \sigma(h_i^{\mu}) \sigma(h_i^{\nu}),
 $

[第5页，第3段]
其中 $ N_1 $ 表示最后一层的神经元数量（对于卷积神经网络，$ N_1 = N_c |N_0/S| $）。注意，当激活函数为奇函数时，式（14）中的可观测值与激活后经验相关性一致。

[第5页，第4段]
我们可以通过取初始化时的相似矩阵（根据定义即 NNGP 核，至多相差高斯先验 $ \lambda_1 $）与训练后同一量之间的差值来追踪训练效果：$ \Delta K_{\mu\nu} \equiv \langle O_{\mu\nu} \rangle - K_{\mu\nu} $，其中平均是对权重的吉布斯系综进行的。我们对全连接网络和卷积神经网络解析计算了该可观测值，如补充方法 4 所示。两种情况的最终结果分别如下（在零温度下）：

[第5页，第5段]
$ 
\Delta K_{\mu\nu}^{\text{FC}} = -\frac{1}{N_1} \left[ K_{\mu\nu} - \frac{\lambda_1}{Q} y^{\mu} y^{\nu} \right];
 $

[第5页，第6段]
$ 
\Delta K_{\mu\nu}^{\text{CNN}} = -\frac{1}{\lambda_1 N_1 |N_0/S|} \sum_{ij, \Delta p=1}^{|N_0/S|} Q_{ij} P_{\mu\nu}^{ij}
 $

[第5页，第7段]
$ 
\times \left[ \left( K_{\text{CNN}}^{(R)} \right)^{-1} - \sum_{\epsilon=0}^{P} \left( K_{\text{CNN}}^{(R)} \right)^{-1} \left( K_{\text{CNN}}^{(R)} \right)^{-1} y^{\epsilon} y^{\mu} \right],
 $

[第5页，第8段]
其中 $ P_{\mu\nu}^{ij} \equiv \frac{1}{2} \sum_k \left[ K_{\mu k}^{ij} K_{\nu p}^{ij} + K_{\mu k}^{ij} K_{\nu p}^{ij} \right] $。现在让我们强调几个直接从这些公式得出的有趣物理含义，这些含义可以通过数值实验进行检验：

[第5页，第9段]
(i) 在固定 $ \alpha_1 = P/N_1 $ 的热力学极限 $ P, N_1 \to \infty $ 下，只要方括号中的项为 $ O(N_1) $ 量级，训练后与未训练相似矩阵之间的差值 $ \Delta K_{\mu\nu}^{\text{FC}} $ 收敛到零。这意味着在所考虑的比例极限区域中，训练对内部表示的影响仅是一个有限尺寸修正 $ O(1/N_1) $，训练后的相似矩阵非常接近其初始化时的值。特别地，我们预期在有限尺寸标度实验中，当保持比值 $ \alpha_1 = P/N_1 $ 固定而增大 $ P $ 和 $ N_1 $ 时，矩阵 $ \Delta K_{\mu\nu}^{\text{FC}} $ 各元素的经验分布将越来越集中在零附近；

[第5页，第10段]
(ii) 通过选择标签为 $ y^{\mu} = 0, 1 $ 的学习任务以及输入模式 $ x^{\mu} $，使得核 $ K_{\mu\nu} $ 的矩阵元素平均以零为中心，则在恒定 $ \alpha_1 $ 下增大 $ P $ 和 $ N_1 $ 进行实验时，块 $ \Delta K_{\mu\nu}^{\text{FC}}|_{11} $（对应于标签为一的训练模式子集）的矩阵元素分布应以 $ 1/N_1 $ 的速率向零漂移。有趣的是，矩阵 $ \Delta K_{\mu\nu}^{\text{FC}} $ 的其余块不应受此漂移影响；

[第5页，第11段]
(iii) 训练后与未训练卷积相似矩阵之间的差值 $ \Delta K_{\mu\nu}^{\text{CNN}} $ 表现出不同的行为，这是由于局部核重整化。例如，即使我们将分析限制在要点 (ii) 中概述的学习设置中，块 $ \Delta K_{\mu\nu}^{\text{CNN}}|_{01} $ 的元素在热力学比例极限下也不应完全收敛到零。事实上，直接的标度分析表明，方括号中项贡献在比例极限下不会消失：如果 $ P $ 与 $ N_1 $ 具有相同的数量级，则式（16）右侧 $ P $ 个 $ O(1) $ 核的双重求和按 $ P $ 标度，并补偿了消失的前因子 $ 1/N_1 $，导致有限的 $ \Delta K^{\text{CNN}} \propto O(P/N_1) $。

[第5页，第12段]
在图 3 中，我们展示了有限尺寸标度分析的结果，以检验上述预测，其中我们在由随机高斯模式组成的合成数据集上训练了单隐藏层全连接网络和卷积神经网络（一维卷积），该数据集的标签由线性教师函数给出，即 $ y = \frac{1}{2} [1 + \text{sign}(t \cdot x)] $，其中 $ t $ 是元素为单位值的 $ N_0 $ 维向量。总体而言，全连接网络内部表示的变化是有限尺寸效应这一事实得到了实验证实。另一方面，卷积神经网络的相同数值模拟清楚地识别出在热力学比例极限下也发生的内部表示的真实变化。我们注意到，全连接网络与卷积神经网络之间差异的这种清晰特征也源于我们选择在接近零温度下工作（此时架构可以精确拟合训练数据）。有限 $ T $ 下的方程更为复杂，在这种情况下测量全局和局部核重整化的间接效应更加困难。有趣的是，尽管我们的理论应仅在贝叶斯设置下有效，但事实证明它对不显式从吉布斯后验分布采样的学习算法也具有预测性：上述实验是使用梯度下降和所谓的 Adam 优化器进行的，代码可在参考文献 51 处获得。在补充方法 5 中，我们提供了这些实验的更多细节，以及 $ \alpha = 0.1, 10 $ 的额外结果（见补充图 1 和 2、补充表 1）。

[第5页，第13段]
**讨论**

[第5页，第14段]
在这项工作中，我们推导了单隐藏层卷积神经网络和局部卷积网络在比例极限下的有效作用量，并将这些结果与文献 38 中发现的全连接网络情况进行了广泛比较。

[第5页，第15段]
我们强调了三种不同架构在比例宽度下所经历的核重整化机制的显著差异，总结在表 1 中，并且我们提出了

[第6页，第1段]
a) $\Delta K_{\mu\nu}|_{01}$ 全连接网络箱线图

[第6页，第2段]
分布

[第6页，第3段]
b) $\Delta K_{\mu\nu}|_{11}$ 全连接网络箱线图

[第6页，第4段]
分布

[第6页，第5段]
c) $\Delta K_{\mu\nu}|_{01}$ 卷积网络箱线图

[第6页，第6段]
Nc 200 Nc 400

[第6页，第7段]
Nc 800 Nc 1600

[第6页，第8段]
分布

[第6页，第9段]
d) $\Delta K_{\mu\nu}|_{11}$ 卷积网络箱线图

[第6页，第10段]
Nc 200 Nc 400

[第6页，第11段]
Nc 800 Nc 1600

[第6页，第12段]
分布

[第6页，第13段]
图 3 | 预测全局和局部核重归一化对全连接网络和卷积网络内部表示的影响。有限尺寸标度分析。我们展示了为检验公式 (15)、(16) 关于训练前后相似矩阵之差 $\Delta K_{\mu\nu}$ 的标度预测而进行的数值实验结果。特别地，我们在由线性教师给出的随机高斯输入和零/一标签的学习任务上，训练具有单个隐藏全连接层/一维卷积层且使用 tanh 激活函数的架构（详见补充方法 5）。我们通过保持 $\alpha_1 = 1$ 并选择递增的 $P, N_1$ 值来进行有限尺寸标度分析。在图 (a) 中，我们观察到零一块 $\Delta K_{\mu\nu}^{\text{FC}}|_{01}$ 矩阵元素的经验分布的方差随着 $N_1$ 增大且 $\alpha_1$ 固定为一而收敛到零，这与公式 (15)（中）的预测一致。特别地，方差以 $1/N_1^2$ 的速度趋于零（下）。训练前后相似矩阵越来越相似这一事实，是卷积网络中可能发生的一种特征学习机制（局部核重归一化）的证据，而仅在具有 LC 或 FC 层的架构中不会发生。

[第6页，第14段]
我们结果的一个技术要求是高斯等价性，其非正式地通过一类一般的中心极限定理（如参考文献 38 中的 Breuer-Major 定理）得到证明。这表明输入维度 $N_0$ 应以与数据集大小 $P$ 相同的速率趋于无穷。如果是这种情况，正如参考文献 38 中那样，步长 $S$ 应选择为在 $N_0$ 中广泛标度，以便最终有效作用量依赖于有限数量的序参量。为完整起见，我们对高斯近似中涉及的概率分布进行了数值分析，结果展示在补充图 3 中。

[第6页，第15段]
我们对训练网络内部表示层面的全局和局部核重归一化效应进行了初步研究，结果与我们的预测一致。此外，我们还表明，局部核重归一化机制足以使卷积网络超越其最佳无限宽度核，通过找到近最优矩阵 $Q \neq 1$，在相同超参数选择下产生比无限宽度解 $Q_{\text{iw}} = 1$ 更低的泛化误差。

[第6页，第16段]
这里值得强调的是，上述观察结果完全没有排除全连接架构中其他可能的特征学习形式：(i) 无限宽度核的重归一化并非唯一可能的特征学习来源。高阶核在无限宽度极限下无关紧要，但可能在特征学习中发挥作用，特别是当考虑数据集大小 $P$ 大致按全连接深度神经网络的参数数量 $\sim L \times N^2$（$N_\ell = N \lor \ell$）标度的情况时。最近的工作 32 是一个显著例子，展示了全连接网络如何在特殊设置下学习卷积结构；(ii) 我们的结果适用于贝叶斯学习，即当网络权重从正则吉布斯系综中采样时。这仅在训练由马尔可夫链蒙特卡洛控制时才能获得。使用最先进优化器的实际学习算法可能表现不同，并可能激活替代形式的特征学习；(iii) 我们的分析适用于标准参数化设置，其中最后一层被归一化为 $1/\sqrt{N_1}$，我们无法描述可能在平均场区域 17 中发生的特征学习机制，其中最后一层被归一化为 $1/N_1$。尽管如此，还必须指出，参考文献 8,10,11,44,45,47 中提供的经验证据相当不利于这些形式的特征学习能在改善全连接网络泛化性能方面发挥重要作用这一事实。

[第6页，第17段]
最后，我们指出本工作的一些可能后续方向：(i) 将我们的框架扩展到 $L$ 个卷积层将会很有趣，遵循为全连接网络提出的相同策略

[第7页，第1段]
层\textsuperscript{38}；(ii) 我们当前的方法无法覆盖平均场（mean-field）区域，在该区域中，全连接网络（FC）和卷积神经网络（CNN）的特征学习机制可能会发生定量变化。我们认为\textsuperscript{36}中提出的形式体系可能更适合研究这种情况下的有限宽度效应；(iii) 我们正在编写一个详细的开放源代码数值程序，已在网上公开可用\textsuperscript{49}，以广泛检验我们有效理论对FC、LC和CNN的理论预测。这一步也将有助于指出当前框架的局限性。

[第7页，第2段]
方法
学习问题的设定及全连接网络结果的回顾
我们考虑一个监督回归问题，训练集为$  X = \{x^{\mu}\}_{\mu=1}^{P}  $，其中每个$  x^{\mu} \in \mathbb{R}^{N_0}  $，对应的标签为$  y = \{y^{\mu}\}_{\mu=1}^{P}  $，其中$  y^{\mu} \in \mathbb{R}  $。我们还将分析限制在二次损失函数$  \mathcal{L}  $上。对于由权重$  \theta = (W, \nu)  $参数化的、实现函数$  f_{\text{HL}}(x; \theta)  $的通用单隐藏层网络，我们将损失函数定义为：

[第7页，第3段]
$ 
\mathcal{L} = \frac{1}{2} \sum_{\mu=1}^{P} [y^{\mu} - f_{\text{HL}}(x^{\mu}; \theta)]^2.
 $ (17)

[第7页，第4段]
我们选择第一层和最后一层的权重，分别为$  W  $和$  \nu  $，使其具有高斯先验分布：

[第7页，第5段]
$ 
\mu(W) = \frac{e^{-\frac{\Lambda_0}{2} \|W\|^2}}{\mathcal{N}_W}, \quad \mu(\nu) = \frac{e^{-\frac{\Lambda_1}{2} \|\nu\|^2}}{\mathcal{N}_\nu},
 $ (18)

[第7页，第6段]
其中$  \|\cdot\|  $是标准Frobenius范数，常数$  \mathcal{N}_W  $和$  \mathcal{N}_\nu  $确保适当的归一化$  \int d\mu(W) = \int d\mu(\nu) = 1  $。参数$  \Lambda_0, \Lambda_1  $可以等价地视为每层权重上的高斯先验，或视为由温度$  T  $重新缩放的$  L^2  $正则化项。

[第7页，第7段]
具有一个FC隐藏层的神经网络形式上从第一层的预激活开始定义：

[第7页，第8段]
$ 
h_i(x) = \frac{1}{\sqrt{N_0}} \sum_{i_0=1}^{N_0} W_{i_0} x_{i_0} + b_i,
 $ (19)

[第7页，第9段]
其中$  b  $是第一层的偏置。由于我们关注的是回归问题，我们添加一个最后的读出层，并将单隐藏层FC网络实现的函数定义为：

[第7页，第10段]
$ 
f_{\text{FC}}(x) = \frac{1}{\sqrt{N_1}} \sum_{i_1=1}^{N_1} v_i \sigma \left[ h_i(x) \right],
 $ (20)

[第7页，第11段]
其中$  \sigma  $是非线性激活函数。在此设定下，当考虑与训练损失函数$  \mathcal{L}  $相关的、温度为$  T = 1/\beta  $的正则配分函数，以及在固定比率$  \alpha_1 = P/N_1  $下的热力学极限$  N_1, P \to \infty  $时，会出现一个有效作用量，我们能够将其约化为适合对两个标量序参量$  \{Q, \bar{Q}\}  $进行鞍点积分的形式，$  Z = \int dQ d\bar{Q} e^{-N_1 S_{\text{FC}}(Q, \bar{Q})/2}  $。对于奇激活函数的情况，作用量由下式给出\textsuperscript{38}：

[第7页，第12段]
$ 
\begin{align*}
S_{\text{FC}} &= -Q\bar{Q} + \log(1 + Q) \\
&\quad + \frac{\alpha_1}{\beta} \text{Tr} \log \beta \left( \frac{1}{\beta} + K^{(R)}(X, X; \bar{Q}) \right) \\
&\quad + \frac{\alpha_1}{\beta} y^T \left( \frac{1}{\beta} + K^{(R)}(X, X; \bar{Q}) \right)^{-1} y,
\end{align*}
 $ (21)

[第7页，第13段]
其中重整化核（renormalized kernel）$  K^{(R)}(X, X; \bar{Q})  $是式(13)中定义的$  P \times P  $矩阵。

[第7页，第14段]
如果$  \alpha_1 \to 0  $，式(21)中有效作用量的最小化是直接的，因为容易发现$  Q = 0, \bar{Q} = 1  $，并恢复众所周知的无限宽度极限NNGP核。在有限$  \alpha_1  $下，可以找到序参量的数据依赖解，这些解产生无限宽度核的重整化，如式(13)所示。

[第7页，第15段]
式(21)中提出的比例宽度下的有效作用量最早在参考文献32中针对深度线性网络推导得出。线性情况下配分函数的非渐近评估在参考文献33中针对单输出全连接网络以Meijer-G函数给出，在参考文献33中针对多输出FC网络和CNN给出。全局门控深度线性网络的有效作用量也已被推导\textsuperscript{44}。在参考文献38中，我们利用通过Breuer和Major\textsuperscript{59}的广义中心极限定理非正式地证明的高斯等价性\textsuperscript{54–58}，获得了具有通用激活函数的单FC隐藏层网络的有效作用量。$  L  $层的结果可以在某种程度上从以下观察中自举得到：在比例极限下描述浅层非线性网络和深层线性网络中信息流的随机过程与Student's $  t  $-过程\textsuperscript{60}相关（更详细的讨论另见\textsuperscript{38}）。近期工作考虑了师生场景下的比例设定，使用复制方法\textsuperscript{61,62}对数据分布进行平均，并且最近出现了一个在几乎比例极限下的首个初步严格结果\textsuperscript{63}，利用了插值方法\textsuperscript{64,65}。

[第7页，第16段]
具有局部连接的浅层架构：符号与定义
我们考虑具有一个隐藏卷积层或一个隐藏局部连接层、后接一个全连接读出层的网络。为简单起见，在本文中我们将分析限制在一维卷积，但该模型可以很容易地推广到$  d  $维卷积。在CNN中，隐藏层的预激活由下式给出：

[第7页，第17段]
$ 
h_i^a(x) = \frac{1}{\sqrt{M}} \sum_{m = -\lfloor M/2 \rfloor}^{\lfloor M/2 \rfloor} W_m^a x_{Si + m}.
 $ (22)

[第7页，第18段]
这里$  M  $是通道掩码的维度，$  S  $是步幅，索引$  i = 1, \ldots, \lfloor N_0/S \rfloor  $遍历输入坐标，索引$  a = 1, \ldots, N_c  $遍历通道，索引$  m  $在卷积滤波器的空间掩码中移动。为简单起见，我们在输入坐标上定义周期性边界条件（PBCs），并考虑$  M  $的奇数值。加上FC读出层后，CNN实现的函数由下式给出：

[第7页，第19段]
$ 
f_{\text{CNN}}(x) = \frac{1}{\sqrt{N_c |N_0/S|}} \sum_{i=1}^{N_0/S} \sum_{a=1}^{N_c} v_i^a \sigma \left[ h_i^a(x) \right],
 $ (23)

[第7页，第20段]
其中$  \sigma  $是奇激活函数，$  \nu  $是读出层的可学习权重。LCN通过在式(22)中的权重矩阵$  W_m^a  $上添加一个$  i  $（块）索引而获得，这意味着网络访问的每个块将有一组不同的权重。

[第7页，第21段]
报告摘要
有关研究设计的更多信息可在与本文链接的Nature Portfolio报告摘要中获取。

[第7页，第22段]
数据可用性
我们在所有实验中使用的CIFAR10\textsuperscript{66}和MNIST\textsuperscript{67}数据集可分别在网上公开获取，地址为https://www.cs.toronto.edu/~kriz/cifar.html和http://yann.lecun.com/exdb/mnist/。

[第7页，第23段]
代码可用性
用于复现我们贝叶斯网络实验并从我们的理论计算理论预测的Python包\textsuperscript{49}可在Zenodo上获取：https://zenodo.org/records/14216887。使用ADAM复现内部表示实验的代码——

[第8页，第1段]
参考文献

[第8页，第2段]
1. Goodfellow, I., Bengio, Y. & Courville, A. 深度学习 (MIT Press, 2016). http://www.deeplearningbook.org.
2. Bengio, Y., Courville, A. & Vincent, P. 表示学习：回顾与新视角。IEEE Trans. Pattern Anal. Mach. Intell. 35, 1798–1828 (2013).
3. Yu, D., Seltzer, M. L., Li, J., Huang, J.-T. & Seide, F. 深度神经网络中的特征学习——语音识别任务研究。arXiv preprint arXiv:1301.3605 (2013).
4. Ciceri, S. et al. 深度学习中类流形的反转动力学揭示了泛化背后的权衡。Nat. Mach. Intell. 6, 40–47 (2024).
5. Neal, R. M. in 神经网络贝叶斯学习 29-53 (Springer New York, New York, NY.), isbn: 978-1-4612-0745-0. https://doi.org/10.1007/978-1-4612-0745-0_2 (1996).
6. Williams, C. 用无限网络进行计算。In Mozer, M., Jordan, M. & Petsche, T. (eds.) 神经信息处理系统进展, vol. 9 (MIT Press, 1996). https://proceedings.neurips.cc/paper/1996/file/ae5e3ce40e0404a45ecacaaf05e5f735-Paper.pdf.
7. de G. Matthews, A. G., Hron, J., Rowland, M., Turner, R. E. & Ghahramani, Z. 宽深度神经网络中的高斯过程行为。In 国际学习表征会议 https://openreview.net/forum?id=H1-nGgWC- (2018).
8. Lee, J. et al. 深度神经网络作为高斯过程。In 国际学习表征会议 https://openreview.net/forum?id=B1EA-M-0Z (2018).
9. Garriga-Alonso, A., Rasmussen, C. E. & Aitchison, L. 深度卷积网络作为浅层高斯过程。In 国际学习表征会议 https://openreview.net/forum?id=Bklfsi0ckm (2019).
10. Novak, R. et al. 具有多通道的贝叶斯深度卷积网络是高斯过程。In 国际学习表征会议 https://openreview.net/forum?id=B1g30j0qF7 (2019).
11. Arora, S. et al. 关于无限宽神经网络的精确计算。In Wallach, H. et al. (eds.) 神经信息处理系统进展, vol. 32 (Curran Associates, Inc., 2019). https://proceedings.neurips.cc/paper_files/paper/2019/file/dbc4d84bfcfe2284ba11bffb853a8c4-Paper.pdf.
12. Jacot, A., Gabriel, F. & Hongler, C. 神经正切核：神经网络中的收敛与泛化。In Bengio, S. et al. (eds.) 神经信息处理系统进展, vol. 31 (Curran Associates, Inc., 2018). https://proceedings.neurips.cc/paper/2018/file/5a4be1fa34e62bb8a6ec6b9d12462f5a-Paper.pdf.
13. Chizat, L., Oyallon, E. & Bach, F. 关于可微编程中的惰性训练。In Wallach, H. et al. (eds.) 神经信息处理系统进展, vol. 32 (Curran Associates, Inc., 2019). https://proceedings.neurips.cc/paper/2019/file/ae614c557843b1df326cb29c57225459-Paper.pdf.
14. Lee, J. et al. 任意深度的宽神经网络在梯度下降下演化为线性模型。In Wallach, H. et al. (eds.) 神经信息处理系统进展, vol. 32 (Curran Associates, Inc., 2019). https://proceedings.neurips.cc/paper/2019/file/0d1a9651497a38d8b1c3871c84528bd4-Paper.pdf.
15. Aitchison, L. 为什么更大并不总是更好：论有限与无限神经网络。In Ill, H. D. & Singh, A. (eds.) 第37届国际机器学习会议论文集, vol. 119 of 机器学习研究论文集, 156–164 (PMLR, 2020). https://proceedings.mlr.press/v119/aitchison20a.html.
16. Favaro, S., Hanin, B., Marinucci, D., Nourdin, I. & Peccati, G. 深度神经网络中的定量中心极限定理。arXiv preprint arXiv:2307.06092 (2023).

[第8页，第3段]
17. Mei, S., Montanari, A. & Nguyen, P.-M. 两层神经网络景观的平均场视角。Proc. Natl Acad. Sci. 115, E7665–E7671 (2018).
18. Chizat, L. & Bach, F. 关于使用最优传输的过参数化模型梯度下降的全局收敛性。In Bengio, S. et al. (eds.) 神经信息处理系统进展, vol. 31 (Curran Associates, Inc., 2018). https://proceedings.neurips.cc/paper_files/paper/2018/file/a1afc58c6ca9540d057299ec3016d726-Paper.pdf.
19. Sirignano, J. & Spiliopoulos, K. 神经网络的平均场分析：大数定律。SIAM J. Appl. Math. 80, 725–752 (2020).
20. Rotskoff, G. & Vanden-Eijnden, E. 参数作为相互作用粒子：神经网络的长时间收敛与渐近误差缩放。In Bengio, S. et al. (eds.) 神经信息处理系统进展, vol. 31 (Curran Associates, Inc., 2018). https://proceedings.neurips.cc/paper_files/paper/2018/file/196f5641aa9dc87067da4ff90fd81e7b-Paper.pdf.
21. Yang, G. & Hu, E. J. 张量程序IV：无限宽神经网络中的特征学习。In Meila, M. & Zhang, T. (eds.) 第38届国际机器学习会议论文集, vol. 139 of 机器学习研究论文集, 11727–11737 (PMLR, 2021). https://proceedings.mlr.press/v139/yang21c.html.
22. Cagnetta, F., Favero, A. & Wyart, M. 宽卷积神经网络能学到什么？(2023). https://openreview.net/forum?id=m3QhpKNXU6-.
23. Favero, A., Cagnetta, F. & Wyart, M. 局部性在卷积教师-学生场景中击败维度灾难。In Beygelzimer, A., Dauphin, Y., Liang, P. & Vaughan, J. W. (eds.) 神经信息处理系统进展 https://openreview.net/forum?id=sBBnfOFtPc (2021).
24. Petrini, L., Cagnetta, F., Vanden-Eijnden, E. & Wyart, M. 学习稀疏特征可能导致神经网络中的过拟合。In Oh, A. H., Agarwal, A., Belgrave, D. & Cho, K. (eds.) 神经信息处理系统进展 https://openreview.net/forum?id=dZEZu7zxJBF (2022).
25. Zavatone-Veth, J. A. & Pehlevan, C. 有限贝叶斯神经网络的精确边缘先验分布。In Beygelzimer, A., Dauphin, Y., Liang, P. & Vaughan, J. W. (eds.) 神经信息处理系统进展 https://openreview.net/forum?id=MxE7xFzVON8 (2021).
26. Yang, A. X., Robeyns, M., Milsom, E., Schoots, N. & Aitchison, L. 深度神经网络中表示学习的理论给出了核方法的深度泛化 2108.13097 (2023).
27. Zavatone-Veth, J., Canatar, A., Ruben, B. & Pehlevan, C. 有限贝叶斯神经网络中表示学习的渐近性。In Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P. & Vaughan, J. W. (eds.) 神经信息处理系统进展, vol. 34, 24765–24777 (Curran Associates, Inc., 2021). https://proceedings.neurips.cc/paper/2021/file/cf9dc5e4e194fc21f397b4cac9cc3ae9-Paper.pdf.
28. Hanin, B. 随机全连接神经网络作为微扰可解层级 2204.01058 (2023).
29. Antognini, J. M. 神经网络高斯过程的有限尺寸修正 1908.10030 (2019).
30. Yaida, S. 有限宽度下的非高斯过程与神经网络。In Lu, J. & Ward, R. (eds.) 第一届数学与科学机器学习会议论文集, vol. 107 of 机器学习研究论文集, 165–192 (PMLR, 2020). https://proceedings.mlr.press/v107/yaida20a.html.
31. Roberts, D. A., Yaida, S. & Hanin, B. 深度学习理论原理 https://deeplearningtheory.com. arXiv: 2106.10165 [cs.LG] (Cambridge University Press, 2022).
32. Li, Q. & Sompolinsky, H. 深度线性神经网络的统计力学：反向传播核重整化。Phys. Rev. X 11, 031059 (2021).

[第9页，第1段]
33. Hanin, B. & Zlokapa, A. 深度线性网络的贝叶斯插值（Bayesian interpolation）。Proc. Natl Acad. Sci. 120, e2301345120 (2023)。
34. Li, Q. & Sompolinsky, H. 2024. 全局门控深度线性网络（Globally gated deep linear networks）。In Proc. 36th International Conference on Neural Information Processing Systems (NIPS ’22) 34789–34801 (Curran Associates Inc., 2024)。
35. Zavatone-Veth, J. A., Tong, W. L. & Pehlevan, C. 深度贝叶斯线性回归中随机特征与学习特征的对比（Contrasting random and learned features in deep Bayesian linear regression）。Phys. Rev. E 105, 064118 (2022)。
36. Seroussi, I., Naveh, G. & Ringel, Z. 某些卷积神经网络中特征学习的尺度分离与热力学描述（Separation of scales and a thermodynamic description of feature learning in some cnns）。Nat. Commun. 14, 908 (2023)。
37. Naveh, G. & Ringel, Z. 高斯过程的自洽理论捕捉有限卷积神经网络中的特征学习效应（A self consistent theory of gaussian processes captures feature learning effects in finite cnns）。In Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P. & Vaughan, J. W. (eds.) Advances in Neural Information Processing Systems, vol. 34, 21352–21364 (Curran Associates, Inc., 2021). https://proceedings.neurips.cc/paper/2021/file/b24d21019de5e59da180f166190f449a-Paper.pdf。
38. Pacelli, R. et al. 超越无限宽度极限的贝叶斯深度神经网络的统计力学框架（A statistical mechanics framework for bayesian deep neural networks beyond the infinite-width limit）。Nat. Mach. Intell. 5, 1497–1507 (2023)。
39. Baglioni, P. et al. 比例极限下全连接单隐藏层神经网络的贝叶斯有效作用量的预测能力（Predictive power of a bayesian effective action for fully connected one hidden layer neural networks in the proportional limit）。Phys. Rev. Lett. 133, 027301 (2024)。
40. Ingrosso, A., Pacelli, R., Rotondo, P. & Gerace, F. 比例极限下全连接网络中迁移学习的统计力学（Statistical mechanics of transfer learning in fully-connected networks in the proportional limit）。arXiv preprint arXiv:2407.07168 (2024)。
41. MacKay, D. J. C. 反向传播网络的实用贝叶斯框架（A Practical Bayesian Framework for Backpropagation Networks）。Neural Comput. 4, 448–472 (1992)。
42. Grant, E., Nestler, S., Šimšek, B. & Solla, S. A. 统计物理、贝叶斯推断与神经信息处理（Statistical physics, Bayesian inference, and neural information processing）。J. Stat. Mech Theory Exp. 2024, 104005 (2024)。
43. Williams, C. K. & Rasmussen, C. E. 机器学习的髙斯过程（Gaussian processes for machine learning），vol. 2 (MIT press Cambridge, MA, 2006)。
44. Lee, J. et al. 有限与无限神经网络：一项实证研究（Finite versus infinite neural networks: an empirical study）。In Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M. & Lin, H. (eds.) Advances in Neural Information Processing Systems, vol. 33, 15156–15172 (Curran Associates, Inc., 2020). https://proceedings.neurips.cc/paper/2020/file/ad086f59924fff0773f8d0ca22ea712-Paper.pdf。
45. Atanasov, A., Bordelon, B., Sainathan, S. & Pehlevan, C. 懒惰与丰富机制下网络方差受限行为的起始（The onset of variance-limited behavior for networks in the lazy and rich regimes）。In The Eleventh International Conference on Learning Representations (ICLR, 2023)。
46. Geiger, M., Petrini, L. & Wyart, M. 深度学习中的景观与训练机制（Landscape and training regimes in deep learning）。Phys. Rep. 924, 1–18 (2021)。
47. Geiger, M., Spigler, S., Jacot, A. & Wyart, M. 解耦深度神经网络中的特征训练与懒惰训练（Disentangling feature and lazy training in deep neural networks）。J. Stat. Mech.: Theory Exp. 2020, 113301 (2020)。
48. Aiudi, R. et al. “局部核重整化作为过参数化卷积神经网络中特征学习机制”的补充信息（Supplementary information for “local kernel renormalization as a mechanism for feature learning in overparametrized convolutional neural networks”）(2024)。
49. Pacelli, R. & Baglioni, P. deepbays。https://github.com/rpacelli/deepbays。
50. Kingma D. P. & Ba, J. Adam：一种随机优化方法（Adam: a method for stochastic optimization）。In 3rd International Conference on Learning Representations (ICLR, 2015)。
51. Aiudi, R. 内部表征的数值实验（Numerical experiments on internal representations）。https://github.com/ricaiu/PhD/tree/main/lkr。
52. Ingrosso, A. & Goldt, S. 神经网络中卷积结构的数据驱动涌现（Data-driven emergence of convolutional structure in neural networks）。Proc. Natl Acad. Sci. 119, e2201854119 (2022)。
53. Bassetti, F., Gherardi, M., Ingrosso, A., Pastore, M. & Rotondo, P. 具有多输出和卷积层的有限宽度贝叶斯深度线性网络中的特征学习（Feature learning in finite-width bayesian deep linear networks with multiple outputs and convolutional layers）2406.03260 (2024)。

[第9页，第2段]
54. Mei, S. & Montanari, A. 随机特征回归的泛化误差：精确渐近与双下降曲线（The generalization error of random features regression: Precise asymptotics and the double descent curve）。Commun. Pure Appl. Math. https://doi.org/10.1002/cpa.22008 (2019)。
55. Goldt, S. et al. 浅层神经网络学习中生成模型的高斯等价性（The Gaussian equivalence of generative models for learning with shallow neural networks）。In Proc. 2nd Mathematical and Scientific Machine Learning Conference 426–471 (PMLR, 2022)。
56. Gerace, F., Loureiro, B., Krzakala, F., Mézard, M. & Zdeborová, L. 随机特征学习与隐藏流形模型中的泛化误差（Generalisation error in learning with random features and the hidden manifold model）。J. Stat. Mech.: Theory Exp. 2021, 124013 (2021)。
57. Aguirre-López, F., Franz, S. & Pastore, M. 随机特征与多项式规则（Random features and polynomial rules）https://synthical.com/article/0a46daf2-150f-45d9-837f-6bb4ecf92e3d. Jan. arXiv: 2402.10164 [cond-mat.dis-nn]. (2024)。
58. Loureiro, B. et al. 基于师生模型的真实数据集通用特征映射的学习曲线（Learning curves of generic features maps for realistic datasets with a teacher-student model）。Adv. Neural Inf. Process. Syst. 34, 18137–18151 (2021)。
59. Breuer, P. & Major, P. 高斯场非线性泛函的中心极限定理（Central limit theorems for non-linear functionals of Gaussian fields）。J. Multivar. Anal. 13, 425–441 (1983)。
60. Shah, A., Wilson, A. & Ghahramani, Z. Student-t过程作为高斯过程的替代方案（Student-t Processes as Alternatives to Gaussian Processes）。In Kaski, S. & Corander, J. (eds.) Proceedings of the Seventeenth International Conference on Artificial Intelligence and Statistics, vol. 33 of Proceedings of Machine Learning Research, 877–885 (PMLR, Reykjavik, Iceland, 2014). https://proceedings.mlr.press/v33/shah14.html。
61. Cui, H., Krzakala, F. & Zdeborová, L. 广泛宽度深度随机网络的贝叶斯最优学习（Bayes-optimal learning of deep random networks of extensive-width）。Proceedings of the 40th International Conference on Machine Learning (2023)。
62. Schröder, D., Cui, H., Dmitriev, D. & Loureiro, B. 深度随机特征学习的确定性等价与误差普适性（Deterministic equivalent and error universality of deep random features learning）。J. Stat. Mech. Theory Exp. 2024, 104017 (2024)。
63. Camilli, F., Tieplova, D. & Barbier, J. 过参数化浅层神经网络用于监督学习的基本极限（Fundamental limits of overparametrized shallow neural networks for supervised learning）。arXiv preprint arXiv:2307.05635 (2023)。
64. Guerra, F. & Toninelli, F. L. 平均场自旋玻璃模型中的热力学极限（The thermodynamic limit in mean field spin glass models）。Commun. Math. Phys. 230, 71–79 (2002)。
65. Agliari, E., Alemanno, F., Barra, A. & Fachechi, A. 稠密联想神经网络的广义Guerra插值方案（Generalized guerra’s interpolation schemes for dense associative neural networks）。Neural Netw. 128, 254–267 (2020)。
66. Krizhevsky, A. & Hinton, G. 从微小图像中学习多层特征（Learning multiple layers of features from tiny images）。Tech. Rep. O, University of Toronto, Toronto, Ontario https://www.cs.toronto.edu/~kriz/learning-%20features-2009-TR.pdf (2009)。
67. Lecun, Y., Bottou, L., Bengio, Y. & Haffner, P. 应用于文档识别的基于梯度的学习（Gradient-based learning applied to document recognition）。Proc. IEEE 86, 2278–2324 (1998)。

[第9页，第3段]
致谢
R.B.、R.P. 和 P.R. 得到 #NEXTGENERATIONEU (NGEU) 的支持。R.B. 和 P.R. 由大学与研究部（MUR）、国家复苏与韧性计划（NRRP）项目 MNESYS (PE0000006)“研究健康与疾病中神经系统的多尺度集成方法”（DN. 1553 11.10.2022）资助。R.P. 由 MUR 项目 PRIN 2022HSKLK9 资助，P.B. 由 MUR 项目 PRIN PNRR P2022A889F 资助。作者感谢 F. Cagnetta 对本手稿初稿的反馈以及指出有趣的相关工作，感谢 G. Naveh、Z. Ringel 和 I. Seroussi 对参考文献 36、37 中结果的讨论与澄清，以及感谢 M. Gherardi 和 M. Pastore 的讨论。

[第9页，第4段]
作者贡献
P.R. 提出了原始想法。P.R.、R.A. 和 R.P. 在 A.V. 和 R.B. 的支持下完成了分析计算。数值实验、数据分析和数据可视化由 R.A. 完成。R.P. 和 P.B. 所有作者都参与了结果的讨论与解释以及手稿的撰写与编辑。R.A. 和 R.P. 对本工作贡献相同。

[第10页，第1段]
利益冲突
作者声明无利益冲突。

[第10页，第2段]
附加信息
补充信息 在线版本包含补充材料，可在 https://doi.org/10.1038/s41467-024-55229-3 获取。

[第10页，第3段]
通信和材料索取请联系 R. Pacelli。

[第10页，第4段]
同行评审信息 Nature Communications 感谢 Runtian Zhai 及其他匿名审稿人对本工作同行评审的贡献。同行评审文件可供查阅。

[第10页，第5段]
转载和许可信息可在 http://www.nature.com/reprints 获取。

[第10页，第6段]
出版商注 Springer Nature 对已出版地图中的管辖权主张和机构隶属关系保持中立。

[第10页，第7段]
开放获取 本文根据 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License 许可，允许任何非商业用途的共享、分发和以任何媒介或格式复制，前提是您给予原作者和来源适当的署名，提供 Creative Commons 许可的链接，并说明您是否修改了许可材料。根据本许可，您无权共享从本文或其部分衍生的改编材料。本文中的图片或其他第三方材料包含在文章的 Creative Commons 许可中，除非在材料的署名行中另有说明。如果材料未包含在文章的 Creative Commons 许可中，且您的预期用途不被法定法规允许或超出允许的使用范围，您需要直接从版权持有人处获得许可。要查看本许可的副本，请访问 http://creativecommons.org/licenses/by-nc-nd/4.0/。

[第10页，第8段]
© 作者 2025
