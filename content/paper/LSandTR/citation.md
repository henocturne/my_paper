### 一、论文作者所属机构与院系
该论文三位作者均隶属于**洛桑联邦理工学院（École Polytechnique Fédérale de Lausanne, EPFL）**，具体信息如下：

1. **Mario Geiger（第一作者）**
   - 论文发表时（2021年）：EPFL 物理学院（Institute of Physics），复杂系统物理实验室（Physics of Complex Systems Laboratory, PCSL）
   - 后续任职：麻省理工学院（MIT）电子工程与计算机科学系（Department of Electrical Engineering and Computer Science）

2. **Leonardo Petrini（第二作者）**
   - EPFL 物理学院（Institute of Physics），复杂系统物理实验室（PCSL），博士研究生，导师为 Matthieu Wyart 教授

3. **Matthieu Wyart（通讯作者）**
   - EPFL 物理学院（Institute of Physics），复杂系统物理实验室（PCSL），正教授
   - 同时兼任约翰斯·霍普金斯大学（Johns Hopkins University）教职，研究方向为统计物理与深度学习理论交叉领域

---

### 二、核心合作者与合作机构
三位作者的研究团队以EPFL PCSL实验室为核心，长期与全球多所高校、科研机构的学者开展合作：

#### 核心合作者
- EPFL内部：Arthur Jacot、Clément Hongler、Francesco Cagnetta、Alessandro Favero、Antonio Sclocchi、Umberto Maria Tomasini、Jonas Paccolat、Kevin Tyloo、Stefano Spigler等
- 国际合作学者：Giulio Biroli（巴黎高等师范学院）、Eric Vanden-Eijnden（纽约大学）、Levent Sagun、Stéphane d'Ascoli、Bloen Metzger（艾克斯-马赛大学）等

#### 主要合作机构
巴黎高等师范学院（ENS Paris）、法国国家科学研究中心（CNRS）、艾克斯-马赛大学（Aix Marseille University）、纽约大学（NYU）、麻省理工学院（MIT）、约翰斯·霍普金斯大学等。

---

### 三、近年代表论文（每人5-10篇）

#### 1. 第一作者 Mario Geiger 代表论文
聚焦深度学习损失景观、训练机制、泛化理论方向：
1. *Landscape and training regimes in deep learning*. **Physics Reports**, 2021（本综述论文）
2. *Disentangling feature and lazy training in deep neural networks*. **Journal of Statistical Mechanics: Theory and Experiment**, 2020
3. *Scaling description of generalization with number of parameters in deep learning*. **Journal of Statistical Mechanics: Theory and Experiment**, 2020
4. *Jamming transition as a paradigm to understand the loss landscape of deep neural networks*. **Physical Review E**, 2019
5. *A jamming transition from under- to over-parametrization affects generalization in deep learning*. **Journal of Physics A: Mathematical and Theoretical**, 2019
6. *Dissecting the Effects of SGD Noise in Distinct Regimes of Deep Learning*. **ICML 2023**
7. *Asymptotic learning curves of kernel methods: empirical data v.s. Teacher-Student paradigm*. **Journal of Statistical Mechanics: Theory and Experiment**, 2020

#### 2. Leonardo Petrini 代表论文
聚焦深度学习不变性学习、特征学习机制、卷积网络性质方向：
1. *Landscape and training regimes in deep learning*. **Physics Reports**, 2021
2. *Relative stability toward diffeomorphisms indicates performance in deep nets*. **NeurIPS 2021**
3. *Learning sparse features can lead to overfitting in neural networks*. **NeurIPS 2022** / **Journal of Statistical Mechanics: Theory and Experiment**, 2023
4. *How deep convolutional neural networks lose spatial information with training*. **Machine Learning: Science and Technology**, 2023
5. *Geometric compression of invariant manifolds in neural nets*. **Journal of Statistical Mechanics: Theory and Experiment**, 2021
6. *How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model*. arXiv preprint, 2023

#### 3. 通讯作者 Matthieu Wyart 代表论文
覆盖统计物理、深度学习理论、扩散模型、大语言模型等多个方向：
1. *Landscape and training regimes in deep learning*. **Physics Reports**, 2021
2. *A phase transition in diffusion models reveals the hierarchical nature of data*. **PNAS (Proceedings of the National Academy of Sciences)**, 2025
3. *How compositional generalization and creativity improve as diffusion models are trained*. **ICML 2025**
4. *On the Emergence of Linear Analogies in Word Embeddings*. **NeurIPS 2025**
5. *Disentangling feature and lazy training in deep neural networks*. **Journal of Statistical Mechanics: Theory and Experiment**, 2020
6. *Scaling description of generalization with number of parameters in deep learning*. **Journal of Statistical Mechanics: Theory and Experiment**, 2020
7. *Bigger isn’t always memorizing: Early stopping overparameterized diffusion models*. **Transactions on Machine Learning Research (TMLR)**, 2026
8. *A jamming transition from under- to over-parametrization affects generalization in deep learning*. **Journal of Physics A: Mathematical and Theoretical**, 2019


### 论文研究方向与所属领域概述
该论文属于**统计物理与深度学习理论的交叉领域**，核心研究方向为深度神经网络的损失景观几何性质、过参数化相变、不同训练机制（懒训练/神经正切核 regime 与特征学习 regime）的划分与性能差异、双下降泛化现象的物理起源，以及深度学习突破维数灾难的不变性学习机制。相关研究课题包括：深度网络损失景观的jamming相变理论、过参数化网络的优化收敛性、神经正切核（NTK）与平均场特征学习的定量分界、有限宽度网络的涨落缩放规律、不变性学习的几何压缩机制、学习曲线的幂律标度理论等。

---

### 逐条引文关联说明
1. **引用序号**：1
**发表信息**：David Marr, Tomaso Poggio. *A computational theory of human stereo vision*. Proceedings of the Royal Society of London B: Biological Sciences, 204(1156): 301–328, 1979.
**与本文关联**：本文引言将视觉任务作为深度学习的核心应用场景，该文献是生物视觉计算理论的奠基性工作，为“深度学习受灵长类视觉皮层启发”的背景论述提供了早期理论框架。

2. **引用序号**：2
**发表信息**：Yann LeCun, Yoshua Bengio, Geoffrey Hinton. *Deep learning*. Nature, 521(7553): 436, 2015.
**与本文关联**：本文开篇介绍深度学习的技术革命背景，该文献是深度学习领域的里程碑综述，系统阐述了深度学习的核心原理、架构与应用成就，是本文研究背景的核心引入依据。

3. **引用序号**：3
**发表信息**：Dario Amodei et al. *Deep speech 2: End-to-end speech recognition in english and mandarin*. Proceedings of the 33rd International Conference on Machine Learning (ICML), 2016: 173–182.
**与本文关联**：本文列举语音识别作为深度学习的标志性应用场景，该文献是端到端语音识别的代表性成果，用于佐证深度学习在语音任务中的技术突破。

