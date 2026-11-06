### 参考文献逐条关联说明
以下按原文引用顺序，逐一说明每篇引文与本文的关联：

1. **引用序号**：1
**发表信息**：Jacot A, Gabriel F, Hongler C. Neural tangent kernel: convergence and generalization in neural networks. *Advances in Neural Information Processing Systems*, 2018, 31: 8571–8580.
**与本文关联**：神经切线核（NTK）领域的奠基性论文，证明无限宽神经网络在梯度下降下等价于核方法。本文将其作为无限宽网络理论的经典代表，指出该类极限理论无法刻画特征学习效应，是本文有限宽度特征学习理论的核心对照基准。

2. **引用序号**：2
**发表信息**：de G. Matthews A G, Hron J, Rowland M, et al. Gaussian process behaviour in wide deep neural networks. *International Conference on Learning Representations*, 2018.
**与本文关联**：深度神经网络高斯过程（NNGP）的核心文献，证明宽网络的输出先验服从高斯过程。本文的理论框架建立在NNGP的层内核递推结构之上，将固定核推广为数据驱动的自适应核，是对无限宽GP理论的有限宽度拓展。

3. **引用序号**：3
**发表信息**：Naveh G, Ben David O, Sompolinsky H, Ringel Z. Predicting the outputs of finite deep neural networks trained with noisy gradients. *Physical Review E*, 2021, 104: 064301.
**与本文关联**：本文作者团队的前期工作，初步研究了带噪声梯度训练的有限深度网络输出预测方法。本文在此基础上进一步发展出完整的热力学状态方程框架，将单层可训练的结果推广到多层非线性网络的特征学习场景。

4. **引用序号**：4
**发表信息**：Li Y, Yosinski J, Clune J, et al. Convergent learning: Do different neural networks learn the same representations? *Proceedings of the 1st International Workshop on Feature Extraction: Modern Questions and Challenges at NIPS 2015*, PMLR, 2015: 196–212.
**与本文关联**：关于神经网络特征学习收敛性的实证研究，发现不同网络会学习到相似的表征。本文从统计物理层面通过慢变量（核函数）的演化刻画特征学习的集体行为，为该类实证发现提供了理论解释。

5. **引用序号**：5
**发表信息**：Chizat L, Oyallon E, Bach F. On lazy training in differentiable programming. *Advances in Neural Information Processing Systems*, 2019, 32: 2937–2947.
**与本文关联**：提出“懒惰训练（lazy training）”概念，刻画无限宽网络下参数仅在初始值附近小幅波动、不发生实质特征学习的训练模式。本文的核心目标正是描述有限宽度下脱离懒惰训练、发生主动特征学习的 regime，该文献是区分两种训练模式的关键参照。

6. **引用序号**：6
**发表信息**：Lee J, et al. Wide neural networks of any depth evolve as linear models under gradient descent. *Advances in Neural Information Processing Systems*, 2019, 32.
**与本文关联**：证明任意深度的宽网络在梯度下降下都等价于线性模型，是NTK理论的重要延伸。本文在背景中引用该结论，说明无限宽极限下网络的线性化特征，反衬有限宽度下非线性特征学习的独特性。

7. **引用序号**：7
**发表信息**：Allen-Zhu Z, Li Y, Song Z. A convergence theory for deep learning via over-parameterization. *Proceedings of the 36th International Conference on Machine Learning*, PMLR, 2019: 242–252.
**与本文关联**：过参数化网络收敛性理论的经典工作，从优化角度解释过参数化网络的训练收敛性。本文从统计物理/热力学视角研究过参数化网络的特征学习，该文献为本文的过参数化研究背景提供了优化理论层面的支撑。

8. **引用序号**：8
**发表信息**：Arora S, et al. On exact computation with an infinitely wide neural net. *Advances in Neural Information Processing Systems*, 2019, 32: 8141–8150.
**与本文关联**：实现了无限宽神经网络的精确核计算，推动了NNGP的实际应用。本文的层内核递推计算借鉴了该类无限宽核的计算方法，同时将其拓展为有限宽度下的自适应核求解。

