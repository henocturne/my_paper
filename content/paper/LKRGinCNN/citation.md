以下按引用序号逐条整理全部67篇参考文献的发表信息与本文关联：

1. **发表信息**：Goodfellow I, Bengio Y, Courville A. *Deep Learning*. MIT Press, 2016.
**与本文关联**：深度学习领域经典教材，为本文引言中“深度学习在计算机视觉、自然语言处理等任务中达到SOTA性能”的背景陈述提供基础支撑。

2. **发表信息**：Bengio Y, Courville A, Vincent P. Representation learning: A review and new perspectives. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2013, 35(8): 1798-1828.
**与本文关联**：表征学习领域的经典综述，明确了特征学习的核心定义与研究范畴，是本文提出“CNN特征学习机制”核心问题的理论背景依据。

3. **发表信息**：Yu D, Seltzer M L, Li J, et al. Feature learning in deep neural networks-studies on speech recognition tasks. arXiv preprint arXiv:1301.3605, 2013.
**与本文关联**：语音识别领域的深度神经网络特征学习实证研究，补充了特征学习在实际任务中应用价值的背景证据。

4. **发表信息**：Ciceri S, et al. Inversion dynamics of class manifolds in deep learning reveals tradeoffs underlying generalization. *Nature Machine Intelligence*, 2024, 6: 40-47.
**与本文关联**：研究深度学习中类别流形的反转动力学与泛化权衡，为本文探讨特征学习与泛化性能的关联提供了动力学视角的参考。

5. **发表信息**：Neal R M. Bayesian Learning for Neural Networks. Springer New York, 1996: 29-53.
**与本文关联**：贝叶斯神经网络领域的经典奠基著作，构建了贝叶斯框架下神经网络学习的基础理论，是本文采用贝叶斯统计力学分析框架的早期理论源头。

6. **发表信息**：Williams C. Computing with infinite networks. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.9, MIT Press, 1996.
**与本文关联**：最早提出无限宽度神经网络与高斯过程等价性的先驱工作，为本文中无限宽度极限（NNGP核）的研究提供了最初的理论雏形。

7. **发表信息**：de G. Matthews A G, Hron J, Rowland M, et al. Gaussian process behaviour in wide deep neural networks. *International Conference on Learning Representations (ICLR)*, 2018.
**与本文关联**：系统验证了宽深度神经网络的高斯过程行为，是无限宽度神经网络理论发展的关键工作，支撑本文中全连接网络无限宽度核的理论背景。

8. **发表信息**：Lee J, et al. Deep neural networks as gaussian processes. *International Conference on Learning Representations (ICLR)*, 2018.
**与本文关联**：神经正切核与NNGP领域的经典核心工作，推导了深度全连接网络的无限宽度高斯过程核；同时其实证观察（全连接网络宽度增加测试精度提升）是本文引言核心问题的重要经验依据。

9. **发表信息**：Garriga-Alonso A, Rasmussen C E, Aitchison L. Deep convolutional networks as shallow gaussian processes. *International Conference on Learning Representations (ICLR)*, 2019.
**与本文关联**：首次将无限宽度高斯过程理论扩展到卷积神经网络，证明深度CNN可等价为浅层高斯过程，是本文卷积核无限宽度极限的重要前期参考。

10. **发表信息**：Novak R, et al. Bayesian deep convolutional networks with many channels are gaussian processes. *International Conference on Learning Representations (ICLR)*, 2019.
**与本文关联**：证明多通道贝叶斯深度CNN在通道数趋于无穷时等价于高斯过程，推导了CNN的局部核形式；本文结果部分的局部核定义、无限宽度CNN核公式均直接参考该工作的结论。

11. **发表信息**：Arora S, et al. On exact computation with an infinitely wide neural net. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.32, Curran Associates, Inc., 2019.
**与本文关联**：提出无限宽度神经网络核的精确计算方法，为本文中核函数的数值计算与验证提供了方法学参考。

