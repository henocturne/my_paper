[第1页，第1段]
演化时间尺度与流行病时间尺度的相互作用挑战控制政策的效果

[第1页，第2段]
Santiago Lamata-Otín\textsuperscript{©},\textsuperscript{1,2} Alex Arenas\textsuperscript{©}, \textsuperscript{3,4,5,6} Jesús Gómez-Gardeñes\textsuperscript{©}, \textsuperscript{1,2,7} 和 David Soriano-Paños\textsuperscript{©}\textsuperscript{3,2,8}

[第1页，第3段]
\textsuperscript{1}凝聚态物理系，萨拉戈萨大学，50009 萨拉戈萨，西班牙
\textsuperscript{2}GOTHAM 实验室，生物计算与复杂系统物理研究所 (BIFI)，萨拉戈萨大学，50018 萨拉戈萨，西班牙
\textsuperscript{3}计算机工程与数学系，罗维拉-威尔吉利大学，43007 塔拉戈纳，西班牙
\textsuperscript{4}太平洋西北国家实验室，902 Battelle Boulevard，里奇兰，华盛顿 99354，美国
\textsuperscript{5}维也纳复杂性科学中心，Metternichgasse 8，1030 维也纳，奥地利
\textsuperscript{6}ComSCIAM，罗维拉-威尔吉利大学，43007 塔拉戈纳，西班牙
\textsuperscript{7}计算社会科学中心，神户大学，657-8501 神户，日本

[第1页，第4段]
\textsuperscript{©}（收稿日期：2026年3月16日；接受日期：2026年8月31日；发表日期：2026年9月22日）

[第1页，第5段]
经典 SIR 模型假设病毒性状恒定，是计算疫情暴发期间关键指标（如预期感染峰值或控制政策的影响）的基石模型。据报道，病毒演化挑战了 SIR 模型的物理基础，改变了流行病转变的性质或暴发的早期动力学。在此，我们考虑 SIR 模型的一个最小扩展，允许传染性演化，以探索后一机制如何影响上述两个指标。我们表明，演化导致流行病峰值随基本传染数呈现非单调行为，并削弱了控制政策的影响，因为过早解除干预可能导致比不采取行动更糟糕的流行病情景。我们推导了支配这一行为的临界突变率和干预时间的解析表达式，并识别出控制策略之间的强烈不对称性：缩短传染期能在不抑制病毒传染性演化的前提下阻碍传播，而降低传播既能减少病例又能减缓这种演化。

[第1页，第6段]
DOI: 10.1103/56vdf-sfks

[第1页，第7段]
\textbf{引言}——传染病的动力学源于病原体性状与宿主群体之间的相互作用 [1,2]。经典流行病模型，如易感-感染-恢复 (SIR) 框架 [3,4]，在理解疫情动力学和指导近期大流行期间控制策略的设计方面发挥了重要作用 [5–8]。近期的理论研究 [9–14]，特别是 Morris 等人 [15] 的工作，进一步分析了简单的固定强度干预如何能够成为稳健且近乎最优的控制策略。

[第1页，第8段]
这些方法的一个关键基本假设是病原体性状在疫情暴发过程中保持有效恒定。然而，许多病原体的演化时间尺度与流行病传播相当，因此突变可以直接影响流行病动力学 [16–20]。控制政策对病毒演化的影响主要在双毒株背景下得到研究，从解析角度刻画了干预措施如何改变突变体在宿主内 [21–24] 和群体水平 [25–27] 上的出现、存活和免疫逃逸概率。在双毒株背景之外，系统发育动力学方法已证明，在分别用于遏制埃博拉 [28] 或 COVID-19 疫情 [29,30] 的非药物干预措施实施后，埃博拉病毒和甲型流感病毒的演化轨迹发生了实质性改变。

[第1页，第9段]
关于病毒演化如何在多毒株背景下塑造流行病轨迹的理论研究在文献中探索得少得多 [31,32]。据报道，演化在 SIR 模型中诱导疫情的超指数增长或突发的流行病转变 [31]；然而，演化对关键指标（如感染峰值或控制政策的影响）的影响仍然是一个理论挑战。在本快报中，我们在 SIR 模型的一个最小扩展中解决这些问题，其中传染性是一个演化的病原体性状 [31]。我们表明，演化逆转了流行病峰值对基本传染数的单调依赖性以及流行病控制政策的短期收益。我们还发现，在演化下，塑造宿主内或宿主间动力学的干预措施产生强烈不对称的结果。因此，我们的结果表明，流行病控制与病原体演化本质上是耦合的，因此对于快速演化的病毒应联合研究。

[第1页，第10段]
\textbf{具有传染性演化的流行病建模}——我们考虑 SIR 模型的一个最小扩展，其中个体要么是易感者 (S)、感染者 (I)，要么是恢复者 (R)，并且传染性是一个演化性状 [见图 1(a)]。对于传染，我们假设感染者每个时间步进行 $k$ 次接触，传播其