4. **引用序号**：4
**发表信息**：Baoguang Shi, Xiang Bai, Cong Yao. *An end-to-end trainable neural network for image-based sequence recognition and its application to scene text recognition*. IEEE Transactions on Pattern Analysis and Machine Intelligence, 39(11): 2298–2304, 2016.
**与本文关联**：本文提及深度学习在文本识别任务中的应用，该文献是场景文本识别的端到端深度学习方案代表，补充说明了深度学习在序列类视觉任务中的有效性。

5. **引用序号**：5
**发表信息**：Brody Huval et al. *An empirical evaluation of deep learning on highway driving*. arXiv preprint arXiv:1504.01716, 2015.
**与本文关联**：本文将自动驾驶列为深度学习的核心应用场景之一，该文献是深度学习在高速驾驶场景中的实证评估研究，支撑了深度学习在自动驾驶领域的应用进展论述。

6. **引用序号**：6
**发表信息**：David Silver et al. *Mastering the game of go without human knowledge*. Nature, 550(7676): 354–359, 2017.
**与本文关联**：本文提及AlphaGo击败人类顶尖棋手是深度学习的标志性成就，该文献是AlphaGo Zero的核心论文，代表深度学习在复杂决策任务中的突破，用于佐证深度学习技术的革命性影响。

7. **引用序号**：7
**发表信息**：Volodymyr Mnih et al. *Playing atari with deep reinforcement learning*. arXiv preprint arXiv:1312.5602, 2013.
**与本文关联**：本文列举电子游戏作为深度学习的应用场景，该文献是深度强化学习的开创性工作（DQN算法），首次实现深度网络直接从像素学习玩Atari游戏，支撑深度学习在决策控制领域的进展论述。

8. **引用序号**：8
**发表信息**：Mario Geiger, Stefano Spigler, Stéphane d’Ascoli, Levent Sagun, Marco Baity-Jesi, Giulio Biroli, Matthieu Wyart. *Jamming transition as a paradigm to understand the loss landscape of deep neural networks*. Physical Review E, 100(1): 012115, 2019.
**与本文关联**：本文核心理论之一是将深度学习损失景观的参数化转变类比为物理中的jamming转变，该文献是作者团队提出该类比的原创核心工作，系统论证了深度网络损失景观的jamming相变性质，是本文第2章的核心理论基础。

9. **引用序号**：9
**发表信息**：Quoc V. Le. *Building high-level features using large scale unsupervised learning*. Proceedings of 2013 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2013: 8595–8598.
**与本文关联**：本文提及深度网络会逐层学习从简单到抽象的特征，该文献是无监督特征学习的代表性工作，验证了深度网络能从大规模数据中自发学习高层特征，支撑了“深度网络分层表征”的相关论述。

10. **引用序号**：10
**发表信息**：Arthur Jacot, Franck Gabriel, Clément Hongler. *Neural tangent kernel: Convergence and generalization in neural networks*. Proceedings of the 32nd International Conference on Neural Information Processing Systems (NeurIPS), 2018: 8580–8589.
**与本文关联**：本文核心概念“神经正切核（NTK）/懒训练”的奠基性论文，首次证明宽网络在梯度下降下收敛于核方法，是本文第3、4章区分NTK与特征学习机制的核心理论依据。

11. **引用序号**：11
**发表信息**：Joel Hestness et al. *Deep learning scaling is predictable, empirically*. arXiv preprint arXiv:1712.00409, 2017.
**与本文关联**：本文用学习曲线指数β量化深度学习性能随数据量的变化规律，该文献系统测量了不同任务下深度学习的缩放定律与学习曲线指数，为本文1.1节中性能量化部分提供了实证数据参考。

12. **引用序号**：12
**发表信息**：Bolei Zhou, Aditya Khosla, Agata Lapedriza, Aude Oliva, Antonio Torralba. *Object detectors emerge in deep scene cnns*. arXiv preprint arXiv:1412.6856, 2014.
**与本文关联**：本文论述深度网络深层神经元会响应高级语义特征，该文献验证了卷积网络中会自发涌现目标检测能力，支撑了“深度网络分层提取抽象特征”的相关论断。

13. **引用序号**：13
**发表信息**：Ulrike von Luxburg, Olivier Bousquet. *Distance-based classification with Lipschitz functions*. Journal of Machine Learning Research, 5(Jun): 669–675, 2004.
**与本文关联**：本文1.2节讨论“维数灾难”的理论根源，该文献严格证明了Lipschitz假设下高维分类的误差下界，是维数灾难理论的经典推导依据，用于支撑“高维空间中通用分类本质困难”的立论。

14. **引用序号**：14
**发表信息**：Francis Bach. *Breaking the curse of dimensionality with convex neural networks*. Journal of Machine Learning Research, 18(1): 629–681, 2017.
**与本文关联**：本文讨论深度学习如何突破维数灾难，该文献从凸神经网络角度论证了网络结构可缓解维数灾难，同时也是NTK与特征学习性能对比的相关理论参考。

15. **引用序号**：15
**发表信息**：Ludovic Berthier, Giulio Biroli. *Theoretical perspective on the glass transition and amorphous materials*. Reviews of Modern Physics, 83(2): 587, 2011.
**与本文关联**：本文将损失景观与玻璃态系统的能量景观做类比，该文献是玻璃转变理论的经典综述，为理解高维非凸景观的复杂性质提供了统计物理背景，支撑了损失景观与玻璃态的类比论述。

16. **引用序号**：16
**发表信息**：Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, Yann LeCun. *The loss surfaces of multilayer networks*. Proceedings of the 18th International Conference on Artificial Intelligence and Statistics (AISTATS), 2015: 192–204.
**与本文关联**：本文1.2节提出“损失景观存在大量差的局部极小”这一经典疑问，该文献是早期从统计物理视角分析深度网络损失曲面的代表性工作，将损失景观与自旋玻璃能量景观类比，是本文相关讨论的前期研究基础。

17. **引用序号**：17
**发表信息**：Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals. *Understanding deep learning requires rethinking generalization*. Proceedings of the 5th International Conference on Learning Representations (ICLR), 2017.
**与本文关联**：本文1.2节讨论过参数化网络的泛化悖论——参数远多于数据仍能良好泛化，该文献是提出该“泛化悖论”的标志性论文，通过实验证明深度网络可拟合随机标签，引发了对过参数化泛化机制的广泛讨论，是本文核心研究问题的重要背景。