12. **发表信息**：Jacot A, Gabriel F, Hongler C. Neural tangent kernel: Convergence and generalization in neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.31, Curran Associates, Inc., 2018.
**与本文关联**：提出神经正切核（NTK）理论，定义了懒惰训练（lazy training） regime，是本文引言中“无限宽度-懒惰训练”研究分支的核心理论基础。

13. **发表信息**：Chizat L, Oyallon E, Bach F. On lazy training in differentiable programming. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.32, Curran Associates, Inc., 2019.
**与本文关联**：系统分析了可微编程中的懒惰训练现象，进一步明确了懒惰训练的适用条件与性质，补充了无限宽度训练 regime 的理论背景。

14. **发表信息**：Lee J, et al. Wide neural networks of any depth evolve as linear models under gradient descent. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.32, Curran Associates, Inc., 2019.
**与本文关联**：证明任意深度的宽神经网络在梯度下降下均演化为线性模型，完善了懒惰训练 regime 的核心结论，支撑本文对无限宽度全连接网络特性的讨论。

15. **发表信息**：Aitchison L. Why bigger is not always better: on finite and infinite neural networks. *Proceedings of the 37th International Conference on Machine Learning (ICML)*, PMLR, 2020: 156-164.
**与本文关联**：讨论有限与无限神经网络的性能差异，直接呼应本文引言提出的“全连接无限宽更优、CNN有限宽更优”的核心问题，提供了理论层面的对比视角。

16. **发表信息**：Favaro S, Hanin B, Marinucci D, et al. Quantitative clts in deep neural networks. arXiv preprint arXiv:2307.06092, 2023.
**与本文关联**：研究深度神经网络中的定量中心极限定理，为本文推导中使用的高斯等价假设提供了数学层面的支撑依据。

17. **发表信息**：Mei S, Montanari A, Nguyen P-M. A mean field view of the landscape of two-layer neural networks. *Proceedings of the National Academy of Sciences (PNAS)*, 2018, 115: E7665-E7671.
**与本文关联**：平均场特征学习 regime 的经典奠基工作，从平均场视角分析两层神经网络的损失景观，是本文引言中“特征学习 regime”分类的重要参考。

18. **发表信息**：Chizat L, Bach F. On the global convergence of gradient descent for over-parameterized models using optimal transport. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.31, Curran Associates, Inc., 2018.
**与本文关联**：基于最优传输理论证明过参数化模型梯度下降的全局收敛性，是平均场特征学习 regime 的核心理论成果，补充了特征学习的动力学背景。

19. **发表信息**：Sirignano J, Spiliopoulos K. Mean field analysis of neural networks: A law of large numbers. *SIAM Journal on Applied Mathematics*, 2020, 80: 725-752.
**与本文关联**：从大数定律角度建立神经网络的平均场分析框架，完善了平均场特征学习的数学基础，为本文的比例极限 regime 提供了对比参照。

20. **发表信息**：Rotskoff G, Vanden-Eijnden E. Parameters as interacting particles: long time convergence and asymptotic error scaling of neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.31, Curran Associates, Inc., 2018.
**与本文关联**：将神经网络参数视为相互作用粒子系统，从粒子动力学角度分析训练收敛与误差标度，为特征学习的动力学机制提供了统计物理视角的参考。

21. **发表信息**：Yang G, Hu E J. Tensor programs iv: Feature learning in infinitewidth neural networks. *Proceedings of the 38th International Conference on Machine Learning (ICML)*, PMLR, 2021: 11727-11737.
**与本文关联**：Tensor Programs系列工作之一，证明无限宽度神经网络中也可存在特征学习，丰富了本文对“无限宽度 vs 有限宽度特征学习”的讨论背景。

22. **发表信息**：Cagnetta F, Favero A, Wyart M. What can be learnt with wide convolutional neural networks? 2023, OpenReview.
**与本文关联**：专门探讨宽卷积神经网络的特征学习能力边界，与本文CNN特征学习的核心主题直接相关，是重要的同类研究参考。