[第2页，第1段]
相关菌株以概率 $\lambda$ 传染给易感接触者，下文将该概率称为该菌株的传染力。我们假设存在竞争排斥机制，因此忽略多种菌株的共感染。遵循 [31–34]，传染力在一维性状空间中通过大小为 $\pm \Delta\lambda$ 的对称突变进行演化，突变发生率为 $D$。最后，感染者以速率 $\mu$ 康复，进入 R  compartment。我们系统的流行病状态由感染者在性状空间上的概率密度 $\rho_I(\lambda, t)$ 和全球康复者比例 $r(t)$ 来表征。考虑上述规则，这些量的时间演化为，

[第2页，第2段]
$$\frac{\partial \rho_I(\lambda, t)}{\partial t} = k\lambda \rho_I(\lambda, t) s(t) - \mu \rho_I(\lambda, t) + \frac{D}{2} \frac{\partial^2 \rho_I(\lambda, t)}{\partial \lambda^2}, \tag{1}$$

[第2页，第3段]
$$\frac{dr(t)}{dt} = \mu i(t), \tag{2}$$

[第2页，第4段]
其中 $i(t) = \int d\lambda \rho_I(\lambda, t)$ 和 $s(t) = 1 - i(t) - r(t)$ 分别是时间 $t$ 的疾病流行率和易感个体比例。为数学方便，我们使用了有效扩散率 $\mathcal{D} = D(\Delta\lambda)^2$，该量在保持 $D(\Delta\lambda)^2$ 不变的 $D$ 和 $\Delta\lambda$ 重缩放变换下保持不变（见补充材料注释 1 [35]）。

[第2页，第5段]
方程 (1) 是性状空间中的反应扩散方程，在结构上等价于时间依赖选择系数下的复制子-突变子动力学（见补充材料注释 1 [35]）。特别地，第一项通过传播选择具有较大 $\lambda$ 的菌株，这由整个动力学过程中易感个体池 $s(t)$ 的耗竭所介导。相反，最后一项显示了突变动力学如何转化为感染者在性状空间中的扩散。

[第2页，第6段]
**传染力演化对流行病轨迹的影响**——为表征流行病轨迹，我们监测流行病流行率 $i(t)$ 和相关基本传染数的随时间演化，后者定义为

[第2页，第7段]
$$\mathcal{R}_0(t) = \frac{k\lambda(t)}{\mu}, \tag{3}$$

[第2页，第8段]
其中平均传染力为

[第2页，第9段]
$$\bar{\lambda}(t) = \frac{\int d\lambda \lambda \rho_I(\lambda, t)}{i(t)}. \tag{4}$$

[第2页，第10段]
除非另有说明，这两个量均通过方程 (1) 和 (2) 的数值积分获得，假设初始条件为单一菌株的基本传染数 $\mathcal{R}_0 = 2$，感染人群的极小比例 $i_0 = 10^{-3}$，其中 $\mu = 1/7$ 天$^{-1}$，$k = 10$ 次接触/天。对于演化，我们假设性状空间的离散表示为 $\Delta\lambda = 10^{-3}$（见补充材料注释 1 [35]）。

[第2页，第11段]
**传染力演化在定性上重塑了流行病轨迹**，诱导了超指数增长，提前了流行病峰值并增加了其幅度 [图 1(b)]。此外，图 1(c) 显示传染力演化呈现初始的超线性增长，随后出现弯曲并在后期阶段减缓。这两个结果都可以从平均传染力的动力学进行解析理解。在补充材料注释 2 [35] 中，我们展示了对 Eq. (4) 求导可得

[第2页，第12段]
$$\frac{d\bar{\lambda}}{dt} = ks(t) \text{ Var}(\lambda), \tag{5}$$

[第2页，第13段]
其中 $\text{Var}(\lambda)$ 是考虑性状间流行率分布 $\rho_I(\lambda, t)$ 时 $\lambda$ 值的方差。扩散贡献产生 $\text{Var}(\lambda) \simeq Dt$。对于早期动力学，可以假设 $s(t) \simeq 1$。结合这两个假设，我们可以积分 Eq. (5)，得到

[第2页，第14段]
$$\bar{\lambda}(t)|_{t \to 0} = \lambda_0 + \frac{1}{2} kDt^2, \tag{6}$$

[第2页，第15段]
这直接转化为流行率的超指数增长，

[第2页，第16段]
$$i(t)|_{t \to 0} = i_0 \exp \left[ \mu (\mathcal{R}_0 - 1)t + \frac{k^2 D}{6} t^3 \right]. \tag{7}$$

[第2页，第17段]
注意，与

[第3页，第1段]
标准SIR模型。方程(6)和(7)准确地捕捉了图1(b)和1(c)中的早期动力学。随着疫情的发展，易感者耗竭减缓了$\tilde{\lambda}(t)$的增长，产生了图1(c)中观察到的弯曲（详见附录A）。

[第3页，第2段]
**传染性演化对疫情控制的影响**——疫情峰值$i_{\text{max}}$是数学流行病学中的一个关键量，因为它表明疫情期间卫生系统承受的最大压力。图1(d)展示了SIR模型的疫情转变如何被演化强烈改变。在没有演化的情况下，即$D = 0$，疫情暴发通过$\mathcal{R}_0 = 1$处的二阶相变发生；而增大$D$会导致在更低的$\mathcal{R}_0$值处发生突发的疫情转变。这是因为传染性演化在暴发期间增强了传播能力，即使从边缘可传播的毒株开始，也能有效地将动力学推入经典SIR相图的超临界区域[31]。注意，在较低的有限$\mathcal{R}_0$值处出现转变是因为我们假设有限种群并设定了流行率阈值$i(t) = 10^{-4}$，低于此阈值疫情即灭绝；在无限种群中，对于有限$D$，活跃相延伸至$\mathcal{R}_0 = 0$（见补充材料注3 [35]）。

