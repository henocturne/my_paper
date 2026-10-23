[第1页，第1段]
复杂无序系统中局部优化的物理学

[第1页，第2段]
Mutian Shen, 1,2 Gerardo Ortiz, 3,4 Zhijiao Dong, 5 Martin Weigel, 6,7 and Zohar Nussinov 1,6,8,9,* 1美国密苏里州圣路易斯市华盛顿大学物理系，邮编63160 2美国密苏里州圣路易斯市华盛顿大学生物医学工程系，邮编63160 3美国印第安纳州布卢明顿市印第安纳大学物理系，邮编47405 4美国新泽西州普林斯顿市高等研究院，邮编08540 5美国伊利诺伊州厄巴纳市伊利诺伊大学厄巴纳-香槟分校机械科学与工程系，邮编61801 6德国开姆尼茨市开姆尼茨工业大学物理研究所，邮编09107 7美国佐治亚州亚特兰大市埃默里大学物理系 8英国牛津市牛津大学鲁道夫·派尔斯理论物理中心，邮编OX1 3PU 9法国巴黎市索邦大学LPTMC，CNRS-UMR 7600，4 Place Jussieu，邮编75252 Paris cedex 05

[第1页，第3段]
（2025年6月1日收到；2026年7月16日接受；2026年10月14日发表）

[第1页，第4段]
有限的资源促使人们将大规模问题分解为较小的“局部”子系统，并将由此得到的解拼接起来。我们探讨了这一方法背后的物理原理，并针对P-hard（P难）和NP-hard（NP难）自旋玻璃及相关阻挫自旋系统的基态问题，讨论了“局部硬度”的概念，即从局部信息预测解的局部性质的复杂性。根据所考虑的模型不同，我们观察到与局部预测相关的误差随已求解子系统尺寸衰减的标度行为存在差异。这些误差与全局临界阈值不稳定性密切相关，其特征是无能隙的、雪崩式的激发，这些激发遵循尺度不变的大小分布。远离临界性时，局部求解器能迅速达到高精度，与计算成本高得多的全局最小化结果高度一致。我们利用这些发现，提出了一种基于收缩的启发式算法，用于全局研究自旋玻璃基态。随着自旋玻璃耦合分布的偏移，局部求解器还显示出从自旋玻璃相到铁磁相变的清晰印记，以及无限程模型的特征差异，暗示存在特定类别的局部硬度。我们的发现揭示了自然界如何可能仅通过其可支配的局部作用来运作。

[第1页，第5段]
DOI: 10.1103/kcbw-6zkv

[第1页，第6段]
一种普遍的“分而治之”型分析大规模问题的方法，是将其分割为较小的“局部”组件并加以求解，然后以类似拼图的方式将所得的局部最优解组装起来，从而为原始大规模问题产生有意义的结果。当受限于有限的时间和计算资源时，这种操作方式是自然的。当人们假设——正如在具有底层几何结构的问题（例如物理系统[1]或蛋白质[2]的图像）中经常发生的那样——这些局部解能提供关于更大系统的正确且有用的信息时，这种做法尤为常见。此类局部少体求解器可以准确捕捉由局部哈密顿量支配的一般多体系统的关键特征，这一结果在某些语境下被称为近视性[3–7]。在此，我们探讨该方法在利用简单局部算法预测短程和长程经典自旋玻璃系统基态（GS）的局部及全局方面的物理特性，这是一个已知的难题[8,9]。

[第1页，第7段]
与其他复杂系统[10–14]类似，自旋玻璃带来的挑战源于无序与阻挫的结合，导致复杂的自由能景观[15]。根据近期结果，这些系统通常具有极低能量的激发态，它们彼此之间以及与基态（GS）之间都截然不同[16–18]。这种跨越整个系统的最低能量激发现象意味着，最优（即基态）子系统解未必与最优的全系统解相匹配。此类激发的出现与相应基态问题在P类或NP类中的分类无关[19]。事实上，具有多项式（P）复杂度基态的自旋玻璃也可能表现出跨越整个系统的最低能量液滴[18]。平面图上二维（2D）伊辛自旋玻璃的基态就是这种情况，其可在多项式时间内求得[20]。

[第1页，第8段]
在此，我们研究局部（即子系统）自旋玻璃求解器在多大程度上近似全局自旋玻璃

[第2页，第1段]
GSS。理解这些特征将有助于揭示局部求解器有效性背后的原理。我们的数值分析（基于精确的GS算法）集中于具有以下哈密顿量的Ising自旋玻璃

[第2页，第2段]
$ 
H = -\sum_{\langle ij \rangle} J_{ij} \sigma_i \sigma_j, \quad \sigma_i = \pm 1,
 $

[第2页，第3段]
其中耦合$ J_{ij} $从均值为$ \bar{J} $、单位方差的高斯分布中抽取。除非另有说明，我们设定$ \bar{J} = 0 $。这里，$ N $个自旋被放置在具有开放边界和最近邻相互作用的2D或3D晶格上[Edwards-Anderson（EA）模型[21]]，或者形成具有全连接相互作用的Sherrington-Kirkpatrick（SK）模型[22]（在这种情况下，我们将$ J_{ij} $按$ 1/\sqrt{N} $重新缩放，以保证有意义的热力学极限）。

[第2页，第4段]
以往的相关研究尝试组合多个局部求解器来处理全局优化问题[23]，融合局部GS以构建带有植入解的全局自旋玻璃实例[24]，以及利用基于规范变换的深度强化学习开发局部自旋玻璃求解器[25,26]。在这里，我们采取不同的视角，直接研究基于局部子系统优化能够在多大程度上预测（部分）全局GS。作为该任务的最小实现，我们研究模型中相邻自旋对（键），并引入一个“局部单键求解器”（LSBS），它检查局部子系统内的相邻自旋。我们首先关注键$ \langle i_0 j_0 \rangle $的GS乘积$ \sigma_{i_0} \sigma_{j_0} $，在最简单的情况下，这些键位于系统的中心，参见图1。

