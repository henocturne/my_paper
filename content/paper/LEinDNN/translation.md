[第1页，第1段]
**深度神经网络的有限时间李雅普诺夫指数**

[第1页，第2段]
L. Storm，¹ H. Linander，² J. Bec，³，⁴ K. Gustavsson，¹ 和 B. Mehlig⁵

[第1页，第3段]
¹哥德堡大学物理系，41296 哥德堡，瑞典
²查尔姆斯理工大学与哥德堡大学数学科学系，哥德堡，瑞典
³MINES Paris，PSL 研究大学，CNRS，Cemef，瓦尔邦讷，F-06900，法国
⁴蔚蓝海岸大学，Inria，CNRS，Cemef，瓦尔邦讷，F-06900，法国

[第1页，第4段]
（2023年6月16日收到；2023年11月5日修订；2024年1月3日接受；2024年2月1日发表）

[第1页，第5段]
我们计算了微小输入扰动如何影响深度神经网络的输出，探索了深度前馈网络与动力系统之间的类比，其中局部扰动的增长或衰减由有限时间李雅普诺夫指数（finite-time Lyapunov exponents）表征。我们表明，最大指数在输入空间中形成几何结构，类似于动力系统中的相干结构（coherent structures）。大正指数的脊线将输入空间划分为网络关联到不同类别的不同区域。这些脊线可视化了深度网络在输入空间中构建的几何结构，揭示了其学习能力背后的基本机制。

[第1页，第6段]
DOI: 10.1103/PhysRevLett.132.057301

[第1页，第7段]
深度神经网络可以被训练来建模复杂的函数关系。此类神经网络的表达力——即展开复杂数据结构的能力——随着层数的增加呈指数增长 [1]。神经网络最近的突破性应用 [2] 使用了具有多层神经元的深度前馈布局 [3]。由于信号在层间传播时的乘性放大，这些网络难以训练，如果层数过多，会导致信号的幅度爆炸或消失。在无限宽层渐近极限下的数学分析揭示了深度网络如何仍能学习解决分类任务 [4–7]。最近的结果表明，有限宽度网络可能以不同方式学习 [8–10]。然而，目前尚不清楚此类网络何时以及如何利用其指数表达力来表示分类任务所需的数据特征，这种表示如何影响预测准确性和不确定性，以及它如何依赖于网络布局。

[第1页，第8段]
在这里，我们使用动力系统理论来回答这些问题。深度前馈网络 [图 1(a)] 是离散动力系统。输入 $ x^{(0)} $ 通过 $ x_i^{(\ell)} = g(\sum_{j=1}^{N_\ell} w_{ij}^{(\ell)} x_j^{(\ell-1)} - \theta_i^{(\ell)}) $ 迭代映射，其中 $ g(\cdot) $ 是非线性激活函数 [11]，层索引 $ \ell = 0, \ldots, L + 1 $ 扮演时间的角色，$ L $ 是隐藏层数，$ N_\ell $ 是第 $ \ell $ 层的神经元数，权重 $ w_{ij}^{(\ell)} $ 和阈值 $ \theta_i^{(\ell)} $ 是参数。

[第1页，第9段]
$ x^{(\ell)} $ 对输入 $ x^{(0)} = x $ 微小变化的敏感性对应于具有正最大李雅普诺夫指数 [12,13] $ \lim_{\ell \to \infty} \lambda_i^{(\ell)}(x) $ 的混沌系统中的指数增长扰动，增长率为 $ \lambda_i^{(\ell)}(x) = \ell^{-1} \log |\partial x^{(\ell)}| / |\partial x| $。后者被称为最大有限时间李雅普诺夫指数（FTLE）。

[第1页，第10段]
网络权重 $ w_{ij}^{(\ell)} $ 通常初始化为随机数，独立地服从均值为零、方差为 $ \sigma_\ell^2 $ 的高斯分布。在这种情况下，李雅普诺夫指数最初由随机矩阵的乘积决定，乘性遍历定理保证当 $ L \to \infty $ 时，$ \lambda_i^{(L)}(x) $ 收敛到一个与 $ x $ 无关的极限 [14]。在 $ N_\ell = N \to \infty $ 的极限下，可以得到 $ \lambda_i^{(L)} \sim \log(GN\sigma^2) $，这解释了为什么初始权重方差应选择为使 $ GN\sigma^2 = 1 $，因为此时信号既不收缩也不扩张 [15–17]，从而稳定学习的初始阶段（常数 $ G $ 取决于激活函数的选择 [15]）。

[第1页，第11段]
**图 1.** 使用全连接前馈网络进行分类。(a) 具有两个输入分量 $ x_1^{(0)} $ 和 $ x_2^{(0)} $、$ L $ 个隐藏层（每层五个神经元）以及一个输出 $ x^{(L+1)} $ 的布局。(b) 用于分类问题的输入平面（示意图），其圆形决策边界将目标为 $ t = +1 $ 的输入模式（空心绿色方块）与目标为 $ t = -1 $ 的输入模式（实心黑色方块）分开。

[第2页，第1段]
在极限 $  N \to \infty  $ 下，深度网络的隐藏权重在训练过程中几乎不变 [4,18,19]。相比之下，对于有限宽度，权重倾向于发生变化 [5]。网络输出如何响应权重的变化而变化，表明了网络是如何学习的。