18. **引用序号**：18
**发表信息**：Behnam Neyshabur, Ryota Tomioka, Ruslan Salakhutdinov, Nathan Srebro. *Geometry of optimization and implicit regularization in deep learning*. arXiv preprint arXiv:1705.03071, 2017.
**与本文关联**：本文1.3节提出“隐式正则化”是过参数化网络泛化的核心原因，该文献从优化几何角度系统讨论了梯度下降的隐式正则化效应，是本文相关论述的核心参考文献之一。

19. **引用序号**：19
**发表信息**：Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, Nathan Srebro. *Towards understanding the role of over-parametrization in generalization of neural networks*. arXiv preprint arXiv:1805.12076, 2018.
**与本文关联**：本文讨论过参数化对泛化的影响，该文献进一步分析了过参数化如何通过影响优化路径带来隐式正则化，支撑了本文关于过参数化收益的理论讨论。

20. **引用序号**：20
**发表信息**：Yamini Bansal, Madhu Advani, David D. Cox, Andrew M. Saxe. *Minnorm training: An algorithm for training overcomplete deep neural networks*. arXiv preprint arXiv:1806.00730, 2018.
**与本文关联**：本文讨论过参数化网络的优化与泛化，该文献提出了最小范数训练算法，是过参数化网络隐式正则化方向的相关研究，补充了过参数化区间下优化性质的相关讨论。

21. **引用序号**：21
**发表信息**：Madhu S. Advani, Andrew M. Saxe, Haim Sompolinsky. *High-dimensional dynamics of generalization error in neural networks*. Neural Networks, 2020.
**与本文关联**：本文第3章讨论双下降现象，该文献从高维动力学角度分析了神经网络泛化误差随参数数量的变化规律，是回归任务中双下降现象的重要理论工作，为本文分类任务双下降的对比分析提供参考。

22. **引用序号**：22
**发表信息**：C. Daniel Freeman, Joan Bruna. *Topology and geometry of deep rectified network optimization landscapes*. Proceedings of the International Conference on Learning Representations (ICLR), 2017.
**与本文关联**：本文1.3节论述过参数化网络损失景观不存在坏的局部极小，该文献从拓扑与几何角度分析了ReLU网络的优化景观性质，支撑了“过参数化下损失景观连通、无坏极小”的论断。

23. **引用序号**：23
**发表信息**：Elad Hoffer, Itay Hubara, Daniel Soudry. *Train longer, generalize better: Closing the generalization gap in large batch training of neural networks*. Advances in Neural Information Processing Systems (NeurIPS), 2017: 1729–1739.
**与本文关联**：本文讨论深度网络的训练与泛化性质，该文献研究了训练时长、批次大小与泛化的关系，涉及训练动力学对泛化的影响，是本文训练机制相关讨论的补充实证参考。

24. **引用序号**：24
**发表信息**：Daniel Soudry, Yair Carmon. *No bad local minima: Data independent training error guarantees for multilayer neural networks*. arXiv preprint arXiv:1605.08361, 2016.
**与本文关联**：本文1.3节提出“过参数化网络无坏局部极小”的观点，该文献从理论上证明了特定条件下多层网络不存在坏的局部极小，是该方向的早期理论支撑。

25. **引用序号**：25
**发表信息**：Yaim Cooper. *The loss landscape of overparameterized neural networks*. arXiv preprint arXiv:1804.10200, 2018.
**与本文关联**：本文论述过参数化损失景观的几何性质，该文献系统分析了过参数化神经网络损失曲面的拓扑结构，进一步支撑了过参数化下损失景观连通性的结论。

26. **引用序号**：26
**发表信息**：Levent Sagun, Léon Bottou, Yann LeCun. *Singularity of the Hessian in deep learning*. Proceedings of the International Conference on Learning Representations (ICLR), 2017.
**与本文关联**：本文第2章通过海森矩阵（Hessian）谱分析损失景观性质，该文献首次实证发现深度网络损失的海森矩阵具有奇异性、大量零特征值，是本文景观曲率分析的重要实证依据。

27. **引用序号**：27
**发表信息**：Levent Sagun, Utku Evci, V. Uğur Güney, Yann Dauphin, Léon Bottou. *Empirical analysis of the Hessian of over-parametrized neural networks*. ICLR 2018 Workshop, arXiv:1706.04454, 2017.
**与本文关联**：本文分析过参数化网络海森矩阵的谱特性，该文献对过参数化网络的海森矩阵做了更系统的实证分析，验证了大量平坦方向的存在，支撑了jamming转变附近的景观性质讨论。

28. **引用序号**：28
**发表信息**：Andrew J Ballard et al. *Energy landscapes for machine learning*. Physical Chemistry Chemical Physics, 2017.
**与本文关联**：本文将机器学习损失景观与物理系统能量景观类比，该综述系统梳理了能量景观理论在机器学习中的应用，为本文的物理类比研究范式提供了框架参考。

29. **引用序号**：29
**发表信息**：Zachary C. Lipton. *Stuck in a what? Adventures in weight space*. Proceedings of the International Conference on Learning Representations (ICLR), 2016.
**与本文关联**：本文讨论损失景观中优化动力学是否会陷入局部极小，该文献从实证角度探讨了深度网络训练中“卡住”的现象，是早期关于损失景观优化路径的相关讨论。

30. **引用序号**：30
**发表信息**：Marco Baity-Jesi et al. *Comparing dynamics: Deep neural networks versus glassy systems*. Proceedings of the 35th International Conference on Machine Learning (ICML), PMLR 80: 314–323, 2018.
**与本文关联**：本文核心研究范式是将深度网络训练动力学与玻璃态系统动力学类比，该文献是作者团队的前期工作，首次系统对比了深度网络SGD动力学与玻璃态系统的动力学特征，为本文的物理类比提供了直接支撑。

31. **引用序号**：31
**发表信息**：Radford M. Neal. Bayesian Learning for Neural Networks. Springer-Verlag New York, Inc., 1996.
**与本文关联**：本文讨论无限宽网络的高斯过程性质，该著作是最早提出宽神经网络输出服从高斯过程的经典工作，是NTK理论的前期基础之一。

32. **引用序号**：32
**发表信息**：Christopher K.I. Williams. *Computing with infinite networks*. Advances in Neural Information Processing Systems (NeurIPS), 1997: 295–305.
**与本文关联**：本文介绍无限宽网络的极限性质，该文献首次推导了无限宽单隐层网络的高斯过程核，是神经高斯过程（NGP）方向的开创性工作，为NTK理论提供了前期铺垫。

33. **引用序号**：33
**发表信息**：Jae Hoon Lee et al. *Deep neural networks as Gaussian processes*. Proceedings of the International Conference on Learning Representations (ICLR), 2018.
**与本文关联**：本文讨论深度网络初始化时的信号传播与高斯过程性质，该文献将高斯过程结论推广到任意深度的全连接网络，是深度网络无限宽极限性质的重要理论工作。