[第2页，第5段]
我们感兴趣的是，该自旋乘积在全局GS中的值是否与以该单键为中心的子系统通过LSBS获得的值相匹配。近期研究[27]考察了在重采样系统中心的“壳层”后相邻自旋之间的关联。相比之下，在这里我们考察该乘积是否在以下两种情况下一致：(i) 包含该键且使用开放边界的小子系统的GS计算，与(ii) 全局系统的GS。通过这种方式，LSBS解决了一个最大程度局部化的问题，因此是一种诊断工具，从而引出了我们对“局部硬度”的定义。然而，如下文所示，这些局部解可以通过基于收缩的方案有意义地拼接在一起，形成完整问题的候选解。我们将发现，跨越整个系统的、自旋玻璃GS的相关变化仅出现在特殊的临界相互作用强度处[18]。当自旋玻璃耦合远离其临界阈值（此时会发生全局雪崩式变化）时，GS对耦合常数的微小变化具有鲁棒性。这种鲁棒性使得LSBS在耦合常数远离其临界值时变得准确。我们发现，对于大晶格系统，LSBS错误率变得与全局系统尺寸无关，并随子系统尺寸呈现幂律衰减。其他几个距离相关的量也表现出幂律行为（见参考文献[28]，S10）。相比之下，LSBS错误率对耦合偏离其临界值的依赖性呈指数形式。

[第2页，第6段]
为了系统地研究自旋系统中局部解与全局解的关系，我们依赖精确的（组合）GS算法，对于多项式时间的2D问题使用基于Blossom V [37]的最小权重完美匹配（MWPM）方法[36]，对于3D系统和SK模型使用通用Gurobi软件[38]。图1示意性地描绘了该设置：我们计算了整个（$ N $个自旋）系统以及以所考虑的键$ \langle i, j \rangle $为中心的具有$ N_{\text{sub}} $个晶格位点的子系统（对应于LSBS）的GS，比较乘积$ \sigma_{i_0} \sigma_{j_0} $的预测值（两种情况均应用开放边界条件）。如果结果一致，则键乘积被正确预测（零误差）。对于尺寸为$ L = 256, 512, 1024 $的$ L \times L $方形晶格，我们检查了$ 4 \leq L_{\text{sub}} \leq 512 $的$ L_{\text{sub}} \times L_{\text{sub}} $子系统，使用了约60,000个无序实现。对于边长为$ L = 10 $和$ 12 $的立方晶格，$ L_{\text{sub}} \times L_{\text{sub}} \times L_{\text{sub}} $子系统的尺寸为$ 4 \leq L_{\text{sub}} \leq 10 $，我们使用了约2,000个实现。根据这些计算，我们估计LSBS错误率$ \mathcal{E} $。图2显示了在几种情况下$ \mathcal{E} $对子系统尺寸的依赖性。对于$ \bar{J} = 0 $的晶格系统，我们发现，尽管2D和3D自旋玻璃GS问题属于不同的复杂性类别（分别为P和NP），但在两种情况下，错误率都很好地由子系统尺寸的幂律衰减描述[39] [40]，即，

[第3页，第1段]
图2. 无序平均LSBS错误率$\mathcal{E}_{ij}$作为子系统尺寸$L_{\text{sub}}$（或$N_{\text{sub}}$）的函数，分别对应(a)方格点(2D) EA模型、(b)立方格点(3D) EA模型和(c) SK模型。每个图中展示了不同系统尺寸$L$（$N$）下的结果。对于(a)，展示了$\bar{J} = 0$和$\bar{J} = 1.2$两种情况，而在(b)和(c)中$\bar{J} = 0$。注意不同系统尺寸数据的近乎完美重合，表明对于(a)和(b)，LSBS的误差渐近地与系统尺寸无关，而对于(c)中的SK模型，只有当$N_{\text{sub}}$随$N$缩放时才是这种情况。对于(a)、(b)中的格点系统和$\bar{J} = 0$，错误率由式(2)拟合，参见直线虚线。

[第3页，第2段]
$$\mathcal{E}_{ij} \equiv \frac{1 - [\sigma_i \sigma_j \sigma_i^{\text{sub}} \sigma_j^{\text{sub}}]}{2} \sim (\mathcal{E}_\mathcal{E}/L_{\text{sub}})^\kappa.$$  \tag{2}$$

[第3页，第3段]
这里，$[\sigma_i \sigma_j \sigma_i^{\text{sub}} \sigma_j^{\text{sub}}]$表示对重叠关联函数，其中$[\cdot \cdot \cdot]$代表无序平均，$\mathcal{E}_\mathcal{E}$是有效长度尺度。重要的是，这种代数衰减与线性系统尺寸$L$无关，参见图2(a)和2(b)中的数据重合。比较表I中收集的各自指数$\kappa$，我们看到2D系统中的误差比（更难的）3D系统中下降得更快。当用总体积$N_{\text{sub}} = L_{\text{sub}}^d$表示时，其中$d$是格点维度，2D和3D情况之间误差代数衰减的这种急剧变化变得更加显著。在参考文献[28]（第S13节）中，我们提出了标度论证，得到的$\kappa$值接近我们数值观察到的值。

[第3页，第4段]
虽然精确的幂律衰减在2D和3D之间有所不同，但这种差异远不如这些情况之间P vs NP计算复杂性的对比那么剧烈。这一观察暗示了一种超越P-NP分类[19]（及相关类别[41]）的“局部硬度”计算复杂性描述符，进一步揭示了自旋玻璃基态计算的内在困难。所谓局部硬度，我们指的是进行计算所需的子系统必须有多大，以便在许多实例上平均后，局部求解器能提供达到固定错误率的正确答案。可以说，局部复杂性是物理局部测量（完整多体系统的微观状态通常无法探测）的一个相关描述符。