[第2页，第2段]
为了理解训练后的网络如何表达分类所需的输入数据特征，我们探究网络输出如何依赖于微小的输入变化，这体现在训练网络的最大FTLE场 $  \lambda_1(x)  $ 对 $  x  $ 的依赖关系中。对于一个输入为二维 $  x  $ 的分类问题，将其分为两类，目标为 $  t(x) = \pm 1  $ [图 1(b)]，我们确定了当改变 $  N  $ 和 $  L  $ 时，最大FTLE的 $  x  $ 依赖性如何变化。对于窄网络，我们发现最大FTLE场在输入平面上形成脊线，非常类似于动力系统中的拉格朗日相干结构 [20–22]。这些脊线为学习过程提供了洞察，说明了网络如何学会通过输入模式跨决策边界的微小移动来使其输出发生数量级为一的变化。随着网络宽度的增加，这些脊线消失，暗示了一种不同的学习机制。对于更复杂的分类问题（MNIST [23] 和 CIFAR-10 [24]），我们表明输入空间中的FTLE结构解释了分类准确率和预测不确定性的变化。

[第2页，第3段]
**有限时间李雅普诺夫指数。**——图 1(a) 展示了一个全连接前馈网络，具有 $  L  $ 个隐藏层，$  N_0  $ 个输入分量，每个隐藏层 $  N  $ 个神经元，以及 $  N_{L+1} = 1  $ 个输出神经元。网络将每个输入 $  x^{(0)} = x  $ 映射到一个输出 $  x^{(L+1)}  $。通过改变权重和阈值来最小化输出误差 $  [x^{(L+1)} - t(x)]^2  $，使得网络对每个输入 $  x  $ 预测正确的目标 $  t(x)  $。$  x^{(\ell)}  $ 对微小变化 $  \delta x  $ 的敏感性由线性化确定，

[第2页，第4段]
$ 
\delta x^{(\ell)} = \mathbb{D}^{(\ell)} \mathbb{W}^{(\ell)} \cdots \mathbb{D}^{(2)} \mathbb{W}^{(2)} \mathbb{D}^{(1)} \mathbb{W}^{(1)} \delta x \equiv \mathbb{J}_{\ell} \delta x. \tag{1}
 $

[第2页，第5段]
这里，$  \mathbb{W}^{(\ell)}  $ 是元素为 $  w_{ij}^{(\ell)}  $ 的权重矩阵，$  \mathbb{D}^{(\ell)}  $ 是对角矩阵，其元素为 $  D_{ij}^{(\ell)} = g(b_{i}^{(\ell)}) \delta_{ij}  $，其中 $  b_{i}^{(\ell)} = \sum_{j=1}^{N_{\ell}} w_{ij}^{(\ell)} x_{j}^{(\ell-1)} - \theta_{i}^{(\ell)}  $ 且 $  g(b_{i}^{(\ell)}) = (d/db)g(b) |_{b=b_{i}^{(\ell)}}  $。雅可比矩阵 $  \mathbb{J}_{\ell}  $ 表征了 $  x  $ 的小扰动的增长或衰减 [12,13]。其最大奇异值 $  \Lambda_{1}^{(\ell)}(x)  $ 作为 $  \ell  $ 的函数呈指数增长或衰减，速率为 $  \lambda_{1}^{(\ell)}(x) \equiv \ell^{-1} \log \Lambda_{1}^{(\ell)}(x)  $。奇异值 $  \Lambda_{1}^{(\ell)}(x) > \Lambda_{2}^{(\ell)}(x) > \cdots  $ 是右柯西-格林张量 $  \mathbb{J}_{\ell}^{T}(x) \mathbb{J}_{\ell}(x)  $ 的非负特征值的平方根。$  \mathbb{J}_{\ell}^{T}(x) \mathbb{J}_{\ell}(x)  $ 的最大特征向量决定了最大拉伸的方向，即输出在哪个输入方向上变化最大。

[第2页，第6段]
FTLE和柯西-格林张量在固体力学中用于识别弹性变形模式 [25]，以及寻找塑性变形 [26] 和裂纹萌生 [27] 中的不稳定区域。更一般地，FTLE有助于表征复杂动力学对初始条件的敏感性 [28–31]。在流体力学中，它们解释了流体输运颗粒的排列 [32,33]，为流体元素随时间和空间的拉伸和旋转提供了宝贵的见解 [34]。FTLE使我们能够识别拉格朗日相干结构 [20–22]；这些流体速度结构有助于组织和理解复杂的时空流动模式 [35]。这些几何结构表现为大最大FTLE的脊线，与最大拉伸方向正交。

[第2页，第7段]
在将这些方法应用于神经网络时，应当认识到几个事实。首先，在深度神经网络中，权重逐层变化。因此，相应的动力系统不是自治的。其次，每层神经元数量 $  N_{\ell}  $ 可能作为 $  \ell  $ 的函数而变化，对应于变化的相空间维度。第三，神经网络权重是经过训练的。这限制了最大奇异值 $  \Lambda_{1}^{(L)}  $ 的指数增长，并导致FTLE $  \lambda_{1}^{(L)}(x)  $ 即使在 $  L  $ 很大的极限下也保持对 $  x  $ 的依赖（下文将更详细讨论）。第四，可以使用不同的激活函数，例如分段线性ReLU函数 [11] 或平滑的tanh函数 [15]。这里我们使用 $  g(b) = \tanh(b)  $，使得网络映射连续可微，就像发现和分析拉格朗日相干结构的动力系统一样。

