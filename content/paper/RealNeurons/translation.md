[第1页，第1段]
真实神经元网络的扩展平均场理论

[第1页，第2段]
Luca Di Carlo, Francesco Mignacco, Christopher W. Lynn, and William Bialek

[第1页，第3段]
1普林斯顿大学物理系约瑟夫·亨利实验室与刘易斯-西格勒研究所，美国新泽西州普林斯顿市，邮编08544

[第1页，第4段]
2纽约城市大学研究生中心理论科学倡议项目，美国纽约州纽约市第五大道365号，邮编10016

[第1页，第5段]
3耶鲁大学物理系、定量生物学研究所与吴蔡研究所，美国康涅狄格州纽黑文市，邮编06510

[第1页，第6段]
（2025年9月10日收到；2026年5月8日接受；2026年6月30日发表）

[第1页，第7段]
如果一个具有大量自由度的系统的行为能够被少数集体变量所刻画，那么很可能存在一个底层的平均场理论。我们表明，这一思想的简单版本无法描述真实神经元网络中的活动模式。一个与集体变量分布相匹配的扩展平均场理论至少是自洽的，尽管它显示出这些网络似乎处于临界点附近的迹象，这与其他观测结果一致。这些结果为分析日益增大的神经元数量所产生的新兴数据提供了一条路径。

[第1页，第8段]
DOI: 10.1103/nr71-phqw

[第1页，第9段]
大脑中的神经元产生离散的动作电位或脉冲；在短时间窗口内，响应本质上是二值的，因为每个细胞要么产生一个脉冲，要么保持静默。因此，神经群体的瞬时状态等价于一个伊辛模型（Ising model）的构型，我们希望了解这些自旋构型所服从的分布。利用统计物理学的思想来处理这一问题有着悠久的历史[1]；里程碑式的工作包括霍普菲尔德模型（Hopfield model）[2–4]和玻尔兹曼机（Boltzmann machine）[5]，尽管它们在生物学上的真实性有限。这两个模型都由伊辛自旋之间的成对相互作用来描述，学习规则通过调整这些相互作用来达到期望的行为。

[第1页，第10段]
从实验数据到成对伊辛模型有一条直接的路径[1,6]。具体而言，我们将每个神经元的状态记为$ s_n $，当细胞活跃时$ s_n = +1 $，当细胞静默时$ s_n = -1 $；网络的状态为$ \mathbf{s} \equiv \{s_1, s_2, \ldots, s_N\} $。我们寻找概率分布$ P(\mathbf{s}) $，并要求它与观测到的均值和关联相匹配，

[第1页，第11段]
$ 
\langle s_n \rangle_P = \langle s_n \rangle_{\text{exp}}, \quad \langle s_n s_m \rangle_P = \langle s_n s_m \rangle_{\text{exp}}, \tag{1}
 $

[第1页，第12段]
其中$ \langle \cdot \cdot \cdot \rangle_P $表示对分布$ P $的平均，$ \langle \cdot \cdot \cdot \rangle_{\text{exp}} $表示对数据的平均。无穷多个分布满足这些约束，但有一个是特殊的，因为它生成的状态尽可能随机，因此除了匹配式(1)中的期望值所必需的结构外，不引入任何额外的知识或结构；这就是最大熵分布[7,8]

[第1页，第13段]
$ 
P_{\text{pairs}}(\mathbf{s}) = \frac{1}{Z_{\text{pairs}}} \exp[-E_{\text{pairs}}(\mathbf{s})], \tag{2}
 $

[第1页，第14段]
$ 
E_{\text{pairs}}(\mathbf{s}) = -\sum_n h_n s_n - \frac{1}{2} \sum_{n,m=1}^{N} s_n J_{nm} s_m. \tag{3}
 $

[第1页，第15段]
我们认识到这是一个特定伊辛自旋玻璃的玻尔兹曼分布，其中场$ \{h_n\} $和耦合$ \{J_{nm}\} $通过式(1)由数据确定；一旦我们求解这些方程，所有进一步的预测都是无参数的。这些定量预测在若干不同的系统中取得了非常大的成功[1]。

[第1页，第16段]
成对最大熵模型从数据中取$ \sim N^2 $个期望值。但当前的实验方法允许$ N $急剧增加，而实验持续时间$ T $却不会成比例增加；最终，测量到的成对关联矩阵不再满秩，受限于$ T $而非$ N $。当$ N \to \infty $而$ T $固定时，我们有足够的数据来测量$ M \propto N $个期望值，然后构建与这些测量一致的最大熵模型。作为一个例子，在具有局域相互作用的伊辛模型中，我们通过求解与近邻关联一致的最大熵模型来恢复正确的玻尔兹曼分布，即使没有平移不变性，这些约束也有$ \mathcal{O}(N) $个；从局域关联进行重构在鸟群中同样有效[9,10]。在没有对称性或局域性指导的情况下，我们如何选择$ \mathcal{O}(N) $个约束？关于神经元群体活动的文献提供了若干直觉。

