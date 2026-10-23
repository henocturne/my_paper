[第1页，第1段]
具有局部灵活性的优先连接

[第1页，第2段]
Tingyu Zhao\textsuperscript{1,2,*}、Balázs Maga\textsuperscript{3,*}、Pierfrancesco Dionigi\textsuperscript{3}、Gergely Ódor\textsuperscript{3,4,5}、Kyle Soni\textsuperscript{6}、Anastasiya Salova\textsuperscript{6,7}、Bingjie Hao\textsuperscript{6}、Miklós Ábért\textsuperscript{3,†} 和 István A. Kovács\textsuperscript{2,6,7,8,‡}

[第1页，第3段]
\textsuperscript{1}美国伊利诺伊州埃文斯顿市西北大学工业工程与管理科学系，邮编60208
\textsuperscript{2}美国伊利诺伊州芝加哥市NSF-Simons国家生物学理论与数学研究所，邮编60611
\textsuperscript{3}匈牙利布达佩斯HUN-REN阿尔弗雷德·雷尼数学研究所，邮编1053
\textsuperscript{4}奥地利维也纳医科大学病理生理学、感染学与免疫学中心卫生学与应用免疫学研究所，邮编1090
\textsuperscript{5}奥地利维也纳中欧大学网络与数据科学系，邮编1100
\textsuperscript{6}美国伊利诺伊州埃文斯顿市西北大学物理与天文系，邮编60208
\textsuperscript{7}美国伊利诺伊州埃文斯顿市西北大学工程科学与应用数学系，邮编60208
\textsuperscript{8}美国伊利诺伊州埃文斯顿市西北大学复杂系统研究所，邮编60208

[第1页，第4段]
\textsuperscript{◊}（2026年1月9日收稿；2026年5月25日修订；2026年9月21日接受；2026年10月16日发表）

[第1页，第5段]
从社会关系的形成到方兴未艾的量子互联网，增长网络在新节点连接到现有网络时往往表现出局部灵活性。在我们提出的模型中，新节点以均匀随机的方式连接到预期目标附近范围内的某个节点，包括但不限于目标本身。通过数值模拟和严格的随机分析，我们发现这种局部灵活性会定性地改变非线性优先连接的全局网络行为。根据优先连接是超线性还是（次）线性，会涌现出两类截然不同的复杂网络架构。超线性相导致分层等级结构，不存在平稳度分布。尽管在线性和次线性情形下存在平稳度分布，但其衰减严格快于Barabási-Albert模型。我们在一个包含重定向的网络增长模型二维相图中解释我们的结果，具有广泛的意义。

[第1页，第6段]
DOI: 10.1103/y9m-q7qj

[第1页，第7段]
在网络科学的发展中，极简生成模型通过为复杂网络拓扑的涌现提供机制性洞见而发挥了核心作用。优先连接的变体尤其具有影响力[1,2]。在这些模型中，增长网络中的新到节点以随机方式连接到现有节点，连接概率由节点受欢迎程度决定，而受欢迎程度被建模为节点度——即当前伙伴数量——的函数。特别地，在线性优先连接下，当受欢迎程度直接由度给出时，即所谓的Barabási-Albert（BA）模型[1]，网络会自组织成无标度结构，其特征是幂律度分布[3]。虽然优先连接已被广泛用作理解复杂网络如何涌现的基准，但它也激发了大量推广和替代框架[4]，纳入了诸如内在节点适应度[5–7]、节点老化[8]、节点相似性[9]、节点中心性[10,11]或节点复制[12–14]等增长因素。

[第1页，第8段]
优先连接模型中一个隐含且往往缺乏依据的假设是，新节点总是直接且精确地连接到其选定的目标。然而在现实中，复杂系统中的动力学往往受到局部连接灵活性的影响：在增长网络中，被引导向某个目标的新节点可能被重定向，转而与附近的一个节点建立连接。例如，Alice可能为了建立社会联系——友谊、学术合作、商业机会或其他——而去找Bob，但最终可能反而与Bob的某个联系人Carol建立了关系。这可能是因为Bob出于利他行为将Alice引荐给Carol[15]；或者，Alice可能已经扩散离开，以随机游走者的方式探索Bob的邻域[16–20]。无论哪种情况，Carol的吸引力不再仅仅源于她自身的受欢迎程度，还源于Bob的受欢迎程度，反映了通过节点邻域产生的间接效用[21]。局部灵活性也与著名的社会理论相一致，如“弱 ties 的力量”[22]和结构洞[23]，这些理论强调社会关系的形成不仅由个体受欢迎程度驱动，还由周围的局部网络环境驱动。

[第1页，第9段]
局部灵活性本质上也在社会场景之外发挥作用。在生物系统中，有限的控制和不完善的信息往往导致连接形成中的局部变异性[24]。例如，在发育中的大脑中，

[第2页，第1段]
神经元在化学梯度的引导下形成突触，而化学梯度本质上具有噪声；此外，基因组缺乏为每个突触编码连接规则的能力，因此需要粗粒度的发育机制来自然产生灵活的连接性[25–27]。最后，我们的工作也受到新兴量子通信网络[28,29]的启发。即使双方之间没有直接的物理链路，通过纠缠交换协议（entanglement swapping protocols）也可以实现完全安全的量子通信，其中中间中继节点可用于在间接连接的双方之间建立端到端通信信道[30–32]。因此，引入网络的新节点不需要直接连接到其预期的通信目标；相反，只要连接到目标附近就足够了。综上所述，这些例子表明，连接灵活性可以是许多现实世界网络的一个普遍特征。