[第2页，第8段]
**二维数据集。**——为了说明最大FTLE形成的几何结构，我们首先考虑一个玩具问题。数据集 [图 1(b)] 包含 $  4 \times 10^4  $ 个输入模式，其中90%用于训练，其余用于测试。我们通过随机梯度下降在此数据集上训练全连接前馈网络，最小化输出误差 $  [x^{(L+1)} - t(x)]^2  $。通过这种方式，我们获得了至少98%的分类准确率。我们使用了不同的布局，改变了层数和每层隐藏神经元数。权重初始化为独立的零均值高斯随机数，方差为 $  \sigma_{\ell}^2 \sim N_{\ell}^{-1}  $。阈值初始化为零（详见补充材料 [36]）。训练后，我们根据式 (1) 计算了第 $  L  $ 层的最大FTLE及相关的拉伸方向，如文献 [38,39] 所述。

[第2页，第9段]
结果总结在图 2 中，显示了不同布局的训练网络的最大FTLE场。我们看到，大正 $  \lambda_{1}^{(L)}(x)  $ 的脊线与两类之间的决策边界对齐 [图 1(b)]。网络通过将输入分组到 $  t = \pm 1  $ 的两个不同吸引域来学习，这两个吸引域由正 $  \lambda_{1}^{(L)}(x)  $ 的脊线分隔。输入跨决策边界的微小移动导致输出的实质性变化。换句话说，大的最大FTLE量化了网络在脊线附近的指数表达性。这与以下观察一致：输出是

[第3页，第1段]
对决策边界附近的权重变化尤为敏感 [8]。当 $N$ 较小且 $L$ 较大时，这些脊线最为显著。随着 $L$ 增大，脊线与背景之间的对比度增加，这量化了深度网络的指数表达能力 [1]。对于更大的 $L$，网络能够分辨更小的输入距离 $\delta x$，因为奇异值会逐层指数级增大或减小。

[第3页，第2段]
大最大 FTLE 的脊线是拉格朗日相干结构（Lagrangian coherent structures），因为对于较大的 $L$，最大拉伸方向（图 2 中的实线）变得与脊线正交。这表明深度神经网络的 FTLE 脊线与拉格朗日相干结构之间存在严格的类比关系。

[第3页，第3段]
随着每层隐藏神经元数量 $N$ 的增加，这些脊线逐渐消失，因为在固定 $L$ 且 $N \to \infty$ 时，$J_L(x)$ 的最大奇异值趋近于一个与 $x$ 无关的确定极限。但在这种情况下，如果没有指示决策边界的脊线，网络如何区分具有不同目标的输入？一种可能性是，大量隐藏神经元使网络能够将输入嵌入到一个高维空间中，借助万能近似定理（universal approximation theorem）[40] 在该空间中将其分开。在这种情况下，仅训练输出权重（和阈值）就足够了，如图 3(a) 所示。随机隐藏权重下的分类误差大于完全训练网络的分类误差并不令人意外，因为当模式数量超过嵌入维度的两倍时，不同的随机嵌入具有不同的分类误差 [11,41]。总之，大 $N$ 网络可以用随机隐藏权重进行分类。这意味着隐藏权重在训练过程中无需改变，正如使用神经正切核（neural-tangent kernel）的核回归一样 [4,18]。换言之，该区域中的学习是惰性的（lazy）[19]。

[第3页，第4段]
图 3(b) 更详细地描述了图 2 中两种学习区域之间的交叉过渡。图中展示了决策边界上最大 FTLE 的局部平均值 $\langle \lambda_L^{(L)}(x) \rangle_d$ 以及输入平面中心处的局部平均值 $\langle \lambda_L^{(L)}(x) \rangle_c$，作为 $N$ 的函数（针对不同的 $L$ 值）。这些结果是通过训练 200 个 epoch 以达到分类准确率 $\geq 99\%$ 获得的。尽管进一步训练后最大 FTLE 场的细节会发生变化，图 3(b) 仍使我们能够就这一转变得出以下结论。第一，随着 $L$ 增大，$L\langle \lambda_L^{(L)}(x) \rangle_d$ 趋于一个与 $N$ 无关的常数，$L\langle \lambda_L^{(L)}(x) \rangle_d \to C_d$。这种饱和归因于训练：网络学会产生量级为 $\delta x^{(L+1)} \sim 1$ 的输出差异，并在决策边界上相邻输入之间的平均距离 $|\delta x^{(0)}|$ 的尺度上分辨输入差异 $\delta x$。第二，图 3(b) 中所示的数据表明，对于足够大的 $L$，$L\langle \lambda_L^{(L)}(x) \rangle_c \approx -C_c L + \log N$。第三，当背景达到脊线水平 $\langle \lambda_L^{(L)}(x) \rangle_c \approx \langle \lambda_L^{(L)}(x) \rangle_d$ 时，随着 $N$ 的增加，脊线与背景之间的对比度消失。此时，学习机制从通过脊线学习转变为随机嵌入。在图 3(b) 中，这大约发生在 $N_c \sim \exp(C_d + C_c L)$ 处。虽然该定律的精确形式可能取决于训练细节，但一般性结论是 $N_c$ 非常敏感地依赖于 $L$，因为该关系的 $N$ 依赖性是对数形式的，正如上文引用的李雅普诺夫指数的 $N \to \infty$ 结果一样。我们指出，上述讨论的 $L$ 标度关系意味着对于大 $L$，$\lambda_L^{(L)}(x)$ 仍然依赖于 $x$。

