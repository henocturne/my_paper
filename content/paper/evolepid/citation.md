### 一、论文研究方向与所属领域
1. **所属领域**：该论文属于**统计物理与复杂系统科学**和**理论流行病学、进化生物学**的交叉领域，以非线性动力学、反应扩散方程为核心数学工具，聚焦病原体进化与流行病传播的多尺度耦合机制，是物理方法在生命科学与公共卫生领域的典型应用。
2. **核心研究方向**：
   - 拓展经典SIR流行病模型，引入病原体传染性的连续进化机制，构建带性状空间扩散的反应-扩散流行病模型；
   - 揭示病原体进化对流行病动力学的重塑效应，包括超指数增长、感染峰值的非单调依赖、突变式流行转变等；
   - 量化三类防控策略（降低接触率、降低传染性、缩短传染期）与病毒进化的相互作用，证明提前解除防控可能导致比不干预更差的疫情结果；
   - 对比不同防控策略对病毒进化的非对称影响，阐明宿主内、宿主间尺度的进化-流行耦合规律。

---

### 二、参考文献与本文关联
1. **引用序号**：[1]
**发表信息**：M. J. Keeling and P. Rohani, *Modeling Infectious Diseases in Humans and Animals*, Princeton University Press, Princeton, NJ, 2008.
**与本文关联**：该著作是传染病建模领域的经典专著，系统梳理了人类与动物传染病的建模框架与核心理论，为本文基于SIR模型拓展进化动力学提供了学科基础与范式参考。

2. **引用序号**：[2]
**发表信息**：R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani, Epidemic processes in complex networks, *Rev. Mod. Phys.* 87, 925 (2015).
**与本文关联**：该综述系统总结了复杂网络上的流行病传播过程，是统计物理视角下流行病学的核心综述，为本文将动力学方法应用于流行病研究提供了学科背景与理论支撑。

3. **引用序号**：[3]
**发表信息**：W. O. Kermack and A. G. McKendrick, A contribution to the mathematical theory of epidemics, *Proc. R. Soc. A* 115, 700 (1927).
**与本文关联**：该论文是经典SIR流行病模型的奠基性工作，提出的易感-感染-恢复仓室框架是本文模型的核心基础，本文的所有拓展工作均建立在该经典模型之上。

4. **引用序号**：[4]
**发表信息**：H. W. Hethcote, The mathematics of infectious diseases, *SIAM Rev.* 42, 599 (2000).
**与本文关联**：该综述系统梳理了传染病动力学的数学理论与分析方法，为本文的模型推导、稳态分析与感染峰值计算提供了数学方法层面的参考。

5. **引用序号**：[5]
**发表信息**：S. Flaxman et al., Estimating the effects of non-pharmaceutical interventions on COVID-19 in Europe, *Nature* (London) 584, 257 (2020).
**与本文关联**：该研究实证评估了新冠疫情中非药物干预措施的效果，是经典流行病学模型指导公共卫生政策的代表性案例，印证了SIR类模型在实际疫情中的应用价值，也为本文研究防控政策效果提供了现实背景。

6. **引用序号**：[6]
**发表信息**：S. Hsiang et al., The effect of large-scale anti-contagion policies on the COVID-19 pandemic, *Nature* (London) 584, 262 (2020).
**与本文关联**：该研究量化了大规模防控政策对新冠疫情的抑制作用，为本文关注“防控政策对流行病的影响”这一核心问题提供了现实实证依据与研究动机。

7. **引用序号**：[7]
**发表信息**：S. M. Kissler, C. Tedijanto, E. Goldstein, Y. H. Grad, and M. Lipsitch, Projecting the transmission dynamics of SARS-CoV-2 through the postpandemic period, *Science* 368, 860 (2020).
**与本文关联**：该研究对新冠后疫情时代的传播动力学进行了预测，体现了经典流行病模型在疫情预判中的作用，也引出了静态病原体假设的局限性，为本文引入进化机制提供了现实动因。

