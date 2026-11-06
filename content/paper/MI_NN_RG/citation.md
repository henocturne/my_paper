### 一、论文研究方向与所属领域
#### 所属领域
该论文属于**统计物理/凝聚态物理**与**机器学习（人工智能）**的交叉领域，具体覆盖实空间重整化群理论、信息论、受限玻尔兹曼机神经网络方向，是“物理+AI”交叉领域中“数据驱动的理论物理方法创新”的代表性研究。

#### 核心研究方向
论文核心方向为**基于实空间互信息（RSMI）的神经网络重整化群方法**：无需预设系统的微观物理知识，仅通过系统的平衡态构型样本，以“最大化局域隐藏自由度与环境的互信息”为目标，自动识别物理系统的长程相关自由度，并迭代执行实空间重整化群（RG）粗粒化过程。

#### 相关研究课题
1.  重整化群理论：实空间RG的普适构造方法、临界现象与临界指数计算、RG流演化规律
2.  信息论物理应用：互信息与有效自由度的对应关系、信息瓶颈方法的物理实现、信息压缩与物理涌现理论
3.  机器学习物理应用：玻尔兹曼机在统计物理中的应用、无监督物理特征提取、神经网络与重整化群的内在关联
4.  经典统计模型：二维Ising模型临界行为、二聚体模型的有效场论描述、无序/噪声系统下RG的鲁棒性

---

### 二、全部引文与本文的关联梳理
1、LeCun, Y., Bengio, Y. & Hinton, G. E. Deep learning. Nature 521, 436–444 (2015)
与本文关联：深度学习领域的里程碑综述，系统总结了深度神经网络的技术框架与核心能力。本文引言部分以此为背景，说明机器学习在图像识别、语音处理等通用领域的突破性进展，佐证神经网络的特征提取与非线性拟合能力，为其应用于物理系统自由度提取提供技术合理性支撑。

2、Silver, D. et al. Mastering the game of Go with deep neural networks and tree search. Nature 529, 584–589 (2016)
与本文关联：AlphaGo的标志性研究，证明机器学习可在复杂决策任务中超越人类水平。本文将其作为机器学习能力的典型例证，引出“将机器学习从游戏、感知领域拓展到物理理论构建”的研究动机，支撑机器学习可处理复杂物理规律的核心假设。

3、Hershey, J. R., Rennie, S. J., Olsen, P. A. & Kristjansson, T. T. Super-human multi-talker speech recognition: A graphical modeling approach. Comput. Speech Lang. 24, 45–66 (2010)
与本文关联：多说话人语音识别领域实现超人类性能的经典工作，体现了机器学习在传统算法难以胜任的感知任务中的优势。本文用其补充论证机器学习的泛化能力，进一步强化“机器学习可挖掘复杂物理系统隐含结构”的研究前提。

4、Carrasquilla, J. & Melko, R. G. Machine learning phases of matter. Nat. Phys. 13, 431–434 (2017)
与本文关联：机器学习应用于凝聚态物理的早期经典工作，首次将监督学习用于物质相分类。本文将其归为“机器学习用于物理模式识别与分类”的代表性研究，以此区分本文的核心创新——并非做物相分类，而是用机器学习自动提取重整化群的相关自由度，参与物理理论推理过程。

5、Torlai, G. & Melko, R. G. Learning thermodynamics with Boltzmann machines. Phys. Rev. B 94, 165134 (2016)
与本文关联：该工作利用玻尔兹曼机学习物理系统的热力学性质，是神经网络作为非线性函数拟合器服务于物理数值模拟的典型研究。本文将其列为机器学习在物理领域的早期应用方向之一，同时本文核心架构也采用受限玻尔兹曼机（RBM），该文献是相关技术的背景参考。