[第1页，第17段]
群体活动——有人提出，神经元网络中的集体效应可以通过追踪求和活动来刻画[11–13]，

[第1页，第18段]
$ 
\phi = \sum_{n=1}^{N} s_n. \tag{4}
 $

[第2页，第1段]
与$\phi$的均值和方差一致的最大熵模型具有能量函数

[第2页，第2段]
$$E_{\text{pop}}(s) = -h\phi - \frac{\lambda}{2N}\phi^2,$$  \hspace{1cm} (5)

[第2页，第3段]
我们将其识别为平均场铁磁体[14–16]。回想一下，在求解这个模型时，我们将其（精确地）重写为自旋与辅助场相互作用。这与以下直觉相联系：网络的高维动力学由少数“潜在场”控制，细胞对这些场独立响应[17,18]；在这里，潜在场是涌现的而非外部强加的。在大$N$极限下，场的涨落被抑制，我们称之为朴素平均场近似。

[第2页，第4段]
均值与投影——关注总和活动会丢失神经元的身份信息。另一种方法是寻求一个模型，使其匹配每个单独细胞的平均活动，但仅通过沿一个或少数几个投影方向来捕捉集体效应

[第2页，第5段]
$$\phi_{\alpha} = \frac{1}{\sqrt{N}}\sum_{n=1}^{N}W_{\alpha n}s_n, \quad \alpha = 1, \ldots, K,$$  \hspace{1cm} (6)

[第2页，第6段]
其中$W \in \mathbb{R}^{K \times N}$。匹配所有平均活动$\langle s_n \rangle$和协方差矩阵$\langle \phi_{\alpha} \phi_{\beta} \rangle$的最大熵模型同样是一个玻尔兹曼分布[19–21]。这与以下直觉相联系：网络的高维动力学由低维流形主导[22–24]。求解该模型同样引入了辅助场，每个投影$\phi_{\alpha}$对应一个共轭场，因此这是一个（略微）广义的平均场模型[19]。对于$K \ll N$，在大$N$极限下这些场的涨落被抑制，我们再次称之为朴素平均场。如果$K \propto N$，则应该存在一个更复杂的平均场理论，类似于接近饱和的Hopfield网络[25]。

[第2页，第7段]
投影的分布——强调沿特定投影方向活动的方差可能过于局限。另一种方法是匹配沿神经活动高维空间中有限方向集的活动分布；为简单起见，我们这里只考虑一个投影$\phi$。此时最大熵模型是一个玻尔兹曼分布，其能量为

[第2页，第8段]
$$E_{\text{dist}}(s) = -\sum_{n=1}^{N}h_n s_n + NU(\phi).$$  \hspace{1cm} (7)

[第2页，第9段]
按照惯例，场$\{h_n\}$被调整以匹配每个神经元测量到的平均活动，势$U(\phi)$被调整以匹配观测到的分布$P_{\text{exp}}(\phi)$；因子$N$使势保持为一阶量。这等价于让一个具有任意分布的单一潜在场作用于所有神经元。它也与密集联想记忆模型或“现代Hopfield”网络[26]相联系。

[第2页，第10段]
我们的主要成果是为这类模型构建了广义平均场理论，并证明了真实网络处于该近似有效的区域。相比之下，我们将看到更简单的平均场理论会失效。

[第2页，第11段]
计算群体活动模型[式(5)]的配分函数是一个标准练习[14–16]。配分函数可以精确地重写为

[第2页，第12段]
$$Z_{\text{pop}}(h, \lambda) = \sqrt{\frac{N}{2\pi\lambda}}2^N \int d\psi e^{-Nf(\psi)},$$  \hspace{1cm} (8)

[第2页，第13段]
$$f(\psi) = \frac{1}{2\lambda}\psi^2 - \ln \cosh(h + \psi).$$  \hspace{1cm} (9)

[第2页，第14段]
在大$N$极限下，式(8)中的积分应由$\psi = \psi_*$主导，该值使局域自由能$f(\psi)$最小化，这导致朴素平均场近似

[第2页，第15段]
$$\ln Z(h, \lambda) = -Nf(\psi_*) + N\ln 2 - \frac{1}{2}\ln[2\pi\lambda f''(\psi_*)] + \ldots,$$  \hspace{1cm} (10)

[第2页，第16段]
其中$\ldots$为$\sim 1/N$的项。在此近似下