[第3页，第3段]
此外，图1(d)还揭示了$i_{\text{max}}$与$\mathcal{R}_0$之间的非单调依赖关系，这意味着轻度传染性病原体由于演化可能导致更严重的疫情情景。这是因为这些病毒在低流行率值下开始演化，持续时间更长而不耗竭易感者池，使得传染性分布变宽并产生高$\lambda$变异株，随后被传播选择（见补充材料注3 [35]）。

[第3页，第4段]
后一结果对控制政策的短期效益提出了警示，因为降低基本再生数可能导致更严重的疫情情景。我们现在通过探讨控制政策对我们模型疫情曲线的影响来解决这一问题。我们的干预措施由两个参数表征[15]：干预持续时间$\tau$及其强度$\epsilon$。即，我们的干预在干预时间$\tau$内重新缩放再生数，即$\mathcal{R}_0(t) \to \epsilon \mathcal{R}_0(t)$，其中$\epsilon \in (0, 1)$。方程(3)表明这一目标可通过三种不同策略实现：(i) $\lambda$控制（将传播能力降低为$\lambda \to \epsilon \lambda$），(ii) $k$控制（将接触减少为$k \to \epsilon k$），以及(iii) $\mu$控制（通过$(\mu \to \mu / \epsilon)$缩短传染期）。前两种策略与宿主间传播事件相关，而最后一种干预旨在加速宿主体内的病毒清除。除非另有说明，我们设定$\epsilon = 0.6$并将$k$控制和$\lambda$控制联合处理，二者在模型中是等价的（见补充材料注4 [35]）。

[第3页，第5段]
在没有传染性演化的情况下，所有政策随着干预持续时间$\tau$的增加单调地降低疫情峰值[见图2(a)的$k$或$\lambda$控制以及图2(b)的$\mu$控制]，这意味着更长的干预总是有益的。然而，当考虑演化时，$i_{\text{max}}$成为$\tau$的非单调函数，先增加，达到最大值后减小。这种在控制政策持续时间较短时的非单调依赖关系也出现在感染率$r_{\infty}$中（见补充材料注5 [35]）。因此，过早解除控制政策可能导致比没有干预（$\tau = 0$）时更大的疫情峰值。注意，所有曲线最终都收敛到平台值，表明传染峰值$i_{\text{max}}$发生在受控阶段而非解除干预之后。

[第3页，第6段]
$i_{\text{max}}$对$\tau$的非单调依赖关系可以通过解析方法捕捉。如补充材料注4 [35]中所推导，干预下平均传染性的早期时间演化为

[第3页，第7段]
$$\bar{\lambda}(t, \epsilon)|_{t \to 0} = \lambda_0 + \frac{1}{2} \alpha k \mathcal{D} t^2, \quad (8)$$

[第3页，第8段]
其中对于$k, \lambda$控制，$\alpha = \epsilon$；对于$\mu$控制，$\alpha = 1$。因此，流行率动力学遵循

[第3页，第9段]
$$i(t, \epsilon)|_{t \to 0} = i_0 \exp \left[ \frac{\mu \alpha}{\epsilon} (\epsilon \mathcal{R}_0 - 1) t + \frac{\alpha^2 k^2}{6} D t^3 \right]. \quad (9)$$

[第3页，第10段]
我们可以通过将$i(\tau)$和$\lambda(\tau)$代入SIR模型疫情峰值的常用表达式来估计在$t = \tau$处解除干预后观察到的峰值，以下记为$i_{\text{max}}(\tau)$（详见附录B和补充材料注4 [35]）。对$i_{\text{max}}$关于$\tau$求导可得：

[第3页，第11段]
$$\frac{di_{\text{max}}}{d\tau} = -\mu i(\tau) \frac{(1 - \epsilon)}{\epsilon} + \frac{\alpha k^2}{\mu} D \tau \frac{\ln(\mathcal{R}_0(\tau) s(\tau))}{\mathcal{R}_0(\tau)^2}. \quad (10)$$

[第4页，第1段]
该表达式明确揭示了在短干预持续时间下，流行病学抑制（第一项）与进化放大（第二项）之间的竞争。特别地，给定干预持续时间 $\tau$，导数符号在临界扩散强度 $D_c$ 处发生变化（详见附录 C 和补充材料注释 4 [35]），这表明对于 $D < D_c$（$D > D_c$）的病毒，干预会改善（恶化）疫情情景。

[第4页，第2段]
考虑 $D > D_c$，我们还可以估计产生最坏疫情情景的干预持续时间 $\tau^\star$，即疫情峰值 $i_{\text{max}}$ 的最大值。令 $(di_{\text{max}}/d\tau)|_{\tau=\tau^\star} = 0$ 可得（详见补充材料注释 4 [35]）