[第2页，第2段]
在本快报中，我们研究了增长网络中的局部连接灵活性如何影响最终的全局网络特征。为了以最纯粹的形式聚焦这一效应，我们引入了一个最小网络增长模型，该模型通过显式纳入连接灵活性来扩展标准的非线性优先连接（preferential attachment）[2,33]。作为我们的关键结果，这种连接灵活性会导致复杂的网络架构，这些架构在性质上不同于优先连接基线，并且特别地，它永远不会产生BA网络。这些发现凸显了网络动力学中的局部扰动对全局网络结构的反直觉后果。我们的结果得到了数值模拟、解析论证以及在可行情况下的严格证明的支持，相关证明列于附录中，详细证明见补充材料[34]。

[第2页，第3段]
模型与分析——我们提出局部灵活优先连接（LFPA）模型，其由单个变量$\alpha$参数化，如下所示。每个新节点首先按照标准非线性优先连接规则进入网络，以与$d_i^\alpha$成比例的概率选择一个初始目标节点$i$[2,33]，其中$d_i$是节点$i$的当前度，$\alpha \in \mathbb{R}$控制非线性。然后，作为局部连接灵活性的最简单表现形式，新节点可以均匀随机地连接到初始目标的图邻域中半径为$R$的任意节点。图邻域定义为从目标节点出发经过$\leq R$跳可达的所有节点，包括目标节点。$R = 0$对应于具有精确连接的标准非线性优先连接。超越这一情形，在允许局部灵活性的最局部设置$R = 1$下，新节点要么连接到目标本身，要么连接到其邻居之一，并在它们之间均匀选择，因此每个节点被选中的概率为$1/(d_i + 1)$；见图1。因此，新节点以概率$r_i = d_i/(d_i + 1)$从初始目标重定向到其邻居之一。

[第2页，第4段]
在这里，我们聚焦于$R = 1$设置，因为它在解析上简单，并表明它已经产生了与$R = 0$根本不同的网络结构。我们允许每个节点仅连接到一个现有节点，从而得到无向树，但将分析推广到新节点形成多个连接的情形是直接的。我们将节点$i$的权重定义为新节点连接到节点$i$的概率，部分由于其邻居$j \sim i$，由下式给出

[第2页，第5段]
$$w_i(\alpha) = (1 - r_i)d_i^\alpha + \sum_{j \sim i} r_j d_j^{\alpha - 1}, \tag{1}$$

[第2页，第6段]
经总图权重$W \equiv \sum_i w_i = \sum_i d_i^\alpha$归一化。注意，在LFPA模型中，重定向概率$r_i = d_i/(d_i + 1) \in [1/2, 1]$是异质的，随目标节点$d_i$的度单调增加。为了便于进一步分析LFPA，引入密切相关但更简单的恒定重定向（CR）模型是有用的，其中$r_i$被替换为固定重定向概率$r \in [0, 1]$，而式(1)的形式和$W$保持不变。正如我们将展示的，CR模型的二参数（$\alpha, r$）连续统囊括了广泛的复杂网络拓扑，其中一些此前已在文献中研究过，另一些则在此引入。由LFPA和CR模型在代表性$\alpha$和$r$值下生成的网络示例如图2所示，度分布绘制于图S1[34]。关键网络可观测量的结果总结于表I并在图3中可视化，综合了我们的解析和数值贡献。作为$\alpha$的函数，我们发现LFPA模型展现出两个性质不同的区域：$\alpha > 1$的超线性相，具有缺乏平稳度分布的分层结构；以及$\alpha \leq 1$的（亚）线性相，具有平稳的无标度度分布，其度指数在$\alpha \to -\infty$时发散。

[第2页，第7段]
作为一个不变的起点，CR模型的线性$\alpha = 1$情形对于任何$r$的选择都恰好是BA树——因为$w_i^{\text{CR}}(1, r) = (1 - r)d_i + r \sum_{j \sim i} 1 = d_i$——具有其特征性的无标度行为，即度指数为$\gamma = 3$的平稳幂律度分布。

[第3页，第1段]
相比之下，当$\alpha = 1$时的LFPA模型——我们称之为局部灵活BA（LFBA）模型——产生了性质上不同的网络拓扑，因为BA模型对异质重定向敏感。我们证明LFBA的叶子比例严格小于BA（定理8）；另见图3(b)。此外，我们表明LFBA增长无法维持BA树的大枢纽（定理9）。在渐近无度相关性的情况下，这一结论可以进一步推广到任何指数为$2 < \gamma < 11/3$的无标度度分布（定理10）。在LFBA下，高度节点的增长比BA中更慢，因为对于任何满足$d_j < d_i$的边$(i, j)$，跨越该边的重定向有利于$j$，因为$d_i/(d_i + 1) > d_j/(d_j + 1)$。网络模拟确实证实了更慢的最大度增长[图3(a)和S3(f) [34]]以及更轻尾的度分布[图4和S3(c)]。基于这些结果，我们推测LFBA具有$\gamma \geq 11/3 \approx 3.67$的平稳幂律度分布，接近数值估计$\gamma \approx 3.7$。模拟还揭示，在有限网络规模下，LFBA表现出比BA略高的度同配性；见图3(d)。注意BA同配系数在有限规模下为负，但在渐近极限下消失[41,42]。