8. **引用序号**：[8]
**发表信息**：A. Arenas et al., Modeling the spatiotemporal epidemic spreading of COVID-19 and the impact of mobility and social distancing interventions, *Phys. Rev. X* 10, 041055 (2020).
**与本文关联**：该研究是本文作者团队此前的工作，构建了新冠时空传播模型并评估了社交距离政策的效果，是本文将物理方法应用于流行病建模的前期基础，也为本文拓展进化维度提供了模型范式参考。

9. **引用序号**：[9]
**发表信息**：F. Di Lauro, I. Z. Kiss, and J. C. Miller, Optimal timing of one-shot interventions for epidemic control, *PLoS Comput. Biol.* 17, e1008763 (2021).
**与本文关联**：该研究聚焦单次干预的最优时机设计，属于经典流行病最优控制领域的工作，为本文研究干预时长对疫情的影响提供了对照与方法参考。

10. **引用序号**：[10]
**发表信息**：P.-A. Bliman, M. Duprez, Y. Privat, and N. Vauchelet, Optimal immunity control and final size minimization by social distancing for the SIR epidemic model, *J. Optim. Theory Appl.* 189, 408 (2021).
**与本文关联**：该研究针对SIR模型分析了社交距离政策对疫情最终规模的最小化控制，属于经典最优流行病控制范畴，为本文对比“有无进化”下的防控效果提供了基准参照。

11. **引用序号**：[11]
**发表信息**：D. I. Ketcheson, Optimal control of an SIR epidemic through finite-time non-pharmaceutical intervention, *J. Math. Biol.* 83, 7 (2021).
**与本文关联**：该研究分析了有限时长非药物干预下的SIR模型最优控制问题，是经典防控策略优化的代表性工作，为本文的干预时长、干预强度参数设置提供了理论参照。

12. **引用序号**：[12]
**发表信息**：T. A. Perkins and G. España, Optimal control of the COVID-19 pandemic with non-pharmaceutical interventions, *Bull. Math. Biol.* 82, 118 (2020).
**与本文关联**：该研究针对新冠疫情开展非药物干预的最优控制研究，体现了经典模型在现实疫情防控中的应用，为本文的防控政策研究提供了现实场景的参考。

13. **引用序号**：[13]
**发表信息**：J. Hindes and I. B. Schwartz, Epidemic extinction and control in heterogeneous networks, *Phys. Rev. Lett.* 117, 028302 (2016).
**与本文关联**：该研究在复杂网络框架下分析了流行病灭绝与控制问题，是统计物理视角下流行病控制的代表性工作，为本文从动力学相变角度研究流行转变提供了思路参考。

14. **引用序号**：[14]
**发表信息**：E. Rozán, M. N. Kuperman, and S. Bouzat, Analysis of non pharmaceutical interventions with SIR epidemic models: Decreasing the infection peak vs. minimizing the epidemic size, arXiv:2604.08420.
**与本文关联**：该研究对比了非药物干预在“降低感染峰值”与“缩小疫情规模”两个目标下的不同效果，印证了多指标评估防控政策的必要性，为本文同时关注感染峰值与攻击率提供了依据。

15. **引用序号**：[15]
**发表信息**：D. H. Morris, F. W. Rossine, J. B. Plotkin, and S. A. Levin, Optimal, near-optimal, and robust epidemic control, *Commun. Phys.* 4, 78 (2021).
**与本文关联**：该研究证明了固定强度干预可以实现接近最优的流行病控制效果，是本文防控策略设计的核心参考之一；本文在此基础上进一步引入病原体进化，重新检验这类防控策略的有效性。

16. **引用序号**：[16]
**发表信息**：B. T. Grenfell et al., Unifying the epidemiological and evolutionary dynamics of pathogens, *Science* 303, 327 (2004).
**与本文关联**：该论文是进化流行病学的奠基性综述，提出了统一病原体流行病学与进化动力学的研究框架，明确了两个时间尺度耦合的核心科学问题，是本文研究方向的核心理论源头。