[第4页，第3段]
$$\tau^\star \simeq \left[-\frac{1}{3BD}W_{-1}\left(-\frac{3B\mu^3(1-\epsilon)^3i_0^3}{\epsilon^3C^3D^2}\right)\right]^{1/3},$$  \hspace{1cm} (11)

[第4页，第4段]
其中 $B = \alpha^2k^2/6$，$C = k^2\ln R_0/(\mu R_0^2)$。$W_{-1}$ 表示 Lambert 函数 $W$ 的其中一个分支，满足 $W(z)e^{W(z)} = z$。所得解析预测与数值模拟在定量上一致（见图 2 中的插图），特别是在 $D$ 值较大时，此时由于病毒在控制下的进化，特征动力学时间尺度缩短，因此解除干预后的进化可以忽略。后者在较低的 $D$ 值下不会发生，此时解除干预后的进化变化对 $\tau^\star$ 值起决定性作用。为完整起见，在补充材料注释 6 [35] 中，我们评估了基本再生数 $R_0$、政策强度 $\epsilon$、干预激活阈值（由时间延迟或流行率触发）以及可能对较低传染性值的负向偏差的影响，表明这种非单调行为是稳健的。

[第4页，第5段]
控制政策塑造宿主间或宿主内动力学的非对称效应——比较图 2(a) 和 2(b)，我们观察到 $k, \lambda$ 控制与 $\mu$ 控制之间存在差异。在不存在传染性进化的情况下，即通常的 SIR 模型，缩短传染期比降低传播率产生更小的解除干预后峰值。我们观察到，传染性进化在短干预下放大了这一效应，而在较长干预下可能逆转这一效应，如图 2(b) 中 $D = 2 \times 10^{-7}$ 时出现的次级峰所示。

[第4页，第6段]
干预措施之间的差异影响在图 3(a) 中明确展示，该图显示了 $\Delta i_{\text{max}} = i_{\text{max}}^{(k,\lambda)} - i_{\text{max}}^{(k,\mu)}$。考虑一个恒定的 $D$ 值，例如 $D = 10^{-6}$，我们首先观察到增加 $\tau$ 会导致从两种干预措施的相似结果（$\Delta i_{\text{max}} \simeq 0$）转变为 $k, \lambda$ 控制后相比 $\mu$ 控制后观察到的疫情峰值大幅增大。注意，这种转变在不存在进化时（即非常低的 $D$ 值）也会出现，但进化加剧了这种转变并使其提前发生。

[第4页，第7段]
为了深入了解这一转变，我们展示了 $\tau = 30$ 天 [图 3(b)] 和 $\tau = 75$ 天 [图 3(c)] 的疫情轨迹 $i(t)$ 以及基本再生数 $R_0(t)$ 和易感人群 $s(t)$ 的演变。比较易感人群曲线，我们可以观察到 $\mu$ 控制触发的疫情时间尺度加速如何导致更快的

[第5页，第1段]
易感人群库的耗竭。虽然这种更快的耗竭对于非常短的干预来说并不显著[图3(b)]，但一旦达到$\mu$控制流行病曲线的峰值，它就变得明显了[图3(c)]。在这种情况下，耗尽的易感人群库阻止了另一次大规模爆发的出现，正如在$k, \lambda$控制的情况下所观察到的那样。利用这一直觉，强不对称区域应由那些对两种干预都产生最高流行病峰值的干预时间来界定，即$\tau_{\mu}^\star$和$\tau_{k,\lambda}^\star$。因此，我们可以使用每种政策的$\alpha$值，通过Eq. (11)来计算它们。图3(a)中的红色虚线显示，我们对该区域的理论边界与数值模拟结果之间有相当好的一致性。

[第5页，第2段]
图3(a)还表明，更长的干预时间和中等的进化速率会逆转控制政策的不对称结果，产生$\mu$控制策略更高的峰值，即$\Delta i_{\text{max}} \leq 0$。为了理解这一现象，我们考虑$\tau = 200$，并分别假设$D = 10^{-8}$[图3(d)]和$D = 10^{-7}$[图3(e)]来绘制流行病和进化曲线。在两种情况下，$s(t)$都无法解释这种不等的结果，因为易感人群库只是部分耗竭，且每种策略的规模相似。我们反而应该关注不同控制政策如何塑造病毒的进化。虽然$\mu$控制产生的$\mathcal{R}_0$早期进化与未控制情况相同，但$k, \lambda$控制减缓了病毒进化。Eq. (8)捕捉到了这一差异，编码在参数$\alpha$中，理论线与数值结果在爆发早期阶段有相当好的一致性。

[第5页，第3段]
因此，对于中等进化速度，即$D \sim 10^{-7}$，在$t = \tau$时，易感人群库很大，且各策略之间规模相似。然而，$\mu$控制下的病毒比$k, \lambda$控制下的病毒具有高得多的传染性，从而解释了二次爆发中更高的流行病峰值[36]。注意，这种行为不会出现在更快的进化速率下，因为它们会导致易感人群更大程度的耗竭，观察不到任何二次峰值。

