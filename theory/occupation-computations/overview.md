# 临界聚焦色散系统的阈值、相干结构与动力学

## R19：积分曲率条件下的尺度定理与背景驱动的二次塌缩候选

真实的二次尺度爆破解尚未构造。

推荐先读本文及 [structural-synthesis.md](../background-interaction/structural-synthesis.md)，再读对应证明。此前阶段的所有文件原样保留；新的结论应连同本轮的假设与范围理解。

## 1. 本轮改变了什么

R18 留下的问题是：能否在次模态只受能量空间控制时，确定临界主核心的宽度？本轮没有把这一问题笼统宣布解决，而是得到了两个数学上不同的推进。

* 对一般质量临界标量 NLS 的实势扰动，完成了一个比 R18 幂次条件更强的尺度定理。它不再预设基态剖面，也不依赖项目的定量剖面稳定性结论。
* 对一维共同密度五次系统，发现并精确计算了背景引起的负一阶尺度能量。这指向一支可能比伪共形更快的塌缩，而不是支持把所有情形强行归入同一个速率。

两条推导的共同结构是：临界质量使静态主核心能量沿缩放族退化；尺度由背景、二次相位和辐射之间的首个非零相互作用确定。

## 2. 完整条件定理：曲率只须满足一个积分条件

在任意有限空间维数 $d\ge1$，考虑

$$
iu_t+\Delta u+|u|^{4/d}u+V(t,x)u=0,
\qquad V\in\mathbb R.
$$

设 $Q$ 满足 $-\Delta Q+Q-Q^{1+4/d}=0$，$M_c=\|Q\|_2^2$。假设：

1. $\|u(t)\|_2^2=M_c$，且解和实势的局部正则性足以通过逼近使用连续性、能量、动量与局部维里恒等式。
2. 不含势能的标量能量 $E_0(u(t))$ 在终端时间区间一致有界。
3. $\|\nabla u(t)\|_2\to\infty$ 当 $t\uparrow T<\infty$。
4. 记 $h=T-t$，满足

$$
\boxed{\int_0^{h_0}h\|\nabla_x^2V(T-h)\|_\infty\,dh<\infty.}
$$

则唯一的全质量浓缩点、整个主密度的有限方差、严格正的终端内能以及固定尺度的共形基态渐近全部随之成立。特别地，真正的梯度归一化尺度满足

$$
\boxed{\lambda_{\rm kin}(t):=
\frac{\|\nabla Q\|_2}{\|\nabla u(t)\|_2},\qquad
\frac{\lambda_{\rm kin}(t)}{T-t}\longrightarrow\mu_*>0.}
$$

设 $b$ 为质心、$P$ 为动量，并令

$$
e=E_0-\frac{|P|^2}{2M_c},\qquad
I=\int|x-b|^2|u|^2,\qquad V_Q=\int|y|^2Q^2.
$$

那么 $e\to e_*>0$，$I/h^2\to8e_*$，$\mu_*^2V_Q=8e_*$。去除质心及平均动量后作共形变换，主场在 $H^1$ 中模去一个常数空间相位，收敛到 $\mu_*^{-d/2}Q(\cdot/\mu_*)$。这里只声称模相位收敛：单独的曲率条件不能控制势的任意时间依赖常数部分所带来的相位。

### 推导中真正加强的一步

临界质量下，相位改变后的标量能量仍非负，故

$$
\left|\int J\cdot\nabla\phi\right|^2
\le2E_0\int|u|^2|\nabla\phi|^2.
$$

第一次使用它，得到主密度的终端原子、自动有限方差，以及中心化能量 $e_*>0$。第二次在去除平均运动的共形坐标中使用它，直接对共形能量的平方根反向积分：

$$
\sqrt{E_{\rm conf}(1/h)}
\lesssim\int_0^h r^2L(r)\,dr,
\qquad L(r)=\|\nabla^2V(T-r)\|_\infty.
$$

于是整个共形密度的二阶输运尾长满足

$$
W_2(\rho_{\rm conf}(1/h),\rho_*)
\lesssim\int_0^h\left(r-\frac{r^2}{h}\right)L(r)\,dr\to0.
$$

这个加权收敛排除了“核心继续变窄、微小质量尾部却承担方差”的可能。随后只用标量尖锐不等式的定性紧性，就能识别完整基态剖面。

R18 的 $L\lesssim h^{-\alpha},\alpha<2$ 包含在新条件内。现在还覆盖

$$
L(h)\lesssim h^{-2}\log^{-p}(1/h),\qquad p>1.
$$

另一方面，经典透镜构造取 $\lambda=h\log^{-\beta}(1/h)$，给出曲率约 $h^{-2}/\log(1/h)$ 的确切受迫标量解，其宽度比 $h$ 更小。这说明仅要求 $h^2L(h)\to0$ 不够。该例不是自主有限质量向量系统的反例，也不说明积分条件对每个势都是必要条件。

完整证明和独立核对见 [sharpness.md](../background-interaction/sharpness.md)、[rough-virial.md](../background-interaction/rough-virial.md)。全空间 Hessian 条件还能换成由主密度加权的力方差条件，详见证明；没有声称它自动由次模态 $H^1$ 有界推出。