17. **引用序号**：[17]
**发表信息**：R. M. Anderson and R. M. May, *Infectious Diseases of Humans: Dynamics and Control*, Oxford University Press, Oxford, 1991.
**与本文关联**：该著作是人类传染病动力学与防控的经典专著，奠定了传染病建模的理论体系，为本文的模型构建、参数定义与防控策略分类提供了基础理论依据。

18. **引用序号**：[18]
**发表信息**：T. Day and S. Gandon, Applying population-genetic models in theoretical evolutionary epidemiology, *Ecol. Lett.* 10, 876 (2007).
**与本文关联**：该综述系统介绍了种群遗传学模型在进化流行病学中的应用，为本文将突变、选择机制引入流行病模型提供了进化生物学层面的方法参考。

19. **引用序号**：[19]
**发表信息**：S. Lion and J. A. Metz, Beyond R0 maximisation: On pathogen evolution and environmental dimensions, *Trends Ecol. Evol.* 33, 458 (2018).
**与本文关联**：该研究指出病原体进化并非仅追求基本再生数R₀最大化，还受环境维度的约束，为本文突破经典假设、研究传染性进化的复杂效应提供了理论启发。

20. **引用序号**：[20]
**发表信息**：L. S. Tsimring, H. Levine, and D. A. Kessler, RNA virus evolution via a fitness-space model, *Phys. Rev. Lett.* 76, 4440 (1996).
**与本文关联**：该研究首次在适应度空间中用扩散方程描述RNA病毒进化，是将统计物理方法应用于病毒进化的开创性工作，为本文用性状空间扩散描述传染性突变提供了方法学源头。

21. **引用序号**：[21]
**发表信息**：Y. Iwasa, F. Michor, and M. A. Nowak, Evolutionary dynamics of escape from biomedical intervention, *Proc. R. Soc. B* 270, 2573 (2003).
**与本文关联**：该研究分析了病原体逃避生物医学干预的进化动力学，属于宿主内进化与干预互作的经典工作，为本文研究防控政策对病毒进化的选择压力提供了理论参考。

22. **引用序号**：[22]
**发表信息**：Y. Iwasa, F. Michor, and M. A. Nowak, Evolutionary dynamics of invasion and escape, *J. Theor. Biol.* 226, 205 (2004).
**与本文关联**：该研究进一步拓展了病原体入侵与免疫逃逸的进化动力学理论，为本文理解突变株的出现、传播与选择机制提供了进化动力学层面的支撑。

23. **引用序号**：[23]
**发表信息**：M. Hartfield and S. Alizon, Within-host stochastic emergence dynamics of immune-escape mutants, *PLoS Comput. Biol.* 11, e1004149 (2015).
**与本文关联**：该研究关注宿主内免疫逃逸突变体的随机出现动力学，是两菌株设置下宿主内进化的代表性工作，为本文对比“多菌株连续进化”与传统两菌株模型的差异提供了参照。

24. **引用序号**：[24]
**发表信息**：D. Van Egeren et al., Controlling long-term SARS-CoV-2 infections can slow viral evolution and reduce the risk of treatment failure, *Sci. Rep.* 11, 22630 (2021).
**与本文关联**：该研究发现控制新冠长期感染可以减缓病毒进化、降低治疗失败风险，实证支持了干预措施可以影响病毒进化速率的结论，为本文的核心假设提供了现实证据。

25. **引用序号**：[25]
**发表信息**：M. Hartfield and S. Alizon, Epidemiological feedbacks affect evolutionary emergence of pathogens, *Am. Nat.* 183, E105 (2014).
**与本文关联**：该研究揭示了流行病学反馈对病原体进化出现的影响，阐明了种群水平流行过程与病原体进化的耦合机制，为本文理解传播选择与突变扩散的相互作用提供了理论基础。