[第5页，第4段]
结论——我们已经表明，允许病原体传染性进化会从根本上重塑流行病动力学和控制策略的有效性。传染（选择）与突变（扩散）之间的相互作用导致了超指数级的早期流行率增长。这种动力学行为已在理论上对流行病进行了预测[31]，并在流感爆发的经验数据中有所报道[37]，尽管当时被归因于不同的潜在机制。加速增长率也在其他生物动力学中被观察到[38]，如肿瘤生长[39]或细菌增殖[40]。该模型还显示出突发的流行病转变[31]，将性状进化定位为传染动力学中爆炸性转变的额外途径[41–43]。

[第5页，第5段]
当纳入控制措施时，这些进化效应会导致性质上不同且反直觉的结果。特别是，感染率和流行病峰值都非单调地依赖于干预持续时间，这意味着过早解除干预可能比什么都不做更糟糕地恶化流行病结果。这种非单调行为对于流行病峰值是单峰的，但对于感染率则呈现多个局部最大值（见补充材料注释5 [35]）；因此，为了全面理解控制政策如何塑造流行病爆发的影响和进化，应计算多个流行病学指标[14]。

[第5页，第6段]
此外，我们发现了控制策略之间的不对称性：在传染性进化存在的情况下，作用于传播参数的干预和缩短传染期的干预不再等效。缩短传染期，例如通过给药，会加速流行病时间尺度而不减缓传染性进化，而作用于宿主间传播则同时减缓流行率和传染性增长。因此，控制策略的相对有效性可能会被逆转：在非进化环境中看似最优的政策，一旦考虑进化效应，就可能变得适得其反，特别是当干预在第一次流行病峰值后被解除时。

[第5页，第7段]
总体而言，使用这个最小模型，我们揭示了宿主内突变动力学与群体水平流行病控制之间自然的多尺度耦合，这决定了新出现变异的选择，从而决定了病毒进化。尽管模型简单，但我们的发现相当普遍，预计会出现在更具生物学基础的模型中，包括互补的进化途径，如抗原漂移[32,44–46]或随时间变化的恢复率、宿主内动力学的详尽描述[47,48]，或限制病毒进化的进化权衡[49–51]。

[第5页，第8段]
致谢——S. L. O.和J. G. G.感谢Departamento de Industria e Innovación del Gobierno de Aragón y Fondo Social Europeo（FENOL group Grant No. E36-23R）和Ministerio de Ciencia e Innovación（Grant No. PID2023-147734NB-I00）的财政支持。S. L. O.感谢Gobierno de Aragón通过博士奖学金提供的财政支持。A. A.和D. S.-P感谢Spanish Ministerio de Ciencia e Innovación（PID2024-158120NB-C21）。A. A.感谢Generalitat de Catalunya（2021SGR-00633）、Universitat Rovira i Virgili（2023PFR-URV-00633）、European Union’s Horizon Europe Programme under the CREXDATA project（Grant No. 101092749）、ICREA Academia、the James S. McDonnell Foundation（Grant No. 220020325）以及Pacific Northwest National Laboratory（PNNL）的Joint Appointment Program。PNNL是为美国运营的多项目国家实验室。

[第6页，第1段]
美国能源部（DOE），由巴特尔纪念研究所根据合同号DE-AC05-76RL01830执行。

[第6页，第2段]
数据可用性——重现本快报所报告结果的代码可在[52]处获取。

[第6页，第3段]
[1] M. J. Keeling and P. Rohani, *人类与动物传染病建模*（普林斯顿大学出版社，普林斯顿，新泽西州，2008年）。

[第6页，第4段]
[2] R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani, *复杂网络中的流行病过程*, Rev. Mod. Phys. 87, 925 (2015)。

[第6页，第5段]
[3] W. O. Kermack and A. G. McKendrick, 对流行病数学理论的贡献, Proc. R. Soc. A 115, 700 (1927)。

[第6页，第6段]
[4] H. W. Hethcote, 传染病的数学, SIAM Rev. 42, 599 (2000)。

[第6页，第7段]
[5] S. Flaxman, S. Mishra, A. Gandy, H. J. T. Unwin, T. A. Mellan, H. Coupland, C. Whittaker, H. Zhu, T. Berah, J. W. Eaton et al., 估计非药物干预措施对欧洲COVID-19的影响, Nature (London) 584, 257 (2020)。

[第6页，第8段]
[6] S. Hsiang, D. Allen, S. Annan-Phan, K. Bell, I. Bolliger, T. Chong, H. Druckenmiller, L. Y. Huang, A. Hultgren, E. Krasovich et al., 大规模抗传染政策对COVID-19大流行的影响, Nature (London) 584, 262 (2020)。

[第6页，第9段]
[7] S. M. Kissler, C. Tedijanto, E. Goldstein, Y. H. Grad, and M. Lipsitch, 预测SARS-CoV-2在大流行后时期的传播动态, Science 368, 860 (2020)。

[第6页，第10段]
[8] A. Arenas, W. Cota, J. Gómez-Gardeñes, S. Gómez, C. Granell, J. T. Matamalas, D. Soriano-Paños, and B. Steinegger, 建模COVID-19的时空流行病传播及流动性和社交距离干预措施的影响, Phys. Rev. X 10, 041055 (2020)。