[第3页，第2段]
### 表一. 我们结果的概览。本工作中得出的解析结果以粗体突出显示，并引用了附录中的支撑定理（证明见补充材料[34]）。基于数值结果的猜想用(*)标记。对于$r = 1/2$行，我们报告了当可用时$r \in (0, 1)$的一般结果（$\dagger$）；对于$\alpha = 2$列，我们报告了当可用时$\alpha \in (1, \infty)$的一般结果（$\ddagger$）。大$O$表示渐近上界，大$\Theta$表示匹配的渐近上下界，即放大到常数乘法因子。$N$是网络中的节点数，$\gamma$代表网络无标度（s.f.）时的幂律指数。我们的框架整合了先前文献中的几个已知模型：$\alpha = 1, r \in [0, 1]$是Barabási-Albert（BA）模型[1]；$\alpha = 0, r = 0$是随机递归树（RRT）[36]；$\alpha = 0, r = 1$是随机友树（RFT）[18–20]；$\alpha = 2, r = 1$是“$k2$”模型[21,37]。


[第4页，第1段]
在超线性相（$\alpha > 1$）中，我们推测LFPA在$r = 1$且$\alpha$值相同时渐近等价于CR，因为被不成比例地选为初始目标的高度数节点在LFPA下会以渐近确定性进行重定向。事实上，图3表明，在模拟中，当$\alpha \gg 1$时，LFPA的可观测量紧密跟随$r = 1$的CR值，但由于显著的有限尺寸效应，它们在$\alpha = 1$附近发生偏离。模拟结果还表明，网络演化为层次结构，没有平稳度分布，其中连通性集中在占主导地位的高度数节点及其近邻周围，而大多数节点保持在外围。为了解析地逼近这种结构的演化，我们研究了$\alpha > 1$时CR的总图权重动力学。我们引入了“分层等级”（layered hierarchy）的概念来描述按度数分层组织的图，并发现具有三个基本层级的分层等级实现了总图权重$W$的最快增长，这表明网络应自发地向这种结构演化。具体而言，三个层级包括：一个度数占主导的节点，其度数随网络规模$N$按$N^{\alpha/(2\alpha-1)}$缩放；一组周围的富跟随者，其度数按$N^{(\alpha-1)/(2\alpha-1)}$缩放；以及其余度数保持有限的贫穷节点（定理5）。我们还发现这种层次结构与网络中一种显著的拓扑平衡形式密切相关，即组合$\eta_i = \sum_{j \sim i} d_j^{\alpha-1}/d_i$渐近独立于节点$i$（注1）。因此，在出现强烈的度数异质性的同时，也出现了一种同质性概念，即所有节点趋向于具有相同的$\eta$值。注意，我们的层次结构结果涵盖了LFPA的整个$\alpha > 1$相以及$r = 1$时的CR模型，揭示的行为极大地扩展了在“$k2$”模型（即$\alpha = 2$、$r = 1$时的CR）中发现的定性相似行为[21,37]。极限情况$\alpha \to \infty$产生了一种新颖的“富俱乐部”（rich club）网络架构。在这里，主导节点与富跟随者之间的度数差距消失，产生了$\Theta(\sqrt{N})$个枢纽，每个枢纽的度数为$\Theta(\sqrt{N})$（定理3），最高度数节点的角色发生无限多次变化（定理4）。最后，在这个超线性相中，LFPA和CR都表现出小世界特性[43]，其直径（至多）随网络规模对数缩放；见图3(c)。此外，由于发现对于更大的网络规模，按$\log N$归一化的直径在减小[图S2(c)]，我们推测对于所有$\alpha > 1$，直径饱和于一个有限值。

[第4页，第2段]
在LFPA模型的整个（亚）线性相（$\alpha \leq 1$）中，我们观察到平稳度分布具有比BA更轻的尾部（图4）。在极限情况$\alpha \to -\infty$下，LFPA模型与$\alpha \to -\infty$、$r = 1/2$的CR模型相同，因为入节点总是选择一个叶节点，然后以概率$1/2$进行重定向。在这里，我们提供了一个完全刻画度分布的精确递推关系（定理11）：设$q_{k,\ell}$表示具有$k$个叶邻居和$\ell$个非叶邻居的节点比例，则

[第4页，第3段]
$$(2k+1)q_{k,\ell} = (k-1)q_{k-1,\ell} + (k+1)q_{k+1,\ell-1} \quad (2)$$

[第4页，第4段]
初始条件为$q_{0,1} = 1/2$，$q_{1,1} = 1/6$。基于此递推关系，我们证明度分布的尾部必须以比任何幂律更快的速度衰减，因为每个