23. **发表信息**：Favero A, Cagnetta F, Wyart M. Locality defeats the curse of dimensionality in convolutional teacher-student scenarios. *Advances in Neural Information Processing Systems (NeurIPS)*, 2021.
**与本文关联**：在师生学习场景下证明卷积的局部性可克服维度灾难，解释了CNN的学习优势，为本文“局部核重整化是CNN特征学习机制”的结论提供了侧面支撑。

24. **发表信息**：Petrini L, Cagnetta F, Vanden-Eijnden E, et al. Learning sparse features can lead to overfitting in neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 2022.
**与本文关联**：研究稀疏特征学习与过拟合的关联，补充了特征学习对泛化性能影响的复杂特性，为本文泛化误差分析提供了参考视角。

25. **发表信息**：Zavatone-Veth J A, Pehlevan C. Exact marginal prior distributions of finite Bayesian neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 2021.
**与本文关联**：推导有限贝叶斯神经网络的精确边缘先验分布，是有限宽度贝叶斯网络修正方向的相关工作，与本文比例极限的有限宽修正形成研究呼应。

26. **发表信息**：Yang A X, Robeyns M, Milsom E, et al. A theory of representation learning in deep neural networks gives a deep generalisation of kernel methods. arXiv:2108.13097, 2021.
**与本文关联**：提出深度神经网络表征学习的统一核方法推广理论，与本文“核重整化解释特征学习”的研究思路高度契合，提供了核视角的表征学习理论参考。

27. **发表信息**：Zavatone-Veth J, Canatar A, Ruben B, et al. Asymptotics of representation learning in finite Bayesian neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.34, 2021: 24765-24777.
**与本文关联**：研究有限贝叶斯神经网络中表征学习的渐近行为，属于有限宽度修正方向的代表性工作，与本文的比例极限研究同属“超越无限宽度”的研究脉络。

28. **发表信息**：Hanin B. Random fully connected neural networks as perturbatively solvable hierarchies. arXiv:2204.01058, 2023.
**与本文关联**：从微扰修正角度分析随机全连接网络，属于无限宽度极限的微扰扩展研究，是本文引言中提到的“无限宽度微扰修正”研究分支的代表工作。

29. **发表信息**：Antognini J M. Finite size corrections for neural network Gaussian processes. arXiv:1908.10030, 2019.
**与本文关联**：研究神经网络高斯过程的有限尺寸修正效应，是无限宽度NNGP的有限宽修正方向的早期工作，与本文比例极限的研究目标相关。

30. **发表信息**：Yaida S. Non-Gaussian processes and neural networks at finite widths. *Proceedings of The First Mathematical and Scientific Machine Learning Conference*, PMLR, 2020: 165-192.
**与本文关联**：分析有限宽度下神经网络的非高斯过程特性，指出有限宽会偏离NNGP的高斯假设，为本文的比例极限核重整化提供了现象层面的背景支撑。

31. **发表信息**：Roberts D A, Yaida S, Hanin B. *The Principles of Deep Learning Theory*. Cambridge University Press, 2022.
**与本文关联**：深度学习统计力学理论的权威专著，系统梳理了宽网络、核方法、有限宽修正等理论方向，为本文的整体研究框架提供了完整的背景知识体系。

32. **发表信息**：Li Q, Sompolinsky H. Statistical mechanics of deep linear neural networks: The backpropagating kernel renormalization. *Physical Review X*, 2021, 11: 031059.
**与本文关联**：推导了深度线性神经网络的统计力学框架与反向传播核重整化机制，是本文有效作用量方法在线性场景下的先驱工作，为非线性网络的推导提供了范式参考。

33. **发表信息**：Hanin B, Zlokapa A. Bayesian interpolation with deep linear networks. *Proceedings of the National Academy of Sciences (PNAS)*, 2023, 120: e2301345120.
**与本文关联**：研究深度线性网络的贝叶斯插值与泛化误差，完善了线性神经网络比例极限的结论，是本文方法学的线性基准参考。

34. **发表信息**：Li Q, Sompolinsky H. Globally gated deep linear networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 2024: 34789-34801.
**与本文关联**：将深度线性网络的统计力学框架扩展到全局门控结构，是线性网络核重整化研究的延伸，体现了该分析框架的可扩展性。