34. **引用序号**：34
**发表信息**：Alexander G. de G. Matthews et al. *Gaussian process behaviour in wide deep neural networks*. Proceedings of the International Conference on Learning Representations (ICLR), 2018.
**与本文关联**：本文论述宽网络初始化的高斯过程性质，该文献独立证明了宽深度网络的高斯过程行为，与文献33共同构成深度NGP的核心理论基础。

35. **引用序号**：35
**发表信息**：Roman Novak et al. *Bayesian deep convolutional networks with many channels are Gaussian processes*. Proceedings of the International Conference on Learning Representations (ICLR), 2019.
**与本文关联**：本文涉及卷积网络的无限宽极限性质，该文献将高斯过程结论推广到多通道卷积网络，为本文讨论CNN的训练机制提供了核方法视角的理论参考。

36. **引用序号**：36
**发表信息**：Greg Yang. *Scaling limits of wide neural networks with weight sharing: Gaussian process behavior, gradient independence, and neural tangent kernel derivation*. arXiv preprint arXiv:1902.04760, 2019.
**与本文关联**：本文讨论权重共享网络（如CNN）的NTK推导，该文献系统给出了带权重共享的宽网络的高斯过程与NTK性质，是卷积网络NTK方向的重要理论工作。

37. **引用序号**：37
**发表信息**：Simon S. Du et al. *Gradient descent provably optimizes over-parameterized neural networks*. Proceedings of the International Conference on Learning Representations (ICLR), 2019.
**与本文关联**：本文论述过参数化网络梯度下降可收敛到全局最优，该文献从理论上证明了过参数化神经网络梯度下降的全局收敛性，支撑了“过参数化无坏极小”的核心论断。

38. **引用序号**：38
**发表信息**：Zeyuan Allen-Zhu, Yuanzhi Li, Zhao Song. *A convergence theory for deep learning via over-parameterization*. Proceedings of the 36th International Conference on Machine Learning (ICML), PMLR 97: 242–252, 2019.
**与本文关联**：本文讨论过参数化下的优化收敛性，该文献是深度网络过参数化收敛理论的代表性工作，证明了深度ReLU网络梯度下降可收敛到零训练损失，为本文过参数化区间的优化性质提供理论支撑。

39. **引用序号**：39
**发表信息**：Jaehoon Lee et al. *Wide neural networks of any depth evolve as linear models under gradient descent*. Advances in Neural Information Processing Systems (NeurIPS) 32, 2019: 8572–8583.
**与本文关联**：本文核心的NTK/懒训练理论支撑，该文献证明任意深度的宽网络在梯度下降下都等价于线性模型，NTK保持恒定，是本文区分懒训练与特征学习的核心理论依据之一。

40. **引用序号**：40
**发表信息**：Sanjeev Arora et al. *On exact computation with an infinitely wide neural net*. Advances in Neural Information Processing Systems (NeurIPS) 32, 2019: 8141–8150.
**与本文关联**：本文讨论无限宽NTK的计算与性质，该文献实现了无限宽神经网络的精确计算，为NTK的实证研究提供了方法支撑，也验证了宽网络的核方法极限。

41. **引用序号**：41
**发表信息**：Daniel Park, Jascha Sohl-Dickstein, Quoc Le, Samuel Smith. *The effect of network width on stochastic gradient descent and generalization: An empirical study*. Proceedings of the 36th International Conference on Machine Learning (ICML), PMLR 97: 5042–5051, 2019.
**与本文关联**：本文第3章讨论网络宽度对泛化性能的影响，该文献系统实证研究了网络宽度对SGD动力学与泛化的影响，为本文的宽度缩放理论提供了实证对照。

42. **引用序号**：42
**发表信息**：Bernhard Scholkopf, Alexander J. Smola. Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond. MIT Press, 2001.
**与本文关联**：本文涉及核方法的基础概念，该著作是核方法与支持向量机的经典教材，为读者理解NTK的核方法本质提供了基础知识参考，文中也明确推荐其作为核方法的入门文献。

43. **引用序号**：43
**发表信息**：Song Mei, Andrea Montanari, Phan-Minh Nguyen. *A mean field view of the landscape of two-layer neural networks*. Proceedings of the National Academy of Sciences, 115(33): E7665–E7671, 2018.
**与本文关联**：本文第4章讨论特征学习的平均场（mean field）极限，该文献是两层神经网络平均场景观理论的开创性工作，用平均场视角刻画了两层网络的损失景观，是本文特征学习区间的核心理论基础之一。

44. **引用序号**：44
**发表信息**：Grant M. Rotskoff, Eric Vanden-Eijnden. *Neural networks as interacting particle systems: Asymptotic convexity of the loss landscape and universal scaling of the approximation error*. arXiv preprint arXiv:1805.00915, 2018.
**与本文关联**：本文将特征学习类比为相互作用粒子系统的流体动力学描述，该文献首次将神经网络训练建模为相互作用粒子系统，证明了宽网络损失景观的渐近凸性，是本文平均场/特征学习机制的重要理论支撑。

45. **引用序号**：45
**发表信息**：Lénaïc Chizat, Francis Bach. *On the global convergence of gradient descent for over-parameterized models using optimal transport*. Advances in Neural Information Processing Systems (NeurIPS) 31, 2018: 3040–3050.
**与本文关联**：本文讨论特征学习区间的梯度下降收敛性，该文献用最优输运理论证明了过参数化两层网络梯度下降的全局收敛性，是平均场特征学习方向的核心理论工作。

46. **引用序号**：46
**发表信息**：Justin Sirignano, Konstantinos Spiliopoulos. *Mean field analysis of neural networks: A law of large numbers*. SIAM Journal on Applied Mathematics, 80(2): 725–752, 2020.
**与本文关联**：本文特征学习的平均场极限理论参考，该文献严格证明了神经网络的平均场大数定律，为宽网络的平均场描述提供了数学基础。

47. **引用序号**：47
**发表信息**：Song Mei, Theodor Misiakiewicz, Andrea Montanari. *Mean-field theory of two-layers neural networks: Dimension-free bounds and kernel limit*. Proceedings of the Conference on Learning Theory (COLT), PMLR: 2388–2464, 2019.
**与本文关联**：本文讨论两层网络平均场理论与核极限的关系，该文献建立了两层网络平均场理论的维度无关界，并分析了其与核极限的联系，支撑了本文对两种训练区间过渡的讨论。

48. **引用序号**：48
**发表信息**：Phan-Minh Nguyen. *Mean field limit of the learning dynamics of multilayer neural networks*. arXiv preprint arXiv:1902.02880, 2019.
**与本文关联**：本文涉及深层网络的特征学习平均场理论，该文献将平均场极限推广到多层神经网络，为深度网络特征学习区间的理论分析提供了扩展依据。