[第4页，第1段]
人们可能会好奇图2中的FTLE场如何依赖于初始权重方差$\sigma^2$。对于$GN\sigma^2 < 1$，FTLEs最初平均为负值。这意味着初始训练的减慢（梯度消失问题）。为了看到这一点，考虑深度神经网络的基本前向-后向二分法[11]：随机梯度算法中的权重更新由$\delta w_{mn}^{(\ell)} \propto \Delta_{mn}^{(\ell)} x_n^{(\ell-1)}$给出，其中

[第4页，第2段]
$$[\Delta^{(\ell)}]^T = [\Delta^{(L)}]^T [\mathbb{D}^{(L)}] \mathbb{W}^{(L)} \cdots [\mathbb{D}^{(\ell+1)}] \mathbb{W}^{(\ell+1)} [\mathbb{D}^{(\ell)}], \quad (2)$$

[第4页，第3段]
且$\Delta_j^{(L)} = g'(b^{(L+1)})[x^{(L+1)} - t(x)]g'(b_j^{(L)})w_j^{(L+1)}$。从公式(2)可以得出，负的FTLEs导致小的权重增量$\delta w_{mn}^{(\ell)}$。相反，当最大FTLE为正且过大时，权重快速增长，导致训练不稳定。

[第4页，第4段]
值得注意的是，训练具有自组织效应。训练后，最大FTLE分布变得独立于初始$\sigma^2$，前提是初始最大FTLE不太大（[36]中的图S1）。特别是对于足够小的$N$，分布集中在零附近。这可以通过网络通过在输入空间中创建最大FTLE脊来学习这一事实来解释：为了适应正的和负的$\lambda_1^{(L)}(x)$，分布必须以零为中心，从而缓解不稳定梯度问题。我们注意到，随着进一步训练，分布的形状，特别是尾部，继续演变。

[第4页，第5段]
**MNIST数据集。**—该数据集由60 000张手写数字0到9的图像组成。每张灰度图像有$28 \times 28$像素，并经过预处理以促进机器学习[23]。深度神经网络可以在分类此数据时达到高精度，在10 000个数字的测试集上准确率高达99.77%[42]。

[第4页，第6段]
我们为这个数据集确定了一个网络的最大FTLE场，该网络有$L = 16$个隐藏层，每层包含$N = 20$个神经元，以及一个具有十个输出的标准softmax层[11]。为了可视化$28^2$维输入空间中的几何结构，我们将其投影到二维如下[43]。我们在完全训练的网络中添加了一个具有两个神经元的瓶颈层，就在softmax输出层之前。我们仅重新训练这个额外层和输出层的权重和阈值，保持所有其他隐藏神经元不变。两个瓶颈神经元的局部场$b_1$和$b_2$是图4(a)中显示的二维表示的坐标。我们看到输入数据分成十个不同的簇，对应于十个数字。这些簇中心的最大FTLEs非常小甚至为负，表明输出对小的输入变化不敏感。这些区域由具有显著较大正FTLEs的区域 delineated [见面板(a)中的$3 \times$放大]。图2让我们预期具有大$\lambda_1^{(L)}(x)$的模式位于高维输入空间中的决策边界附近。这通过$\lambda_1^{(L)}(x)$与分类误差和预测不确定性之间的强相关性得到验证。图4(b)显示，对于具有较大$\lambda_1^{(L)}(x)$的输入$x$，测试集上的分类误差更大，并且$\lambda_1^{(L)}(x)$的大值与高预测不确定性相关，通过后验预测分布的熵$H$测量[44]。对于softmax输出，其中$x_i^{(L+1)}$可以解释为概率，$H = -\sum_i \langle x_i^{(L+1)} \rangle \log \langle x_i^{(L+1)} \rangle$，其中$\langle \cdot \rangle$表示对具有相同布局但不同权重初始化的网络集合的平均[45,46]。这些观察确认最大FTLEs的脊在输入空间中定位决策边界。类似的结论适用于其他架构（[36]中的图S2），以及更复杂的CIFAR-10数据集（图S3）。

[第4页，第7段]
图4(a)还显示了沿对抗攻击生成的路径的$\lambda_1^{(L)}(x)$。攻击从对应于数字9的簇内的样本开始，旨在通过向输入数据[47]向类4做小扰动，将其转换为数字4。我们看到最大FTLE最初很小，然后随着路径接近决策边界而增加，最终再次减少。这

[第5页，第1段]
这表明，首先，我们关于大最大FTLE与决策边界之间相关性的结论，可推广到MNIST训练集的邻域，这些邻域包含网络在训练期间未曾遇到的模式。其次，最大拉伸方向与对抗攻击在输入空间中找到的方向相关（图S4 [36]）。第三，由于在高维输入空间中难以定位FTLE脊，我们通过FTLE分布的均值和标准差来刻画两种学习机制之间的转变。图4(c)显示，随着$N$增大，均值变为正且方差趋于零，从而导致随机嵌入学习的均匀FTLE场特征。