## 3. 一维五次系统：背景产生一个严格负的一阶尺度能量

方程仍为

$$
iu_{j,t}+u_{j,xx}+\rho^2u_j=0,\qquad \rho=\sum_j|u_j|^2.
$$

给定有限个光滑紧支撑奇函数组成的次模态背景 $W$，其占据空间上的 Gram 矩阵正定。令

$$
A=\sum_{j\ge2}|W_j'(0)|^2,\qquad
c=\frac\pi4+\log2-1>0,\qquad
V_Q=\frac{\sqrt3\pi^3}{32}.
$$

本轮构造了保持**完整 Gram 矩阵精确不变**的初态族 $U_{\lambda,k}$，其中主分量是带二次相位的 $Q_\lambda$，并证明

$$
\boxed{E(U_{\lambda,k})
=E(W)+\frac{V_Q}{8}k^2-cA\lambda+o(\lambda).}
$$

次模态强 $H^1$ 收敛于 $W$，密度一致有界于 $W^{2,\infty}$。二次相位能量 $V_Qk^2/8$ 是精确项，误差不依赖 $k$。因此可选择 $k_\lambda$，使总能量精确等于 $E(W)$。这些是合格的真实初态，但尚未证明它们位于同一条奇异轨道上。

系数来自横向零能方程

$$
HF=0,\quad H=-\partial_y^2-3\operatorname{sech}^2(2y),
\quad F(y)\sim y+c\operatorname{sgn}y.
$$

必须把内层匹配到原外场。未经匹配的内区能量系数为 $+2c$，真正需要的匹配恒等式则是