49. **引用序号**：49
**发表信息**：Justin Sirignano, Konstantinos Spiliopoulos. *Mean field analysis of neural networks: A central limit theorem*. Stochastic Processes and their Applications, 130(3): 1820–1852, 2020.
**与本文关联**：本文第3章讨论有限宽度带来的涨落，该文献证明了神经网络平均场极限的中心极限定理，为有限宽度涨落的统计性质提供了数学支撑，对应本文中N^{-1/4}的涨落缩放规律。

50. **引用序号**：50
**发表信息**：Phan-Minh Nguyen, Huy Tuan Pham. *A rigorous framework for the mean field limit of multilayer neural networks*. arXiv preprint arXiv:2001.11443, 2020.
**与本文关联**：本文讨论深层网络特征学习的平均场理论，该文献为多层神经网络的平均场极限建立了严格数学框架，是深度网络特征学习区间的重要理论进展。

51. **引用序号**：51
**发表信息**：Lenaic Chizat, Edouard Oyallon, Francis Bach. *On lazy training in differentiable programming*. Advances in Neural Information Processing Systems (NeurIPS), 2019: 2937–2947.
**与本文关联**：本文第4章核心理论依据，该文献正式提出“懒训练（lazy training）”概念，通过缩放初始化参数区分了懒训练与特征学习两种区间，是本文(h, α)相图划分的直接理论来源。

52. **引用序号**：52
**发表信息**：Joan Bruna, Stéphane Mallat. *Invariant scattering convolution networks*. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(8): 1872–1886, 2013.
**与本文关联**：本文第5章讨论深度学习通过学习不变性突破维数灾难，该文献提出的散射卷积网络是手工设计的微分同胚不变性网络，为“不变性是视觉可学习性核心”的假说提供了原型参考。

53. **引用序号**：53
**发表信息**：Stéphane Mallat. *Understanding deep convolutional networks*. Philosophical Transactions of the Royal Society A, 374(2065): 20150203, 2016.
**与本文关联**：本文讨论卷积网络的不变性学习机制，该综述系统阐述了深度卷积网络的群不变性理论，是“微分同胚不变性破解维数灾难”假说的核心论述文献。

54. **引用序号**：54
**发表信息**：Ravid Shwartz-Ziv, Naftali Tishby. *Opening the black box of deep neural networks via information*. arXiv preprint arXiv:1703.00810, 2017.
**与本文关联**：本文讨论表征学习的量化观测方法，该文献提出用信息瓶颈理论解释深度学习，用互信息表征网络层的信息变化，是本文提及的“互信息方法表征不变性学习”的相关工作。

55. **引用序号**：55
**发表信息**：Andrew M Saxe et al. *On the information bottleneck theory of deep learning*. Journal of Statistical Mechanics: Theory and Experiment, 2019(12): 124020, 2019.
**与本文关联**：本文指出互信息方法在确定性网络中的局限性，该文献对信息瓶颈理论在深度学习中的适用性提出了质疑，支撑了本文“互信息方法存在问题”的论断。

56. **引用序号**：56
**发表信息**：Alessio Ansuini, Alessandro Laio, Jakob H Macke, Davide Zoccolan. *Intrinsic dimension of data representations in deep neural networks*. Advances in Neural Information Processing Systems (NeurIPS), 2019: 6111–6122.
**与本文关联**：本文提及用内在维度表征神经网络的表征压缩，该文献系统测量了深度网络各层表征的内在维度，是相关实证研究的代表性工作。

57. **引用序号**：57
**发表信息**：Stefano Recanatesi et al. *Dimensionality compression and expansion in deep neural networks*. arXiv preprint arXiv:1906.00443, 2019.
**与本文关联**：本文讨论神经网络表征的维度变化，该文献分析了深度网络中维度压缩与扩张的现象，为理解特征学习中的维度变换提供了实证参考。

58. **引用序号**：58
**发表信息**：Mario Geiger, Stefano Spigler, Arthur Jacot, Matthieu Wyart. *Disentangling feature and lazy training in deep neural networks*. Journal of Statistical Mechanics: Theory and Experiment, 2020(11): 113301, 2020.
**与本文关联**：本文作者团队的核心前期工作，系统区分了深度网络的特征学习与懒训练两种区间，给出了相图划分的定量标准与实证结果，是本文第4章最核心的直接研究基础。

59. **引用序号**：59
**发表信息**：Yann LeCun, Corinna Cortes. MNIST handwritten digit database, 2010.
**与本文关联**：本文实证研究使用的核心数据集之一（MNIST手写数字数据集），该文献是MNIST数据集的官方来源，为本文的分类实验提供数据基础。

60. **引用序号**：60
**发表信息**：Alex Krizhevsky. Learning Multiple Layers of Features from Tiny Images. Technical Report, 2009.
**与本文关联**：本文实证研究使用的核心数据集之二（CIFAR-10图像数据集），该技术报告是CIFAR-10数据集的原始发布文献，为本文的图像分类实验提供数据支撑。

61. **引用序号**：61
**发表信息**：S. Spigler, M. Geiger, S. d’Ascoli, L. Sagun, G. Biroli, M. Wyart. *A jamming transition from under- to over-parametrization affects generalization in deep learning*. Journal of Physics A: Mathematical and Theoretical, 52(47): 474001, 2019.
**与本文关联**：本文作者团队的前期核心工作，首次发现jamming转变处泛化误差出现峰值（双下降现象），将jamming相变与泛化性能直接关联，是本文第2、3章的核心研究基础。

62. **引用序号**：62
**发表信息**：Mikhail Belkin, Daniel Hsu, Siyuan Ma, Soumik Mandal. *Reconciling modern machine-learning practice and the classical bias–variance trade-off*. Proceedings of the National Academy of Sciences, 116(32): 15849–15854, 2019.
**与本文关联**：本文第3章讨论的“双下降”现象的标志性论文，该文献正式提出双下降概念，调和了现代机器学习实践与经典偏差-方差权衡的矛盾，是本文双下降讨论的核心背景文献。

63. **引用序号**：63
**发表信息**：Mario Geiger et al. *Scaling description of generalization with number of parameters in deep learning*. Journal of Statistical Mechanics: Theory and Experiment, 2020(2): 023401, 2020.
**与本文关联**：本文作者团队的核心工作，建立了过参数化区间下泛化误差随参数数量缩放的定量理论，解释了双下降的涨落起源，是本文第3章最核心的理论与实证依据。

64. **引用序号**：64
**发表信息**：Jaehoon Lee et al. *Finite versus infinite neural networks: An empirical study*. arXiv preprint arXiv:2007.15801, 2020.
**与本文关联**：本文关于有限宽与无限宽网络对比、集成平均消除双下降的结论的第三方验证，该谷歌团队的研究独立验证了相关现象，支撑了本文结论的鲁棒性。