[第5页，第2段]
**结论。**——对于在不同分类问题上训练的深度神经网络，我们探索了输入空间中有限时间李雅普诺夫指数的几何结构。在流体力学中，此类拉格朗日相干结构表现为大指数的脊，并被非常成功地用于组织复杂时空流动模式的相空间。深度神经网络也是如此：FTLE脊将输入空间划分为与不同类别相关的不同区域。我们的分析表明网络如何利用其指数表达性来形成这些脊。它们的锐度决定了一个人远离脊时分类误差和预测不确定性下降的速度。随着网络宽度增加，脊与背景之间的对比消失，导致一种不同的学习机制——随机嵌入，在分类误差和预测不确定性方面存在定性差异。向这种懒惰学习机制[4,18,19]的转变发生在非常宽的网络中，宽度为$\sim \exp(L)$。这种转变可能解释了为什么更宽的网络对对抗攻击更具鲁棒性[47]：脊对于表示相关数据结构的 importance 越小，实现对抗攻击就越困难。这里提出的几何方法可能扩展到其他网络架构，如resnets [48]或transformers [49]，并可能有助于可视化和理解使此类神经网络能够学习的机制，但这仍是未来的问题。

[第5页，第3段]
我们感谢A. Dubey和J. Meibohm关于具有随机权重的神经网络的FTLE分布的讨论。L. S. 得到了Knut和Alice Wallenberg（KAW）基金会（编号2019.0079）和Vetenskapsrådet（VR）编号2021-4452的资助。J. B. 得到了UCA-JEDI未来投资（资助编号ANR-15-IDEX-01）的支持。H. L. 得到了KAW基金会的资助。K. G. 得到了VR资助编号2018-03974的支持，B. M. 得到了VR资助编号2021-4452的支持。本项目的部分数值计算是在瑞典国家计算基础设施（SNIC）提供的资源上进行的。

[第5页，第4段]
[1] B. Poole, S. Lahiri, M. Raghu, J. Sohl-Dickstein, and S. Ganguli, Exponential expressivity in deep neural networks through transient chaos, Adv. Neural Inf. Process. Syst. 29, 3360 (2016), https://proceedings.neurips.cc/paper_files/paper/2016/file/148510031349642de5ca0c544f3b2ef-Paper.pdf.

[第5页，第5段]
[2] J. Jumper et al., Highly accurate protein structure prediction with AlphaFold, Nature (London) 596, 583 (2021).

[第5页，第6段]
[3] M. Tan and Q. Le, Efficientnet: Rethinking model scaling for convolutional neural networks, in *International Conference on Machine Learning* (PMLR, Cambridge, 2019), pp. 6105–6114.

[第5页，第7段]
[4] A. Jacot, F. Gabriel, and C. Hongler, Neural tangent kernel: Convergence and generalization in neural networks, Adv. Neural Inf. Process. Syst. 31, 8580 (2018), https://proceedings.neurips.cc/paper_files/paper/2018/file/5a4be1fa34e62bb8a6ec6b91d2462f5a-Paper.pdf.

[第5页，第8段]
[5] M. Geiger, L. Petrini, and M. Wyart, Landscape and training regimes in deep learning, Phys. Rep. 924, 1 (2021).

[第5页，第9段]
[6] P. M. Nguyen and H. T. Pham, A rigorous framework for the mean field limit of multilayer neural networks, arXiv:2001.11443.

[第5页，第10段]
[7] I. Seroussi, G. Naveh, and R. Zohar, Separation of scales and a thermodynamic description of feature learning in some CNNs, Nat. Commun. 14, 908 (2023).

[第5页，第11段]
[8] A. Baratin, T. George, C. Laurent, R. D. Hjelm, G. Lajoie, P. Vincent, and S. Lacoste-Julien, Implicit regularization via neural feature alignment, in *International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第12段]
[9] J. Paccolat, L. Petrini, M. Geiger, K. Tyloo, and M. Wyart, Geometric compression of invariant manifolds in neural networks, J. Stat. Mech. (2021) 044001.

[第5页，第13段]
[10] R. Pacelli, S. Ariosto, M. Pastore, F. Ginelli, M. Gherardi, and P. Rotondo, A statistical mechanics framework for Bayesian deep neural networks beyond the infinite-width limit, Nat. Mach. Intell. 5, 1497 (2023).

[第5页，第14段]
[11] B. Mehlig, *Machine Learning with Neural Networks: An Introduction for Scientists and Engineers* (Cambridge University Press, Cambridge, England, 2021).

[第5页，第15段]
[12] E. Ott, *Chaos in Dynamical Systems*, 2nd ed. (Cambridge University Press, Cambridge, England, 2002).

[第5页，第16段]
[13] P. Cvitanović, R. Artuso, R. Mainieri, G. Tanner, and G. Vattay, *Chaos: Classical and Quantum* (Niels Bohr Institute, Copenhagen, 2020).

[第5页，第17段]
[14] A. Crisanti, A. Vulpiani, and G. Paladin, *Products of Random Matrices in Statistical Physics* (Springer, Berlin, 1993).

[第5页，第18段]
[15] J. Pennington, S. Schoenholz, and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: Theory and practice, Adv. Neural Inf. Process. Syst. 30, 4785 (2017), https://proceedings.neurips.cc/paper_files/paper/2017/file/d9fc0cdb67638d50f411432d0d41d0ba-Paper.pdf.

[第5页，第19段]
[16] I. Sutskever, J. Martens, G. Dahl, and G. E. Hinton, On the importance of initialization and momentum in deep learning, in *Proceedings of the 30th International Conference on Machine Learning—Volume 28* (PMLR, Cambridge, 2013), pp. III–1139–III–1147.