[第6页，第11段]
[9] F. Di Lauro, I. Z. Kiss, and J. C. Miller, 流行病控制中一次性干预措施的最优时机, PLoS Comput. Biol. 17, e1008763 (2021)。

[第6页，第12段]
[10] P.-A. Bliman, M. Duprez, Y. Privat, and N. Vauchelet, SIR流行病模型通过社交距离实现的最优免疫控制和最终规模最小化, J. Optim. Theory Appl. 189, 408 (2021)。

[第6页，第13段]
[11] D. I. Ketcheson, 通过有限时间非药物干预对SIR流行病的最优控制, J. Math. Biol. 83, 7 (2021)。

[第6页，第14段]
[12] T. A. Perkins and G. España, 非药物干预措施下COVID-19大流行的最优控制, Bull. Math. Biol. 82, 118 (2020)。

[第6页，第15段]
[13] J. Hindes and I. B. Schwartz, 异质网络中的流行病灭绝与控制, Phys. Rev. Lett. 117, 028302 (2016)。

[第6页，第16段]
[14] E. Rozán, M. N. Kuperman, and S. Bouzat, 用SIR流行病模型分析非药物干预措施：降低感染峰值与最小化流行病规模, arXiv:2604.08420。

[第6页，第17段]
[15] D. H. Morris, F. W. Rossine, J. B. Plotkin, and S. A. Levin, 最优、近最优和稳健的流行病控制, Commun. Phys. 4, 78 (2021)。

[第6页，第18段]
[16] B. T. Grenfell, O. G. Pybus, J. R. Gog, J. L. Wood, J. M. Daly, J. A. Mumford, and E. C. Holmes, 统一病原体的流行病学和进化动力学, Science 303, 327 (2004)。

[第6页，第19段]
[17] R. M. Anderson and R. M. May, *人类传染病：动力学与控制*（牛津大学出版社，牛津，1991年）。

[第6页，第20段]
[18] T. Day and S. Gandon, 在理论进化流行病学中应用群体遗传学模型, Ecol. Lett. 10, 876 (2007)。

[第6页，第21段]
[19] S. Lion and J. A. Metz, 超越$R_0$最大化：论病原体进化和环境维度, Trends Ecol. Evol. 33, 458 (2018)。

[第6页，第22段]
[20] L. S. Tsimring, H. Levine, and D. A. Kessler, 通过适应度空间模型的RNA病毒进化, Phys. Rev. Lett. 76, 4440 (1996)。

[第6页，第23段]
[21] Y. Iwasa, F. Michor, and M. A. Nowak, 逃逸生物医学干预的进化动力学, Proc. R. Soc. B 270, 2573 (2003)。

[第6页，第24段]
[22] Y. Iwasa, F. Michor, and M. A. Nowak, 入侵与逃逸的进化动力学, J. Theor. Biol. 226, 205 (2004)。

[第6页，第25段]
[23] M. Hartfield and S. Alizon, 免疫逃逸突变体的宿主内随机出现动力学, PLoS Comput. Biol. 11, e1004149 (2015)。

[第6页，第26段]
[24] D. Van Egeren, A. Novokhodko, M. Stoddard, U. Tran, B. Zetter, M. S. Rogers, D. Joseph-McCarthy, and A. Chakravarty, 控制长期SARS-CoV-2感染可减缓病毒进化并降低治疗失败风险, Sci. Rep. 11, 22630 (2021)。

[第6页，第27段]
[25] M. Hartfield and S. Alizon, 流行病学反馈影响病原体的进化出现, Am. Nat. 183, E105 (2014)。

[第6页，第28段]
[26] M. T. Meehan, R. C. Cope, and E. S. McBryde, 论地方性流行环境中毒株入侵的概率：考虑多毒株动力学中的个体异质性和控制, J. Theor. Biol. 487, 110109 (2020)。

[第6页，第29段]
[27] B. Ashby, C. A. Smith, and R. N. Thompson, 非药物干预措施与病原体变异株的出现, Evol. Med. Public Health 11, 80 (2023)。

[第6页，第30段]
[28] S. Dellicour, G. Baele, G. Dudas, N. R. Faria, O. G. Pybus, M. A. Suchard, A. Rambaut, and P. Lemey, 西非埃博拉病毒暴发干预策略的系统动力学评估, Nat. Commun. 9, 2222 (2018)。

[第6页，第31段]
[29] Z. Chen, J. L.-H. Tsui, B. Gutierrez, S. Busch Moreno, L. Du Plessis, X. Deng, J. Cai, S. Bajaj, M. A. Suchard, O. G. Pybus et al., COVID-19大流行干预措施重塑了季节性流感病毒的全球传播, Science 386, eadq3003 (2024)。

[第6页，第32段]
[30] Z. Chen, J. L.-H. Tsui, J. Cai, S. Su, C. Viboud, L. Du Plessis, P. Lemey, M. U. Kraemer, and H. Yu, 2009年H1N1和COVID-19大流行期间东南亚季节性流感传播和进化的中断, Nat. Commun. 16, 475 (2025)。