[第3页，第5段]
对于非零平均耦合$\bar{J}$的情况，只要保持在（零温）自旋玻璃相中，我们就发现相同的幂律衰减，从而表明局部硬度行为具有一定程度的普适性。然而，一旦进入无序铁磁相，错误率就会出现快得多的指数衰减，参见图2(a)中$\bar{J} = 1.2$的数据、图6（End Matter）以及参考文献[28]第S8节中的进一步细节。同样，对于耦合从原本恒定值受到微弱随机扰动的平面反铁磁体，我们发现相同的2D型标度和指数（参考文献[28]，第S9节）。另一方面，对于全连接SK模型，

[第4页，第1段]
图2(c)的数据表明，局部硬度确实依赖于总系统尺寸 $N$，而不仅仅依赖于构成“局部”子系统的 $N_{\text{sub}}$ 个随机选取的自旋，因此表明SK模型具有更高程度的局部硬度。这与以下事实一致：SK系统中不存在局部几何结构，因而其特征是具有更复杂的自由能景观，包含无穷多个热力学态[42]。因此，需要在SK模型中按比例缩放 $N_{\text{sub}}$ 与 $N$ 成正比，才能为LSBS实现低错误率。

[第4页，第2段]
接下来我们转向核心工作——理解局部求解器背后的物理机制。我们的方法依赖于“临界阈值” $J_{c,ij}$ [18,43]的概念，其定义如下。对于任意键，自旋乘积 $\sigma_i \sigma_j$ 要么为 $+1$，要么为 $-1$。现在考虑将 $J_{ij}$ 从 $-\infty$ 连续变化到 $+\infty$，同时保持所有其他键的强度不变。正如我们在其他地方所展示的[18]，存在一个唯一值 $J_{ij} = J_{c,ij}$，在该处 $\sigma_i$ 和 $\sigma_j$ 的相对取向从 $\sigma_i = -\sigma_j$（$J_{ij} < J_{c,ij}$）变为 $\sigma_i = \sigma_j$（$J_{ij} > J_{c,ij}$），因此两个基态（GS）变得简并。类似的定义适用于子系统——将耦合 $J_{ij}$ 改变超过 $J_{\text{sub}}^{\text{sub}}$ 会导致子系统基态的改变。对于LSBS，我们有以下重要观察：如果 $J_{\text{sub}}^{\text{sub}}$ 和 $J_{c,ij}$ 要么（i）都小于 $J_{ij}$，要么（ii）都大于 $J_{ij}$，那么LSBS（在较小子系统基态内计算确定 $\sigma_i \sigma_j$ 的值）将给出正确的 $\sigma_i \sigma_j$ 值（即在全局系统基态内计算的值）。相反的情况是 $J_{ij}$ 被夹在 $J_{c,ij}$ 和 $J_{\text{sub}}^{\text{sub}}$ 之间，导致LSBS失效，这种情况在 $J_{ij}$ 接近临界阈值时更可能发生。图3说明了这一点，该图将键预测的错误率与耦合偏离临界性的程度相关联。因此，键的（子系统）稳定性——由裸耦合与其子系统临界阈值之间的距离 $|J_{\text{sub}}^{\text{sub}} - J_{ij}|$ 来刻画——可以作为LSBS可靠性的预测指标[44]。当 $J_{\text{sub}}^{\text{sub}}$ 和 $J_{ij}$ 相距较远时，$J_{\text{sub}}^{\text{sub}}$ 和 $J_{c,ij}$ 确实可能容易地同时大于或同时小于 $J_{ij}$。反之，当 $J_{\text{sub}}^{\text{sub}}$ 和 $J_{ij}$ 接近时，轻微的计算误差可能导致 $J_{\text{sub}}^{\text{sub}}$ 和 $J_{c,ij}$ 出现在 $J_{ij}$ 的两侧，从而导致LSBS给出错误的 $\sigma_i \sigma_j$ 值（另见文献[28]第S3节）。

[第4页，第3段]
在临界阈值 $J_{c,ij}$ 处，基态对无穷小的单键变化响应敏感。类似于随机场Ising模型[45]、神经网络[46]、具有高度优化容限的系统[47]以及其他问题[48]中的雪崩现象，由于此类变化而翻转的基态自旋形成了我们称之为零能液滴（ZEDs）的结构，其特征是具有分形边界和符合幂律分布的尺寸[18]。在[28]（第S13节）中，我们提出了一个简单的关系，该关系似乎与我们的数据一致，将ZED边界的Hausdorff维数与Eq. (2)的指数 $\kappa$ 联系起来。ZED分布和这些稀有事件的不均匀结构——以高度非均匀的空间分布为特征——类似于自旋玻璃中的温度混沌[49–51]和无序混沌[17,51]现象，其中稀有事件驱动系统尺度的变化。这些分布可能与复杂的临界空间关联有关（文献[28]第S14节）。与一般激发相关的构型可以构造为（单键）ZED的复合体[18]。这些激发按构造具有消失的能量。在给定键的临界阈值附近，全局基态对该局部键耦合的无穷小变化极其敏感，LSBS达到其最低精度。然而，当耦合常数充分远离其（测度为零的）临界阈值时，局部求解器逐渐变得更加精确。如图3以及图4（End Matter）所示，错误率随 $|J_{\text{sub}}^{\text{sub}} - J_{ij}|$ 的增大而衰减。这种衰减可以很好地用以下公式描述

[第4页，第4段]
$$J_{ij} \sim k_J e^{-\left(\frac{|J_{\text{sub}}^{\text{sub}} - J_{ij}|}{J}\right)^\beta},$$  \hspace{1cm} (3)