[第2页，第17段]
$$\langle \phi \rangle \equiv \mu = \tanh(h + \lambda\mu) + \mathcal{O}(N^{-1}),$$  \hspace{1cm} (11)

[第2页，第18段]
$$\frac{1}{N}\langle (\delta\phi)^2 \rangle \equiv \chi = \frac{1 - \mu^2}{1 - \lambda(1 - \mu^2)} + \mathcal{O}(N^{-1}).$$  \hspace{1cm} (12)

[第2页，第19段]
这些方程意味着在固定均值$\mu$下存在最大方差$\chi$，

[第2页，第20段]
$$\chi_{\text{max}}(\mu) = \frac{\mu(1 - \mu^2)}{\mu - \tanh(\mu)(1 - \mu^2)}.$$  \hspace{1cm} (13)

[第2页，第21段]
在图1中，我们展示了来自多个系统数据的$\chi$对$\mu$的关系，我们看到式(13)的界限被一致地违反。这些结果对潜在非平稳性的鲁棒性在末尾材料中进行了明确评估。

[第2页，第22段]
图1的结论是，真实神经元与朴素平均场理论不一致。但最大熵问题会发生什么？我们仍然可以找到式(5)中$h$和$\lambda$的值，使得预测的$\mu$和$\chi$与测量值一致，但这必须非常小心地进行[20,21]。我们可以利用式(8)中$Z_{\text{pop}}$的精确积分表示，数值构造一条轨迹$h_*(\lambda)$，沿此轨迹$\mu = \mu_{\text{exp}}$（图2，插图）。该轨迹始于$h_*(\lambda = 0) = \tanh(\mu_{\text{exp}})$，随着$\lambda$增大，$h_*$向$h_* = 0$移动。轨迹停滞，$dh_*/d\lambda$在临界$\lambda$处几乎为零，此时磁化率$\chi$迅速上升；在图1的例子中，$\chi_{\text{exp}}$与此陡峭上升相交，因此$\lambda$由数据非常精确地确定。

[第3页，第1段]
在找到与群体活动 $\phi$ 的均值和方差相匹配的 $h$ 和 $\lambda$ 后，我们可以直接查看式 (9) 中的局部自由能 $f(\psi)$；结果如图 2 所示，针对小鼠海马体 [28,29] 中的神经元群体。存在两个局部极小值，几乎简并。这里分析的海马神经元群体生活在一个平面内，因此我们可以通过扩大圆的半径来改变 $N$ [31,32]。随着 $N$ 增加，局部自由能的两个极小值变得更加近乎简并，并且局部自由能差按 $1/N$ 缩放 [20,21]。这是一阶相变的定义性特征。我们强调，这完全由实验观测 $\mu_{\text{exp}}$ 和 $\chi_{\text{exp}}$ 驱动。

[第3页，第2段]
数据驱动这些最小结构模型趋向一阶相变这一事实是引人深思的。这一结果解释了朴素平均场近似的失败，并暗示了一个在宏观有序活动模式之间平衡的网络。不幸的是，$f(\psi)$ 中两个局部极小值的存在预测总和活动的分布将是双峰的，而这在定性上是错误的。

[第3页，第3段]
这些在匹配群体活动均值和方差方面的问题，在匹配单个神经元平均活动和任意投影方差的模型中依然存在，尽管细节取决于我们对投影的选择。如果我们选择一个由独立高斯随机数给出的系数 $W_n$ 的单一投影，那么朴素平均场近似有效，但所得模型的熵仅略低于完全独立神经元的熵，且当 $N \to \infty$ 时差距消失 [20,21]。

[第3页，第4段]
为了对投影系数的可能选择进行排序，考虑相关矩阵是有用的

[第3页，第5段]
$$\tilde{C}_{nm} \equiv \frac{\langle s_n s_m \rangle - \langle s_n \rangle \langle s_m \rangle}{[(1 - \langle s_n \rangle^2)(1 - \langle s_m \rangle^2)]^{1/2}}.$$  (14)

[第3页，第6段]
该矩阵具有特征向量 $\tilde{W}$ 和特征值 $\rho$。如果我们选择系数为

[第3页，第7段]
$$W_{an} = \frac{1}{\sqrt{1 - \langle s_n \rangle^2}} \tilde{W}_{an},$$  (15)

[第3页，第8段]
的投影，那么遵循导致式 (10) 的相同朴素平均场近似，得到熵 [19–21]，

[第3页，第9段]
$$S = S_0 - \frac{1}{2} \sum_{\alpha} [\rho_{\alpha} - 1 - \ln(\rho_{\alpha})],$$  (16)