[第5页，第1段]
渐近度分布的各阶矩是有限的（定理12）。相反，无标度尾部会导致所有 $2 \gamma - 1$ 阶矩发散。直观上，这一结果可以通过“有效退休”（effective retirement）的概念来理解：高度枢纽节点随着其叶邻居数量的减少而难以获得新邻居，导致在较大网络规模下（有效）最大度指数递减；见图S2(a)。尽管递推式Eq. (2)的完整求解似乎难以处理，但 $k$ 的边缘递推式是可解析求解的[44]；见注2。此外，我们通过数值迭代该递推式获得了精确的渐近度分布，与网络模拟结果一致。受最大度作为度分布极值统计量的启发，我们用Weibull型拉伸指数 $f(d) = (k/\lambda)(d/\lambda)^{k-1}e^{-(d/\lambda)^k}$ 拟合递推迭代的度分布，得到参数 $k \approx 0.335$ 和 $\lambda \approx 0.063$；见图4。基于拟合分布进行自举的Kolmogorov-Smirnov检验发现，在显著性水平0.01下，在度频率超过 $> 20$ 个数量级的范围内，没有显著的拟合不一致性。关于拟合Weibull参数作为度分布尾部截断函数的收敛性分析；见图S4。Weibull型尾部意味着最大度按 $\Theta[(log N)^{1/k}]$ 缩放，与图S3(g)一致[34]。在有限 $\alpha$ 下，我们无法排除无标度尾部。基于图S3[34]，我们推测度分布在有限 $\alpha \leq 1$ 时保持无标度，指数 $\gamma \geq 11/3$ 随着 $\alpha$ 从 $\alpha = 1$ 端点减小而缓慢增大，最终在 $\alpha \to -\infty$ 时发散。与超线性相相比，此（亚）线性相中的LFPA具有较小但仍然占主导的叶子比例，该比例随 $\alpha$ 减小而单调递减[图3(b)]，以及较大但仍然对数缩放的直径，保持了小世界性质[图3(c)]。

[第5页，第2段]
除了促进LFPA的分析之外，CR模型族本身也值得关注。我们关于CR丰富涌现行为的结果与LFPA一起总结在表I中。对于所有 $\alpha \neq 1$，引入任何正的重定向概率 $r > 0$ 都会导致定性不同的网络拓扑。特别地，如图3所示，与 $r = 0$ 时的非线性优先连接不同，所有研究的可观测量在 $r = 1$ 时都表现出对 $\alpha$ 的非单调依赖。一般来说，二维相图将CR模型族的不同情况统一为一个连续体，不仅揭示了新发现的结构，还将这些模型相互关联。例如，接近富俱乐部（rich club）模型的一种方式是将其作为 $\alpha > 0$、$r = 1$ 分层区域的极限情况。然而，将其作为 $\alpha \to \infty$、$r \in (0, 1)$ 时星形架构的极限情况来接近是更有启发性的。我们证明这些星形架构表现出稳定的最高度节点和有限直径（定理1），并且我们精确求解了它们的度分布（定理2）。对于 $\alpha$ 和 $r$ 的中间值，也会出现复杂的网络架构，例如 $\alpha = 0$、$r = 1/2$ 模型导致的网络拓扑在定性上似乎与LFBA相似；见图S1。

[第5页，第3段]
**讨论**——我们证明了，即使在建立连接时仅有极少量的局部灵活性，也使得标准的非线性优先连接不足以描述由此产生的网络架构。在超线性 $\alpha > 1$ 相中，由于增长过程不成比例地 targeting 高度节点，新节点通常连接到最高度节点或其邻居之一。这些动力学导致以一小部分高度连接节点为中心的非平稳分层架构，可能形成富俱乐部。尽管我们在此关注 $R = 1$ 的图邻域，但我们预期主要定性发现对于更大的图邻域 $R > 1$ 仍然成立，其中较大的 $R$ 导致层次中 $2R + 1$ 层。

[第5页，第4段]
在 $\alpha \leq 1$ 相中，增长过程偏向小度外围，导致平稳度分布但尾部严格轻于BA模型的尾部，并且最终在 $\alpha \to -\infty$ 时完全破坏无标度性。作为BA模型对异质重定向敏感性的更简单表现，我们发现即使是从[0, 1]均匀随机抽取的静态 $r_i$ 也会改变BA行为。注意，与LFBA中度依赖重定向存在时较轻尾部形成鲜明对比的是，静态异质性导致更重的尾部，$\gamma \approx 2.4$，与我们的解析预期一致；详见[34]图S5。

[第5页，第5段]
局部灵活性不仅重塑网络结构，还具有切实的功能意义，影响对攻击的鲁棒性以及网络上的传播和通信动力学[45]。例如，图S6[34]表明LFBA对针对性节点攻击具有增强的容忍度，这意味着当高度节点失效时，它比BA更好地保持图连通性[46]，这可能归因于其更高的同配性[15,41]。然而，作为一个最小模型，LFPA并不旨在捕捉局部灵活性发挥作用的现实世界网络的所有方面——相反，它旨在作为更精细模型的起点。例如，在量子通信网络中，目标图邻域内的连接概率可能取决于节点可用性、可靠性、带宽、地理距离和成本等几个重要因素。类似地，局部灵活性可能通过扩散过程产生[16–20]，尽管连接权重随与初始目标的距离而衰减。理解局部连接灵活性在多大程度上影响现实世界网络的演化是一个丰富的未来研究方向。

[第5页，第6段]
**致谢**——我们感谢X. Meng和L. Luzzatto的有益讨论。本工作受益于2023

[第6页，第1段]
以及2024年在匈牙利布达佩斯Erdős中心举办的“网络及其极限专题研讨会”，该研讨会由ERC协同基金DYNASNET（编号810115）资助。T. Z.和I. A. K.感谢NSF-Simons国家生物学理论与数学研究所的支持，该研究所由美国国家科学基金会（奖项编号2235451）和Simons基金会（奖项编号MP-TMPS-00005320）共同资助。I. A. K.还得到了国家科学基金会物理学部QIS项目的支持（资助编号PHY-2310706）。B. M.得到了NKFIH的支持（资助编号152535），该资助由匈牙利创新与技术部通过国家研究、发展与创新基金提供。G. Ö.得到了瑞士国家科学基金会的支持（资助编号P500PT-211129）以及奥地利科学基金卓越集群的支持（资助DOI：10.55776/COE7）。