[第4页，第5段]
其中 $\beta > 1$（2D）和 $\beta = 1$（3D），分别见表I。至于Eq. (2)中表达的对 $L_{\text{sub}}$ 的依赖关系，错误率 $J_{ij}$ 在2D和3D中对稳定性表现出相同的函数依赖关系（文献[28]第S7节）。模量 $|J_{\text{sub}}^{\text{sub}} - J_{ij}|$ 等于子系统内键激发能 $\Delta E$ 的两倍，参见文献[28]第S1节中的Eq. (S1)。因此，LSBS精度由该激发能决定。

[第4页，第6段]
我们进一步将 $L = 128$ 正方晶格和 $L = 12$ 立方晶格的中心键调谐至其临界值，并计算了临界阈值的相应变化

[第5页，第1段]
其他所有键的 (ΔJc,ij)。我们发现，平均差异 |ΔJc,ij| 随距被修改中心键的距离呈代数衰减（见 Fig. 5，End Matter），

[第5页，第2段]
$ 
[|ΔJc,ij|] \sim (ℰ_c/r)^{a_c}.
 $

[第5页，第3段]
在二维和三维系统中，长度 ℰ_c 和指数 a_c 均为量级为 1 的量，拟合参数见表 I。对于足够大的 r，中心键耦合对远处键的 Jc,ij 影响可忽略不计。换言之，给定键的临界耦合几乎完全只由与其邻近的键上的耦合决定。这体现了“临界阈值 Jc,ij 的局域性”。由于 ZED 体积分布呈代数衰减 [18]，对于被调节键与观测键之间的大距离 r，ZED 激发连接这些键的概率变得很小。当对系统边界进行重采样时，|ΔJc,ij| 的衰减类似于 Eq. (4)，见 Ref. [28], Sec. S10。因此，通过移除外围键来生成子系统对中心键的临界耦合影响有限，从而解释了 Jc,ij 与 Jc,ij 的接近性。

[第5页，第4段]
总之，我们使用精确 GS 算法研究了分治型局部子系统求解器的有效性，并将其与系统尺度的雪崩式零能激发的临界阈值 ZED 物理 [18] 联系起来。在短程自旋玻璃中，远离临界阈值时，系统 GS 对局部扰动的响应迅速衰减。通常，局部最小化与全局最小化之间的差异仅在临界耦合阈值附近才变得显著。远离这些临界值时，局部 GS 求解器获得更高的精度。重要的是，对于大系统，局部求解器的相关错误率变得与系统尺寸无关 [见 Fig. 2(a)]，并随子系统尺寸迅速下降。因此，局部求解器对于大 L 可能变得越来越有效。我们的分析揭示，各种长度相关量表现出代数标度，正如雪崩尺寸的无标度分布 [18] 一样，而对于铁磁相，我们观察到误差随子系统尺寸呈指数衰减（另见 End Matter 和 Ref. [28], Sec. S8）。这些行为可能为更复杂的求解器在自旋玻璃 [24–26] 和其他系统 [1,2] 中的成功提供合理解释，并可能广泛适用于不受“重叠间隙性质” [52] 约束的系统。另一方面，对于全连接 SK 模型，错误率始终依赖于整个系统的尺寸。这些差异引导我们猜想局部硬度的可能层级分类（Ref. [28], Sec. S6）。研究发现，无论全局问题是 P（二维）还是 NP（三维）复杂度，局部求解器对所研究的晶格都是有效的。键接近其临界耦合的稀有事件的发生，解释了为什么局部求解器通常无法保证找到整个系统的精确 GS。这种机制让人联想到自旋玻璃中的混沌 [49–51]，对于我们研究的系统类别是普遍存在的。简要地将局部硬度视角与亚稳态及混沌尺寸依赖框架 [13] 联系起来是有启发性的，在该框架中，人们追问局部可观测量在热力学态上的分布是有效“集中”还是更“分散”。在我们的设定中，大的稳定性 |Jc,ij| 对应于低 LSBS 误差的局部可观测量的稳健亚稳态集中的可计算代理，而小的稳定性反映了近简并态之间的竞争。

[第5页，第5段]
虽然这些考虑聚焦于预测单个键两端自旋的超局部任务，但可以将此类计算的结果拼接成全系统候选基态。在 End Matter 和 Ref. [28]（Sec. S16）中，我们概述了一种基于 LSBS 的求解器，它使用子系统临界阈值 Jc,ij 来识别“良定”键，即 |Jc,ij| = Jij 很大且 LSBS 错误率指数小的键，参见 Eq. (3)。这种识别使得在求解 GS 之前，能够将系统收缩为较少数量的内聚大尺度元素（或“社区” [53–56]）。此扩展在此作为概念验证演示，展示局部硬度如何指导算法设计，需要进一步详细研究以评估其全部潜力。推广到包含外场和多体相互作用的设定（Ref. [28], Sec. S15），我们的框架适用于其他重要的 NP 难优化问题，例如最小顶点覆盖问题（见 End Matter 和 Ref. [28], Sec. S17）。局域性进一步是众多具有连续自由度的多体物理问题的基础 [3–7]。将 Eq. (1) 替换为 $ H = -\sum_{ij} J_{ij} s_i s_j + u \sum_i (s_i^2 - 1)^2 $，其中 $ u \gg 1 $ 且连续 $ s_i \in \mathbb{R} $ [当 $ u \to \infty $ 时恢复 Eq. (1)]，表明我们的发现扩展到具有足够大四阶耦合 $ u $ 的连续系统。在由全局约束定义的连续自旋变体——球模型 [57,58]——中，我们在此描述的局域性发生了改变（Ref. [28], Sec. S12）。此处概述的思想的另一个有趣应用领域在于机器学习，有潜力用快速顺序局部随机梯度下降型方法 [55,56,59–62] 替代缓慢的全局梯度方法。机器学习中使用的反向传播算法的局部塑性变体可能模拟高效的生物神经计算 [63,64]。局部最小化和优化结构的其他显著方面出现在生物和人工神经网络中 [65,66]。我们将基于 LSBS 的收缩求解器视为未来研究局部硬度引导启发式的起点。将大规模问题划分为更小、更易求解的片段也可能有利于量子计算方案，因为较小尺度的系统可能较少受到退相干的影响。此处分析的 GS 问题的扩展，包括远距离自旋之间的乘积（见 Ref. [28], Sec. S4）到有限温度