26. **引用序号**：[26]
**发表信息**：M. T. Meehan, R. C. Cope, and E. S. McBryde, On the probability of strain invasion in endemic settings: Accounting for individual heterogeneity and control in multi-strain dynamics, *J. Theor. Biol.* 487, 110109 (2020).
**与本文关联**：该研究在地方病场景下分析了多菌株动力学中的菌株入侵概率与防控的影响，属于多菌株流行病进化的经典工作，为本文的多性状连续进化模型提供了对照参考。

27. **引用序号**：[27]
**发表信息**：B. Ashby, C. A. Smith, and R. N. Thompson, Non-pharmaceutical interventions and the emergence of pathogen variants, *Evol. Med. Public Health* 11, 80 (2023).
**与本文关联**：该研究分析了非药物干预对病原体变异株出现的影响，是防控与进化互作领域的近期工作，为本文研究干预政策对传染性进化的作用提供了文献对照与研究背景。

28. **引用序号**：[28]
**发表信息**：S. Dellicour et al., Phylodynamic assessment of intervention strategies for the West African Ebola virus outbreak, *Nat. Commun.* 9, 2222 (2018).
**与本文关联**：该研究通过系统发育动力学方法实证评估了埃博拉疫情中干预措施对病毒进化轨迹的改变，为本文的理论结论提供了真实病毒进化的实证支撑。

29. **引用序号**：[29]
**发表信息**：Z. Chen et al., COVID-19 pandemic interventions reshaped the global dispersal of seasonal influenza viruses, *Science* 386, eadq3003 (2024).
**与本文关联**：该研究实证发现新冠防控干预重塑了季节性流感的全球传播与进化格局，证明了人类防控措施可以显著改变病毒的进化路径，为本文的核心结论提供了现实流行病学证据。

30. **引用序号**：[30]
**发表信息**：Z. Chen et al., Disruption of seasonal influenza circulation and evolution during the 2009 H1N1 and COVID-19 pandemics in Southeastern Asia, *Nat. Commun.* 16, 475 (2025).
**与本文关联**：该研究聚焦东南亚地区，实证揭示了大流行干预对流感病毒传播与进化的扰动，进一步验证了防控政策与病毒进化的强耦合性，为本文的理论发现提供了地域化的实证支撑。

31. **引用序号**：[31]
**发表信息**：X. Zhang et al., Epidemic spreading under mutually independent intra- and inter-host pathogen evolution, *Nat. Commun.* 13, 6218 (2022).
**与本文关联**：该研究是本文最核心的前置工作，首次提出了宿主内-宿主间独立进化下的超指数流行病增长与突变式流行转变；本文直接沿用其连续性状进化的建模框架，并进一步拓展研究防控政策的影响。

32. **引用序号**：[32]
**发表信息**：D. Soriano-Paños, Eco-evolutionary constraints for the endemicity of rapidly evolving viruses, *PRX Life* 3, 043001 (2025).
**与本文关联**：该研究是本文作者之一的前期工作，分析了快速进化病毒的地方病生态进化约束，为本文理解长期进化与流行动力学的耦合提供了理论基础，也体现了研究团队的工作延续性。

33. **引用序号**：[33]
**发表信息**：I. M. Rouzine and G. Rozhnova, Antigenic evolution of viruses in host populations, *PLoS Pathogens* 14, e1007291 (2018).
**与本文关联**：该研究关注病毒在宿主种群中的抗原进化，是多菌株抗原漂变建模的代表性工作，为本文的结论推广——连续传染性进化可拓展至抗原进化场景——提供了参照。

34. **引用序号**：[34]
**发表信息**：V. Chardès, A. Mazzolini, T. Mora, and A. M. Walczak, Evolutionary stability of antigenically escaping viruses, *Proc. Natl. Acad. Sci. U.S.A.* 120, e2307712120 (2023).
**与本文关联**：该研究分析了抗原逃逸病毒的进化稳定性，属于病毒抗原进化的前沿理论工作，为本文结论的普适性拓展——涵盖抗原漂变等其他进化路径——提供了理论支撑。