9. **引用序号**：9
**发表信息**：Neyshabur B, Li Z, Bhojanapalli S, et al. Towards understanding the role of over-parametrization in generalization of neural networks. *International Conference on Learning Representations*, 2019.
**与本文关联**：研究过参数化对神经网络泛化能力的影响，是深度学习泛化理论的重要文献。本文提出的特征学习尺度（FLS）可用于刻画有限宽度下的泛化行为差异，与该文献的研究主题形成呼应。

10. **引用序号**：10
**发表信息**：Zhang C, Bengio S, Hardt M, et al. Understanding deep learning (still) requires rethinking generalization. *Communications of the ACM*, 2021, 64: 107–115.
**与本文关联**：提出深度学习泛化悖论的经典综述，指出现有泛化理论无法解释过参数化网络的泛化能力。本文的热力学理论从慢变量和尺度分离的角度为理解泛化提供了新的理论视角，回应了该文献提出的核心问题。

11. **引用序号**：11
**发表信息**：Foong A, Burt D, Li Y, Turner R. On the expressiveness of approximate inference in bayesian neural networks. *Advances in Neural Information Processing Systems*, 2020: 15897–15908.
**与本文关联**：研究贝叶斯神经网络近似推断的表达能力，指出宽贝叶斯网络的推断局限。本文针对贝叶斯神经网络后验分布展开研究，提出变分高斯近似框架，该文献为本文的近似方法有效性提供了对照背景。

12. **引用序号**：12
**发表信息**：Coker B, Bruinsma W P, Burt D R, et al. Wide mean-field bayesian neural networks ignore the data. *International Conference on Artificial Intelligence and Statistics*, PMLR, 2022: 5276–5333.
**与本文关联**：指出宽平均场贝叶斯神经网络会出现“忽略数据”的现象，即后验与先验差异极小。本文的理论恰好刻画了有限宽度下网络如何通过核的自适应变化响应数据、发生特征学习，解释了从“忽略数据”到“学习特征”的转变机制。

13. **引用序号**：13
**发表信息**：Zavatone-Veth J, Canatar A, Ruben B, Pehlevan C. Asymptotics of representation learning in finite bayesian neural networks. *Advances in Neural Information Processing Systems*, 2021, 34: 24765–24777.
**与本文关联**：研究有限贝叶斯神经网络表征学习的渐近行为，是有限宽网络表征学习的相关理论工作。本文同样聚焦有限宽网络的特征学习，该文献的结论与本文的热力学描述形成互补对照。

14. **引用序号**：14
**发表信息**：Cho Y, Saul L K. Kernel Methods for Deep Learning. *Advances in Neural Information Processing Systems*, 2009, 22.
**与本文关联**：深度核方法的奠基性工作，提出了逐层计算神经网络核函数的经典Cho-Saul核方法。本文中无限宽极限下的后核递推公式直接基于该文献的核函数计算方法，是本文理论的重要数学基础。

15. **引用序号**：15
**发表信息**：Hinton G E, Srivastava N, Krizhevsky A, et al. Improving neural networks by preventing coadaptation of feature detectors. arXiv preprint arXiv:1207.0580, 2012.
**与本文关联**：提出Dropout等防止网络层间共适应的方法，指出层间强关联不利于网络性能。本文的平均场解耦假设正是基于层间弱关联的特性，该文献的观点为本文的层间解耦近似提供了直觉支撑。

16. **引用序号**：16
**发表信息**：Li Q, Sompolinsky H. Statistical mechanics of deep linear neural networks: The backpropagating kernel renormalization. *Physical Review X*, 2021, 11: 031059.
**与本文关联**：深度线性神经网络的统计力学研究，提出反向传播核重整化理论。本文针对非线性网络推导状态方程，该文献的线性网络结果是本文的特例参照，验证了理论框架在线性情形下的一致性。