[第6页，第1段]
关联函数可能为我们结果与参考文献[67–70]之间提供富有启发性的联系。在未来的工作中，我们将进一步详述与先前未报道的临界性（参考文献[28]，第S14节）的关系。局部优化的物理机制可能是自然界效率的基础，塑造着跨越不同领域的计算。

[第6页，第2段]
致谢——我们感谢Mark Goh在讨论中提醒我们注意[52]。Z. N.和M. W.感谢开姆尼茨工业大学通过访问学者计划提供的支持。Z. N.还感谢华盛顿大学“赋能卓越与杰出种子项目”（SPEED）以及通过Leverhulme信托国际教授资助（资助号LIP2020-014，S. L. Sondhi）在牛津大学获得的Leverhulme-Peierls高级研究员教授职位提供的支持。G. O. 感谢高等研究院的支持。

[第6页，第3段]
数据可用性——支持本研究结果的数据可根据合理请求向作者获取。

[第6页，第4段]
[1] A. Krizhevsky, I. Sutskever, and G. E. Hinton, Imagenet classification with deep convolutional neural networks, in Advances in Neural Information Processing Systems (NeurIPS), edited by F. Pereira, C. J. Burges, L. Bottou, and K. Weinberger (Curran Associates, New York, 2012).

[第6页，第5段]
[2] J. Jumper et al., Highly accurate protein structure prediction with AlphaFold, Nature (London) 596, 583 (2021).

[第6页，第6段]
[3] W. Kohn, Density functional and density matrix method scaling linearly with the number of atoms, Phys. Rev. Lett. 76, 3168 (1996).

[第6页，第7段]
[4] D. Ruelle, Cluster property of the correlation functions of classical gases, Rev. Mod. Phys. 36, 580 (1964).

[第6页，第8段]
[5] E. H. Lieb and D. W. Robinson, The finite group velocity of quantum spin systems, Commun. Math. Phys. 28, 251 (1972).

[第6页，第9段]
[6] B. Nachtergaele and R. Sims, Lieb-Robinson bounds and the exponential clustering theorem, Commun. Path. Phys. 265, 119 (2006).

[第6页，第10段]
[7] M. Hastings and T. Koma, Spectral gap and exponential decay of correlations, Commun. Math. Phys. 265, 781 (2006).

[第6页，第11段]
[8] B. A. Cipra, The Ising model is NP-complete, SIAM News 33, 6 (2000).

[第6页，第12段]
[9] F. Barahona, On the computational complexity of Ising spin glass models, J. Phys. A 15, 3241 (1982).

[第6页，第13段]
[10] M. Mezard, G. Parisi, and M. A. Virasoro, Spin Glass Theory and Beyond (World Scientific, Singapore, 1987).

[第6页，第14段]
[11] D. L. Stein and C. M. Newman, Spin Glasses and Complexity (Princeton University Press, Princeton, New Jersey, 2013).

[第6页，第15段]
[12] F. Menczer, S. Fortunato, and C. A. Davis, A First Course in Network Science (Cambridge University Press, Cambridge, England, 2020).

[第6页，第16段]
[13] M. Newman, Networks: An Introduction (Oxford University Press, Oxford, 2018), 2nd ed.

[第6页，第17段]
[14] J. D. Bryngelson and P. G. Wolynes, Spin glasses and the statistical mechanics of protein folding, Proc. Natl. Acad. Sci. U.S.A. 84, 7425 (1987).

[第6页，第18段]
[15] Rugged Free Energy Landscapes—Common Computational Approaches to Spin Glasses, Structural Glasses and Biological Macromolecules, Lect. Notes Phys. edited by W. Janke (Springer, Berlin, 2007), Vol. 736.

[第6页，第19段]
[16] J. Lamarcq, J. P. Bouchaud, O. C. Martin, and M. Mézard, Non-compact local excitations in spin-glasses, Europhys. Lett. 58, 321 (2002).

[第6页，第20段]
[17] F. Krzakala and J.-P. Bouchaud, Disorder chaos in spin glasses, Europhys. Lett. 72, 472 (2005).

[第6页，第21段]
[18] M. Shen, G. Ortiz, Y.-Y. Liu, M. Weigel, and Z. Nussinov, Universal fragility of spin-glass ground states under single bond changes, Phys. Rev. Lett. 132, 247101 (2024).

[第6页，第22段]
[19] C. H. Papadimitriou, Computational Complexity (Addison-Wesley, Reading, MA, 1994).

[第6页，第23段]
[20] L. Bieche, J. P. Uhry, R. Maynard, and R. Rammal, On the ground-states of the frustration model of a spin-glass by a matching method of graph-theory, J. Phys. A 13, 2553 (1980).

[第6页，第24段]
[21] S. F. Edwards and P. W. Anderson, Theory of spin glasses, J. Phys. F 5, 965 (1975).

[第6页，第25段]
[22] D. Sherrington and S. Kirkpatrick, Solvable model of a spin-glass, Phys. Rev. Lett. 35, 1792 (1975).

[第6页，第26段]
[23] B. Sun, B. Leonard, P. Ronhovde, and Z. Nussinov, An interacting replica approach applied to the traveling salesman problem, 2016 SAI Computing Conference (IEEE, New York, 2016), p. 319.