6、van Nieuwenburg, E. P. L., Liu, Y.-H. & Huber, S. D. Learning phase transitions by confusion. Nat. Phys. 13, 435–439 (2017)
与本文关联：提出“混淆法”通过无监督学习识别相变的经典工作，属于机器学习+相变研究的重要分支。本文将其作为“机器学习用于相变检测、物相分析”的领域进展案例，衬托本文在“自动执行重整化群、提取有效自由度”方向的差异化创新。

7、Wang, L. Discovering phase transitions with unsupervised learning. Phys. Rev. B 94, 195105 (2016)
与本文关联：无监督学习发现相变的代表性研究，拓展了无监督方法在统计物理中的应用。本文将其纳入机器学习物理应用的背景梳理，用于说明当前机器学习多集中于相变、物相识别任务，进而引出本文面向重整化群的新研究方向。

8、Ohtsuki, T. & Ohtsuki, T. Deep learning the quantum phase transitions in random electron systems: applications to three dimensions. J. Phys. Soc. Jpn 86, 044708 (2017)
与本文关联：将深度学习应用于三维无序电子系统量子相变的研究，拓展了机器学习在量子物态领域的应用边界。同属机器学习用于物态分类的研究脉络，是本文引言中梳理的相关领域进展之一，用于铺垫领域研究现状。

9、Ronhovde, P. et al. Detecting hidden spatial and spatio-temporal structures in glasses and complex physical systems by multiresolution network clustering. Eur. Phys. J. E 34, 105 (2011)
与本文关联：提出用多分辨率网络聚类识别玻璃态等复杂系统隐藏时空结构的方法，是数据驱动提取复杂系统结构的早期探索。本文将其作为机器学习/数据方法应用于非晶、复杂材料的代表案例，同时呼应本文二聚体模型、噪声鲁棒性验证中“隐藏结构提取”的核心任务。

10、Ronhovde, P. et al. Detection of hidden structures for arbitrary scales in complex physical systems. Sci. Rep. 2, 329 (2012)
与本文关联：承接引用9的工作，进一步实现了任意尺度下复杂系统隐藏结构的检测。其多尺度结构提取的思路与本文“迭代重整化、跨尺度粗粒化”的核心逻辑相呼应，是本文研究思路的相关背景参考。

11、Hinton, G. E. & Salakhutdinov, R. R. Reducing the dimensionality of data with neural networks. Science 313, 504–507 (2006)
与本文关联：深度学习降维的奠基性工作，证明了深度神经网络具备强大的高维数据维度约简能力。本文的核心目标是通过神经网络对物理系统自由度进行粗粒化降维，该文献是本文采用受限玻尔兹曼机实现自由度压缩的核心技术依据。

12、Lin, H. W. & Tegmark, M. Why does deep and cheap learning work so well? J. Stat. Phys. 168, 1223–1247 (2017)
与本文关联：从统计物理与重整化群视角解释深度学习的有效性，提出深度学习的层次化特征提取与物理系统的重整化群粗粒化具有内在一致性。该工作是“机器学习-重整化群”交叉领域的核心理论铺垫，为本文用神经网络实现重整化群提供了底层逻辑支撑。

13、Carleo, G. & Troyer, M. Solving the quantum many-body problem with artificial neural networks. Science 355, 602–606 (2017)
与本文关联：神经网络量子态的里程碑工作，首次用人工神经网络高效求解量子多体问题，属于神经网络作为物理数值模拟工具的代表性研究。本文将其归为“机器学习作为数值模拟器”的应用方向，以此区分本文“机器学习参与物理理论构建”的全新范式。

14、Deng, D.-L., Li, X. & Sarma, S. D. Machine learning topological states. Phys. Rev. B 96, 195145 (2017)
与本文关联：将机器学习用于拓扑物态识别的经典工作，属于机器学习在凝聚态物理中模式识别方向的典型应用。本文将其列为领域相关进展，用于衬托本文“提取物理有效自由度、执行重整化群”的研究定位差异。