[第3页，第10段]
其中 $S_0$ 是独立神经元的熵。因此，最具信息量的投影是与相关矩阵的最大或最小特征值相关的那些投影。但如果我们选择这些优化投影，我们又被带回简并局部极小值的问题 [20,21]。

[第3页，第11段]
为了驯服多重极小值，我们坚持同时匹配单个神经元的平均活动和沿投影的活动分布，从而得到式 (7)。

[第4页，第1段]
配分函数（见文末补充材料），

[第4页，第2段]
$ 
Z_{\text{dist}} = 2^N \int \frac{dz}{2\pi} \int d\varphi \exp[-Nf_{\text{dist}}(\varphi; z)], \tag{17}
 $

[第4页，第3段]
其中自由能为

[第4页，第4段]
$ 
f_{\text{dist}}(\varphi; z) = U(\varphi) + \frac{1}{N} \left[ iz\varphi - \sum_{n=1}^{N} \ln \cosh \left( h_n + iz \frac{W_n}{\sqrt{N}} \right) \right]. \tag{18}
 $

[第4页，第5段]
按照通常做法，我们寻找使$ f_{\text{dist}}(\varphi; z) $取极值的鞍点$ \varphi_{\text{sp}}, z_{\text{sp}}) $；我们得到

[第4页，第6段]
$ 
\varphi_{\text{sp}} = \frac{1}{\sqrt{N}} \sum_{n=1}^{N} W_n \tanh \left( h_n + iz_{\text{sp}} \frac{W_n}{\sqrt{N}} \right), \tag{19}
 $

[第4页，第7段]
$ 
z_{\text{sp}} = iNU'(\varphi_{\text{sp}}), \tag{20}
 $

[第4页，第8段]
并近似有$ \ln Z_{\text{dist}} \approx -Nf_{\text{dist}}(\varphi_{\text{sp}}; z_{\text{sp}}) $。注意$ E_{\text{dist}}(s) $在规范变换$ U(\varphi) \to U(\varphi) - \varphi U'(\varphi_{\text{sp}}) $和$ h_n \to h_n + \sqrt{N}U'(\varphi_{\text{sp}})W_n $下保持不变，因此我们可以令$ U'(\varphi_{\text{sp}}) = 0 $。这固定了$ z_{\text{sp}} = 0 $，并得到

[第4页，第9段]
$ 
\langle s_n \rangle = \frac{\partial Z_{\text{dist}}}{\partial h_n} = \tanh h_n, \tag{21}
 $

[第4页，第10段]
就好像神经元独立地响应外场

[第4页，第11段]
$ 
h_n = \tanh(\langle s_n \rangle_{\text{exp}}). \tag{22}
 $

[第4页，第12段]
沿投影方向的活动分布为

[第4页，第13段]
$ 
P(\varphi) = \frac{2^N}{Z_{\text{dist}}} \int \frac{dz}{2\pi} \exp[-Nf_{\text{dist}}(\varphi; z)]. \tag{23}
 $

[第4页，第14段]
鞍点近似为

[第4页，第15段]
$ 
P(\varphi) \propto \exp[-Nf_{\text{dist}}(\varphi; z_{\star}(\varphi))], \tag{24}
 $

[第4页，第16段]
其中$ z_{\star} $依赖于$ \varphi $，并且是以下方程的解

[第4页，第17段]
$ 
\sum_{n=1}^{N} \frac{W_n}{\sqrt{N}} \tanh \left[ h_n + i \frac{W_n}{\sqrt{N}} z_{\star}(\varphi) \right] = \varphi. \tag{25}
 $

[第4页，第18段]
给定权重$ \{W_n\} $和由式(22)得到的外场，我们数值求解式(25)以得到$ z_{\star}(\varphi) $。由式(24)，自由能$ f_{\text{dist}}[\varphi; z_{\star}(\varphi)] $可以直接从沿投影方向测得的活动估计；结合式(18)并求解$ U(\varphi) $，得到

[第4页，第19段]
$ 
NU(\varphi) = \ln P_{\text{exp}} - i\varphi z_{\star}(\varphi) + \sum_{n=1}^{N} \ln \cosh \left( h_n + iz_{\star}(\varphi) \frac{W_n}{\sqrt{N}} \right). \tag{26}
 $

[第4页，第20段]
我们将这一分析应用于小鼠海马体的实验，选择对应于相关矩阵最大特征值的投影（图3）。我们看到，势函数$ U(\varphi) $在大的$ |\varphi| $处显著偏离二次形式，这暗示了即使如上所述固定沿投影方向活动的方差会失败，该模型仍然可以“工作”的方式。