[第6页，第2段]
数据可用性——用于高效LFPA和CR网络模拟的Python代码可在[47]获取。

[第6页，第3段]
[1] A.-L. Barabási and R. Albert, Emergence of scaling in random networks, Science 286, 509 (1999).

[第6页，第4段]
[2] P. L. Krapivsky, S. Redner, and F. Leyvraz, Connectivity of growing random networks, Phys. Rev. Lett. 85, 4629 (2000).

[第6页，第5段]
[3] M. E. Newman, Power laws, Pareto distributions and Zipf’s law, Contemp. Phys. 46, 323 (2005).

[第6页，第6段]
[4] S. N. Dorogovtsev and J. F. Mendes, Evolution of networks, Adv. Phys. 51, 1079 (2002).

[第6页，第7段]
[5] G. Bianconi and A.-L. Barabási, Competition and multiscaling in evolving networks, Europhys. Lett. 54, 436 (2001).

[第6页，第8段]
[6] G. Bianconi and A.-L. Barabási, Bose-Einstein condensation in complex networks, Phys. Rev. Lett. 86, 5632 (2001).

[第6页，第9段]
[7] G. Caldarelli, A. Capocci, P. De Los Rios, and M. A. Munoz, Scale-free networks from varying vertex intrinsic fitness, Phys. Rev. Lett. 89, 258702 (2002).

[第6页，第10段]
[8] S. N. Dorogovtsev and J. F. F. Mendes, Evolution of networks with aging of sites, Phys. Rev. E 62, 1842 (2000).

[第6页，第11段]
[9] F. Papadopoulos, M. Kitsak, M. A. Serrano, M. Boguna, and D. Krioukov, Popularity versus similarity in growing networks, Nature (London) 489, 537 (2012).

[第6页，第12段]
[10] A. Topirceanu, M. Udrescu, and R. Marculescu, Weighted betweenness preferential attachment: A new mechanism explaining social network formation and evolution, Sci. Rep. 8, 10871 (2018).

[第6页，第13段]
[11] V. Adami, Z. Ebadi, and M. Nattagh-Najafi, A dandelion structure of eigenvector preferential attachment networks, Sci. Rep. 14, 16994 (2024).

[第6页，第14段]
[12] R. Kumar, P. Raghavan, S. Rajagopalan, D. Sivakumar, A. Tomkins, and E. Upfal, Stochastic models for the web graph, in Proceedings 41st Annual Symposium on Foundations of Computer Science (IEEE, Redondo Beach, CA, USA, 2000), pp. 57–65, 10.1109/SFCS.2000.892065.

[第6页，第15段]
[13] A. Vázquez, A. Flammini, A. Maritan, and A. Vespignani, Modeling of protein interaction networks, Complexus 1, 38 (2003).

[第6页，第16段]
[14] P. L. Krapivsky and S. Redner, Network growth by copying, Phys. Rev. E 71, 036118 (2005).

[第6页，第17段]
[15] P. Li, J. Zhang, and M. Small, Emergence of scaling and assortative mixing through altruism, Physica A (Amsterdam) 390, 2192 (2011).

[第6页，第18段]
[16] J. Saramäki and K. Kaski, Scale-free networks generated by random walkers, Physica A (Amsterdam) 341, 80 (2004).

[第6页，第19段]
[17] T. S. Evans and J. P. Saramäki, Scale-free networks from self-organization, Phys. Rev. E 72, 026138 (2005).

[第6页，第20段]
[18] C. Cannings and J. Jordan, Random walk attachment graphs, Electron. Commun. Probab. 18, 1 (2013).

[第6页，第21段]
[19] P. L. Krapivsky and S. Redner, Emergent network modularity, J. Stat. Mech. (2017) P073405.

[第6页，第22段]
[20] L. Addario-Berry, S. Briend, L. Devroye, S. Donderwinkel, C. Kerriou, and G. Lugosi, Random friend trees, Random Struct. Algorithms 69, e70082 (2026).

[第6页，第23段]
[21] J.-H. Lee and K.-i. Ogawa, Emergence of a mutual-growth mechanism in networks evolved by social preference based on indirect utility, Sci. Rep. 13, 21680 (2023).

[第6页，第24段]
[22] M. S. Granovetter, The strength of weak ties, Am. J. Sociology 78, 1360 (1973).

[第6页，第25段]
[23] R. S. Burt, Structural holes and good ideas, Am. J. Sociology 110, 349 (2004).

[第6页，第26段]
[24] V. Shahrezaei and P. S. Swain, The stochastic nature of biochemical networks, Curr. Opin. Biotechnol. 19, 369 (2008).

[第6页，第27段]
[25] M. Tessier-Lavigne and C. S. Goodman, The molecular biology of axon guidance, Science 274, 1123 (1996).

[第6页，第28段]
[26] B. A. Hassan and P. R. Hiesinger, Beyond molecular codes: Simple rules to wire complex brains, Cell 163, 285 (2015).

[第6页，第29段]
[27] A. M. Zador, A critique of pure learning and what artificial neural networks can learn from animal brains, Nat. Commun. 10, 3770 (2019).