65. **引用序号**：65
**发表信息**：Corey S. O’Hern, Leonardo E. Silbert, Andrea J. Liu, Sidney R. Nagel. *Jamming at zero temperature and zero applied stress: The epitome of disorder*. Physical Review E, 68(1): 011306–011324, 2003.
**与本文关联**：本文jamming转变类比的物理基础文献，该文献是零温零应力jamming转变的经典研究，定义了jamming相变的核心性质，是本文物理类比的核心参考。

66. **引用序号**：66
**发表信息**：M. Wyart. *On the rigidity of amorphous solids*. Annalen der Physik, 30(3): 1–113, 2005.
**与本文关联**：本文通讯作者的前期经典工作，系统研究了无定形固体的刚性与jamming转变的振动性质，为本文分析损失景观海森谱、等静压/次静压性质提供了物理理论工具。

67. **引用序号**：67
**发表信息**：Andrea J Liu, Sidney R Nagel, W Saarloos, Matthieu Wyart. The Jamming Scenario - An Introduction and Outlook. OUP Oxford, 2010.
**与本文关联**：本文jamming转变理论的背景综述著作，系统介绍了jamming场景的核心概念与研究框架，为本文的jamming类比提供了完整的物理背景支撑。

68. **引用序号**：68
**发表信息**：Matthieu Wyart, Leonardo E Silbert, Sidney R Nagel, Thomas A Witten. *Effects of compression on the vibrational modes of marginally jammed solids*. Physical Review E, 72(5): 051306, 2005.
**与本文关联**：本文jamming转变附近振动模式（对应损失景观海森谱）分析的物理依据，该文献研究了临界jamming固体的振动模随压缩的变化规律，对应本文损失景观曲率的相变行为分析。

69. **引用序号**：69
**发表信息**：Eric DeGiuli et al. *Effects of coordination and pressure on sound attenuation, boson peak and elasticity in amorphous solids*. Soft Matter, 10(30): 5628–5644, 2014.
**与本文关联**：本文jamming转变动力学性质的物理参考，该文献研究了无定形固体的弹性、玻色峰等性质与配位数、压强的关系，为类比损失景观的动力学响应提供了物理基础。

70. **引用序号**：70
**发表信息**：Silvio Franz, Giorgio Parisi, Pierfrancesco Urbani, Francesco Zamponi. *Universal spectrum of normal modes in low-temperature glasses*. Proceedings of the National Academy of Sciences, 112(47): 14539–14544, 2015.
**与本文关联**：本文玻璃态/ jamming系统振动谱普适性的参考，该文献发现了低温玻璃简正模谱的普适性，支撑了本文中jamming相变海森谱普适类的讨论。

71. **引用序号**：71
**发表信息**：Carolina Brito, Harukuni Ikeda, Pierfrancesco Urbani, Matthieu Wyart, Francesco Zamponi. *Universality of jamming of nonspherical particles*. Proceedings of the National Academy of Sciences, 115(46): 11736–11741, 2018.
**与本文关联**：本文核心结论“深度网络jamming属于椭球普适类”的物理依据，该文献证明了非球形粒子jamming的普适性，对应次静压jamming的谱特征，是本文第2章普适类讨论的核心参考。

72. **引用序号**：72
**发表信息**：Mitch Mailman, Carl F. Schreck, Corey S. O’Hern, Bulbul Chakraborty. *Jamming in systems composed of frictionless ellipse-shaped particles*. Physical Review Letters, 102(25): 255501, 2009.
**与本文关联**：本文椭球jamming的模拟参考，该文献研究了无摩擦椭圆粒子的jamming转变，验证了非球形粒子的次静压jamming性质，为本文的普适类对比提供了依据。

73. **引用序号**：73
**发表信息**：Z. Zeravcic, N. Xu, A.J. Liu, S.R. Nagel, W. van Saarloos. *Excitations of ellipsoid packings near jamming*. Europhysics Letters, 87(2): 26001, 2009.
**与本文关联**：本文椭球jamming激发性质的参考，该文献研究了椭球堆积在jamming附近的激发模式，验证了零模、带隙等次静压jamming的特征，对应本文损失景观的海森谱性质。

74. **引用序号**：74
**发表信息**：Matthieu Wyart. *Marginal stability constrains force and pair distributions at random close packing*. Physical Review Letters, 109(12): 125502, 2012.
**与本文关联**：本文jamming转变边际稳定性理论的参考，该文献用边际稳定性约束解释了无规密堆积的力分布与对分布，支撑了jamming相变的临界性质理论。

75. **引用序号**：75
**发表信息**：Edan Lerner, Gustavo During, Matthieu Wyart. *Low-energy non-linear excitations in sphere packings*. Soft Matter, 9: 8252–8263, 2013.
**与本文关联**：本文jamming系统低能激发性质的参考，该文献研究了球堆积的低能非线性激发，对应损失景观中的平坦方向与软模，为类比分析提供了物理依据。

76. **引用序号**：76
**发表信息**：Patrick Charbonneau et al. *Fractal free energy landscapes in structural glasses*. Nature Communications, 5: 3725, 2014.
**与本文关联**：本文玻璃态能量景观分形性质的参考，该文献发现了结构玻璃自由能景观的分形结构，为理解高维损失景观的复杂结构提供了类比参考。

77. **引用序号**：77
**发表信息**：Patrick Charbonneau et al. *Exact theory of dense amorphous hard spheres in high dimension. III. The full replica symmetry breaking solution*. Journal of Statistical Mechanics: Theory and Experiment, 2014(10): 10009, 2014.
**与本文关联**：本文高维硬球玻璃态的精确理论参考，该系列工作建立了高维密堆积硬球的复制对称破缺精确理论，为高维系统jamming性质提供了严格理论支撑。

78. **引用序号**：78
**发表信息**：Edan Lerner, Gustavo Düring, Matthieu Wyart. *A unified framework for non-Brownian suspension flows and soft amorphous solids*. Proceedings of the National Academy of Sciences, 109(13): 4798–4803, 2012.
**与本文关联**：本文jamming系统流变学性质的参考，该文献建立了非布朗悬浮流与软无定形固体的统一框架，为类比训练动力学的流变行为提供了物理基础。

79. **引用序号**：79
**发表信息**：E. DeGiuli, G. Düring, E. Lerner, M. Wyart. *Unified theory of inertial granular flows and non-Brownian suspensions*. Physical Review E, 91(6): 062206, 2015.
**与本文关联**：本文颗粒流与悬浮流统一理论的参考，进一步拓展了jamming系统的动力学理论，为类比不同训练速率下的网络动力学提供了物理视角。

80. **引用序号**：80
**发表信息**：Florent Krzakala, Jorge Kurchan. *Landscape analysis of constraint satisfaction problems*. Physical Review E, 76(2): 021122, 2007.
**与本文关联**：本文约束满足问题景观分析的参考，该文献分析了离散约束满足问题的能量景观，为本文连续约束满足（jamming）的讨论提供了对比参考。