[第5页，第20段]
[17] X. Glorot and Y. Bengio, Understanding the difficulty of training deep feedforward neural networks, in *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第21段]
[18] A. Baratin, T. George, C. Laurent, R. D. Hjelm, G. Lajoie, P. Vincent, and S. Lacoste-Julien, Implicit regularization via neural feature alignment, in *International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第22段]
[19] J. Paccolat, L. Petrini, M. Geiger, K. Tyloo, and M. Wyart, Geometric compression of invariant manifolds in neural networks, J. Stat. Mech. (2021) 044001.

[第5页，第23段]
[20] R. Pacelli, S. Ariosto, M. Pastore, F. Ginelli, M. Gherardi, and P. Rotondo, A statistical mechanics framework for Bayesian deep neural networks beyond the infinite-width limit, Nat. Mach. Intell. 5, 1497 (2023).

[第5页，第24段]
[21] B. Mehlig, *Machine Learning with Neural Networks: An Introduction for Scientists and Engineers* (Cambridge University Press, Cambridge, England, 2021).

[第5页，第25段]
[22] E. Ott, *Chaos in Dynamical Systems*, 2nd ed. (Cambridge University Press, Cambridge, England, 2002).

[第5页，第26段]
[23] P. Cvitanović, R. Artuso, R. Mainieri, G. Tanner, and G. Vattay, *Chaos: Classical and Quantum* (Niels Bohr Institute, Copenhagen, 2020).

[第5页，第27段]
[24] A. Crisanti, A. Vulpiani, and G. Paladin, *Products of Random Matrices in Statistical Physics* (Springer, Berlin, 1993).

[第5页，第28段]
[25] J. Pennington, S. Schoenholz, and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: Theory and practice, Adv. Neural Inf. Process. Syst. 30, 4785 (2017), https://proceedings.neurips.cc/paper_files/paper/2017/file/d9fc0cdb67638d50f411432d0d41d0ba-Paper.pdf.

[第5页，第29段]
[26] I. Sutskever, J. Martens, G. Dahl, and G. E. Hinton, On the importance of initialization and momentum in deep learning, in *Proceedings of the 30th International Conference on Machine Learning—Volume 28* (PMLR, Cambridge, 2013), pp. III–1139–III–1147.

[第5页，第30段]
[27] X. Glorot and Y. Bengio, Understanding the difficulty of training deep feedforward neural networks, in *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第31段]
[28] A. Baratin, T. George, C. Laurent, R. D. Hjelm, G. Lajoie, P. Vincent, and S. Lacoste-Julien, Implicit regularization via neural feature alignment, in *International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第32段]
[29] J. Paccolat, L. Petrini, M. Geiger, K. Tyloo, and M. Wyart, Geometric compression of invariant manifolds in neural networks, J. Stat. Mech. (2021) 044001.

[第5页，第33段]
[30] R. Pacelli, S. Ariosto, M. Pastore, F. Ginelli, M. Gherardi, and P. Rotondo, A statistical mechanics framework for Bayesian deep neural networks beyond the infinite-width limit, Nat. Mach. Intell. 5, 1497 (2023).

[第5页，第34段]
[31] B. Mehlig, *Machine Learning with Neural Networks: An Introduction for Scientists and Engineers* (Cambridge University Press, Cambridge, England, 2021).

[第5页，第35段]
[32] E. Ott, *Chaos in Dynamical Systems*, 2nd ed. (Cambridge University Press, Cambridge, England, 2002).

[第5页，第36段]
[33] P. Cvitanović, R. Artuso, R. Mainieri, G. Tanner, and G. Vattay, *Chaos: Classical and Quantum* (Niels Bohr Institute, Copenhagen, 2020).

[第5页，第37段]
[34] A. Crisanti, A. Vulpiani, and G. Paladin, *Products of Random Matrices in Statistical Physics* (Springer, Berlin, 1993).

[第5页，第38段]
[35] J. Pennington, S. Schoenholz, and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: Theory and practice, Adv. Neural Inf. Process. Syst. 30, 4785 (2017), https://proceedings.neurips.cc/paper_files/paper/2017/file/d9fc0cdb67638d50f411432d0d41d0ba-Paper.pdf.

[第5页，第39段]
[36] I. Sutskever, J. Martens, G. Dahl, and G. E. Hinton, On the importance of initialization and momentum in deep learning, in *Proceedings of the 30th International Conference on Machine Learning—Volume 28* (PMLR, Cambridge, 2013), pp. III–1139–III–1147.

[第5页，第40段]
[37] X. Glorot and Y. Bengio, Understanding the difficulty of training deep feedforward neural networks, in *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第41段]
[38] A. Baratin, T. George, C. Laurent, R. D. Hjelm, G. Lajoie, P. Vincent, and S. Lacoste-Julien, Implicit regularization via neural feature alignment, in *International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第42段]
[39] J. Paccolat, L. Petrini, M. Geiger, K. Tyloo, and M. Wyart, Geometric compression of invariant manifolds in neural networks, J. Stat. Mech. (2021) 044001.

[第5页，第43段]
[40] R. Pacelli, S. Ariosto, M. Pastore, F. Ginelli, M. Gherardi, and P. Rotondo, A statistical mechanics framework for Bayesian deep neural networks beyond the infinite-width limit, Nat. Mach. Intell. 5, 1497 (2023).

[第5页，第44段]
[41] B. Mehlig, *Machine Learning with Neural Networks: An Introduction for Scientists and Engineers* (Cambridge University Press, Cambridge, England, 2021).

[第5页，第45段]
[42] E. Ott, *Chaos in Dynamical Systems*, 2nd ed. (Cambridge University Press, Cambridge, England, 2002).