17. **引用序号**：17
**发表信息**：Aitchison L. Why bigger is not always better: on finite and infinite neural networks. *International Conference on Machine Learning*, PMLR, 2020: 156–164.
**与本文关联**：讨论有限与无限神经网络的性能差异，指出有限宽度网络的独特优势。本文的核心贡献正是定量刻画有限宽度带来的特征学习效应，为该文献观察到的性能差异提供了微观理论解释。

18. **引用序号**：18
**发表信息**：Fort S, et al. Deep learning versus kernel learning: an empirical study of loss landscape geometry and the time evolution of the neural tangent kernel. *Advances in Neural Information Processing Systems*, 2020, 33: 5850–5861.
**与本文关联**：通过实验对比深度学习与核学习的损失地貌和NTK演化，验证训练中核函数的动态变化。本文提出的动态自适应核理论，为该文献观察到的核演化现象提供了理论依据。

19. **引用序号**：19
**发表信息**：Aitchison L, Yang A, Ober S W. Deep kernel processes. *International Conference on Machine Learning*, PMLR, 2021: 130–140.
**与本文关联**：提出深度核过程算法，是层叠高斯过程的深度学习实现。本文在相关工作讨论中提及，该工作是与本文思路相近的层式GP方法，但本文提供了更基础的第一性原理推导，预测精度更高。

20. **引用序号**：20
**发表信息**：Atanasov A, Bordelon B, Pehlevan C. Neural networks as kernel learners: The silent alignment effect. *International Conference on Learning Representations*, 2022.
**与本文关联**：提出神经网络作为核学习器的“静默对齐效应”，研究有限宽网络的核演化。本文同样将有限宽网络描述为数据自适应的核学习过程，该文献的实证发现与本文的理论结论形成相互印证。

21. **引用序号**：21
**发表信息**：Mei S, Montanari A, Nguyen P-M. A mean field view of the landscape of two-layer neural networks. *Proceedings of the National Academy of Sciences*, 2018, 115: E7665–E7671.
**与本文关联**：两层神经网络损失地貌的平均场理论，是浅层网络统计力学的经典工作。本文的平均场方法借鉴了该文献的思路，并将其推广到深层卷积网络的特征学习场景。

22. **引用序号**：22
**发表信息**：Mannelli S S, Vanden-Eijnden E, Zdeborová L. Optimization and generalization of shallow neural networks with quadratic activation functions. *Advances in Neural Information Processing Systems*, 2020, 33: 13445–13455.
**与本文关联**：二次激活浅层网络的优化与泛化研究，属于浅层网络统计力学领域。本文针对深层非线性网络展开研究，该文献的浅层网络结果为本文的理论验证提供了参照。

23. **引用序号**：23
**发表信息**：Naveh G, Ringel Z. A self consistent theory of gaussian processes captures feature learning effects in finite CNNs. *Advances in Neural Information Processing Systems*, 2021, 34: 21352–21364.
**与本文关联**：本文作者团队的前期工作，首次提出自洽高斯过程理论捕捉有限CNN的特征学习效应。本文是该工作的全面拓展，将单层可训练的结果推广到多层可训练网络，建立了完整的热力学描述框架。

24. **引用序号**：24
**发表信息**：Yaida S. Non-gaussian processes and neural networks at finite widths. *Mathematical and Scientific Machine Learning*, PMLR, 2020: 165–192.
**与本文关联**：有限宽度网络的非高斯过程微扰修正研究。本文在相关工作讨论中指出，这类1/宽度的微扰展开收敛速度慢，而本文的非微扰方法在特征学习显著的实用场景下更有效。

25. **引用序号**：25
**发表信息**：Martin C H, Mahoney M W. Implicit self-regularization in deep neural networks: evidence from random matrix theory and implications for learning. *Journal of Machine Learning Research*, 2021, 22: 1–73.
**与本文关联**：用随机矩阵理论研究深度网络的隐式自正则化效应，发现权重协方差谱的尾效应和尖峰特征。本文讨论了输入层权重协方差的谱分布，指出其可产生与该文献描述相符的各类谱形态，与该实证发现形成呼应。