[第6页，第33段]
[31] X. Zhang, Z. Ruan, M. Zheng, J. Zhou, S. Boccaletti, and B. Barzel, 相互独立的宿主内和宿主间病原体进化下的流行病传播, Nat. Commun. 13, 6218 (2022)。

[第6页，第34段]
[32] D. Soriano-Paños, 快速进化病毒地方性流行的生态进化约束, PRX Life 3, 043001 (2025)。

[第7页，第1段]
[33] I. M. Rouzine 和 G. Rozhnova，宿主种群中病毒的抗原进化，PLoS Pathogens 14, e1007291 (2018)。

[第7页，第2段]
[34] V. Chardès、A. Mazzolini、T. Mora 和 A. M. Walczak，抗原逃逸病毒的进化稳定性，Proc. Natl. Acad. Sci. U.S.A. 120, e2307712120 (2023)。

[第7页，第3段]
[35] 参见补充材料 http://link.aps.org/supplemental 1/10.1103/56yd-sfks，了解模型的更多细节、不同进化模型下控制策略非单调影响的鲁棒性分析，以及对该现象起源的进一步分析性见解。

[第7页，第4段]
[36] P. Castioni、S. Gómez、C. Granell 和 A. Arenas，流行病控制中的反弹：疫苗接种时机错位如何放大感染峰值，npj Complex 1, 20 (2024)。

[第7页，第5段]
[37] S. V. Scarpino、A. Allard 和 L. Hébert-Dufresne，审慎自适应行为对疾病传播的影响，Nat. Phys. 12, 1042 (2016)。

[第7页，第6段]
[38] R. Durrett、J. Foo、K. Leder、J. Mayberry 和 F. Michor，随机适应度值下肿瘤进展的进化动力学，Theor. Popul. Biol. 78, 54 (2010)。

[第7页，第7段]
[39] B. Ocaña-Tienda、J. Pérez-Beteta、J. Jiménez-Sánchez、D. Molina-García、A. Ortiz de Mendivil、B. Asenjo、D. Albillo、L. A. Pérez-Romasanta、M. Valiente、L. Zhu 等，生长指数反映脑转移中的进化过程和治疗反应，npj Syst. Biol. Appl. 9, 35 (2023)。

[第7页，第8段]
[40] A. Cylke 和 S. Banerjee，杆状细菌中的超指数生长和随机尺寸动力学，Biophys. J. 122, 1254 (2023)。

[第7页，第9段]
[41] R. M. D'Souza、J. Gómez-Gardenes、J. Nagler 和 A. Arenas，复杂网络中的爆炸性现象，Adv. Phys. 68, 123 (2019)。

[第7页，第10段]
[42] S. Lamata-Otín、J. Gómez-Gardenes 和 D. Soriano-Paños，相互作用传染动力学中不连续转变的路径，J. Phys. Complex. 5, 015015 (2024)。

[第7页，第11段]
[43] S. Lamata-Otín、A. Reyna-Lara、D. Soriano-Paños、V. Latora 和 J. Gómez-Gardenes，资源有限检测下流行病传播的崩溃转变，Phys. Rev. E 108, 024305 (2023)。

[第7页，第12段]
[44] A. Sasaki、S. Lion 和 M. Boots，抗原逃逸选择更高病原体传播和毒力的进化，Nat. Ecol. Evol. 6, 51 (2022)。

[第7页，第13段]
[45] S. Lamata-Otín、O. C. Rotita-Ion、A. Arenas、D. Soriano-Paños 和 J. Gómez-Gardenes，基因型网络驱动病毒进化中的振荡地方性和流行轨迹，Commun. Phys. 8, 502 (2025)。

[第7页，第14段]
[46] B. J. Williams、G. St-Onge 和 L. Hébert-Dufresne，具有潜在基因型网络的多毒株流行病的局部化、流行病转变和不可预测性，PLoS Comput. Biol. 17, e1008606 (2021)。

[第7页，第15段]
[47] N. Mideo、S. Alizon 和 T. Day，连接传染病进化流行病学中的宿主内和宿主间动力学，Trends Ecol. Evol. 23, 511 (2008)。

[第7页，第16段]
[48] F. Fabre、J. Montarry、J. Coville、R. Senoussi、V. Simon 和 B. Moury，模拟病毒在宿主内的进化动力学：使用高通量测序的案例研究，PLoS Pathogens 8, e1002654 (2012)。

[第7页，第17段]
[49] S. Alizon，研究寄生虫进化的传播-恢复权衡，Am. Nat. 172, E113 (2008)。

[第7页，第18段]
[50] J. C. De Roode、A. J. Yates 和 S. Altizer，天然存在的蝴蝶寄生虫中毒力-传播权衡和毒力的种群分化，Proc. Natl. Acad. Sci. U.S.A. 105, 7489 (2008)。

[第7页，第19段]
[51] M. A. Acevedo、F. P. Dillemuth、A. J. Flick、M. J. Faldyn 和 B. D. Elderd，疾病传播中毒力驱动的权衡：一项荟萃分析，Evolution 73, 636 (2019)。

[第7页，第20段]
[52] S. Lamata-Otín，SIRevolution，https://github.com/santiagolaot/SIRevolution (2026)。

[第7页，第21段]
结束语

