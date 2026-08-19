[第1页，第1段]
动力学相变（Dynamical Phase Transitions, DPTs）是一种揭示随时间涌现的临界行为的临界现象，代表了非平衡物理（nonequilibrium physics）的新前沿[1–10]。与传统相变（通常由温度或压力等外部参数驱动）不同，DPTs发生在临界时间$t_c$处，此时物理可观测量表现出非解析行为。尽管这些相变已在量子系统中得到广泛研究，但其在经典情境中的作用仍 largely 未被充分探索，仅有的进展来自非平衡弛豫至平衡态的均场分析（mean-field analyses）[11,12]及数值模拟[13]。

[第1页，第2段]
有趣的是，近期关于宏观复杂系统的实验，包括生态崩溃（ecological collapse）[14,15]、金融危机（financial crises）[16,17]和电网故障（power grid failures）[18]，均报告了有限时间内发生的突变动力学变化。这些事件虽未被正式归类为DPTs，但具有突然的集体变化等关键特征。这些现象与量子DPTs的惊人相似性表明，临界时间动力学（critical temporal dynamics）可能是复杂系统的普遍特征。这引发了关于其更广泛关联性与潜在普适性的深刻问题。

[第1页，第3段]
更近期，关于社交网络（social networks）的研究为经典情境中DPTs的涌现提供了有力证据[19–22]。这些实验揭示，某些物理可观测量$z(t)$在临界时间$t_c$处根据普适双曲标度（hyperbolic scaling）发散：

[第1页，第4段]
$$z(t) \sim (t_c - t)^{-1}.$$  (1)

[第1页，第5段]
与量子DPTs（非解析性出现但不发散）不同，这种经典双曲标度揭示了时间临界性（temporal criticality）的独特特征，且似乎在不同领域中普遍存在。例如，经济学中观察到的双曲贴现（hyperbolic discounting）[23–26]（可解释拖延行为和截止日期效应）也遵循此标度，这从截止日期前学术投稿量的激增中得到证实[27]。尽管这种现象普遍存在，但其普适性的理论基础仍未被充分理解。

[第1页，第6段]
现有的非平衡经典相变理论框架大致分为两类。第一类处理在时变控制参数下出现的不同相，类似于平衡相变[21,28–31]。第二类包含自组织临界性（self-organized criticality）模型[32–36]，其中临界点出现在渐近极限$t \to \infty$而非有限$t_c$处。这两类框架均未能完全捕捉DPTs特有的有限时间奇异性（finite-time singularities），表明需要新的理论方法。

[第1页，第7段]
在本快报（Letter）中，我们提出一个预测非平衡网络中DPTs涌现的理论框架。核心洞见在于：非线性相互作用（nonlinear interactions）起着关键作用。类比多体物理（many-body physics），无相互作用的随机图类似于无DPTs的非相互作用粒子系统。然而，一旦引入非线性相互作用，系统的集体动力学（collective dynamics）将发生根本性改变。为证明这一点，我们考虑一个包含二次相互作用的简单模型，其动机源于三角闭合（triangle closure）——

[第2页，第1段]
社会网络中普遍存在的机制。在该模型中，边之间的二次相互作用自然产生了动态相变（DPT）。值得注意的是，该模型可以解析求解，再现了公式(1)中表达的普适标度行为。此外，我们证明了关键网络特征，如度分布（degree distribution）和聚类系数（clustering coefficient），在接近$t_c$时表现出临界标度行为。这些结果为理解经典系统中的非平衡临界性（nonequilibrium criticality）奠定了理论基础，并揭示了与量子DPT的相似之处。

[第2页，第2段]
**理论框架**——我们考虑一个有向网络，包含$N$个顶点，经历随机边的添加和移除。具体来说，顶点$i$以概率速率$\alpha/N$连接到顶点$j$形成新边，而边以速率$\gamma$被移除。参数$\alpha$和$\gamma$分别表征边形成和移除的速率，因子$1/N$确保了网络的稀疏性。期望平均度$\bar{z}(t) = (1/N) \left\langle \sum_{ij} A_{ij} \right\rangle$的演化，其中$\left\langle \ldots \right\rangle = \int \ldots P(A, t) dA$，遵循线性微分方程，