15、Wilson, K. G. The renormalization group: Critical phenomena and the Kondo problem. Rev. Mod. Phys. 47, 773–840 (1975)
与本文关联：重整化群（RG）理论的经典综述，Wilson的奠基性成果，系统阐述了RG在临界现象、近藤问题中的核心思想与方法。该文献是本文研究的核心理论基础，全文的研究框架均围绕实空间重整化群展开，该文献是RG领域的权威背景引用。

16、Politzer, H. D. Reliable perturbative results for strong interactions? Phys. Rev. Lett. 30, 1346–1349 (1973)
与本文关联：量子色动力学中渐近自由的发现论文，是重整化群方法在粒子物理领域的标志性成功应用。本文用其例证RG是横跨凝聚态、粒子物理的通用核心工具，佐证RG方法的重要学术价值，进而引出“自动识别RG自由度”这一问题的研究意义。

17、Berezinskii, V. L. Destruction of long-range order in one-dimensional and two-dimensional systems having a continuous symmetry group I. Classical systems. Sov. J. Exp. Theor. Phys. 32, 493 (1971)
与本文关联：BKT相变的奠基性工作（Berezinskii部分），是重整化群方法成功解释的经典相变现象。本文将其作为RG方法的经典应用案例，用于完整呈现RG在不同物理体系中的广泛适用性，强化RG的理论背景地位。

18、Kosterlitz, J. M. & Thouless, D. Ordering, metastability and phase transitions in two-dimensional systems. J. Phys. C 6, 1181 (1973)
与本文关联：Kosterlitz-Thouless相变的核心论文，与引用17共同构成BKT相变理论体系，是重整化群的经典应用场景。属于本文中重整化群理论背景的组成部分，用于说明RG方法的学术影响力。

19、Kadanoff, L. P. Scaling laws for Ising models near T(c). Physics 2, 263–272 (1966)
与本文关联：实空间重整化群的奠基工作，提出了Ising模型的块自旋粗粒化方案（Kadanoff块自旋），是本文实空间RG方法的直接理论源头。本文在Ising模型验证部分，证明RSMI算法可自动重现Kadanoff块自旋的结果，该文献是核心的理论对照与验证依据。

20、Wetterich, C. Exact evolution equation for the effective potential. Phys. Lett. B 301, 90–94 (1993)
与本文关联：泛函重整化群（FRG）的核心奠基工作，提出有效势的精确演化方程。本文在介绍重整化群的技术体系时，将泛函RG列为RG的主要分支之一，用于说明RG方法的多样性，衬托本文聚焦的实空间RG的方法定位。

21、White, S. R. Density matrix formulation for quantum renormalization groups. Phys. Rev. Lett. 69, 2863–2866 (1992)
与本文关联：密度矩阵重整化群（DMRG）的奠基论文，是量子多体系统中RG方法的核心技术。本文将其列为RG的重要分支，用于完整梳理重整化群的技术谱系，同时对比说明本文方法面向经典统计物理实空间RG的特点。

22、Ma, S.-k, Dasgupta, C. & Hu, C.-k Random antiferromagnetic chain. Phys. Rev. Lett. 43, 1434–1437 (1979)
与本文关联：研究无序反铁磁链重整化群处理的经典工作，体现了强无序、强关联系统中RG自由度识别的难度。本文以此佐证“复杂系统中相关自由度难以手动识别”的核心问题，同时对应本文未来可拓展的无序系统研究方向。

23、Corboz, P. & Mila, F. Tensor network study of the Shastry–Sutherland model in zero magnetic field. Phys. Rev. B 87, 115144 (2013)
与本文关联：用张量网络方法研究Shastry-Sutherland模型的工作，属于强关联系统数值RG的范畴，体现了复杂量子模型中构建有效RG自由度的技术挑战。支撑本文“强相互作用系统RG自由度识别困难，需要自动化方法”的研究动机。