35. **发表信息**：Zavatone-Veth J A, Tong W L, Pehlevan C. Contrasting random and learned features in deep Bayesian linear regression. *Physical Review E*, 2022, 105: 064118.
**与本文关联**：在深度贝叶斯线性回归中对比随机特征与学习特征的差异，从线性角度探讨特征学习的本质，为本文非线性CNN特征学习的结论提供了线性对照。

36. **发表信息**：Seroussi I, Naveh G, Ringel Z. Separation of scales and a thermodynamic description of feature learning in some cnns. *Nature Communications*, 2023, 14: 908.
**与本文关联**：同样从热力学统计力学角度研究CNN的特征学习机制，提出尺度分离框架，是本文最直接的同类核心相关工作；本文在讨论部分将自身结论与该工作进行了对标。

37. **发表信息**：Naveh G, Ringel Z. A self consistent theory of gaussian processes captures feature learning effects in finite cnns. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.34, 2021: 21352-21364.
**与本文关联**：提出自洽高斯过程理论来捕捉有限CNN的特征学习效应，是有限宽度CNN核修正方向的关键前期工作，为本文的局部核重整化结论提供了对照参考。

38. **发表信息**：Pacelli R, Ariosto S, Pastore M, et al. A statistical mechanics framework for bayesian deep neural networks beyond the infinite-width limit. *Nature Machine Intelligence*, 2023, 5(12): 1497-1507.
**与本文关联**：本文作者团队的核心前期工作，首次推导了全连接深度神经网络在比例极限下的有效作用量与全局核重整化机制；本文的整体分析框架、推导方法均直接基于该工作，将其从全连接扩展到卷积与局部连接网络。

39. **发表信息**：Baglioni P, Pacelli R, Aiudi R, et al. Predictive power of a bayesian effective action for fully connected one hidden layer neural networks in the proportional limit. *Physical Review Letters*, 2024, 133: 027301.
**与本文关联**：本文作者团队的前期实验验证工作，通过数值实验验证了全连接单隐层网络比例极限有效作用量的预测准确性；本文的数值实验方法、验证思路均参考该工作的范式。

40. **发表信息**：Ingrosso A, Pacelli R, Rotondo P, et al. Statistical mechanics of transfer learning in fully-connected networks in the proportional limit. arXiv preprint arXiv:2407.07168, 2024.
**与本文关联**：本文作者团队将比例极限有效作用量框架扩展到迁移学习场景，体现了该理论框架的通用性，是同一系列的延伸研究。

41. **发表信息**：MacKay D J C. A Practical Bayesian Framework for Backpropagation Networks. *Neural Computation*, 1992, 4: 448-472.
**与本文关联**：贝叶斯反向传播神经网络的经典先驱工作，最早建立了实用的贝叶斯神经网络训练框架，是本文贝叶斯研究范式的早期理论源头。

42. **发表信息**：Grant E, Nestler S, Şimşek B, et al. Statistical physics, Bayesian inference, and neural information processing. *Journal of Statistical Mechanics: Theory and Experiment*, 2024: 104005.
**与本文关联**：统计物理与贝叶斯神经网络交叉领域的最新综述，系统梳理了该领域的研究脉络，为本文的跨学科研究视角提供了背景支撑。

43. **发表信息**：Williams C K, Rasmussen C E. *Gaussian processes for machine learning*, vol. 2. MIT press Cambridge, MA, 2006.
**与本文关联**：高斯过程机器学习领域的经典权威教材，系统介绍了高斯过程回归、核方法等基础理论，是本文中NNGP核、贝叶斯预测分布等内容的基础知识参考。

44. **发表信息**：Lee J, et al. Finite versus infinite neural networks: an empirical study. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.33, 2020: 15156-15172.
**与本文关联**：大规模实证对比有限与无限宽度神经网络的泛化性能，明确观察到“全连接网络无限宽更优、CNN有限宽更优”的现象；这一经验观察是本文研究问题的核心出发点。