26. **引用序号**：26
**发表信息**：Fischer K, et al. Decomposing neural networks as mappings of correlation functions. *Physical Review Research*, 2022, 4: 043143.
**与本文关联**：将神经网络分解为相关函数的映射，研究固定网络下输入测度的统计特性。本文与该研究思路相近，但统计对象是网络参数而非输入数据，二者从不同维度刻画网络的相关函数演化规律。

27. **引用序号**：27
**发表信息**：Dyer E, Gur-Ari G. Asymptotics of wide networks from feynman diagrams. *International Conference on Learning Representations*, 2020.
**与本文关联**：用费曼图方法推导宽网络的渐近行为，是有限宽网络微扰修正的代表性方法。本文在相关工作讨论中将其归为高阶微扰展开类方法，并指出这类方法在特征学习显著的场景下收敛较慢。

28. **引用序号**：28
**发表信息**：Huang J, Yau H-T. Dynamics of deep neural networks and neural tangent hierarchy. *International Conference on Machine Learning*, PMLR, 2020: 4542–4551.
**与本文关联**：提出神经切分层级（NTK hierarchy），刻画有限宽网络的动力学高阶修正。本文同样研究有限宽网络的偏离效应，该文献的动力学层级方法与本文的热力学平衡态方法形成互补。

29. **引用序号**：29
**发表信息**：Roberts D A, Yaida S, Hanin B. The principles of deep learning theory. arXiv preprint arXiv:2106.10165, 2021.
**与本文关联**：深度学习理论的专著，系统梳理了无限宽网络、NTK等核心理论。本文的理论背景和数学工具建立在该专著梳理的深度学习理论体系之上，是对现有理论体系的延伸。

30. **引用序号**：30
**发表信息**：Welling M, Teh Y W. Bayesian learning via stochastic gradient langevin dynamics. *Proceedings of the 28th International Conference on Machine Learning*, 2011: 681–688.
**与本文关联**：随机梯度朗之万动力学（SGLD）的奠基性论文，提出用梯度下降加噪声实现贝叶斯采样。本文实验采用的朗之万训练算法正是基于该类方法，用于生成贝叶斯网络后验样本。

31. **引用序号**：31
**发表信息**：Mandt S, Hoffman M D, Blei D M. Stochastic gradient descent as approximate bayesian inference. *Journal of Machine Learning Research*, 2017, 18: 1–35.
**与本文关联**：证明随机梯度下降可视为近似贝叶斯推断，建立了优化算法与贝叶斯后验的对应关系。本文采用的朗之万训练与SGD的对应关系基于该文献的结论，使本文的贝叶斯框架可关联到实际常用的SGD训练。

32. **引用序号**：32
**发表信息**：Mingard C, Valle-Pérez G, Skalse J, Louis A A. Is sgd a bayesian sampler? well, almost. *Journal of Machine Learning Research*, 2021, 22: 1–64.
**与本文关联**：系统验证SGD作为贝叶斯采样器的近似程度，量化其与真实后验的偏差。本文贝叶斯网络设定与朗之万算法的合理性，得到该文献结论的支撑。

33. **引用序号**：33
**发表信息**：Izmailov P, Vikram S, Hoffman M D, Wilson A G G. What are bayesian neural network posteriors really like? *International Conference on Machine Learning*, PMLR, 2021: 4629–4640.
**与本文关联**：实证研究贝叶斯神经网络后验的真实形态，对比不同采样算法的效果。本文选择朗之万算法并验证其平衡态性质，该文献的发现提供了重要的背景依据。

34. **引用序号**：34
**发表信息**：Lee J, et al. Deep neural networks as gaussian processes. *International Conference on Learning Representations*, 2018.
**与本文关联**：深度神经网络高斯过程（NNGP）的标志性论文，系统证明了无限宽深度网络的GP等价性。本文的无限宽基准极限完全基于该文献建立的NNGP框架，是本文最核心的理论基础。