[第6页，第27段]
[24] W. Wang, S. Mandrà, and H. G. Katzgraber, Patch-planting spin-glass solution for benchmarking, Phys. Rev. E 96, 023312 (2017).

[第6页，第28段]
[25] C. Fan, M. Shen, Z. Nussinov, Z. Liu, Y. Sun, and Y.-Y. Liu, Finding spin glass ground states through deep reinforcement learning, Nat. Commun. 14, 725 (2023).

[第6页，第29段]
[26] C. Fan, M. Shen, Z. Nussinov, Z. Liu, Y. Sun, and Y.-Y. Liu, Reply to: Deep reinforced learning heuristic tested on spin-glass ground states: The larger picture, Nat. Commun. 14, 5659 (2023).

[第6页，第30段]
[27] A. K. Hartmann and A. P. Young, Metastate analysis of the ground states of two-dimensional Ising spin glasses, Phys. Rev. E 108, 024142 (2023).

[第6页，第31段]
[28] 参见补充材料 http://link.aps.org/supplemental/10.1103/kcbw-6zkv，其中包含标度论证、扩展数值拟合、收缩求解器细节、多体关联、MVC映射以及额外的模型研究，并包括参考文献[29–35]。

[第6页，第32段]
[29] G. H. Wannier, Antiferromagnetism. The triangular Ising net, Phys. Rev. 79, 357 (1950).

[第6页，第33段]
[30] J. Villain, Spin glass with non-random interactions, J. Phys. C 10, 1717 (1977).

[第6页，第34段]
[31] M. E. Fisher, Statistical mechanics of dimers on a plane lattice, Phys. Rev. 124, 1664 (1961).

[第6页，第35段]
[32] M.-S. Vaezi, G. Ortiz, M. Weigel, and Z. Nussinov, The binomial spin glass, Phys. Rev. Lett. 121, 080601 (2018).

[第6页，第36段]
[33] A. Lucas, Ising formulations of many NP problems, Front. Phys. 2, 5 (2014).

[第6页，第37段]
[34] J. Chen, L. Kou, and X. Cui, An approximation algorithm for the minimum vertex cover problem, Procedia Eng. 137, 180 (2016).

[第6页，第38段]
[35] J. Chen, R. Zhou, J. Wu, H. Zhang, and W. Gui, Vertex cover of networks and its related optimization problems: An

[第7页，第1段]
综述，IEEE Trans. Neural Networks Learn. Syst. 36, 11738 (2024)。

[第7页，第2段]
[36] H. Khoshbakht 和 M. Weigel，二维 Ising 自旋玻璃中的畴壁激发，Phys. Rev. B 97, 064410 (2018)。

[第7页，第3段]
[37] V. Kolmogorov，Blossom v：最小代价完美匹配算法的一种新实现，Math. Program. Comput. 1, 43 (2009)。

[第7页，第4段]
[38] Gurobi Optimization, LLC，Gurobi 优化器参考手册，2022。

[第7页，第5段]
[39] 虽然我们将主要关注中心最近邻键（其中 $i = i_0$ 且 $j = j_0$），但在 End Matter 中我们讨论了更一般的情形，即格点 $i$ 和 $j$ 相距 $r_{ij} > 1$。为避免繁琐的记号，在正文中我们常常省略“0”下标。

[第7页，第6段]
[40] 对于 $L_{\text{sub}} = \mathcal{O}(L)$ 的最大取值，式 (2) 的右侧构成误差 $\mathcal{E}_{ij}$ 的一个上界。显然，当 $L_{\text{sub}} = L$（即子系统为整个系统）时，根据定义误差 $\mathcal{E}_{ij} = 0$。

[第7页，第7段]
[41] M. Yannakakis，均衡、不动点与复杂性类，Comput. Sci. Rev. 3, 71 (2009)。

[第7页，第8段]
[42] G. Parisi，自旋玻璃的无穷多个序参量，Phys. Rev. Lett. 43, 1754 (1979)。

[第7页，第9段]
[43] C. M. Newman 和 D. L. Stein，基态稳定性与自旋玻璃相的本质，Phys. Rev. E 105, 044132 (2022)。

[第7页，第10段]
[44] 对于距离 $|J_{c,ij} - J_{ij}|$ 也观察到非常相似的行为，参见补充材料第 S10 节的讨论，但该量从局部求解器的角度是无法获取的。

[第7页，第11段]
[45] J. P. Sethna、K. A. Dahmen 和 C. R. Myers，噼啪噪声，Nature (London) 410, 242 (2001)。

[第7页，第12段]
[46] A. Klaus、S. Yu 和 D. Plenz，统计分析支持在神经元雪崩中发现的幂律分布，PLoS One 6, e19779 (2011)。

[第7页，第13段]
[47] J. M. Carlson 和 J. Doyle，高度优化容限：复杂系统中的鲁棒性与设计，Phys. Rev. Lett. 84, 2529 (2000)。

[第7页，第14段]
[48] V. Navas-Portella、I. Serra、A. Corral 和 E. Vives，增大雪崩幅度与能量分布中的幂律范围，Phys. Rev. E 97, 022134 (2018)。

[第7页，第15段]
[49] L. Fernandez、V. Martin-Mayor、G. Parisi 和 B. Seoane，3D Ising 自旋玻璃中的温度混沌由稀有事件驱动，Europhys. Lett. 103, 67003 (2013)。

[第7页，第16段]
[50] M. Baity-Jesi 等，温度混沌存在于非平衡自旋玻璃动力学中，Commun. Phys. 4, 74 (2021)。

[第7页，第17段]
[51] H. G. Katzgraber 和 F. Krzakala，三维 Ising 自旋玻璃中的温度与无序混沌，Phys. Rev. Lett. 98, 017201 (2007)。

[第7页，第18段]
[52] D. Gamarnik，重叠间隙性质：在随机结构上优化的拓扑障碍，Proc. Natl. Acad. Sci. U.S.A. 118, e2108492118 (2021)。