[第2页，第3段]
$$\frac{dz}{dt} = \alpha - \gamma z,$$

[第2页，第4段]
其稳态解为$z(t \to \infty) = \alpha/\gamma$。在这种非相互作用场景中，网络保持为随机图，不表现出DPT。

[第2页，第5段]
接下来我们将证明，DPT的出现需要非线性相互作用。一种自然的方法是将边添加速率修改为$\alpha/N + U_{\text{int}}$，其中$U_{\text{int}}(A)$表示依赖于布尔邻接矩阵（adjacency matrix）$A$的相互作用项。虽然边移除速率也可以类似修改，但为简单起见，我们保持该参数不变。相互作用项可以展开为$U_{\text{int}}(A) = \beta_0 A + \beta A^2 + O(A^3)$。为了隔离非线性效应，我们忽略线性项，仅保留主要的非线性贡献，得到$U_{\text{int}}(A) \approx \beta A^2$，其中$\beta$是耦合常数（coupling constant）。这些相互作用自然被解释为三角闭合机制（triadic closure mechanism）[37]：两个共享共同邻居的顶点$i$和$j$更可能形成直接连接。这以与$\sum_k A_{ik} A_{kj} = (A^2)_{ij}$成比例的额外速率发生，导致以下网络动力学：

[第2页，第6段]
$$W[A_{ij}(0 \to 1)] = \left(\frac{\alpha}{N} + \beta (A^2)_{ij}\right), \tag{2a}$$

[第2页，第7段]
$$W[A_{ij}(1 \to 0)] = \gamma. \tag{2b}$$

[第2页，第8段]
虽然三角闭合通常与社会网络相关，但我们的理论将其视为主要的非线性相互作用，将其适用性扩展到社会背景之外。

[第2页，第9段]
在弱相互作用区域（$\beta$较小），网络表现为随机图，没有DPT。然而，随着$\beta$增加，非线性相互作用显著改变了动力学，导致边聚类（edge clustering）和有限时间奇点（finite-time singularities）。图1展示了所提出模型在$\beta = 0.5$、$\alpha = \gamma = 1$时网络的时间演化，这表明存在一个临界时间$t_c$，此时网络结构发生显著变化。

[第2页，第10段]
为了量化这种快速变化，我们推导了任意连通子图（connected subgraph）密度$\rho(G)$的时间演化，这由稀疏性条件下的Schwinger-Dyson（SD）方程给出（见补充材料[38]，第1.1节）。对于最简单的子图，即两个顶点之间的连接，密度对应于平均度$z$，遵循

[第2页，第11段]
$$\frac{dz}{dt} = \alpha - \gamma z + \beta (z^2 - \Delta), \tag{3}$$

[第2页，第12段]
其中$\Delta = (1/N) \left\langle \sum_{ijk} A_{ij} A_{jk} A_{ik} \right\rangle$测量网络中的三角形密度（triangle density）。动力学项$\alpha - \gamma z$与非相互作用随机图模型相同，而相互作用项$\beta (z^2 - \Delta)$引入了一个放大聚类的反馈回路。

[第2页，第13段]
这个微分方程不是封闭的，因为$\Delta$依赖于四顶点矩形形状的数量。这些四顶点矩形形状又依赖于五顶点形状的数量，依此类推。这种层级结构创建了一个无限方程塔，这是SD方程的一个标志。例如，

[第2页，第14段]
$$\frac{d\Delta}{dt} = \beta (z^2 - \Delta) - 3\gamma \Delta + O(\beta^3), \tag{4}$$

[第2页，第15段]
其中$O(\beta^3)$表示更高阶项，如四顶点形状。对SD方程应用标准的微扰截断方案（perturbative truncation scheme），并注意到$\Delta \sim O(\beta)$，我们可以在公式(3)中忽略它，得到