35. **引用序号**：35
**发表信息**：Williams C. Computing with infinite networks. *Advances in Neural Information Processing Systems*, 1996, 9.
**与本文关联**：无限网络高斯过程的早期开创性工作，最早提出单隐层网络无限宽极限等价于GP。本文中erf激活对应的核函数公式可追溯至该文献的经典推导，是核函数计算的源头依据。

36. **引用序号**：36
**发表信息**：Cohen O, Malka O, Ringel Z. Learning curves for overparametrized deep neural networks: a field theory perspective. *Physical Review Research*, 2021, 3: 023034.
**与本文关联**：用场论视角研究过参数化网络的学习曲线，提出了等效核近似及其领头阶修正。本文在两层CNN的解析求解中采用了等效核近似方法，直接借鉴了该文献的技术思路。

37. **引用序号**：37
**发表信息**：Bradbury J, et al. JAX: composable transformations of Python +NumPy programs. 2018.
**与本文关联**：JAX数值计算框架的介绍文献。本文的状态方程数值求解基于JAX实现自动微分与并行计算，该文献对应本文使用的核心计算工具。

38. **引用序号**：38
**发表信息**：Yu J, Spiliopoulos K. Normalization effects on shallow neural networks and related asymptotic expansions. *Foundations of Data Science*, 2021, 3: 151.
**与本文关联**：研究归一化对浅层网络的影响及相关渐近展开。本文讨论了平均场缩放（MF scaling）与标准缩放的差异，该文献的结论支撑了平均场缩放对特征学习的增强作用。

39. **引用序号**：39
**发表信息**：Brutzkus A, Globerson A. An optimization and generalization analysis for max-pooling networks. *Uncertainty in Artificial Intelligence*, PMLR, 2021: 1650–1660.
**与本文关联**：最大池化网络的优化与泛化分析，是CNN理论研究的相关工作。本文理论可推广到带池化层的CNN，该文献的CNN理论结果为本文的架构拓展提供了参照。

40. **引用序号**：40
**发表信息**：Brutzkus A, Globerson A. Globally optimal gradient descent for a convnet with gaussian inputs. *International Conference on Machine Learning*, PMLR, 2017: 605–614.
**与本文关联**：高斯输入下卷积网络梯度下降的全局最优性证明，是早期CNN优化理论的经典工作。本文针对CNN的特征学习展开理论研究，该文献的CNN分析框架为本文提供了前期基础。

41. **引用序号**：41
**发表信息**：Rasmussen C E, Williams C K I. Gaussian Processes for Machine Learning. MIT Press, 2005.
**与本文关联**：高斯过程机器学习的经典专著，系统介绍GP回归、等效核等核心内容。本文的GP推断公式、等效核概念均源自该专著，是本文高斯过程部分的核心参考资料。

42. **引用序号**：42
**发表信息**：Shankar V, et al. Neural kernels without tangents. *International Conference on Machine Learning*, PMLR, 2020: 8614–8623.
**与本文关联**：提出Myrtle-5等CNN架构对应的神经核，是无切线核的CNN核构造工作。本文在真实数据实验中采用Myrtle-5 CNN架构，该文献对应实验所用网络的原始出处与核计算基准。

43. **引用序号**：43
**发表信息**：Martin C H, Peng T S, Mahoney M W. Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data. *Nature Communications*, 2021, 12: 1–13.
**与本文关联**：提出无需训练测试数据即可预测网络质量的诊断工具，基于权重谱分析。本文在展望中提出可通过测量层间核差异来诊断网络的特征学习负载，用于泛化、迁移学习、剪枝分析，与该文献的网络诊断思路形成呼应。

44. **引用序号**：44
**发表信息**：Seroussi I, Zeitouni O. Lower bounds on the generalization error of nonlinear learning models. *IEEE Transactions on Information Theory*, 2022, 68(12): 7956–7970.
**与本文关联**：本文第一作者的前期工作，建立非线性学习模型泛化误差的下界。本文的热力学理论可用于进一步推导泛化误差的定量结果，与该研究方向形成延续。