[第4页，第21段]
为了检验我们的广义平均场理论，我们使用来自式(7)的能量、来自图3(a)的势函数以及来自式(22)的外场进行了蒙特卡洛模拟。图3(b)表明我们正确地重现了沿投影方向的活动分布；插图表明我们也恢复了正确的平均活动。那些麻烦的局部极小值已被消除。

[第4页，第22段]
对于某些参数值，自由能的曲率在鞍点处消失，标志着二阶相变。发生这种情况的条件并不简单地是$ U''(\varphi_{\text{sp}}) = 0 $，因为自由能还包括熵的贡献（见文末补充材料）。该条件实际上是$ 1 + NU''(\varphi_{\text{sp}}) \Delta = 0 $，其中$ \Delta $是如果神经元相互独立时我们会得到的沿投影方向活动的方差，

[第4页，第23段]
$ 
\begin{align*}
\text{(a)} & \quad 0.00 \\
\text{(b)} & \quad 0.02 \\
\text{(c)} & \quad 0.04 \\
\text{(d)} & \quad 0.06 \\
\text{(e)} & \quad 0.08 \\
\text{(f)} & \quad 0.10 \\
\end{align*}
 $

[第4页，第24段]
图3. 来自式(7)的分布最大熵模型，针对小鼠海马体中$ N = 1416 $个神经元。投影对应于相关矩阵的最大特征值。(a) 势函数$ U(\varphi) $（红色实线）与二次函数（黑色虚线）和三次函数（黑色实线）的比较。(b) 模型（红色）、数据（灰色）和独立神经元（虚线）的活动分布$ P(\varphi) $。实验分布用$ N_b = 32 $个柱的直方图近似；阴影表示数据十分位数之间的标准差。插图：每个神经元的平均活动，模型与数据的比较。

[第5页，第1段]
图4. 图3模型中的临界性趋近。(a) 对于不同投影：随机（绿色）、随机正（橙色）以及相关矩阵的特征向量（灰色，如式(15)所示），$NU''(\varphi_{sp})$ 与 $\Delta$ 的散点图，较浅的颜色对应较大的 $\Delta S$。临界线 $1 + NU''(\varphi_{sp})\Delta = 0$ 以红色表示。(b) 当我们考察每个神经元具有相同平均活动但相关性较弱的网络时，$NU''(\varphi_{sp})$ 和 $-\Delta^{-1}$ 的轨迹，这些网络是通过对每个神经元独立地打乱一部分时间箱而生成的。

[第5页，第2段]
$ 
\Delta = \frac{1}{N} \sum_{n=1}^{N} W_n^2 [1 - \langle s_n \rangle^2].
 $

[第5页，第3段]
对于随机投影，$NU''(\varphi_{sp})$ 接近于零[20,21]，远离临界性[图4(a)]；对于随机正系数，$NU''(\varphi_{sp})$ 始终为负，但仍不接近 $-\Delta^{-1}$。当沿相关矩阵的特征向量进行投影时[式(15)]，我们看到模式趋向临界线，其中方差最大的主成分位于临界性的约8%范围内。

[第5页，第4段]
趋近临界性取决于相关性的强度。我们可以设想这样的系统：每个神经元的平均活动相同，但神经元对之间的相关性较弱，我们可以通过对每个神经元独立地打乱一部分时间箱来生成此类数据。对于每个打乱后的数据集，我们重复上述构造，发现 $NU''(\varphi_{sp})$ 和 $-\Delta^{-1}$ 逐渐分离[图4(b)]：合理的神经元群体比真实网络更远离临界性。这与近临界行为的其他特征[1]一致，包括这些相同数据在粗粒化下的标度行为[29]。

[第5页，第5段]
我们可以在平均场近似下计算式(7)中模型的熵（见文末材料），

[第5页，第6段]
$ 
S = S_0 + N[\langle U(\varphi) \rangle - U(\varphi_{sp})] - \frac{1}{2} \ln [1 + NU''(\varphi_{sp})\Delta],
 $

[第5页，第7段]
结果如图5所示，使用的是与图4相同的数据。仅沿一个投影匹配分布会导致熵减少约独立熵的5%。大约有200个投影各自提供的贡献超过每个神经元的独立熵。仅凭熵不足以评估模型的质量；一个好的模型应该捕捉超出其明确约束的可观测量的统计结构[1]。在这方面，该模型也是成功的（见文末材料）。

[第5页，第8段]
总之，为真实神经元网络中的活动模式构建一致的平均场理论被证明是出乎意料地困难。我们最终通过一个模型取得了成功，该模型匹配了单个神经元的平均活动以及沿一个投影的活动分布。但存在许多投影，沿这些投影约束分布会产生显著的熵减少。我们的方法对动力学不做假设，仅捕捉神经活动的稳态分布。一个重要的未来方向是将此框架扩展到约束整个轨迹的模型，这将不仅能够获得临界性的静态特征，还能获得动态特征[33]，例如相关时间的发散。因此，一个重要的未来方向是将此方法扩展到匹配多个投影的分布，从而提供一个描述具有 $\mathcal{O}(N)$ 个约束的 $N$ 个神经元网络的框架，并使得在更大的 $N$ 下分析数据成为可能。