[第7页，第19段]
[53] M. Girvan 和 M. E. J. Newman，社会网络与生物网络中的社区结构，Proc. Natl. Acad. Sci. U.S.A. 99, 7821 (2002)。

[第7页，第20段]
[54] Santo Fortunato，图中的社区检测，Phys. Rep. 486, 75 (2010)。

[第7页，第21段]
[55] P. Ronhovde 和 Z. Nussinov，基于信息副本关联的超大规模网络多分辨率社区检测，Phys. Rev. E 80, 016109 (2009)。

[第7页，第22段]
[56] P. Ronhovde 和 Z. Nussinov，无局部分辨率极限的社区检测模型，Phys. Rev. E 81, 046114 (2010)。

[第7页，第23段]
[57] T. H. Berlin 和 M. Kac，铁磁体的球模型，Phys. Rev. 86, 821 (1952)。

[第7页，第24段]
[58] J. M. Kosterlitz、D. J. Thouless 和 R. C. Jones，自旋玻璃的球模型，Physica B+C (Amsterdam) 86–88, 859 (1977)。

[第7页，第25段]
[59] A. Harju、B. Barbiellini、S. Siljamäki、R. M. Nieminen 和 G. Ortiz，随机梯度近似：一种优化多体波函数的有效方法，Phys. Rev. Lett. 79, 1173 (1997)。

[第7页，第26段]
[60] S. Ruder，梯度下降优化算法综述，2016，arXiv:1609.04747。

[第7页，第27段]
[61] L. Bottou、F. E. Curtis 和 J. Nocedal，大规模机器学习的优化方法，SIAM Rev. 60, 223 (2018)。

[第7页，第28段]
[62] K. Choudhary 等，深度学习方法在材料科学中的最新进展与应用，npj Comput. Mater. 8, 59 (2022)。

[第7页，第29段]
[63] Y. Song、T. Lukasiewicz、Z. Xu 和 R. Bogacz，大脑能进行反向传播吗？预测编码网络中反向传播的精确实现，载于《神经信息处理系统进展》(NeurIPS)，由 H. Larochelle、M. Ranzato、R. Hadsell、M. F. Balcan 和 H. Lin 编辑（Curran Associates，纽约，2020）。

[第7页，第30段]
[64] I. Goodfellow、Y. Bengio 和 A. Courville，深度学习（MIT Press，剑桥，马萨诸塞州，2016）。

[第7页，第31段]
[65] F. Alet、T. Lozano-Perez 和 L. P. Kaelbling，模块化元学习，载于第二届机器人学习会议 (CoRL)，（瑞士苏黎世，2018）。

[第7页，第32段]
[66] D. Meunier、R. Lambiotte 和 E. T. Bullmore，脑网络的模块化与层次模块化组织，Front. Neurosci. 4, 200 (2010)。

[第7页，第33段]
[67] D. A. Huse 和 I. Morgenstern，二维 Ising 自旋玻璃的有限尺寸标度研究，Phys. Rev. B 32, 3032 (1985)。

[第7页，第34段]
[68] A. C. Carter、A. J. Bray 和 M. A. Moore，关于利用有限尺寸标度测量自旋玻璃指数，J. Phys. A 36, 5699 (2003)。

[第7页，第35段]
[69] F. Parisen Toldin、A. Pelissetto 和 E. Vicari，二维 Ising 自旋玻璃模型中的有限尺寸标度，Phys. Rev. E 84, 051116 (2011)。

[第7页，第36段]
[70] T. Aspelmeier、H. G. Katzgraber、D. Larson、M. A. Moore、M. Wittmann 和 J. Yeo，平均场区域 Ising 自旋玻璃中的有限尺寸临界标度，Phys. Rev. E 93, 032123 (2016)。

[第7页，第37段]
[71] 我们强调，所收集的数据及其拟合针对的是图中所示的 $|J_{c,ij}^{\text{sub}} - J_{ij}|$ 的有限值。当 $J_{c,ij}^{\text{sub}} \neq J_{c,ij}$ 时，误差率 $\mathcal{E}_{ij} \to 1/2$ 当 $|J_{c,ij}^{\text{sub}} - J_{ij}| \to 0^+$，而阈值重合 $J_{c,ij}^{\text{sub}} = J_{c,ij}$（如在开放 1D 链中总是发生的那样）在此极限下产生零误差。在精确 GS 简并时，数值求解器不必对两个 GS 进行等概率采样。对于图 4 中的有限横坐标值，3D 数据比 2D 数据更接近 1/2。

[第7页，第38段]
[72] O. Melchert 和 A. K. Hartmann，零温铁磁体到自旋玻璃转变中畴壁的标度行为，Phys. Rev. B 79, 184402 (2009)。

[第8页，第1段]
在此，我们为式(3)和式(4)提供了数值证据，证明了当耦合分布发生偏移（从而使系统更具铁磁性且更易于求解）时，LSBS精度中存在转变，并且我们讨论了LSBS发现的超越最近邻的相关性。

[第8页，第2段]
**偏离临界阈值的误差率**——为说明正文中分析的适用性，图4表明LSBS误差确实随着$|J_{c,ij}^{\text{sub}} - J_{ij}|$的增大而衰减，其方式符合式(3)的拉伸指数下降[71]。

[第8页，第3段]
**临界阈值的距离依赖性**——如正文所述，给定键的临界阈值在很大程度上仅由与其非常接近的其他键的耦合决定。当我们将$L = 128$方形晶格和$L = 12$立方晶格的中心键调至其临界值时，所有其他距离为$r$的键各自的临界阈值变化（$\Delta J_{c,ij}$）符合式(4)，其中$\ell_c$的量级为晶格常数，见表I[在2D系统中，式(4)的拟合成为最大距离处的上界]。这在图5中进行了说明。在参考文献[28]第S5节（见其中的图S4）中，我们进一步提供了这种典型临界耦合变化随远离原点而快速衰减的实空间可视化计算结果。我们还观察到，对于较小的ZED，对远处键的影响较小。