45. **发表信息**：Atanasov A, Bordelon B, Sainathan S, et al. The onset of variance-limited behavior for networks in the lazy and rich regimes. *The Eleventh International Conference on Learning Representations (ICLR)*, 2023.
**与本文关联**：研究懒惰与丰富训练 regime 下网络的方差限制行为，观察到训练集增大时全连接无限宽网络逐渐超过有限宽，进一步支撑了本文引言中的核心经验观察。

46. **发表信息**：Geiger M, Petrini L, Wyart M. Landscape and training regimes in deep learning. *Physics Reports*, 2021, 924: 1-18.
**与本文关联**：深度学习损失景观与训练 regime 的权威综述，系统区分了懒惰训练与特征学习两种 regime，为本文的研究定位提供了清晰的领域分类框架。

47. **发表信息**：Geiger M, Spigler S, Jacot A, et al. Disentangling feature and lazy training in deep neural networks. *Journal of Statistical Mechanics: Theory and Experiment*, 2020: 113301.
**与本文关联**：提出解耦特征学习与懒惰训练的定量方法，是区分两种训练 regime 的经典工作；本文对“特征学习机制”的讨论均建立在该工作的定义基础上。

48. **发表信息**：Aiudi R, et al. Supplementary information for “local kernel renormalization as a mechanism for feature learning in overparametrized convolutional neural networks”. 2024.
**与本文关联**：本文的配套补充材料，包含补充推导、实验细节、补充图表等内容，是正文结论的补充支撑。

49. **发表信息**：Pacelli R, Baglioni P. deepbays. GitHub/Zenodo, 2024.
**与本文关联**：本文作者团队开源的Python工具包，可复现本文的贝叶斯网络实验与理论预测，是研究结果可复现性的代码支撑。

50. **发表信息**：Kingma D P, Ba J. Adam: a method for stochastic optimization. *3rd International Conference on Learning Representations (ICLR)*, 2015.
**与本文关联**：Adam随机优化算法的原始文献，本文数值实验中采用该优化器进行梯度下降训练，属于方法工具类引用。