24、Capponi, S., Chandra, V. R., Auerbach, A. & Weinstein, M. p6 chiral resonating valence bonds in the kagome antiferromagnet. Phys. Rev. B 87, 161118 (2013)
与本文关联：研究Kagome反铁磁体手征共振价键态的工作，属于强关联体系中有效模型映射、自由度构建的研究范畴。该类工作体现了复杂系统需通过人工数学映射才能找到合适RG自由度的现状，进一步凸显本文无先验自动提取RG自由度的方法价值。

25、Auerbach, A. Interacting Electrons and Quantum Magnetism (Springer, New York, NY, 1994)
与本文关联：量子磁学领域的经典专著，系统阐述了相互作用电子与量子磁性的理论框架。为本文涉及的自旋模型、强关联系统物理背景提供了基础参考，是领域基础参考资料。

26、Gaite, J. & O’Connor, D. Field theory entropy, the h theorem, and the renormalization group. Phys. Rev. D 54, 5163–5173 (1996)
与本文关联：早期将场论熵、H定理与重整化群结合的理论研究，探索了信息论视角下的RG机制。属于本文“信息论刻画重整化群”核心思路的前期理论铺垫，印证了用信息熵/互信息描述RG过程的理论可行性。

27、Preskill, J. Quantum information and physics: some future directions. J. Mod. Opt. 47, 127–137 (2000)
与本文关联：量子信息与物理交叉领域的展望文章，提出信息论与基础物理深度融合的研究方向。本文“信息论+重整化群+机器学习”的交叉研究范式，属于该宏观方向下的具体探索，该文献是领域前瞻背景引用。

28、Apenko, S. M. Information theory and renormalization group flows. Phys. A 391, 62–77 (2012)
与本文关联：直接研究信息论与重整化群流关联的理论工作，是本文“实空间互信息驱动RG”核心方法的直接理论前驱。为本文通过最大化互信息来定义RG相关自由度的思路提供了理论依据与参考。

29、Machta, B. B., Chachra, R., Transtrum, M. K. & Sethna, J. P. Parameter space compression underlies emergent theories and predictive models. Science 342, 604–607 (2013)
与本文关联：提出参数空间压缩是涌现理论、有效模型的核心本质，将重整化群粗粒化的本质解读为信息压缩与参数约简。该工作从底层解释了RG的信息论内涵，是本文用互信息（信息度量）实现RG粗粒化的核心理论支撑之一。

30、Beny, C. & Osborne, T. J. The renormalization group via statistical inference. New. J. Phys. 17, 083005 (2015)
与本文关联：从统计推断视角重构重整化群理论，将RG过程表述为一种概率推断任务，与本文的概率/信息论视角下的RG思路高度契合。是本文核心方法的重要理论参考，支撑了用概率分布、信息度量刻画RG的研究框架。

31、Stephan, J.-M., Inglis, S., Fendley, P. & Melko, R. G. Geometric mutual information at classical critical points. Phys. Rev. Lett. 112, 127204 (2014)
与本文关联：研究经典临界点处几何互信息的性质，是实空间互信息在临界现象中的具体应用研究。为本文用实空间互信息（RSMI）刻画临界系统的重整化群提供了直接的相关研究参考，验证了互信息在临界物理系统中的有效性。

32、Tishby, N., Pereira, F. C. & Bialek, W. The information bottleneck method. In Proc. 37th Allerton Conf. on Communication, Control and Computation 49, 368–377 (University of Illinois, 2001)
与本文关联：信息瓶颈方法的奠基论文，提出在保留相关信息的前提下对数据进行压缩的理论框架。本文提出的RSMI算法本质是信息瓶颈方法在实空间物理系统中的神经网络实现——最大化隐藏自由度与环境的互信息，同时压缩局域自由度，该文献是本文核心算法的理论源头。

33、Hinton, G. E. Training products of experts by minimizing contrastive divergence. Neural Comput. 14, 1771–1800 (2002)
与本文关联：对比散度（CD）算法的提出论文，是受限玻尔兹曼机的核心训练算法。本文中两个用于拟合概率分布的辅助RBM均采用CD算法训练，该文献是本文算法实现的关键技术背景与依据。