[第8页，第4段]
**基于LSBS的收缩求解器**——LSBS为各个最近邻键自旋乘积提供局部预测。在此我们概述如何将这些局部预测组合成一个近似完整基态（GS）自旋构型的收缩求解器。对于每个键，我们计算其子系统临界阈值。

[第8页，第5段]
**误差率$\mathcal{E}_{ij}$作为$|J_{c,ij}^{\text{sub}} - J_{ij}|$的函数**，针对(a)二维（方形晶格）$L = 1024$系统，$L_{\text{sub}} = 8, 16, 32, 64$，以及(b)三维（立方）$L = 12$系统，$L_{\text{sub}} = 4, 10$。点百分比表示$|J_{c,ij}^{\text{sub}} - J_{ij}|$值低于其横坐标的累积概率（即实例比例）。

[第8页，第6段]
**临界阈值的平均变化**（$|\Delta J_{c,ij}|$），针对(a)二维（$L = 128$）和(b)三维（$L = 12$）系统中沿笛卡尔方向距中心键距离为$r$的键。虚线：式(4)，参数见表I。正如在二维中更为明显的那样，当$r = \mathcal{O}(L)$时，平均$|\Delta J_{c,ij}|$被这些超局部形式从上界约束，拟合的$\ell_c$量级为晶格常数。

[第8页，第7段]
**图4.** 误差率$\mathcal{E}_{ij}$作为$|J_{c,ij}^{\text{sub}} - J_{ij}|$的函数，针对(a)二维（方形晶格）$L = 1024$系统，$L_{\text{sub}} = 8, 16, 32, 64$，以及(b)三维（立方）$L = 12$系统，$L_{\text{sub}} = 4, 10$。点百分比表示$|J_{c,ij}^{\text{sub}} - J_{ij}|$值低于其横坐标的累积概率（即实例比例）。

[第8页，第8段]
**图5.** 临界阈值的平均变化（$|\Delta J_{c,ij}|$），针对(a)二维（$L = 128$）和(b)三维（$L = 12$）系统中沿笛卡尔方向距中心键距离为$r$的键。虚线：式(4)，参数见表I。正如在二维中更为明显的那样，当$r = \mathcal{O}(L)$时，平均$|\Delta J_{c,ij}|$被这些超局部形式从上界约束，拟合的$\ell_c$量级为晶格常数。

[第8页，第9段]
**图6.** 对于非对称键分布，随着$\tilde{J}$增大，系统从自旋玻璃相转变为无序铁磁相[72]。我们观察了拟合系数$\kappa$随调整$\tilde{J}$的变化。$\kappa$值越大意味着子系统求解器的误差率衰减越快，在超过阈值$1/\tilde{J} = 0.96$后过渡为指数衰减，此时系统进入铁磁相[72]。

[第9页，第1段]
图 7. 收缩求解器示意图。(a) 良好确定的键（$|J_{ij} - J_{c,ij}| \geq \theta$，其中 $\theta$ 是手动选择的阈值）形成连通分量，这些连通分量被收缩为有效位点（显示为较大的节点），继承该分量与系统其余部分之间的所有相互作用。(b) 每个连通分量内位点的相对自旋取向（由 + 和 − 符号表示）由良好确定的键锁定。然后，可以通过传播分量取向，从收缩系统的基态（GS）重建整个系统的基态。不同颜色代表不同的连通分量。

[第9页，第2段]
$J_{c,ij}$ 并识别满足 $|J_{ij} - J_{c,ij}| \geq \theta$ 的良好确定的键，其中 $\theta$ 是选定的阈值。这些键远离其临界阈值，具有较高的局部预测精度。良好确定的键形成连通分量（或“社区”[53–56]），在其中相对自旋取向被可靠地固定。每个这样的分量被收缩为单个有效位点，继承该分量与系统其余部分之间的所有相互作用。收缩后的系统被精确求解，并通过传播分量取向来重建原始自旋配置。该收缩过程在图 7 中示意性地说明。对于适当选择的 $\theta$，这种方法产生的配置非常接近精确基态，同时大幅减小有效问题规模。详细的示意图、算法步骤和性能分析见补充材料（参考文献 [28]，第 S16 节）。

[第9页，第3段]
最小顶点覆盖作为伊辛问题——作为自旋玻璃之外的一个代表性 NP 难优化问题，我们还研究了由 Delaunay 三角剖分生成的随机平面图上的最小顶点覆盖（MVC）问题。通过将覆盖中的顶点 $i$ 映射为 $\sigma_i = +1$，否则映射为 $\sigma_i = -1$，代价函数可以写为

[第9页，第4段]
$$H_{MVC} = A \sum_{i \in V} \frac{1 + \sigma_i}{2} + B \sum_{\langle ij \rangle \in E} \frac{1 - \sigma_i}{2} \frac{1 - \sigma_j}{2}, \tag{D1}$$

[第9页，第5段]
其中边 $\langle ij \rangle \in E$ 上的耦合为 $J_{ij} = -B/4$，场为 $h_i = -A/2 + (B/4) \deg(i)$（对于 $A = 1$，$B = 2$），其中 $\deg(i)$ 对应于位点 $i$ 的度（邻居数）。在中心位点周围图距离半径为 $r$ 的子系统上使用 LSBS，我们预测其在 MVC 基态中的相对自旋取向，并将其与精确解进行比较。我们发现 LSBS 错误率随子系统大小呈类幂律衰减（图 8），指数 $\kappa \approx 0.8$，接近自旋玻璃情形。这表明我们基于局域性的硬度图景更广泛地适用于组合优化问题。