[第5页，第46段]
[43] P. Cvitanović, R. Artuso, R. Mainieri, G. Tanner, and G. Vattay, *Chaos: Classical and Quantum* (Niels Bohr Institute, Copenhagen, 2020).

[第5页，第47段]
[44] A. Crisanti, A. Vulpiani, and G. Paladin, *Products of Random Matrices in Statistical Physics* (Springer, Berlin, 1993).

[第5页，第48段]
[45] J. Pennington, S. Schoenholz, and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: Theory and practice, Adv. Neural Inf. Process. Syst. 30, 4785 (2017), https://proceedings.neurips.cc/paper_files/paper/2017/file/d9fc0cdb67638d50f411432d0d41d0ba-Paper.pdf.

[第5页，第49段]
[46] I. Sutskever, J. Martens, G. Dahl, and G. E. Hinton, On the importance of initialization and momentum in deep learning, in *Proceedings of the 30th International Conference on Machine Learning—Volume 28* (PMLR, Cambridge, 2013), pp. III–1139–III–1147.

[第5页，第50段]
[47] X. Glorot and Y. Bengio, Understanding the difficulty of training deep feedforward neural networks, in *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第51段]
[48] A. Baratin, T. George, C. Laurent, R. D. Hjelm, G. Lajoie, P. Vincent, and S. Lacoste-Julien, Implicit regularization via neural feature alignment, in *International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第52段]
[49] J. Paccolat, L. Petrini, M. Geiger, K. Tyloo, and M. Wyart, Geometric compression of invariant manifolds in neural networks, J. Stat. Mech. (2021) 044001.

[第5页，第53段]
[50] R. Pacelli, S. Ariosto, M. Pastore, F. Ginelli, M. Gherardi, and P. Rotondo, A statistical mechanics framework for Bayesian deep neural networks beyond the infinite-width limit, Nat. Mach. Intell. 5, 1497 (2023).

[第5页，第54段]
[51] B. Mehlig, *Machine Learning with Neural Networks: An Introduction for Scientists and Engineers* (Cambridge University Press, Cambridge, England, 2021).

[第5页，第55段]
[52] E. Ott, *Chaos in Dynamical Systems*, 2nd ed. (Cambridge University Press, Cambridge, England, 2002).

[第5页，第56段]
[53] P. Cvitanović, R. Artuso, R. Mainieri, G. Tanner, and G. Vattay, *Chaos: Classical and Quantum* (Niels Bohr Institute, Copenhagen, 2020).

[第5页，第57段]
[54] A. Crisanti, A. Vulpiani, and G. Paladin, *Products of Random Matrices in Statistical Physics* (Springer, Berlin, 1993).

[第5页，第58段]
[55] J. Pennington, S. Schoenholz, and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: Theory and practice, Adv. Neural Inf. Process. Syst. 30, 4785 (2017), https://proceedings.neurips.cc/paper_files/paper/2017/file/d9fc0cdb67638d50f411432d0d41d0ba-Paper.pdf.

[第5页，第59段]
[56] I. Sutskever, J. Martens, G. Dahl, and G. E. Hinton, On the importance of initialization and momentum in deep learning, in *Proceedings of the 30th International Conference on Machine Learning—Volume 28* (PMLR, Cambridge, 2013), pp. III–1139–III–1147.

[第5页，第60段]
[57] X. Glorot and Y. Bengio, Understanding the difficulty of training deep feedforward neural networks, in *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics* (PMLR, Cambridge, 2021), pp. 2269–2277.

[第5页，第61段]
[58] A. Baratin, T. George, C. Laurent, R. D. Hjelm

[第6页，第1段]
Intelligence and Statistics，机器学习研究会议录第9卷，由Y. W. Teh和M. Titterington编辑（JMLR研讨会与会议录，Chia Laguna度假村，撒丁岛，意大利，2010年），第249–256页。

[第6页，第2段]
[18] S. Chen, H. He, and W. Su，标签感知神经正切核：面向更好的泛化与局部弹性，Adv. Neural Inf. Process. Syst. 33, 15847 (2020)，https://proceedings.neurips.cc/paper_files/paper/2020/file/b6b9023b3ebd1e462a5d11dbc5c4dae-Paper.pdf。

[第6页，第3段]
[19] L. Chizat, E. Oyallon, and F. Bach，论可微编程中的惰性训练，Adv. Neural Inf. Process. Syst. 32, 2933 (2019)，https://proceedings.neurips.cc/paper_files/paper/2019/file/ae614c557843b1df326cb29c57225459-Paper.pdf。

[第6页，第4段]
[20] G. Haller and G. Yuan，二维湍流中的拉格朗日相干结构与混合，Physica (Amsterdam) 147D, 352 (2000)。

[第6页，第5段]
[21] V. Lucarini and T. Bódai，气候系统中的边缘态：探索全局不稳定性与临界转变，Nonlinearity 30, R32 (2017)。

[第6页，第6段]
[22] M Beneitez, Y Duguet, P Schlatter, and D. S. Henningson，高维状态空间中的边缘流形作为拉格朗日相干结构，Phys. Rev. Res. 2, 033258 (2020)。

[第6页，第7段]
[23] Y. LeCun, C. Cortes, and C. J. C. Burges，MNIST手写数字数据库，yann.lecun.com/exdb/mnist (2018)。

[第6页，第8段]
[24] A. Krizhevsky, G. Hinton et al.，从微小图像中学习多层特征，技术报告，多伦多大学计算机科学系，加拿大，(2009)。