[第6页，第30段]
[28] N. Gisin and R. Thew, Quantum communication, Nat. Photonics 1, 165 (2007).

[第6页，第31段]
[29] H. J. Kimble, The quantum internet, Nature (London) 453, 1023 (2008).

[第6页，第32段]
[30] M. Zukowski, A. Zeilinger, M. Horne, and A. Ekert, “Event-ready-detectors” Bell experiment via entanglement swapping, Phys. Rev. Lett. 71, 4287 (1993).

[第6页，第33段]
[31] M. Riebe, T. Monz, K. Kim, A. Villar, P. Schindler, M. Chwalla, M. Hennrich, and R. Blatt, Deterministic entanglement swapping with an ion-trap quantum computer, Nat. Phys. 4, 839 (2008).

[第6页，第34段]
[32] X. Meng, B. Hao, B. Räth, and I. A. Kovács, Path percolation in quantum communication networks, Phys. Rev. Lett. 134, 030803 (2025).

[第6页，第35段]
[33] P. L. Krapivsky and S. Redner, Organization of growing random networks, Phys. Rev. E 63, 066123 (2001).

[第6页，第36段]
[34] 详见 http://link.aps.org/supplemental/10.1103/9y9m-q7qj 上的补充材料，其中包含附录中列出的所有定理的详细证明以及额外的支持图表，并包括参考文献[35]。

[第6页，第37段]
[35] V. S. Borkar and S. P. Meyn, The O. D. E. method for convergence of stochastic approximation and reinforcement learning, SIAM J. Control Optim. 38, 447 (2000).

[第7页，第1段]
[36] A. Frieze 和 M. Karonski，递归树，载于 *随机图引论*（剑桥大学出版社，英国剑桥，2015年），第17.2章。

[第7页，第2段]
[37] M. Falkenberg, J.-H. Lee, S. I. Amano, K. I. Ogawa, K. Yano, Y. Miyake, T. S. Evans, 和 K. Christensen，识别网络增长中的时间依赖性，Phys. Rev. Res. 2, 023352 (2020)。

[第7页，第3段]
[38] B. Bollobás, O. Riordan, J. Spencer, 和 G. Tusnady，无标度随机图过程的度序列，Random Struct. Algorithms 18, 279 (2001)。

[第7页，第4段]
[39] T. F. Móri，Barabási–Albert 随机树的最大度，Comb. Probab. Comput. 14, 339 (2005)。

[第7页，第5段]
[40] B. Bollobás 和 O. Riordan，无标度随机图的直径，Combinatorica 24, 5 (2004)。

[第7页，第6段]
[41] M. E. J. Newman，网络中的同配混合，Phys. Rev. Lett. 89, 208701 (2002)。

[第7页，第7段]
[42] N. Litvak 和 R. Van Der Hofstad，揭示大规模无标度网络中的异配性，Phys. Rev. E 87, 022801 (2013)。

[第7页，第8段]
[43] D. J. Watts 和 S. H. Strogatz，“小世界”网络的集体动力学，Nature (London) 393, 440 (1998)。

[第7页，第9段]
[44] H. Hartle 和 P. L. Krapivsky，优先连接树的叶子，J. Phys. A 59, 165001 (2026)。

[第7页，第10段]
[45] R. Pastor-Satorras 和 A. Vespignani，无标度网络中的流行病传播，Phys. Rev. Lett. 86, 3200 (2001)。

[第7页，第11段]
[46] R. Albert, H. Jeong, 和 A.-L. Barabási，复杂网络的错误与攻击容忍性，Nature (London) 406, 378 (2000)。

[第7页，第12段]
[47] https://zenodo.org/records/22314855。

[第7页，第13段]
[48] A. Klenke，*概率论：综合教程*（Springer，纽约，2008年）。

[第7页，第14段]
[49] B. Fotouhi 和 M. G. Rabbat，无标度图中的度相关性，Eur. Phys. J. B 86, 510 (2013)。

[第7页，第15段]
### 结尾部分

[第7页，第16段]
**附录 A：CR 模型（CR model）的解析结果——**

[第7页，第17段]
*定理 1——*对于 $\alpha \to \infty$ 和 $r < 1$，最高度节点几乎必然稳定，因此以线性速率 $1 - r$ 获得度。 consequently，树的直径几乎必然有限。

[第7页，第18段]
*证明概要——*我们分析 $D_1(N)$ 和 $D_2(N)$，即大小为 $N$ 时的最高度和次高度。我们证明 $D_1 > D_2 + 2$ 几乎必然无限次发生，并且每当这种差距成立时，出现新的最高度节点的概率为 $O(D_1^{-2})$。Borel-Cantelli [48] 然后意味着新的最高度节点几乎必然只出现有限次。

[第7页，第19段]
*定理 2——*对于 $\alpha \to \infty$ 和 $r \in (0, 1)$，

[第7页，第20段]
$$p_k \to 
\begin{cases} 
1 - r + r^2, & \text{if } k = 1, \\
(1 - r)^2 r^{k-1}, & \text{if } k \geq 2,
\end{cases}$$

[第7页，第21段]
其中 $p_k$ 表示度为 $k$ 的节点的比例，不包括最高度节点。

[第7页，第22段]
*证明概要——*根据定理 1，新节点要么直接连接到单个持久最高度节点，成为其邻居，要么被重定向到其现有邻居之一，增加该邻居的度。这将度分布简化为沿最高度节点邻域的增长过程，由此得出所述的极限比例。