34、Ludwig, A. W. W. & Cardy, J. L. Perturbative evaluation of the conformal anomaly at new critical points with applications to random systems. Nucl. Phys. B 285, 687–718 (1987)
与本文关联：研究无序系统临界点共形反常的微扰计算，涉及RG流过程中有效自由度的演化规律。本文提到RSMI算法可在每一步RG迭代中重新计算自由度，能够捕捉RG流中自由度的演化，该文献对应这一特性的物理背景与未来应用场景（无序系统）。

35、Fisher, M. E. & Stephenson, J. Statistical mechanics of dimers on a plane lattice. II. Dimer correlations and monomers. Phys. Rev. 132, 1411–1431 (1963)
与本文关联：二维二聚体模型统计力学的经典奠基工作，系统研究了二聚体的关联函数、单体性质等核心物理特性。是本文二聚体模型验证部分的物理理论基础，为验证算法提取的自由度是否合理提供了底层物理参照。

36、Fradkin, E. Field Theories of Condensed Matter Physics (Cambridge Univ. Press, Cambridge, 2013)
与本文关联：凝聚态场论的经典专著，其中详细阐述了二聚体模型到高度场、局域电场的数学映射关系。本文通过该专著中的解析结论，验证RSMI算法从二聚体样本中自动提取的有效自由度（局域电场）符合理论预期，是验证环节的核心理论依据。

37、Mehta, P. & Schwab, D. J. An exact mapping between the variational renormalization group and deep learning. Preprint at abs/1410.3831 (2014)
与本文关联：该预印本声称变分重整化群与深度学习存在精确映射。本文通过实验对比指出，最小化KL散度的标准RBM并不能正确执行RG，只有最大化互信息的RSMI方法才能得到符合物理预期的结果，该文献是本文直接商榷、对比的对象，用于凸显本文方法的正确性与创新性。

38、McCoy, B. M. & Wu, T. T. The Two-Dimensional Ising Model (Harvard Univ. Press, Cambridge, MA, 1973)
与本文关联：二维Ising模型的经典权威专著，包含该模型关联函数、临界指数等全套精确解析结果。本文在Ising模型验证中，将算法计算得到的关联函数、临界指数与该专著的精确结果进行对比，以此验证RSMI算法的定量准确性。

39、Schoenholz, S. S., Cubuk, E. D., Sussman, D. M., Kaxiras, E. & Liu, A. J. A structural approach to relaxation in glassy liquids. Nat. Phys. 12, 469–471 (2016)
与本文关联：通过机器学习提取玻璃态液体的微观结构特征，揭示其宏观弛豫规律的工作。该研究证明神经网络的内部表示可以对应真实的物理结构，支撑本文的核心结论——RSMI网络的权重并非“黑箱”，而是直接对应系统的物理有效自由度。

40、Jordan, M. I. & Mitchell, T. M. Machine learning: Trends, perspectives, and prospects. Science 349, 255–260 (2015)
与本文关联：机器学习领域的权威展望综述，提出“人机协作”的未来科研范式。本文结尾展望部分引用该观点，提出“机器学习挖掘数据中隐含规律+人类创造力与先验知识”的协作式物理研究模式，呼应本文的研究范式创新。

41、Slonim, N. & Tishby, N. Document clustering using word clusters via the information bottleneck method. In Proc. 23rd Annual International ACM SIGIR Conf. on Research and Development in Information Retrieval, SIGIR ’00 208–215 (ACM, 2000)
与本文关联：信息瓶颈方法在文本聚类领域的经典应用，证明了该方法在非物理领域的有效性。本文结尾展望RSMI算法可拓展到物理之外的压缩、聚类任务，该文献佐证了信息瓶颈方法的跨领域适用性，支撑RSMI的泛化应用前景。