35. **引用序号**：[35]
**发表信息**：Supplemental Material, [http://link.aps.org/supplemental/10.1103/56yd-sfks](http://link.aps.org/supplemental/10.1103/56yd-sfks)
**与本文关联**：为本文的补充材料，包含模型细节推导、非单调防控效果的鲁棒性分析、现象起源的进一步解析证明等内容，是正文结论的核心数学支撑与拓展验证。

36. **引用序号**：[36]
**发表信息**：P. Castioni, S. Gómez, C. Granell, and A. Arenas, Rebound in epidemic control: How misaligned vaccination timing amplifies infection peaks, *npj Complex* 1, 20 (2024).
**与本文关联**：该研究关注疫苗接种时机错位导致的疫情反弹，是防控策略时序错位加剧疫情的代表性工作，为本文“提前解除防控导致更差结果”的结论提供了同类现象的对照与方法参考。

37. **引用序号**：[37]
**发表信息**：S. V. Scarpino, A. Allard, and L. Hébert-Dufresne, The effect of a prudent adaptive behaviour on disease transmission, *Nat. Phys.* 12, 1042 (2016).
**与本文关联**：该研究在流感数据中观察到了超指数增长现象，并将其归因于人群适应性行为；本文则提出了另一种机制——病原体传染性进化，为该实证现象提供了新的理论解释。

38. **引用序号**：[38]
**发表信息**：R. Durrett, J. Foo, K. Leder, J. Mayberry, and F. Michor, Evolutionary dynamics of tumor progression with random fitness values, *Theor. Popul. Biol.* 78, 54 (2010).
**与本文关联**：该研究揭示了肿瘤进展中的进化动力学与超指数增长规律，属于进化导致加速增长的跨领域案例，佐证了“进化驱动超指数增长”这一规律的普适性。

39. **引用序号**：[39]
**发表信息**：B. Ocaña-Tienda et al., Growth exponents reflect evolutionary processes and treatment response in brain metastases, *npj Syst. Biol. Appl.* 9, 35 (2023).
**与本文关联**：该研究在脑转移瘤中实证发现生长指数反映进化过程与治疗响应，是进化驱动加速生长的医学实证，为本文“进化改变增长动力学”的核心结论提供了跨领域的实证支撑。

40. **引用序号**：[40]
**发表信息**：A. Cylke and S. Banerjee, Super-exponential growth and stochastic size dynamics in rod-like bacteria, *Biophys. J.* 122, 1254 (2023).
**与本文关联**：该研究在细菌增殖中观察到超指数增长与随机尺寸动力学，是微生物层面进化驱动加速增长的实证，进一步印证了进化诱导超指数增长现象的普适性。

41. **引用序号**：[41]
**发表信息**：R. M. D’Souza, J. Gómez-Gardeñes, J. Nagler, and A. Arenas, Explosive phenomena in complex networks, *Adv. Phys.* 68, 123 (2019).
**与本文关联**：该综述系统总结了复杂网络中的爆炸式相变现象，为本文理解“进化导致突变式流行转变”提供了统计物理相变理论的背景与分析框架。

42. **引用序号**：[42]
**发表信息**：S. Lamata-Otín, J. Gómez-Gardeñes, and D. Soriano-Paños, Pathways to discontinuous transitions in interacting contagion dynamics, *J. Phys. Complex.* 5, 015015 (2024).
**与本文关联**：该研究是本文作者团队的前期工作，分析了相互作用传染动力学中的不连续转变路径，为本文研究进化诱导的突发流行转变提供了相变分析的方法基础。

43. **引用序号**：[43]
**发表信息**：S. Lamata-Otín et al., Collapse transition in epidemic spreading subject to detection with limited resources, *Phys. Rev. E* 108, 024305 (2023).
**与本文关联**：该研究是作者团队前期关于流行病检测资源约束下的崩塌转变研究，体现了团队在流行病相变领域的研究积累，其中的峰值近似方法也为本文的感染峰值推导提供了参考。

44. **引用序号**：[44]
**发表信息**：A. Sasaki, S. Lion, and M. Boots, Antigenic escape selects for the evolution of higher pathogen transmission and virulence, *Nat. Ecol. Evol.* 6, 51 (2022).
**与本文关联**：该研究发现抗原逃逸会选择出传播力与毒力更高的病原体，证明了进化可以同时改变多个病原体性状，为本文结论的拓展——传染性进化的机制可推广至抗原进化等其他路径——提供了理论依据。

45. **引用序号**：[45]
**发表信息**：S. Lamata-Otín et al., Genotype networks drive oscillating endemicity and epidemic trajectories in viral evolution, *Commun. Phys.* 8, 502 (2025).
**与本文关联**：该研究是作者团队的前期工作，分析了基因型网络驱动的病毒地方病振荡与流行轨迹，为本文从连续性状空间拓展到离散基因型网络的结论普适性提供了支撑。

46. **引用序号**：[46]
**发表信息**：B. J. Williams, G. St-Onge, and L. Hébert-Dufresne, Localization, epidemic transitions, and unpredictability of multistrain epidemics with an underlying genotype network, *PLoS Comput. Biol.* 17, e1008606 (2021).
**与本文关联**：该研究分析了基因型网络下多菌株流行病的局域化、转变与不可预测性，是离散基因型空间进化流行病的代表性工作，为本文连续性状模型的结论普适性提供了对照。

47. **引用序号**：[47]
**发表信息**：N. Mideo, S. Alizon, and T. Day, Linking within- and between-host dynamics in the evolutionary epidemiology of infectious diseases, *Trends Ecol. Evol.* 23, 511 (2008).
**与本文关联**：该综述系统阐述了如何联结宿主内与宿主间动力学的进化流行病学框架，为本文理解“缩短传染期（宿主内）与降低传播（宿主间）两类策略的非对称效应”提供了多尺度耦合的理论视角。

48. **引用序号**：[48]
**发表信息**：F. Fabre et al., Modelling the evolutionary dynamics of viruses within their hosts: A case study using high-throughput sequencing, *PLoS Pathogens* 8, e1002654 (2012).
**与本文关联**：该研究利用高通量测序建立了病毒宿主内进化动力学模型，为本文的宿主内进化速率、突变机制等假设提供了生物学实证与参数参考。

49. **引用序号**：[49]
**发表信息**：S. Alizon, Transmission-recovery trade-offs to study parasite evolution, *Am. Nat.* 172, E113 (2008).
**与本文关联**：该研究提出了寄生虫进化中的传播-恢复权衡理论，是病原体进化约束的经典框架，为本文结论的拓展——考虑进化权衡下的模型普适性——提供了理论基础。

50. **引用序号**：[50]
**发表信息**：J. C. De Roode, A. J. Yates, and S. Altizer, Virulence-transmission trade-offs and population divergence in virulence in a naturally occurring butterfly parasite, *Proc. Natl. Acad. Sci. U.S.A.* 105, 7489 (2008).
**与本文关联**：该研究在自然蝴蝶寄生虫系统中实证验证了毒力-传播权衡的存在，为进化权衡的生物学现实性提供了实证，也为本文模型拓展进化约束场景提供了现实依据。

51. **引用序号**：[51]
**发表信息**：M. A. Acevedo, F. P. Dillemuth, A. J. Flick, M. J. Faldyn, and B. D. Elderd, Virulence-driven trade-offs in disease transmission: A meta-analysis, *Evolution* 73, 636 (2019).
**与本文关联**：该研究通过元分析验证了疾病传播中毒力驱动的权衡关系，进一步夯实了病原体进化权衡的实证基础，为本文结论在更现实进化约束下的普适性提供了支撑。

52. **引用序号**：[52]
**发表信息**：S. Lamata-Otín, SIRevolution, [https://github.com/santiagolaot/SIRevolution](https://github.com/santiagolaot/SIRevolution), 2026.
**与本文关联**：为本文配套的开源代码仓库，包含复现本文所有数值模拟结果的程序，实现了带传染性进化的SIR模型数值求解，是本文研究结果可重复性的技术支撑。