[第5页，第9段]
致谢——我们感谢我们的实验同事MJ Berry II、CD Brody、JL Gauthier、O Marre和DW Tank。这项工作部分得到了美国国家科学基金会的支持，通过生物功能物理中心（资助号PHY–1734030）；以及人类前沿科学计划（F. M.）、J. S. McDonnell基金会（C. W. L.）、J. S. Guggenheim纪念基金会（W. B.）和Simons基金会（W. B.和F. M.）的资助。

[第6页，第1段]
数据可用性——支持本文研究结果的部分数据已公开可用 [34]。支持图1–4的CA1小鼠脑区钙成像记录未公开，因其归第三方所有，且使用条款禁止公开分发。这些数据可在合理请求下向作者获取。

[第6页，第2段]
[1] L. Meshulam and W. Bialek, Rev. Mod. Phys. 97, 045002 (2025).
[2] J. J. Hopfield, Proc. Natl. Acad. Sci. U.S.A. 79, 2554 (1982).
[3] J. J. Hopfield and D. W. Tank, Biol. Cybern. 52, 141 (1985).
[4] J. J. Hopfield and D. W. Tank, Science 233, 625 (1986).
[5] D. H. Ackley, G. E. Hinton, and T. J. Sejnowski, Cogn. Sci. 9, 147 (1985).
[6] E. Schneidman, M. J. Berry II, R. Segev, and W. Bialek, Nature (London) 440, 1007 (2006).
[7] E. T. Jaynes, Phys. Rev. 106, 620 (1957).
[8] E. T. Jaynes, Proc. IEEE 70, 939 (1982).
[9] W. Bialek, A. Cavagna, I. Giardina, T. Mora, E. Silvestri, M. Viale, and A. M. Walczak, Proc. Natl. Acad. Sci. U.S.A. 109, 4786 (2012).
[10] A. Cavagna, L. Del Castello, S. Dey, I. Giardina, S. Melillo, L. Parisi, and M. Viale, Phys. Rev. E 92, 012705 (2015).
[11] M. Okun, P. Yger, S. L. Marguet, F. Gerard-Mercier, A. Benucci, S. Katzner, L. Busse, M. Carandini, and K. D. Harris, J Neurosci 32, 17108 (2012).
[12] G. Tkačik, O. Marre, T. Mora, D. Amodei, M. J. Berry II, and W. Bialek, J. Stat. Mech. (2013) P03011.
[13] C. Gardella, O. Marre, and T. Mora, eNeuro 3, 4 (2016).
[14] G. Parisi, Statistical Field Theory (Frontiers in Physics, Addison-Wesley, 1988).
[15] J. Sethna, Statistical Mechanics: Entropy, Order Parameters, and Complexity (Oxford University Press, Oxford, 2021).
[16] S. A. Kivelson, J. M. Jiang, and J. Chang, Statistical Mechanics of Phases and Phase Transitions (Princeton University Press, Princeton, 2024).
[17] M. Sahani, Ph.D. thesis, California Institute of Technology, Pasadena, CA, 1999.