[第7页，第23段]
*定理 3——*在富俱乐部模型（rich club model）中，当 $\alpha \to \infty$ 和 $r = 1$ 时，最大度 $D_1(N)$ 满足

[第7页，第24段]
$$D_1(N) = \Theta(\sqrt{N}) w.p.1.$$

[第7页，第25段]
*证明概要——*该过程在具有唯一最高度节点的时期和几个相邻节点并列最高度的时期之间交替。最大度只有在这样的并列被解决时才能增加，并且它从 $d$ 增长到 $2d$ 所需的时间是 $\Theta(d^2)$。结果然后通过连续应用这个界限得出。

[第7页，第26段]
*定理 4——*在富俱乐部模型中，当 $\alpha \to \infty$ 和 $r = 1$ 时，无限多个节点无限多次参与最高度的并列。

[第7页，第27段]
*证明概要——*相反，假设只有固定有限集节点能无限次并列最高度。比较该集中一个边界节点与其外部一个相邻节点，它们的度差对称演化，直到一个外部节点加入并列，因此它无限次返回零。每次返回给外部节点一个正机会参与最高度的并列，与假设矛盾。

[第7页，第28段]
*定理 5（分层层次结构）——*我们说 $G_N$ 具有指数为 $\beta_1, \beta_2, \ldots, \beta_k$ 的分层层次结构，如果有一个度为 $\approx N^{\beta_1}$ 的单个节点形成第一层，并且第 $i$ 层中的每个节点度为 $\approx N^{\beta_i}$。第 $(k + 1)$ 层由叶子组成。由于 $G_N$ 的总节点数为 $N$，我们有 $N^{\beta_1}N^{\beta_2} \cdots N^{\beta_k} \approx N$，所以 $\sum_{i=1}^k \beta_i = 1$。

[第7页，第29段]
在 $\alpha > 1$ 和 $r = 1$ 时，在所有具有分层层次结构的图中，期望总图权重增长 $\mathbb{E}[W(G_{N+1}) - W(G_N)|G_N]$ 由那些具有三个基本层的图最大化，即那些满足

[第7页，第30段]
$$\beta_1 = \frac{\alpha}{2\alpha - 1}, \quad \beta_2 = \frac{\alpha - 1}{2\alpha - 1}.$$

[第7页，第31段]
*证明概要——*我们可以将期望一步总图权重增长写为 $\gamma_\alpha(N)/m_\alpha(N)$，其中 $m_\alpha(N) = W(G_N) = \sum_i d_i^\alpha$，并且到主导阶，$\gamma_\alpha(N) = 2\alpha \sum_{i \sim j} (d_i d_j)^{\alpha-1}$。将这两个量用层指数表示，将问题转化为

[第8页，第1段]
这是对 $\beta_i$ 的优化。当仅有两个非叶指数非零时，该优化达到最大值，而约束 $\sum_i \beta_i = 1$ 给出了所述的值。

[第8页，第2段]
**注1（平衡性质）**——定理5中的最优层级结构诱导出以下平衡性质：

[第8页，第3段]
$$\eta_i \equiv \frac{\sum_{j \sim i} d_j^{a-1}}{d_i}$$

[第8页，第4段]
渐近独立于节点 $i$。我们认为这种平衡与定理5的最大化目标具有共生关系：如果新叶子节点连接到节点 $i$，则 $\gamma_\alpha$、$m_\alpha$ 的变化由下式给出

[第8页，第5段]
$$\Delta \gamma_\alpha = (d_i + 1)^{a-1} + ((d_i + 1)^{a-1} - d_i^{a-1}) \sum_{j \sim i} d_j^{a-1}$$

[第8页，第6段]
$$\propto d_i^{a-2} \sum_{j \sim i} d_j^{a-1},$$

[第8页，第7段]
$$\Delta m_\alpha = 1 + (d_i + 1)^\alpha - d_i^\alpha \propto d_i^{a-1},$$

[第8页，第8段]
因此 $\Delta \gamma_\alpha / \Delta m_\alpha \approx \eta_i$。为了优化这一点，连接到具有较大 $\eta_i$ 的节点是有利的。这种连接会降低 $\eta_i$ 的值，因此在最优配置中，量 $\eta_i$ 应在所有节点之间渐近恒定。在BA极限下，平衡性质对每个网络结构都平凡地满足，而对于 $\alpha > 1$，平衡性质本身意味着一个规则的层级结构：所有叶子节点都连接到具有相同度数的非叶节点，而这些非叶节点又恰好有一个具有相同度数的非叶邻居，依此类推。

[第8页，第9段]
**定理6**——如果 $\alpha \to -\infty$，叶子节点的比例 $p_1(N)$ 几乎必然趋于 $r$，并且对于 $r < 1$，网络的直径几乎必然趋于无穷大。

[第8页，第10段]
**证明概要**——在此极限下，每个新节点首先瞄准一个叶子节点。叶子节点的数量恰好在发生重定向时增加，这以概率 $r$ 发生，因此根据大数定律，$p_1(N) \to r$。对于 $r < 1$，增加直径的连接继续无限频繁地发生，迫使直径发散。

[第8页，第11段]
**定理7**——如果 $\alpha = 0$，$r \neq 1$，则对于叶子节点的渐近比例