[第2页，第16段]
$$z(t) \sim \begin{cases} \text{常数} & (\beta \leq \frac{\gamma^2}{4\alpha}, t \to \infty), \\ 1/(t - t_c) & (\beta > \frac{\gamma^2}{4\alpha}, t \to t_c), \end{cases} \tag{5}$$

[第3页，第1段]
其中临界时间 $  t_c  $ 由 $  t_c = \omega^{-1}[\text{acot}(2\omega) + (\pi/2)]  $ 给出，且 $  \omega = \sqrt{\alpha\beta - (\gamma^2/4)}  $。因此，$  t_c  $ 仅通过 $  \omega  $ 依赖于 $  (\alpha, \beta, \gamma)  $，且有限时间奇点仅出现在超临界区域 $  \beta > \gamma^2/(4\alpha)  $（参见补充材料[38]第1.1节）。此外，方程(5)识别出两个不同相：在“平衡相”（equilibrium phase）中，当 $  \beta \leq (\gamma^2/4\alpha)  $ 时，$  z(t)  $ 在 $  t \to \infty  $ 时趋近于常数，表明网络收敛到稳态（stationary state）。在“非平衡相”（nonequilibrium phase）中，当 $  \beta > (\gamma^2/4\alpha)  $ 时，模型预测了动态相变（DPT, dynamical phase transition），其中 $  z(t)  $ 在 $  t \to t_c  $ 时呈双曲发散，与方程(1)中的经验定律一致。重要的是，除平均度（average degree）外的可观测量以不同指数发散，反映了其结构序（structural order）。例如，三角形密度（triangle density）按 $  \Delta \sim z^2 \sim [1/(t_c - t)^2]  $ 标度，捕捉了其次近邻特性。更一般地，高阶子图密度（higher-order subgraph density）以 $  z  $ 的幂次发散，其指数由有效邻域阶数（effective neighborhood order）决定。