[第6页，第9段]
[25] C. Truesdell and W. Noll，in 力学的非线性场论，物理学百科全书第III卷，由S. Flügge编辑（Springer，柏林，1965年），第1–579页。

[第6页，第10段]
[26] J. L. Ren, C. Chen, Z. Y. Liu, R. Li, and G. Wang，玻璃态金属中通过多重分形中间态在混沌与自组织临界态之间的塑性动力学转变，Phys. Rev. B 86, 134303 (2012)。

[第6页，第11段]
[27] X. Jin, Y. Chen, L. Wang, H. Han, and P. Chen，大型风力发电机回转轴承的故障预测、监测与诊断方法：综述，Measurement 172, 108855 (2021)。

[第6页，第12段]
[28] G. Haller，拉格朗日相干结构，Annu. Rev. Fluid Mech. 47, 137 (2015)。

[第6页，第13段]
[29] S. Vannitsem，大尺度大气运动的可预测性：李雅普诺夫指数与误差动力学，Chaos 27, 032101 (2017)。

[第6页，第14段]
[30] A. Uthamacumaran，用于检测癌症网络中混沌吸引子的动力系统方法综述，Patterns 2, 100226 (2021)。

[第6页，第15段]
[31] A. Morozov, K. Abbott, K. Cuddington, T. Francis, G. Gellner, A. Hastings, Y.-C. Lai, S. Petrovskii, K. Scranton, and M. L. Zeeman，生态学中的长瞬态：理论与应用，Phys. Life Rev. 32, 1 (2020)。

[第6页，第16段]
[32] R. Ni, N. T. Ouellette, and G. A. Voth，湍流中涡度与杆状物随拉格朗日流体拉伸的排列，J. Fluid Mech. 743, R3 (2014)。

[第6页，第17段]
[33] V. Bezuglyy, M. Wilkinson, and B. Mehlig，流变镜可视化的庞加莱指数，Europhys. Lett. 89, 34003 (2009)。

[第6页，第18段]
[34] P. L. Johnson, S. S. Hamilton, R. Burns, and C. Meneveau，使用数据库任务并行粒子追踪算法分析湍流槽道流中拉格朗日拉伸的几何与统计特征，Phys. Rev. Fluids 2, 014605 (2017)。

[第6页，第19段]
[35] J. F. Gibson, J. Halcrow, and P. Cvitanovic，可视化平面库埃特流中状态空间的几何结构，J. Fluid Mech. 611, 107 (2008)。

[第6页，第20段]
[36] 详见补充材料 http://link.aps.org/supplemental/10.1103/PhysRevLett.132.057301 以获取有关实验装置和理论模型的详细信息。其中还包含参考文献[37]。

[第6页，第21段]
[37] A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin, A. Desmaison, L. Antiga, and A. Lerer，PyTorch中的自动微分，技术报告，(2017)，https://openreview.net/forum?id=BJJsrmfCZ。

[第6页，第22段]
[38] J. P. Eckmann and D. Ruelle，混沌与奇异吸引子的遍历理论，Rev. Mod. Phys. 57, 617 (1985)。

[第6页，第23段]
[39] T. Okushima，计算有限时间李雅普诺夫指数的新方法，Phys. Rev. Lett. 91, 254101 (2003)。

[第6页，第24段]
[40] P. Kidger and T. Lyons，深度窄网络的通用逼近，arXiv:1905.08539。

[第6页，第25段]
[41] T. M. Cover，线性不等式系统的几何与统计性质及其在模式识别中的应用，IEEE Trans. Electron. Comput. EC-14, 326 (1965)。

[第6页，第26段]
[42] D. Ciregan, U. Meier, and J. Schmidhuber，用于图像分类的多列深度神经网络，in 2012 IEEE计算机视觉与模式识别会议（IEEE计算机学会，Silver Spring，2012年），第3642–3649页。

[第6页，第27段]
[43] Y. Wang, H. Yao, and S. Zhao，基于自编码器的降维，Neurocomputing 184, 232 (2016)。

[第6页，第28段]
[44] J. Gawlikowski, C. R. N. Tassi, M. Ali, J. Lee, M. Humt, J. Feng, A. Kruspe, R. Triebel, P. Jung, R. Roscher et al.，深度神经网络中的不确定性综述，arXiv:2107.03342。

[第6页，第29段]
[45] B. Lakshminarayanan, A. Pritzel, and C. Blundell，使用深度集成进行简单且可扩展的预测不确定性估计，Adv. Neural Inf. Process. Syst. 30, 6402 (2017)，https://proceedings.neurips.cc/paper_files/paper/2017/file/9ef2ed4b7fd2c810847ffa5fa85bce38-Paper.pdf。

[第6页，第30段]
[46] L. Hoffmann and C. Elster，贝叶斯视角下的深度集成，arXiv:2105.13283。

[第6页，第31段]
[47] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu，面向对抗攻击鲁棒的深度学习模型，in 国际学习表征会议（国际学习表征会议，温哥华，2018年）。

[第6页，第32段]
[48] K. He, X. Zhang, S. Ren, and J. Sun，用于图像识别的深度残差学习，in IEEE计算机视觉与模式识别会议论文集（2016年），第770–778页。

[第6页，第33段]
[49] A. Dosovitskiy, L. Beyer, A Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly et al.，一图胜16 × 16词：面向大规模图像识别的Transformer，arXiv:2010.11929。