45. **引用序号**：45
**发表信息**：Seeger M. Pac-bayesian generalisation error bounds for gaussian process classification. *Journal of Machine Learning Research*, 2003, 3: 233–269.
**与本文关联**：高斯过程分类的PAC-贝叶斯泛化误差界经典工作。本文在展望中提出可基于本文得到的有效核发展GP泛化界，该文献是该方向的核心参考基础。

46. **引用序号**：46
**发表信息**：Levit S, Orgad D. Statistics of hartree-fock levels in small disordered systems. *Physical Review B*, 1999, 60: 5549–5560.
**与本文关联**：无序系统中Hartree-Fock能级的统计研究，属于凝聚态物理领域。本文的变分高斯近似（VGA）与物理中的Hartree-Fock自洽方法同源，该文献为本文的平均场自洽方法提供了物理背景参照。

47. **引用序号**：47
**发表信息**：Fischer C, Hartree D. The Hartree-Fock Method for Atoms: A Numerical Approach. Wiley-Interscience, 1977.
**与本文关联**：原子物理中Hartree-Fock方法的经典专著，系统介绍自洽平均场计算方法。本文的逐层自洽状态方程方法本质是深度学习场景下的Hartree-Fock近似，该文献是方法论的物理源头。

48. **引用序号**：48
**发表信息**：Bonneau L, Quentin P, Samsoen D. Fission barriers of heavy nuclei within a microscopic approach. *European Physical Journal A*, 2004, 21: 391–406.
**与本文关联**：重核裂变位垒的微观Hartree-Fock计算研究。本文的自洽平均场方法与核物理中的Hartree-Fock计算思路一致，该文献是该方法在物理中应用的佐证。

49. **引用序号**：49
**发表信息**：Pfannkuche D, Gudmundsson V, Maksym P A. Comparison of a hartree, a hartree-fock, and an exact treatment of quantum-dot helium. *Physical Review B*, 1993, 47: 2244–2250.
**与本文关联**：量子点氦原子的Hartree、Hartree-Fock与精确解的对比研究，验证了平均场近似的精度。本文采用的变分高斯近似等价于Hartree-Fock方法，该文献支撑了此类平均场方法的有效性。

50. **引用序号**：50
**发表信息**：Vempala S, Wibisono A. Rapid convergence of the unadjusted langevin algorithm: Isoperimetry suffices. *Advances in Neural Information Processing Systems*, 2019, 32.
**与本文关联**：未调整朗之万算法（ULA）收敛性的理论证明，指出等周性质足以保证快速收敛。本文实验采用ULA进行后验采样，该文献为算法的收敛性提供了理论保障。

51. **引用序号**：51
**发表信息**：Durmus A, Moulines E. Nonasymptotic convergence analysis for the unadjusted langevin algorithm. *Annals of Applied Probability*, 2017, 27: 1551–1587.
**与本文关联**：未调整朗之万算法的非渐近收敛分析，给出了定量收敛速率。本文选择ULA作为采样算法，其收敛性质的理论依据来源于该文献。

52. **引用序号**：52
**发表信息**：Mou W, Flammarion N, Wainwright M J, Bartlett P L. Improved bounds for discretization of langevin diffusions: near-optimal rates without convexity. *Bernoulli*, 2022, 28: 1577–1601.
**与本文关联**：朗之万扩散离散化误差的改进界，给出非凸情形下的近最优收敛速率。本文采用的离散时间朗之万训练算法，其离散误差分析可参考该文献结论。

53. **引用序号**：53
**发表信息**：Knoll D A, Keyes D E. Jacobian-free newton–krylov methods: a survey of approaches and applications. *Journal of Computational Physics*, 2004, 193: 357–397.
**与本文关联**：无雅可比牛顿-克雷洛夫方法（Newton-Krylov）的综述，介绍该类非线性方程求解方法。本文两层CNN的状态方程数值求解采用了Newton-Krylov方法，该文献对应求解算法的技术来源。