[第6页，第3段]
[18] M. R. Whiteway and D. A. Butts, Curr. Opin. Neurobiol. 58, 86 (2019).
[19] S. Cocco, R. Monasson, and V. Sessak, Phys. Rev. E 83, 051123 (2011).
[20] 技术细节与推导见 http://link.aps.org/supplemental/10.1103/nr71-phqw 处的补充材料。
[21] L. Di Carlo, F. Mignacco, C. W. Lynn, and W. Bialek, arXiv:2508.02633.
[22] J. P. Cunningham and B. M. Yu, Nat. Neurosci. 17, 1500 (2014).
[23] J. A. Gallego, M. G. Perich, L. E. Miller, and S. A. Solla, Neuron 94, 978 (2017).
[24] E. H. Nieh, M. Schottdorf, N. W. Freeman, R. J. Low, S. Lewallen, S. A. Koay, L. Pinto, J. L. Gauthier, C. D. Brody, and D. W. Tank, Nature (London) 595, 80 (2021).
[25] D. J. Amit, H. Gutfreund, and H. Sompolinsky, Ann. Phys. (N.Y.) 173, 30 (1987).
[26] D. Krotov and J. J. Hopfield, in Advances in Neural Information Processing Systems, edited by D. Lee, M. Sugiyama, U. Luxburg, I. Guyon, and R. Garnett (Curran Associates, Inc., Barcelona Spain, 2016), Vol. 29, pp. 1172–1180.
[27] G. Tkačik, O. Marre, D. Amodei, E. Schneidman, W. Bialek, and M. J. Berry, PLoS Comput. Biol. 10, e1003408 (2014).
[28] J. L. Gauthier and D. W. Tank, Neuron 99, 179 (2018).
[29] L. Meshulam, J. L. Gauthier, C. D. Brody, D. W. Tank, and W. Bialek, Phys. Rev. Lett. 123, 178103 (2019).
[30] Allen Institute MindScope Program Allen Brain Observatory, Neuropixels visual coding (dataset), 2019, https://brain-map.org/explore/circuits.
[31] L. Meshulam, J. L. Gauthier, C. D. Brody, D. W. Tank, and W. Bialek, arXiv:2112.14735.
[32] C. W. Lynn, Q. Yu, R. Pang, S. E. Palmer, and W. Bialek, Phys. Rev. E 111, 054411 (2025).
[33] P. C. Hohenberg and B. I. Halperin, Rev. Mod. Phys. 49, 435 (1977).
[34] Allen Institute MindScope Program Allen Brain Observatory, Neuropixels Visual Coding (Dataset) (2019), https://brain-map.org/explore/circuits.

[第6页，第4段]
结束语

[第6页，第5段]
平稳性考量——在本文中，我们始终假设所记录的神经活动在每个数据集的持续时间内是平稳且遍历的。为从经验上评估这些假设的有效性，我们将每次记录划分为两个连续且等长的时间段。对于每个时间段，我们独立计算了实验测得的可观测量 $\chi_{\text{exp}}$ 和 $\mu_{\text{exp}}$。如图6所示，我们发现，在所有数据集中，由记录的前半段和后半段计算得到的 $\chi_{\text{exp}}$ 和 $\mu_{\text{exp}}$ 值之间存在强相关性。这种一致性表明，缓慢的非平稳性不会显著影响此处所考虑的可观测量。

[第6页，第6段]
$E_{\text{dist}}$ 的配分函数——在此我们计算匹配单个神经元平均活动以及沿选定投影分布的模型的配分函数，从而得到式(7)。配分函数定义为，

[第6页，第7段]
$$Z_{\text{dist}} \equiv \sum_s \exp \left[ \sum_{n=1}^N h_n s_n - NU \left( \sum_{n=1}^N \frac{W_n}{\sqrt{N}} s_n \right) \right].$$  (B1)

[第6页，第8段]
为计算配分函数 $Z_{\text{dist}}$，我们首先引入以下积分，

[第7页，第1段]
图6. 观测值在不同时间分段上的一致性。每个数据集被划分为两个连续且大小相等的时间分段。实验测量的观测值 $\mu_{\text{exp}}$ (a) 和 $\chi_{\text{exp}}$ (b) 分别对每个分段独立计算。颜色和大小标识数据集，并遵循正文图1中使用的相同颜色编码。沿恒等线的强相关性表明这些观测值在不同时间上是稳定的。

[第7页，第2段]
$ 
Z_{\text{dist}} = \sum_s \int d\varphi \delta \left( \varphi - \sum_n \frac{W_n}{\sqrt{N}} s_n \right) \exp[-E_{\text{dist}}(s)].
 $

[第7页，第3段]
这允许我们将 $U\left(\sum_n s_n W_n / \sqrt{N}\right)$ 对构型 $s$ 的复杂依赖关系重写为 $U(\varphi)$。然后，我们利用 delta 函数的积分表示来解耦变量 $\{s_n\}$，得到，

[第7页，第4段]
$ 
Z_{\text{dist}} = \sum_s \int \frac{dz}{2\pi} \int d\varphi \exp^{-NU(\varphi) - iz\varphi + \sum_n s_n \left( h_n + iz \frac{W_n}{\sqrt{N}} \right)}.
 $

[第7页，第5段]
对 $2^N$ 个构型 $\{s_n\}$ 求和，得到正文式(17)中出现的积分表达式。

[第7页，第6段]
熵的计算——式(7)中分布模型的熵为

[第7页，第7段]
$ 
S_{\text{dist}} = \ln Z_{\text{dist}} + \langle E_{\text{dist}}(\mathbf{s}) \rangle.
 $

[第7页，第8段]
平均能量的计算是直接的

[第7页，第9段]
$ 
\langle E_{\text{dist}} \rangle = \sum_n h_n \mu_n + N \langle U(\varphi) \rangle.
 $

[第7页，第10段]
在 $1/N$ 的领头阶，配分函数为，