[第3页，第2段]
上述推导代表了施温格-戴森方程（Schwinger-Dyson equation）无穷级数的一个特例，该方程将邻接矩阵（adjacency matrix）$  A(t)  $ 视为量子场论中的场变量，并忽略了高阶项 $  \square \sim O(\beta^3)  $（参见补充材料[38]第1.1节）。注意，添加高阶项不会改变上述物理图像，但会引入耦合常数（coupling constant）的修正。例如，考虑方程(4)中 $  \Delta  $ 的贡献，同时忽略 $  O(\beta^3)  $ 项并应用绝热近似（adiabatic approximation），得到修正 $  \beta \to \beta' := (3\beta\gamma/3\gamma + \beta) = \beta - \beta^2/(3\gamma) + O(\beta^3)  $。这可解释为由高阶修正产生的重整化耦合常数（dressed coupling constant）。将方程(5)中的 $  \beta  $ 替换为重整化值 $  \beta'  $，可精确预测 $  z(t)  $，如图2(a)所示。尽管绝热近似在快速变化（尤其是 $  t \to t_c  $ 时）下预期失效，但我们发现即使这种简单近似也与平衡相和非平衡相的数值模拟结果吻合良好。上述理论分析可总结为以 $  \alpha/\gamma  $ 和 $  \beta/\gamma  $ 为变量的相图（phase diagram），其中相边界 $  \beta'(\beta)/\gamma = (4\alpha/\gamma)^{-1}  $ 分隔了平衡相和非平衡相。图3(a)比较了我们的理论预测与数值模拟结果，虚线表示树图层次（tree level）的理论预测 $  (\beta' = \beta)  $，实线则包含了三角形修正 $  (\beta' = (3\beta\gamma/3\gamma + \beta))  $。我们发现两种预测在小 $  \beta  $ 值时均与数值结果吻合良好，而三角形修正即使在相对较大的 $  \beta  $ 值下也与数值结果一致。

[第3页，第3段]
令人惊讶的是，我们的理论表明，只要动力学速率（kinetic rate）$  \alpha  $ 足够大，即使很小的 $  \beta  $ 值也能导致非平衡相。这意味着向随机图模型（random graph model）引入任意小的非线性相互作用，可以从根本上改变底层网络演化的性质，并可能引发动态相变。

[第3页，第4段]
**图2.** (a) 平均度 $  z(t)  $ 和 (b) 序参量（order parameter）$  q(t)  $ 的理论预测与数值模拟对比，参数为 $  \alpha = 1  $，$  \gamma = 1  $，$  \beta = 1/4  $（绿色）和 $  \beta = 1/2  $（红色）。实线表示理论预测，散点对应 $  N = 2000  $ 的模拟结果。对于 $  \beta = 1/4  $（绿色），平均度 $  z(t)  $ 收敛，而序参量 $  q(t)  $ 趋于零，表明处于平衡相。对于 $  \beta = 1/2  $（红色），$  z(t)  $ 呈现双曲标度并在有限临界时间 $  t_c \approx 5.9  $ 处发散。相应地，$  q(t)  $ 在 $  t_c  $ 处出现尖锐跳变，标志着从稀疏网络到稠密网络的一阶动态相变（first-order DPT）。

[第3页，第5段]
**一阶相变（First-order phase transition）**——为进一步表征非平衡相，我们定义序参量 $  q = \lim_{N \to \infty} z/N  $，表示边数相对于完全图（complete graph）的比例。根据定义，$  0 \leq q \leq 1  $。在稀疏图（sparse graph）区域 $  [z \sim O(1)]  $ 中，有 $  q = 0  $，这既适用于平衡相，也适用于非平衡相中临界时间之前 $  t < t_c  $ 的情况。然而，对于

[第3页，第6段]
**图3.** (a) 模型在 $  \alpha-\beta  $ 参数空间中的相图，显示两个不同相：平衡相和非平衡相（灰色区域）。曲线表示理论预测，散点对应相边界的模拟结果。(b) 相图展示了从稀疏图相到稠密图相（dense graph phase）的转变。彩色曲面量化了相边界。此处，$  \alpha  $、$  \beta  $ 和 $  t  $ 均通过 $  \gamma  $ 重新标度以使其无量纲化。

[第4页，第1段]
当 $  t > t_c  $ 时，网络变得稠密，导致 $  q > 0  $。这种稀疏-稠密网络相变已在理论模型和现实世界系统中被观察到，包括网络致密化（network densification）[39]和团簇渗流（clique percolation）[40]。这些系统共享类似于三角闭合（triangle closure）的聚类机制，当聚类强度超过临界阈值时，稀疏性会崩溃。然而，传统模型展示的相变由外部参数控制。相比之下，在我们的模型中，这种相变由有限临界时间决定，标志着它是一个DPT。方程(5)中 $  t = t_c  $ 处的奇异性表明这是一级相变（first-order phase transition），其特征是 $  q(t = t_c)  $ 从零到非零值的不连续性，即潜热（latent heat）。这种行为如图2(b)所示。

[第4页，第2段]
方程(4)中的解析结果仅对 $  (t < t_c)  $ 有效，因为稀疏条件在临界时间之后失效。为了确定 $  t > t_c  $ 时的 $  q(t)  $，我们需要更好地理解所观察到的DPT。对于足够大的耦合，网络初始时是稀疏的，动力学项主导着演化过程。随着连接的增长，由三角闭合驱动的非线性相互作用（nonlinear interaction）变得越来越显著，在动力学项与非线性相互作用之间产生了竞争。一旦非线性相互作用占据主导地位，就会发生边形成的快速级联（rapid cascade），导致DPT。

[第4页，第3段]
在DPT之后，网络凝聚成一个紧密连接的核心，形成一个完全图（complete graph），同时伴有少数度为零的孤立顶点（isolated vertex）。假设孤立顶点的比例为 $  p  $，则完全图核心的比例为 $  [1 - p(t)]N  $，因此 $  q(t) = [1 - p(t)]^2  $。一旦一个孤立顶点与核心建立了一条边，它会立即连接到核心中的所有其他顶点，因为共同邻居的数量为 $  O(N)  $，这是发散的。因此，孤立顶点连接到核心中一个顶点的速率会增加。这意味着 $  p(t) = p_0 e^{-a(t-t_c)}  $ 由于与核心的随机连接而呈指数衰减，其中 $  p_0  $ 是 $  t = t_c  $ 时孤立顶点的比例。由此，我们得到

[第4页，第4段]
$ 
q(t) = \left( 1 - p_0 e^{-a(t-t_c)} \right)^2,
 $

[第4页，第5段]
(6)

[第4页，第6段]
对于 $  t \geq t_c  $。这一预测与数值模拟结果吻合良好[图2(b)]。潜热 $  q(t_c) = (1 - p_0)^2  $ 与孤立顶点的临界比例 $  p_0  $ 相关，我们将在稍后讨论。

[第4页，第7段]
总之，对于平衡相（equilibrium phase），网络在任何 $  t  $ 下都将保持稀疏。对于非平衡相（nonequilibrium phase），临界时间 $  t_c  $ 进一步将状态区分为稀疏网络 $  (t < t_c)  $ 和稠密网络 $  (t > t_c)  $。临界时间 $  t_c  $ 取决于 $  \alpha  $、$  \beta  $ 和 $  \gamma  $，其中相对较大的 $  \beta  $ 对应较小的 $  t_c  $，即系统更早达到临界时间。图3(b)在三维相图中展示了这些发现。着色的相边界曲面将稀疏网络和稠密网络对应的区域分隔开来。

[第4页，第8段]
**临界行为（Critical behavior）**——为了研究DPT附近的临界行为，我们特别关注度分布（degree distribution）。对于非相互作用模型（$  \beta = 0  $），度遵循泊松分布（Poisson distribution）。对于有限非线性耦合，在树级近似（tree level）下，我们发现时间依赖的度分布 $  P(k, t)  $ 满足

[第4页，第9段]
$ 
\frac{\partial}{\partial t} P(k, t) = [\alpha + \beta(k - 1)z(t)]P(k - 1, t) - [\alpha + \beta k z(t) + \gamma k]P(k, t) + \gamma (k + 1)P(k + 1, t).
 $

[第4页，第10段]
(7)

[第4页，第11段]
该方程可以使用生成函数法（generating function method）解析求解（参见补充材料[38]，第1.2节）。对于非平衡相，当系统接近临界时间 $  t_c  $ 时，度分布变为幂律形式（power-law form），如图4(a)和4(b)所示，其中包含了理论预测和数值模拟结果。最终，$  P(k, t \to t_c) \sim k^{-\gamma}  $ 形成了一个无标度网络（scale-free network）[41,42]，其指数 $  \gamma = 1  $，表明平均度 $  z  $ 发散，这是DPT的信号。这一点特别有趣，因为我们没有使用诸如优先连接（preferential attachment）[41,42]之类的机制来生成无标度性。相反，DPT附近的临界行为自动生成了无标度性，这超越了传统无标度网络的范式。

[第4页，第12段]
此外，虽然树级近似仅适用于 $  t \leq t_c  $，但这个解析结果使我们能够计算孤立顶点的比例 $  p_0 = P(0, t_c)  $（参见补充材料[38]，第1.2节）。图4(c)显示了在固定 $  \alpha = \gamma = 1  $ 的情况下，不同耦合常数 $  \beta  $ 下孤立顶点比例 $  p_0  $ 的变化。结果表明，更强的非线性相互作用，即更大的 $  \beta  $，对应更大的 $  p_0  $，从而产生更小的潜热。因此，一级DPT有可能在强耦合极限下转变为连续相变（continuous phase transition）。

[第4页，第13段]
临界行为也反映在其他物理量中。例如，考虑顶点 $  i  $ 的局部聚类系数（local clustering coefficient）$  C_i := \sum_{j,k} A_{ij} A_{jk} A_{ki} / k_i (k_i - 1)  $ [43,44]。在 $  t_c  $ 附近，非线性相互作用变得占主导地位。四次相互作用（quartic interaction）意味着新三角形的数量近似随新边的数量线性增加。因此，连接到顶点 $  i  $ 的三角形数量与其度成正比，即 $  \sum_{j,k} A_{ij} A_{jk} A_{ki} \sim k_i  $。等价地，这导致当 $  t \to t_c  $ 时，$  C \sim (1/k)  $。这一理论预测得到了数值模拟的证实，如图4(d)所示。这种标度关系常见于具有模块化结构（modular structure）的网络中，正如许多通常由层次机制（hierarchical mechanism）[45,46]生成的现实世界网络中所观察到的那样。值得注意的是，在不依赖任何这些假设的情况下，

[第5页，第1段]
DPT（动力学相变）的临界行为自然遵循相同的规律。

[第5页，第2段]
**讨论**——我们在非平衡网络动力学中发现了一种DPT，这种现象在已知的增长模型（如三元闭包模型[47]和复制模型[48]）中并不存在，这些模型未表现出有限时间奇异性。虽然我们主要关注非平衡动力学，但系统在$t \to \infty$时达到的渐近稳态与常见的平衡系综密切相关。在最简单的线性情况（$\beta = 0$）下，稳态分布与Erdős-Rényi系综一致；而在非线性相互作用（$\beta > 0$）下，则与包含三角形项（triangle terms）的Strauss型模型[49–51]相关联（参见补充材料[38]第1.3节）。这些渐近态从稀疏到稠密的转变与Strauss凝聚（Strauss condensation）现象一致。

[第5页，第3段]
另一方面，Strauss型模型通常会坍缩为均匀稠密结构，仅在临界点附近表现出异质性。相比之下，在我们的模型中，异质性在达到平衡之前就动态出现，并在临界时间$t_c$处导致有限时间奇异性，这与先前在平衡或增长模型[47–53]中研究的转变有本质区别。

[第5页，第4段]
这一视角也阐明了我们的结果对真实系统的适用性。在金融危机、流行病暴发、基础设施故障或社会动荡等情境中，干预通常发生在不稳定性出现之后，因此系统可能永远无法达到其渐近平衡态。实证研究[19]表明，在线社交动力学中的密度类测量（densitylike measures）表现出与方程(1)一致的双曲发散（hyperbolic divergence）。这一观察结果自然可由我们的理论预测（方程(5)）解释，凸显了瞬态非平衡动力学的核心作用以及有限时间奇异性的可能性。更广泛地说，我们的结果表明，动力学网络模型为捕捉复杂系统中的有限时间临界现象提供了自然框架。这种从平衡系综视角无法观察到的行为，可能在理解现实世界中多种领域的突然不稳定性中发挥核心作用。

[第5页，第5段]
最后，这种最小经典设定中DPT的出现也暗示了与量子动力学相变（quantum dynamical phase transitions）的有趣相似性。在量子系统中，演化算符（evolution operator）$U = e^{-\int Hdt}$ 是理解相变的核心，它将时间依赖率函数（time-dependent rate function）的非解析性与$U$的特征值联系起来。在经典系统中，尽管缺乏幺正性（unitarity），演化算符的谱可能扮演类似角色。我们的最小模型为经典系统中出现DPT提供了具体实例，揭示了与量子DPT的相似性。SD方程（SD equation）作为捕捉非平衡动力学的强大工具，可能成为分析经典和量子DPT的统一框架，如本快报及量子DPT研究[54]所示。

[第5页，第6段]
**致谢**——C. S. 部分受美国国家科学基金会（National Science Foundation）资助（项目编号：2150830和IBSS-1620294）、美国教育科学研究院（Institute of Education Sciences）资助（项目编号：R324A180203）、美国国立卫生研究院（National Institutes of Health）资助（项目编号：R01DC018542）以及西蒙斯基金会自闭症研究计划（Simons Foundation Autism Research Initiative）资助（项目编号：SFI-AR-HUMAN-00004115-01）。

[第5页，第7段]
J. L. 和 N. A. 对本文贡献相同。

[第5页，第8段]
**数据可用性**——支持本文结论的模拟代码已公开[55]。

[第5页，第9段]
[1] M. Heyl, Rep. Prog. Phys. 81, 054001 (2018).
[2] M. Eckstein, M. Kollar, and P. Werner, Phys. Rev. Lett. 103, 056403 (2009).
[3] J. P. Garrahan and I. Lesanovsky, Phys. Rev. Lett. 104, 160601 (2010).

[第6页，第1段]
[4] S. Diehl, A. Tomadin, A. Micheli, R. Fazio, and P. Zoller, Phys. Rev. Lett. 105, 015702 (2010).
[5] B. Sciolla and G. Biroli, J. Stat. Mech. (2011) P11003(R).
[6] B. Sciolla and G. Biroli, Phys. Rev. B 88, 201110 (2013).
[7] E. Canovi, P. Werner, and M. Eckstein, Phys. Rev. Lett. 113, 265702 (2014).
[8] A. Maraga, P. Smacchia, and A. Silva, Phys. Rev. B 94, 245122 (2016).
[9] J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker, H. Kaplan, A. V. Gorshkov, Z.-X. Gong, and C. Monroe, Nature (London) 551, 601 (2017).
[10] M. Heyl, A. Polkovnikov, and S. Kehrein, Phys. Rev. Lett. 110, 135704 (2013).
[11] J. Meibohm and M. Esposito, Phys. Rev. Lett. 128, 110603 (2022).
[12] J. Meibohm and M. Esposito, New J. Phys. 25, 023034 (2023).
[13] Y. Tang, J. Liu, J. Zhang, and P. Zhang, Nat. Commun. 15, 1117 (2024).
[14] L. Xu, D. Patterson, S. A. Levin, and J. Wang, Proc. Natl. Acad. Sci. U.S.A. 120, e2218663120 (2023).
[15] H. Fan, L.-W. Kong, X. Wang, A. Hastings, and Y.-C. Lai, Natl. Sci. Rev. 8, nwaa269 (2021).
[16] R. H. Heiberger, Physica (Amsterdam) 393A, 376 (2014).
[17] L. Gao, C. Song, Z. Gao, A.-L. Barabási, J. P. Bagrow, and D. Wang, Sci. Rep. 4, 3997 (2014).
[18] P. Fairley, IEEE Spectrum 41, 22 (2004).
[19] N. F. Johnson, M. Zheng, Y. Vorobyeva, A. Gabriel, H. Qi, N. Velásquez, P. Manrique, D. Johnson, E. Restrepo, C. Song et al., Science 352, 1459 (2016).
[20] N. F. Johnson, R. Leahy, N. J. Restrepo, N. Velásquez, M. Zheng, P. Manrique, P. Devkota, and S. Wuchty, Nature (London) 573, 261 (2019).
[21] P. D. Manrique, M. Zheng, Z. Cao, E. M. Restrepo, and N. F. Johnson, Phys. Rev. Lett. 121, 048301 (2018).
[22] N. F. Johnson, N. Velásquez, N. J. Restrepo, R. Leahy, N. Gabriel, S. El Oud, M. Zheng, P. Manrique, S. Wuchty, and Y. Lupu, Nature (London) 582, 230 (2020).
[23] P. Dasgupta and E. Maskin, Am. Econ. Rev. 95, 1290 (2005).
[24] D. Laibson, Q. J. Econ. 112, 443 (1997).
[25] L. Karp, J. Public Econ. 89, 261 (2005).
[26] P. Diamond and B. Köszegi, J. Public Econ. 87, 1839 (2003), https://www.sciencedirect.com/science/article/abs/pii/S0047272702000415.
[27] T. Durakiewicz, Phys. Today 69, No. 2, 11 (2016).
[28] P. L. Krapivsky, S. Redner, and E. Ben-Naim, A Kinetic View of Statistical Physics (Cambridge University Press, Cambridge, England, 2010).
[29] F. Radicchi, C. Castellano, A. Flammini, M. A. Muñoz, and D. Notarmuzi, Phys. Rev. Res. 2, 033171 (2020).
[30] S. Liang, P. De Los Ríos, and D. M. Busiello, Phys. Rev. Lett. 132, 228402 (2024).

[第6页，第2段]
[31] J. Moran, M. Romeijnders, P. L. Doussal, F. P. Pijpers, U. Weitzel, D. Panja, and J.-P. Bouchaud, Nat. Phys. 20, 1352 (2024).
[32] P. Bak, How Nature Works: The Science of Self-Organized Criticality (Springer Science & Business Media, New York, 2013).
[33] P. Bak, K. Chen, and M. Creutz, Nature (London) 342, 780 (1989).
[34] P. Bak, C. Tang, and K. Wiesenfeld, Phys. Rev. A 38, 364 (1988).
[35] B. Vidiella, A. Guillamon, J. Sardanyés, V. Maull, J. Pla, N. Conde, and R. Solé, Nat. Commun. 12, 4415 (2021).
[36] D. Garlaschelli, A. Capocci, and G. Caldarelli, Nat. Phys. 3, 813 (2007).
[37] H. Sun, F. Radicchi, J. Kurths, and G. Bianconi, Nat. Commun. 14, 1308 (2023).
[38] 参见补充材料（Supplemental Material），网址：http://link.aps.org/supplemental/10.1103/lys4-kdvj，以获取更多推导和模拟细节。
[39] R. Lambiotte, P. L. Krapivsky, U. Bhat, and S. Redner, Phys. Rev. Lett. 117, 218301 (2016).
[40] G. Palla, I. Derényi, I. Farkas, and T. Vicsek, Nature (London) 435, 814 (2005).
[41] A.-L. Barabási and R. Albert, Science 286, 509 (1999).
[42] R. Albert and A.-L. Barabási, Rev. Mod. Phys. 74, 47 (2002).
[43] D. J. Watts and S. H. Strogatz, Nature (London) 393, 440 (1998).
[44] A. Allard, M. Á. Serrano, and M. Boguñá, Nat. Phys. 20, 150 (2024).
[45] E. Ravasz and A.-L. Barabási, Phys. Rev. E 67, 026112 (2003).
[46] E. Ravasz, A. L. Somera, D. A. Mongru, Z. N. Oltvai, and A.-L. Barabási, Science 297, 1551 (2002).
[47] G. Bianconi, R. K. Darst, J. Iacovacci, and S. Fortunato, Phys. Rev. E 90, 042806 (2014).
[48] I. Ispolatov, P. L. Krapivsky, and A. Yuryev, Phys. Rev. E 71, 061911 (2005).
[49] D. J. Strauss, Biometrika 62, 467 (1975).
[50] Z. Burda, J. Jurkiewicz, and A. Krzywicki, Phys. Rev. E 69, 026106 (2004).
[51] G. Bianconi, Phys. Rev. E 105, 034310 (2022).
[52] D. Achlioptas, R. M. D’souza, and J. Spencer, Science 323, 1453 (2009).
[53] R. A. da Costa, S. N. Dorogovtsev, A. V. Goltsev, and J. F. F. Mendes, Phys. Rev. Lett. 105, 255701 (2010).
[54] S. Banerjee and E. Altman, Phys. Rev. B 95, 134302 (2017).
[55] J. Liu, N. M. Aden, D. Sarker, and C. Song, 模拟代码（Simulation code），用于“非平衡网络中的动力学相变”（Dynamical Phase Transitions in Nonequilibrium Networks），GitHub仓库，2025年，https://github.com/jay83780323/DPT。