[第7页，第22段]
附录 A：易感者耗竭的 S 形近似——为了分析易感者耗竭引起的平均感染性增长的减缓，我们用以流行病峰值为中心的 S 形函数近似易感者比例，$  s(t) \approx s(\infty) + (1 - s(\infty))/(1 + e^{\sigma(t - t_p)} )  $。将此表达式代入 Eq. (5) 并积分，得到中间时刻平均感染性演化的显式近似（见补充材料 Note 7 [35]）。保留峰值时间 $  t_p  $ 附近及之后时间的主要贡献，我们得到

[第7页，第23段]
$ 
\bar{\lambda}(t) \sim kD \left[ s(\infty) \frac{t^2}{2} - (1 - s(\infty)) \left( \frac{\sigma t + 1}{\sigma^2} e^{-\sigma(t - t_p)} \right) \right], \tag{A1}
 $

[第7页，第24段]
这明确显示了一个负的瞬态贡献，暂时阻碍了感染性的增长[见图 1(c)]。随着时间增加，指数项消失，动力学平滑过渡到由剩余易感者比例 $  s(\infty)  $ 控制的二次增长。

[第7页，第25段]
附录 B：推导流行病峰值的混合近似——为了评估感染性进化对控制策略有效性的影响，我们采用混合近似，其中干预窗口 $  t \in [0, \tau]  $ 内的流行病动力学遵循 $  i(t, \varepsilon)  $ 和 $  \bar{\lambda}(t, \varepsilon)  $ 的早期受控演化，而在解除干预后，疫情作为未受控的 SIR 过程演化，初始条件由 $  t = \tau  $ 时的状态给出（详见补充材料 Note 4 [35]）。

[第7页，第26段]
在此近似下，并假设流行病峰值出现在解除干预之后，干预后的峰值可以使用标准 SIR 结果 [43] 近似

[第7页，第27段]
$ 
i_{\text{max}}(\tau) \approx 1 - r(\tau) - \frac{1}{R_0(\tau)} \left[ 1 + \ln(R_0(\tau)s(\tau)) \right], \tag{B1}
 $

[第8页，第1段]
其中 $R_0(\tau) = k\lambda(\tau)/\mu$，$s(\tau) = 1 - i(\tau) - r(\tau)$。注意，该表达式是一个强假设，因为它忽略了演化对疫情峰值的影响；演化仅影响解除干预时的初始条件。

[第8页，第2段]
对式 (B1) 关于 $\tau$ 求导，并利用解除时刻受控动力学的表达式 [式 (8) 和 (9)]，可得到式 (10) 中给出的一般恒等式，该式明确地将直接的流行病学贡献与演化贡献分离开来。

[第8页，第3段]
**附录 C：临界有效扩散强度**——为了量化传染性演化何时会逆转疫情峰值对干预时长的单调依赖性，我们分析条件 $di_{\text{max}}/d\tau = 0$，该条件在式 (10) 中给出并在附录 B 中推导。令 $di_{\text{max}}/d\tau = 0$ 定义了临界有效扩散强度的隐式关系，

[第8页，第4段]
$$D_c(\tau) = \frac{\mu^2(1 - \epsilon)i(\tau)R_0(\tau)^2}{\epsilon k^2\tau\ln(R_0(\tau)s(\tau))}. \quad (C1)$$

[第8页，第5段]
假设解除时刻疫情流行率仍然很小，$i(\tau) \ll 1$，我们近似 $s(\tau) \approx 1$ 和 $\ln(R_0(\tau)s(\tau)) \approx \ln R_0$，并在其零阶值处计算对数项和前因子项，$R_0(\tau) \approx R_0$，同时仅通过 $i(\tau)$ 中的指数贡献保留对 $\mathcal{D}$ 的主导依赖性。如补充材料注释 4 [35] 中详述，在这些近似下并使用式 (9)，式 (C1) 简化为一个超越方程，该方程允许以 Lambert $W$ 函数表示的闭式解，

[第8页，第6段]
$$D_c(\tau) = -\frac{1}{P(\tau)}W_0[-P(\tau)Q(\tau)], \quad (C2)$$

[第8页，第7段]
其中 $P(\tau) = \alpha^2k^2\tau^3/6$，$Q(\tau) = (\mu^2(1 - \epsilon)R_0^2)/(\epsilon k^2\tau\ln R_0)i_0 e[\mu\alpha(\epsilon R_0 - 1)\tau/\epsilon]$。在上述表达式中，对于 $k$ 或 $\lambda$ 控制，$\alpha = \epsilon$；对于 $\mu$ 控制，$\alpha = 1$。

[第8页，第8段]
式 (C2) 在 $\tau \to 0$ 时表现出 $D_c(\tau) \to \infty$ 的发散，反映了混合近似仅考虑受控阶段的传染性演化，因此无法捕捉 $\tau \to 0$ 极限这一事实。然而，对于有限的干预时长，它预测了一个临界有效扩散强度，使得当 $\mathcal{D} > D_c(\tau)$ 时，疫情峰值随干预时长增加而增大；而当 $\mathcal{D} < D_c(\tau)$ 时，疫情峰值随干预时长增加而减小。