81. **引用序号**：81
**发表信息**：Silvio Franz, Giorgio Parisi. *The simplest model of jamming*. Journal of Physics A: Mathematical and Theoretical, 49(14): 145001, 2016.
**与本文关联**：本文感知机jamming模型的参考，该文献将感知机模型作为最简单的jamming系统进行分析，是从简单模型到深度网络jamming的过渡理论基础。

82. **引用序号**：82
**发表信息**：Silvio Franz, Giorgio Parisi, Maxime Sevelev, Pierfrancesco Urbani, Francesco Zamponi. *Universality of the SAT-UNSAT (jamming) threshold in non-convex continuous constraint satisfaction problems*. SciPost Physics, 2(3): 019, 2017.
**与本文关联**：本文连续约束满足问题jamming阈值普适性的理论参考，该文献证明了非凸连续约束满足问题中可满足-不可满足转变的普适性，支撑了深度网络jamming相变的普适性讨论。

83. **引用序号**：83
**发表信息**：Silvio Franz, Sungmin Hwang, Pierfrancesco Urbani. *Jamming in multilayer supervised learning models*. Physical Review Letters, 123(16): 160602, 2019.
**与本文关联**：本文多层监督学习模型jamming转变的理论参考，该文献从理论上分析了多层学习模型的jamming相变，与本文的深度网络jamming研究直接呼应。

84. **引用序号**：84
**发表信息**：Silvio Franz, Antonio Sclocchi, Pierfrancesco Urbani. *Critical jammed phase of the linear perceptron*. Physical Review Letters, 123(11): 115702, 2019.
**与本文关联**：本文线性感知机临界jamming相的参考，该文献研究了线性hinge损失感知机的临界jamming相性质，为本文深度网络hinge损失jamming的讨论提供了简单模型对照。

85. **引用序号**：85
**发表信息**：Alexei V. Tkachenko, Thomas A. Witten. *Stress propagation through frictionless granular material*. Physical Review E, 60(1): 687–696, 1999.
**与本文关联**：本文jamming几何论证的物理基础，该文献研究了无摩擦颗粒材料中的应力传播，提出的约束流形维度分析是本文第2章几何论证的思想来源。

86. **引用序号**：86
**发表信息**：Matthieu Wyart. *Scaling of phononic transport with connectivity in amorphous solids*. Europhysics Letters, 89(6): 64001, 2010.
**与本文关联**：本文jamming系统声输运与配位数缩放关系的参考，该文献建立了无定形固体中声子输运随配位数的缩放规律，对应损失景观中曲率与约束数的缩放关系。

87. **引用序号**：87
**发表信息**：Arthur Jacot, Franck Gabriel, Clément Hongler. *The asymptotic spectrum of the Hessian of DNN throughout training*. arXiv preprint arXiv:1910.02875, 2019.
**与本文关联**：本文讨论训练过程中海森矩阵的渐近谱，该文献分析了无限宽网络训练全程的海森谱渐近性质，为本文jamming附近海森谱的讨论提供了理论对照。

88. **引用序号**：88
**发表信息**：Brady Neal et al. *A modern take on the bias-variance tradeoff in neural networks*. arXiv preprint arXiv:1810.08591, 2018.
**与本文关联**：本文第3章偏差-方差分解的参考，该文献从现代视角重新解读了神经网络的偏差-方差权衡，为过参数化下泛化改善的方差解释提供了框架参考。

89. **引用序号**：89
**发表信息**：Boris Hanin, Mihai Nica. *Finite depth and width corrections to the neural tangent kernel*. arXiv preprint arXiv:1909.05989, 2019.
**与本文关联**：本文NTK有限宽度修正的理论参考，该文献严格推导了有限深度、有限宽度对NTK的修正，支撑了本文中NTK涨落随h^{-1/2}缩放的结论。

90. **引用序号**：90
**发表信息**：Ethan Dyer, Guy Gur-Ari. *Asymptotics of wide networks from feynman diagrams*. arXiv preprint arXiv:1909.11304, 2019.
**与本文关联**：本文宽网络渐近性质的理论参考，该文献用费曼图方法推导了宽网络的渐近行为，为NTK的有限宽度修正提供了另一种理论推导路径。

91. **引用序号**：91
**发表信息**：Zhengdao Chen, Grant Rotskoff, Joan Bruna, Eric Vanden-Eijnden. *A dynamical central limit theorem for shallow neural networks*. Advances in Neural Information Processing Systems (NeurIPS) 33, 2020.
**与本文关联**：本文特征学习区间有限宽度涨落的理论依据，该文献证明了浅层神经网络训练动力学的中心极限定理，严格支撑了特征学习下涨落随N^{-1/4}缩放的结论。

92. **引用序号**：92
**发表信息**：Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, Andrea Montanari. *Linearized two-layers neural networks in high dimension*. arXiv preprint arXiv:1904.12191, 2019.
**与本文关联**：本文高维线性化两层网络的理论参考，该文献研究了高维下两层网络的线性化模型，为双下降现象的高维理论分析提供了模型基础。

93. **引用序号**：93
**发表信息**：Stéphane D’Ascoli, Maria Refinetti, Giulio Biroli, Florent Krzakala. *Double trouble in double descent: bias and variance(s) in the lazy Regime*. Proceedings of the 37th International Conference on Machine Learning (ICML), PMLR 119: 2280–2290, 2020.
**与本文关联**：本文懒训练区间下双下降的偏差-方差分解参考，该文献在懒训练框架下分解了双下降的偏差与方差贡献，支撑了本文“双下降源于有限宽度涨落”的解释。

94. **引用序号**：94
**发表信息**：Arthur Jacot et al. *Implicit regularization of random feature models*. Proceedings of the 37th International Conference on Machine Learning (ICML), PMLR 119: 4631–4640, 2020.
**与本文关联**：本文随机特征模型隐式正则化的参考，该文献分析了随机特征模型的隐式正则化效应，为核方法/懒训练区间的泛化性质提供了理论解释。

95. **引用序号**：95
**发表信息**：Sanjeev Arora et al. *Harnessing the Power of Infinitely Wide Deep Nets on Small-data Tasks*. Proceedings of the International Conference on Learning Representations (ICLR), 2019.
**与本文关联**：本文NTK在小数据任务上性能的实证参考，该文献验证了无限宽深度网络在小数据任务上的优异性能，支撑了懒训练区间的实用价值讨论。

96. **引用序号**：96
**发表信息**：Vaishaal Shankar et al. *Neural kernels without tangents*. Proceedings of the 37th International Conference on Machine Learning (ICML), PMLR 119: 8614–8623, 2020.
**与本文关联**：本文神经核方法的相关研究参考，该文献提出了不依赖正切核的神经核方法，丰富了核视角下深度学习的研究路径。