$$
\int\bigl((F'-1)^2-Q^4F^2\bigr)=-2c.
$$

忽略外场匹配会得到相反的符号。完整证明见 [quintic-closure.md](../background-interaction/quintic-closure.md)，独立计算见 [quintic-details.md](../background-interaction/quintic-details.md)、[transverse-dispersion.md](../background-interaction/transverse-dispersion.md)。

## 4. 动态推进：三个独立计算给出同一二次尺度系数

在零剩余核心能量支上，待构造的候选规律是

$$
\boxed{\lambda(t)\sim\kappa(T-t)^2,
\qquad\kappa=\frac{2cA}{V_Q}.}
$$

这里 $\lambda$ 是宽度；对应梯度增长约为 $(T-t)^{-2}$。本轮没有把形式能量式直接当成动力学证明，而是继续做了以下推导。

* **主剖面质量约束。** 解下一阶偶剖面方程并保持主质量为 $M_c$，独立得到 $\lambda''=4cA/V_Q$。下一阶主虚部方程也因同一个质量正交性而可解。
* **内区时间修正。** 精确求解 $HG=F-yF'$，得到 $G\sim-cy|y|/2+K\operatorname{sgn}y$。这里没有对数尾，且首个纯虚修正不改变领先密度项。
* **外区辐射和总方差。** 精确半线响应为 $R=bh^2B(x/\sqrt h)$。它传播到 $\sqrt h$ 尺度，产生 $-2c\kappa Ah^4$ 的次模态方差交叉项。在同一个 $\kappa$ 下，这恰好抵消主核心的 $V_Q\kappa^2h^4$，符合总维里恒等式。

外区必须由次模态自身的非线性演化作为背景，才能保留其能量与 Gram 守恒；不能用自由演化替代后忽略额外能量漂移。

进一步，零能散射给出一个有效外区关系

$$
w_j(0^+)=c\lambda\,\partial_xw_j(0^+).
$$

作为辅助 Robin 边界问题，它的共同实系数使全部 Gram 条目精确守恒；加入相应边界能量后，其做功恒等式为

$$
\frac{d}{dt}E_{\rm sec,eff}
=-c\lambda'\sum_j|\partial_xw_j(0^+)|^2.
$$

与主核心的相位动能交换再次给出相同的尺度加速度。原方程没有物理边界；把该有效边界模型严格导出为原方程的渐近极限，仍是构造的一部分。

此外，外区斜率的半阶时间导数反馈不能省略。省略它会被缩小的核心势放大成严重的残差。已得到带精确余项的有限阶递推，但最直接的无限级数一般发散，不能据此宣称收缩映射已经完成。

动态推导见 [quintic-dynamics.md](../background-interaction/quintic-dynamics.md)、[quintic-outer-matching.md](../background-interaction/quintic-outer-matching.md)、[quintic-virial.md](../background-interaction/quintic-virial.md)。

## 5. 尚未完成的动力学与本轮定理之间的关系

二次尺度真实解的构造仍需要：统一的高阶内外区复合近似；针对完整动态近似的终端估计；非线性误差及全部守恒约束的闭合。已完成的散射、匹配和守恒量计算不能替代这些步骤。

本轮已完成其中一个实际的线性步骤。对明确给出的静态匹配族，主误差取偶对称、次误差取奇对称，投影去除主分量质量、相位与尺度方向后，定义

$$
\mathcal N_\lambda(z)^2=
\|\partial_xz_1\|_2^2+\lambda^{-2}\|z_1\|_2^2
+\|\partial_xz_{\rm sec}\|_2^2+\|z_{\rm sec}\|_2^2.
$$

相应线性能量与该范数平方等价，并满足

$$
|\mathcal E_{\rm lin}'|
\le\frac{C}{h}\mathcal E_{\rm lin}
+C\sqrt{\mathcal E_{\rm lin}}\,\mathcal N_\lambda(f).
$$

因此终端反向估计只有幂次损失。证明利用 Hamilton 结构取消快速振荡，并保留所有投影项：次模态奇对称性使主次耦合只有相对 $\lambda^{3/2}$ 的大小，配合 $\lambda\asymp h^2$，残余增长恰为 $h^{-1}$。这是一个定义清楚的投影线性问题的结论；仍须证明完整动态近似及实际非线性误差满足所需条件。见 [backward-energy.md](../background-interaction/backward-energy.md)。

另一方面，二次候选并不反驳第 2 节的定理。一维五次主方程的有效势是

$$
V_{\rm eff}=2S|u_1|^2+S^2,
$$

不是次模态密度 $S$ 本身。在已匹配的核心内，$V_{\rm eff}(\lambda y)\sim2A\lambda Q^2F^2$，其曲率约为 $\lambda^{-1}\sim h^{-2}$，正处于不满足积分条件的边界。

二维原有粗糙背景问题也仍未完全闭合。本轮从已有横向强制性推出静态算子没有零能障碍，并接上经典的静态色散定理；但实际核心在不断缩小，尚未证明所需的动态局部能量衰减。已有 $H^1$ 控制与 Gram 正交性本身允许小质量携带有限核心动能，不能以静态代数直接排除。

## 6. 文献对应、物理含义与成果归属

* Carles 的时变势 NLS 工作已有广义透镜变换。本轮不把透镜变换、标量尖锐不等式或调制方法本身说成原创。新增推导是对共形能量平方根的终端积分及其尺度结论；其历史首创性仍需进一步核查。
* Li–Malomed–Li–Chen–Sherman 的准一维双分量凝聚体模型，在关闭自旋轨道、Zeeman 耦合并令同自旋与交叉三体吸引强度相等时，正好化为这里的共同密度五次系统。这提供了明确的物理模型对应，不是已经完成实验或工程应用。
* Jeong–Kim–Kim–Kwon 对不同的 Calogero–Moser 导数 NLS 已研究并证明偶数幂塌缩分类。因此 $h^2$ 指数本身不是跨模型首次出现；需要比较的是这里的局域五次耦合、指数局域基态、占据约束、零能散射系数与最终真实解。

原始文献与逐项模型比较见 [literature.md](../background-interaction/literature.md)、[quintic-literature.md](../background-interaction/quintic-literature.md)。本次检索未发现已证明或禁止这条具体局域向量候选分支的定理；有限检索不能证明首创性。

四阶非径向负能量强制爆破的无条件命题已由激发态全局解构造否定；近临界一般轨道的分类仍未完成。本轮没有将其他模型中的结果重新命名为对该原问题的证明。

## 7. 本轮主要文件

| 文件 | 内容与状态 |
| --- | --- |
| [structural-synthesis.md](../background-interaction/structural-synthesis.md) | 中文结构说明：临界能量、零能散射、不同尺度与物理模型 |
| [sharpness.md](../background-interaction/sharpness.md) | 完整的积分曲率尺度定理及对数边界例子 |
| [quintic-closure.md](../background-interaction/quintic-closure.md) | 完整固定 Gram 匹配能量定理 |
| [transverse-dispersion.md](../background-interaction/transverse-dispersion.md) | 精确散射系数与主剖面可解性 |
| [quintic-dynamics.md](../background-interaction/quintic-dynamics.md) | 下一阶内区方程、尾部匹配及其适用范围 |
| [quintic-outer-matching.md](../background-interaction/quintic-outer-matching.md) | 精确半线响应、反馈递推及未闭合处 |
| [quintic-virial.md](../background-interaction/quintic-virial.md) | 总方差、Gram、能量交换与有效 Robin 模型 |
| [backward-energy.md](../background-interaction/backward-energy.md) | 指定匹配族的投影线性化与幂次终端估计 |
| [modulation.md](../background-interaction/modulation.md) | 原能量空间条件下的尺度—二次相位正规形 |
| [rough-virial.md](../background-interaction/rough-virial.md) | 积分曲率证明的独立推导及粗糙背景的剩余项 |
| [quintic-details.md](../background-interaction/quintic-details.md) | 匹配能量定理的独立复核 |
| [literature.md](../background-interaction/literature.md) | 分类与色散文献；静态横向谱推论 |
| [quintic-literature.md](../background-interaction/quintic-literature.md) | 候选分支、已知速率与物理模型的对应 |

本包还保留 R15–R18 的全部依赖文件，文件清单与摘要由 `MANIFEST_R19_SHA256.json` 记录。