[第8页，第12段]
$$\frac{1}{2} \leq \lim_{N \to \infty} \inf p_1(N), \quad \lim_{N \to \infty} \sup p_1(N) \leq \frac{1}{2 - r}.$$

[第8页，第13段]
这些界可推广到 $\alpha > 0$：下界对任意 $r \in [0, 1/2]$ 成立，而上界对任意 $r \in [0, 1]$ 成立。

[第8页，第14段]
**证明概要**——我们追踪下一次连接连接到非叶节点的概率，因为这是创建新叶子节点的时候。用当前叶子节点比例来界定该概率并取渐近极限，即得到所述的不等式。

[第8页，第15段]
**附录B：LFPA模型的解析结果**

[第8页，第16段]
**定理8**——LFPA模型在 $\alpha = 1$ 时，即LFBA模型，在长期运行中叶子节点数量严格少于BA模型。

[第8页，第17段]
**证明概要**——我们证明 $w_{\text{leaf}}^{\text{LFBA}} \geq 7/6$，而 $w_{\text{leaf}}^{\text{BA}} = 1$。连接到一个叶子节点等价于将非叶节点数量增加一，反之亦然。通过分析渐近极限，我们证明LFBA中叶子节点的比例上界为 $12/19 \approx 0.63$，而在BA中已知为 $2/3$ [38]。

[第8页，第18段]
**定理9**——BA树的枢纽结构，精确遵循BA度相关性 [49]，在LFBA动力学下是不稳定的。

[第8页，第19段]
**证明概要**——在LFBA树中，设 $i_N$ 为规模 $N$ 时度数最高的节点，并设 $D_N \equiv d(i_N)$。假设（为了导出矛盾）$i_N$ 周围的局部结构渐近为BA结构，枢纽的邻居遵循BA条件度分布 [49]。我们证明对于任意 $\epsilon > 0$，诱导的LFBA枢纽增长满足

[第8页，第20段]
$$D_N = O\left(N^{\frac{1}{2}\left(\frac{\epsilon^2}{6} - 1\right) + \epsilon}\right) \approx O(N^{0.322 + \epsilon})$$

[第8页，第21段]
对所有充分大的 $N$ 成立，这与BA枢纽定律 $D_N \approx N^{1/2}$ [38] 矛盾。

[第8页，第22段]
**定理10**——任何度指数为 $2 < \gamma < 11/3$，特别是 $2 < \gamma \leq 3$ 的度不相关无标度树的枢纽结构，在LFBA动力学下是不稳定的。

[第8页，第23段]
**证明概要**——假设（为了导出矛盾）LFBA树渐近为无标度且无度相关性，即 $p(k) \sim k^{-\gamma}$，$p(\ell|k) \sim \ell p(\ell)$。我们证明在所有充分大的 $N$ 处，对于任意 $\epsilon > 0$，$D_N = O(N^{3/8 + \epsilon})$。然而，$2 < \gamma < 11/3$ 意味着 $D_N \approx N^\beta$，其中 $\beta > 3/8$，从而产生矛盾。

[第8页，第24段]
**定理11**——考虑 $\alpha \to -\infty$ 时的LFPA（或等价地，$\alpha \to -\infty$、$r = 1/2$ 时的CR）。渐近度分布由 $p_x = \sum_{k+\ell=x} q_{k,\ell}$ 给出，其中 $q_{k,\ell}$ 表示具有 $k$ 个叶子邻居和 $\ell$ 个非叶邻居的节点比例。值 $q_{k,\ell}$ 由平稳线性递推确定

[第8页，第25段]
$$(2k + 1)q_{k,\ell} = (k - 1)q_{k-1,\ell} + (k + 1)q_{k+1,\ell-1}$$

[第8页，第26段]
初始条件为 $q_{0,1} = 1/2$，$q_{1,1} = 1/6$。

[第8页，第27段]
**证明概要**——我们通过枚举由所选枢轴叶子节点引起的可能转移，写出 $Q_N(k,\ell)$ 的一步主方程，其中 $Q_N(k,\ell)$ 是树有 $N$ 个节点时处于状态 $(k,\ell)$ 的期望节点数。该主方程为在渐近极限下推导式(2)提供了基础。

[第8页，第28段]
**定理12**——对于 $\alpha \to -\infty$，LFPA模型渐近度分布的所有矩都是有限的。特别地，$\alpha \to -\infty$ 时的LFPA不是无标度的。

[第9页，第1段]
证明概要——采用定理11的记号，对于第s阶矩，我们的断言等价于

[第9页，第2段]
$ 
\sum_{k \geq 0, \ell \geq 1} (k + \ell)^s q_{k, \ell} < \infty.
 $

[第9页，第3段]
取权重为$ \phi(k, l) $的递推式(2)并将所得方程相加，经过一些形式化操作后，我们得到一个涉及$ q_{k, l} $的收敛级数。通过某些线性代数观察，我们可以保证存在$ \phi(k, l) $使得该收敛级数恰好与上述不等式的左侧重合。这些形式化操作通过截断论证得以严格化。

[第9页，第4段]
注2——Hartle和Krapivsky的并行工作[44]对式(2)提供了进一步分析。他们指出（我们同意），求解这个双指标递推以获得完整的度分布是困难的。然而，通过对$ \ell $进行边缘化，他们仅针对$ k $构建并求解了一个封闭递推，得到了具有拉伸指数尾部的“叶度分布”。