97. **引用序号**：97
**发表信息**：Blake Woodworth et al. *Kernel and rich regimes in overparametrized models*. Proceedings of the Conference on Learning Theory (COLT), PMLR: 3635–3673, 2020.
**与本文关联**：本文核区间与丰富（特征学习）区间对比的理论参考，该文献系统对比了过参数化模型中的核区间与丰富区间，与本文的懒训练/特征学习划分直接呼应。

98. **引用序号**：98
**发表信息**：Lénaïc Chizat, Francis Bach. *Implicit bias of gradient descent for wide two-layer neural networks trained with the logistic loss*. Proceedings of the Conference on Learning Theory (COLT), PMLR: 1305–1338, 2020.
**与本文关联**：本文第5章特征学习隐式偏见的理论参考，该文献证明了逻辑损失下宽两层网络梯度下降的隐式偏见是最大间隔分类器，为特征学习的不变性学习机制提供了理论基础。

99. **引用序号**：99
**发表信息**：Gilad Yehudai, Ohad Shamir. *On the power and limitations of random features for understanding neural networks*. Advances in Neural Information Processing Systems (NeurIPS), 2019: 6598–6608.
**与本文关联**：本文随机特征/核方法局限性的参考，该文献分析了随机特征模型在表征神经网络能力上的局限，支撑了特征学习区间优于核方法的相关讨论。

100. **引用序号**：100
**发表信息**：Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, Andrea Montanari. *Limitations of lazy training of two-layers neural network*. Advances in Neural Information Processing Systems (NeurIPS), 2019: 9111–9121.
**与本文关联**：本文懒训练局限性的理论参考，该文献严格证明了两层网络懒训练的能力局限，从理论上解释了为何特征学习区间在复杂任务上更优。

101. **引用序号**：101
**发表信息**：Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, Andrea Montanari. *When do neural networks outperform kernel methods?*. Advances in Neural Information Processing Systems (NeurIPS) 33, 2020.
**与本文关联**：本文神经网络与核方法性能对比的核心参考，该文献系统分析了神经网络超越核方法的场景与条件，为本文两种训练区间的性能差异讨论提供了理论依据。

102. **引用序号**：102
**发表信息**：Stefano Spigler, Mario Geiger, Matthieu Wyart. *Asymptotic learning curves of kernel methods: Empirical data versus teacher–student paradigm*. Journal of Statistical Mechanics: Theory and Experiment, 2020(12): 124001, 2020.
**与本文关联**：本文核方法学习曲线的实证与理论参考，该文献系统研究了核方法的渐近学习曲线，对比了实证数据与师生模型，为本文分析核方法的维数灾难问题提供了定量基础。

103. **引用序号**：103
**发表信息**：Jonas Paccolat, Matthieu Wyart, Stefano Spigler. *How isotropic kernels perform on simple invariants*. Machine Learning: Science and Technology, 2020.
**与本文关联**：本文第5章简单不变性模型的核方法性能参考，该文献分析了各向同性核在简单不变性数据上的表现，为对比特征学习的优势提供了基准。

104. **引用序号**：104
**发表信息**：Sebastian Goldt, Marc Mézard, Florent Krzakala, Lenka Zdeborová. *Modeling the influence of data structure on learning in neural networks: The hidden manifold model*. Physical Review X, 10(4): 041044, 2020.
**与本文关联**：本文数据结构对学习影响的模型参考，该文献提出的隐藏流形模型刻画了低维流形数据的学习性质，为本文讨论数据内在维度与可学习性提供了模型框架。

105. **引用序号**：105
**发表信息**：Greg Ongie, Rebecca Willett, Daniel Soudry, Nathan Srebro. *A function space view of bounded norm infinite width relu nets: the multivariate case*. Proceedings of the 8th International Conference on Learning Representations (ICLR), 2020.
**与本文关联**：本文无限宽ReLU网络函数空间视角的参考，该文献从函数空间角度刻画了有界范数无限宽ReLU网络的性质，补充了特征学习区间的函数空间刻画。

106. **引用序号**：106
**发表信息**：Jonas Paccolat, Leonardo Petrini, Mario Geiger, Kevin Tyloo, Matthieu Wyart. *Geometric compression of invariant manifolds in neural nets*. arXiv preprint arXiv:2007.11471, 2020.
**与本文关联**：本文第5章核心研究基础，作者团队提出了神经网络通过几何压缩不变流形学习不变性的机制，是本文“特征学习压缩无关维度”核心观点的直接来源。

107. **引用序号**：107
**发表信息**：Samet Oymak, Zalan Fabian, Mingchen Li, Mahdi Soltanolkotabi. *Generalization guarantees for neural networks via harnessing the low-rank structure of the jacobian*. arXiv preprint arXiv:1906.05392, 2019.
**与本文关联**：本文雅可比矩阵低秩结构与泛化关系的参考，该文献利用雅可比的低秩结构给出神经网络泛化保证，与本文中NTK谱对齐、特征学习改善核性质的讨论相呼应。

108. **引用序号**：108
**发表信息**：Dmitry Kopitkov, Vadim Indelman. *Neural spectrum alignment: Empirical study*. Proceedings of the 29th International Conference on Artificial Neural Networks (ICANN), 2020.
**与本文关联**：本文神经谱对齐现象的实证参考，该文献实证研究了训练过程中神经谱与标签的对齐现象，支撑了本文“NTK在训练中持续优化”的论述。

109. **引用序号**：109
**发表信息**：Blake Bordelon, Abdulkadir Canatar, Cengiz Pehlevan. *Spectrum dependent learning curves in kernel regression and wide neural networks*. Proceedings of the 37th International Conference on Machine Learning (ICML), PMLR 119: 1024–1034, 2020.
**与本文关联**：本文核回归学习曲线与谱关系的理论参考，该文献建立了核回归学习曲线与核谱的依赖关系，为本文中核PCA对齐改善泛化的机制提供了理论解释。

110. **引用序号**：110
**发表信息**：Bernhard Scholkopf, Alexander Smola, Klaus-Robert Müller. *Kernel principal component analysis*. Advances in Kernel Methods - Support Vector Learning, MIT Press: 327–352, 1999.
**与本文关联**：本文核PCA方法的原始文献，该文献提出了核主成分分析方法，是本文第5章用核PCA分析NTK不变性学习的方法学基础。

111. **引用序号**：111
**发表信息**：Eric Degiuli, E. Lerner, M. Wyart. *Theory of the jamming transition at finite temperature*. The Journal of Chemical Physics, 142(16): 164503, 2015.
**与本文关联**：本文有限温度jamming转变的物理参考，该文献建立了有限温度下的jamming转变理论，为本文类比SGD噪声（温度）对jamming奇异性的正则化作用提供了物理依据。