[第7页，第11段]
$ 
\ln Z_{\text{dist}} = N \ln 2 - N f_{\text{dist}}(\varphi_{\text{sp}}, z_{\text{sp}}) - \frac{1}{2} \ln \det H + \mathcal{O}(1/N),
 $

[第7页，第12段]
其中 $H$ 是 Hessian 矩阵（黑塞矩阵），即在鞍点处计算的 $f_{\text{dist}}(\varphi, z)$ 的二阶导数矩阵，

[第7页，第13段]
$ 
H = \begin{pmatrix} \frac{1}{N} \sum_n W_n^2 \left[ 1 - \tanh^2 \left( h_n + i \frac{W_n}{\sqrt{N}} z_{\text{sp}} \right) \right] & i \\ i & NU''(\varphi_{\text{sp}}) \end{pmatrix}.
 $

[第7页，第14段]
自由能的曲率，由 $H$ 的行列式给出，

[第7页，第15段]
$ 
\det H = 1 + U''(\varphi_{\text{sp}}) \sum_n W_n^2 \left[ 1 - \tanh^2 \left( h_n + i \frac{W_n}{\sqrt{N}} z_{\text{sp}} \right) \right]
 $

[第7页，第16段]
决定了鞍点近似的稳定性，其中 $\det H = 0$ 对应于临界相变。

[第7页，第17段]
利用式(C3)中 $1/N$ 领头阶的平均场近似，我们有

[第8页，第1段]
$  S_{\text{dist}} \approx N \ln 2 - N f_{\text{dist}} (\varphi_{\text{sp}}, z_{\text{sp}}) - \frac{1}{2} \ln \det H  $
$  - \sum_{n} h_n \mu_n + N \langle U(\varphi) \rangle.  $
(C6)

[第8页，第2段]
如果我们分离出对应于独立模型熵的项，$  S_0 = N \ln 2 + \sum_n [\ln \cosh(h_n) - h_n \mu_n]  $，则熵差 $  \delta S_{\text{dist}} = S_{\text{dist}} - S_0  $ 为，

[第8页，第3段]
$  \delta S_{\text{dist}} \approx N [\langle U(\varphi) \rangle - U(\varphi_{\text{sp}}) ] - \frac{1}{2} \ln [1 + NU''(\varphi_{\text{sp}}) \Delta ],  $
(C7)

[第8页，第4段]
其中 $  \Delta  $ 如式 (27) 所定义。最后，det $  H  $ 的逆与磁化率 $  \chi  $ 相关，

[第8页，第5段]
$  \chi = \frac{\Delta}{1 + NU''(\varphi_{\text{sp}}) \Delta}  $
(C8)

[第8页，第6段]
与数值模拟的比较——在此我们检验正文中讨论的模型能在多大程度上捕捉最大熵构造中所约束的可观测量之外的特征。我们考虑总群体活动 $  m = (1/N) \sum s_n  $ 的分布，以及沿协方差矩阵第二特征向量投影的活动分布；结果分别见图 7(a) 和 7(b)。

[第8页，第7段]
从图 7(a) 中可以看出，我们的模型很好地描述了总群体活动的实验分布。特别是，它准确地再现了高度非高斯的右侧尾部，这对应于高活动状态相对于神经元独立时预期值的巨大过剩。这种匹配一直延伸到约 $  \sim 4.2\%  $ 的神经元同时活跃的状态，而这种情况仅以 0.038% 的概率发生。这一成功不仅仅是因为权重 $  W  $ 与均匀向量重叠，因为随机化 $  W  $ 的分量会保持这种重叠但破坏一致性。

[第8页，第8段]
与总活动的情况相反，该模型在预测沿第二主成分的活动分布方面表现非常差 [图 7(b)]。实际上，预测分布与神经元完全独立时我们所看到的非常相似。这也许并不令人惊讶，因为主成分按定义在主导阶上是不相关的，因此我们预期了解一个成分的信息对其他成分相对没有信息量；这并不完全正确，因为分布并非高斯分布。

[第8页，第9段]
尽管仅使用协方差矩阵来选择方差最大的方向，但势 $  U(\varphi)  $ 的非二次形式使我们能够对所有 $  \sim N^2/2  $ 个相关性做出非平凡的预测。如图 8 所示，该模型捕捉到了实验数据的总体趋势，并在误差棒范围内再现了相关矩阵中的若干大元素，尽管这些并未被显式约束。我们强调，这并不是因为协方差矩阵是低秩的——朴素近似 $  C \sim \Delta WW^T  $ 完全失败。我们得出结论，$  U(\varphi)  $ 中的非二次项使得一个专注于单一投影的模型能够做出超越协方差秩一近似的粗略但非平凡的预测。