51. **发表信息**：Aiudi R. Numerical experiments on internal representations. GitHub repository: [https://github.com/ricaiu/PhD/tree/main/lkr](https://github.com/ricaiu/PhD/tree/main/lkr), 2024.
**与本文关联**：本文内部表示实验的配套开源代码，用于复现相似矩阵、有限尺寸标度等数值实验。

52. **发表信息**：Ingrosso A, Goldt S. Data-driven emergence of convolutional structure in neural networks. *Proceedings of the National Academy of Sciences (PNAS)*, 2022, 119: e2201854119.
**与本文关联**：证明全连接网络可在特定数据下涌现出卷积结构，补充了“全连接网络也可实现类卷积特征学习”的特例；本文在讨论部分引用该工作，说明自身结论的适用边界。

53. **发表信息**：Bassetti F, Gherardi M, Ingrosso A, et al. Feature learning in finite-width bayesian deep linear networks with multiple outputs and convolutional layers. arXiv:2406.03260, 2024.
**与本文关联**：研究多输出、带卷积层的深度线性网络有限宽特征学习，是本文卷积核重整化在线性场景下的对应研究，为非线性结论提供了线性基准对照。

54. **发表信息**：Mei S, Montanari A. The generalization error of random features regression: Precise asymptotics and the double descent curve. *Communications on Pure and Applied Mathematics*, 2019.
**与本文关联**：推导随机特征回归的精确泛化误差渐近与双下降现象，是随机特征理论的经典工作；本文的高斯等价假设、泛化误差分析均参考该工作的理论框架。

55. **发表信息**：Goldt S, et al. The Gaussian equivalence of generative models for learning with shallow neural networks. *Proceedings of the 2nd Mathematical and Scientific Machine Learning Conference*, PMLR, 2022: 426-471.
**与本文关联**：证明浅层神经网络生成模型的高斯等价性，为本文推导中采用的高斯近似假设提供了进一步的理论支撑。

56. **发表信息**：Gerace F, Loureiro B, Krzakala F, et al. Generalisation error in learning with random features and the hidden manifold model. *Journal of Statistical Mechanics: Theory and Experiment*, 2021: 124013.
**与本文关联**：研究随机特征与隐藏流形模型的泛化误差，完善了随机特征理论的泛化分析，为本文的泛化误差计算提供了方法参考。

57. **发表信息**：Aguirre-López F, Franz S, Pastore M. Random features and polynomial rules. arXiv:2402.10164, 2024.
**与本文关联**：研究随机特征与多项式规则的关联，补充了随机特征理论的应用场景，丰富了高斯等价假设的研究背景。

58. **发表信息**：Loureiro B, et al. Learning curves of generic features maps for realistic datasets with a teacher-student model. *Advances in Neural Information Processing Systems (NeurIPS)*, vol.34, 2021: 18137-18151.
**与本文关联**：基于师生模型推导通用特征映射的学习曲线，为本文的泛化性能分析、师生实验设置提供了方法学参考。

59. **发表信息**：Breuer P, Major P. Central limit theorems for non-linear functionals of Gaussian fields. *Journal of Multivariate Analysis*, 1983, 13: 425-444.
**与本文关联**：Breuer-Major定理的原始文献，该定理是本文高斯等价假设的核心数学基础（广义中心极限定理），支撑了有效作用量推导的数学严谨性。

60. **发表信息**：Shah A, Wilson A, Ghahramani Z. Student-t Processes as Alternatives to Gaussian Processes. *Proceedings of the 17th International Conference on Artificial Intelligence and Statistics (AISTATS)*, PMLR, 2010: 877-885.
**与本文关联**：学生t过程的经典文献，本文在讨论比例极限下的随机过程时，提及该过程与Student's t过程的关联，以此作为理论对照。

61. **发表信息**：Cui H, Krzakala F, Zdeborová L. Bayes-optimal learning of deep random networks of extensive-width. *Proceedings of the 40th International Conference on Machine Learning (ICML)*, 2023.
**与本文关联**：采用复制品方法研究宽深度随机网络的贝叶斯最优学习，属于比例极限师生场景的同类研究，为本文的热力学极限分析提供了方法参考。

62. **发表信息**：Schröder D, Cui H, Dmitriev D, et al. Deterministic equivalent and error universality of deep random features learning. *Journal of Statistical Mechanics: Theory and Experiment*, 2024: 104017.
**与本文关联**：研究深度随机特征学习的确定性等价与误差普适性，补充了核方法与随机特征的泛化普适性结论，与本文核重整化的泛化影响形成呼应。

63. **发表信息**：Camilli F, Tieplova D, Barbier J. Fundamental limits of overparametrized shallow neural networks for supervised learning. arXiv preprint arXiv:2307.05635, 2023.
**与本文关联**：采用插值方法得到了近比例极限下过参数化浅层网络的严格结果，为本文的比例极限结论提供了数学严谨性层面的参考与对照。

64. **发表信息**：Guerra F, Toninelli F L. The thermodynamic limit in mean field spin glass models. *Communications in Mathematical Physics*, 2002, 230: 71-79.
**与本文关联**：Guerra插值方法的原始文献，该方法是自旋玻璃热力学极限严格证明的核心工具，也是文献63中插值方法的理论源头。

65. **发表信息**：Agliari E, Alemanno F, Barra A, et al. Generalized guerra’s interpolation schemes for dense associative neural networks. *Neural Networks*, 2020, 128: 254-267.
**与本文关联**：将Guerra插值方法扩展到密集联想神经网络，体现了插值方法在神经网络理论中的应用，补充了比例极限严格证明的方法背景。

66. **发表信息**：Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images. Technical Report 0, University of Toronto, 2009.
**与本文关联**：CIFAR-10图像数据集的原始技术报告，本文数值实验采用该数据集进行验证，属于数据来源类引用。

67. **发表信息**：LeCun Y, Bottou L, Bengio Y, et al. Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 1998, 86: 2278-2324.
**与本文关联**：MNIST手写数字数据集的原始文献，本文引言中提及该数据集作为计算机视觉基准，属于基准数据集来源类引用。