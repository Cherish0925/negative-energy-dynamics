# 临界聚焦动力学

**相干运动、守恒占据与塌缩**  
Shuxing Yang

[最新研究文件](#最新研究文件) · [English](README.md) · [研究总论](RESEARCH.zh-CN.md) · [成果与证明](RESULTS.md) · [全部内容](CONTENTS.md) · [按原文件名查找](catalog/files.md) · [参考文献](references/README.md)

**聚焦波何时集中，何时能够保持相干运动？** 在临界缩放下，色散能与非线性吸引能具有相同的缩放阶数。锐质量阈值控制两者的平衡，动量、相位响应和守恒模态占据进一步决定允许的动力学。

研究由三个相连的问题展开：负能量全局运动及其质量间隙；占据谱决定的阈值与塌缩核心；多模态吸引与正交代价之间的竞争。[第一篇工作的完整入口](papers/negative-energy/README.md)集中呈现负能量主线；本仓库也保存此后发展出的占据谱与集体束缚研究。

## 1. 负能量与全局相干运动可以共存

对质量临界双调和薛定谔方程

$$
i\partial_tu=\Delta^2u-|u|^{8/N}u,
$$

三维和四维激发态产生负 Hamilton 能量的全局行波。机制是负相位响应：

$$
I=\langle\partial_1Q,L_-^{-1}\partial_1Q\rangle<0,
\qquad P_1(U_v)=2Iv+O(v^3),
\qquad E(U_v)=\frac I4v^2+O(v^4).
$$

慢行波的动量与运动速度反向。平移保持波形与 Sobolev 范数，因此仅凭负能量不能推出非径向解必然塌缩。这些行波具有谱不稳定性；现有构造给出精确相干运动及指定的趋近轨道。

![激发驻波、移动波强度及相位响应的实际计算](figures/coherent-profiles.svg)

*图中为保存的数值剖面。有限网格行波用于展示形状与相位；连续方程的存在定理使用另外的精确算术与区间证书。*

[四维论文](manuscripts/biharmonic-certificates/BNLS-Nonradial-Research-20261007.pdf) · [三维定理](theory/zero-momentum/n3-full-theorem.md) · [谱与非平稳动力学](theory/spectral-dynamics/README.md) · [剖面数据](computations/excited-waves/axial-profiles/) · [计算证书](computations/biharmonic-certificates/)

## 2. 总动量可以抵消，行波质量间隙仍然存在

四维中，两个分离行波，以及一个相干核心加辐射，都能产生**总动量为零、能量为负的精确向前全局解**。若核心的动量大小为 $q$、速度为 $v$，质量为 $\mu$ 的四阶自由辐射具有精确能量下确界

$$
E_{\mathrm{rad}}^{\inf}=\frac{q^4}{2\mu^3},
\qquad \mu_{\mathrm{crit}}=q\left(\frac4v\right)^{1/3}.
$$

严格超过该辐射质量阈值即可完成构造。速度趋零时，总质量趋向一个激发态的质量，将此前双核心构造的极限质量减半。另一方面，标量临界质量附近的优化子相位强制性排除了负能量行波：

$$
E(U)<0\quad\Longrightarrow\quad M(U)\ge M_c+\delta,
\qquad \delta>0.
$$

![辐射能量代价和行波质量间隙](figures/radiation-and-gap.svg)

*左图是精确的归一化自由辐射代价；右图是定理示意，间隙宽度没有被赋予数值。一般持续变形的轨道还需要动力学估计。*

[10 月 18 日单核心构造](theory/coherent-radiation/wave-radiation.md) · [质量间隙论文](manuscripts/profile-mass-gap/BNLS-Mass-Gap-and-Momentum-20261007.pdf) · [无矩条件残差下界](theory/coherent-radiation/robust-gap.md) · [端点与 Fourier 矩界](theory/coherent-radiation/endpoint.md) · [一般色散](theory/homogeneous-dispersion/README.md)

## 3. 守恒占据决定哪部分质量能够集中

共同密度薛定谔系统

$$
i\partial_tu_j+\Delta u_j+\rho^{2/d}u_j=0,
\qquad \rho=\sum_j|u_j|^2
$$

保持整个 Gram 矩阵 $\Gamma_{jk}=\langle u_j,u_k\rangle$。其归一化本征值 $p_1\ge p_2\ge\cdots$ 表示模态占据。二维三次模型在 $p_2/p_1\le\varepsilon_0$ 时有精确阈值 $M_*(p)=M_c/p_1$。在主模态达到临界质量时，全局能量余项进一步给出

$$
E(U)\ge\frac12E_{\mathrm{scalar}}(u_1)
+\frac1{64}\sum_{j\ge2}\|\nabla u_j\|_2^2.
$$

占据比条件与秩和次占据总和无关。发生临界奇性时，主模态形成相干核心，其余占据的总动能保持有界。相关工作还给出保持精确占据谱的端点构造、核心输运，以及相应条件下的无限模态推广。

![占据阈值、Townes 核心缩放及塌缩尺度](figures/occupations-and-core.svg)

*阈值曲线展示一维五次模型对全部有限占据谱的公式，其锐不等式输入来自 Read–Schulz；二维同一公式成立于上述占据范围。中图是保存的 Townes 剖面的缩放。右图线性尺度律具有曲率条件，虚线二次尺度对应尚未构造真实奇异轨道的候选机制。*

[固定占据论文](manuscripts/fixed-occupation/Fixed-Occupation-Thresholds.pdf) · [锐占据阈值](theory/occupation-thresholds/occupation-gap.md) · [核心与背景](theory/critical-core/README.md) · [尺度与相位](theory/scale-and-phase/README.md) · [背景相互作用](theory/background-interaction/README.md)

## 4. 多个正交模态能否比单模态更有效地束缚？

密度重叠增强吸引，正交化增加动能。二维问题要求对任意有限正交归一族比较

$$
F=\int\left(\sum_j|\phi_j|^2\right)^2,\quad
T=\sum_j\|\nabla\phi_j\|_2^2,\quad
\langle\phi_i,\phi_j\rangle=\delta_{ij},
\qquad F\ \stackrel{?}{\le}\ \frac2{M_c}T.
$$

它等价于相应的二维 Lieb–Thirring 锐常数问题。已有推导包括分离核心的正亏损、横向估计、Townes 全尺度散射系数符号、有限分离势阱的负谱计数，以及任意秩矩阵余项。完整二维锐不等式仍未解决。

![由保存的 Hermite 系数重建的双模态和四模态密度及搜索差距](figures/collective-binding.svg)

*密度图由原始 Hermite 系数重建。61 次搜索中有 20 次达到迭代上限；当前候选低于单态参考值，不能据此判定全局上确界。分裂现象在已有文献中有先例。*

[变分问题](theory/collective-threshold/README.md) · [分离核心](theory/separated-cores/README.md) · [全尺度散射](theory/all-scale-scattering/main-theorem.md) · [矩阵余项](theory/matrix-remainders/README.md) · [Hermite 数据](computations/hermite-optimization/) · [周期势计算](computations/periodic-potentials/)

## 5. 完整谱响应揭示受限扰动遗漏的方向

完整响应允许未占据态参与调整。Schur 补恒等式给出相对于受限伸缩试探的修正。在保存的三模态鞍点计算中，二次势试探仍低于失稳阈值，而完整导数响应已超过阈值。

同一阶段还排除了一个曾考虑的普遍线性密度梯度修正：两个远离的 Townes 核心中，原不等式亏损按 $e^{-2R}$ 衰减，而拟加入的修正按更慢的 $R^{-1/2}e^{-R}$ 衰减。

![完整谱响应和分离核心渐近阶数](figures/spectral-response.svg)

*响应计算的对象是 $a>M_c$ 的已知鞍点。渐近比较否定的是更强的辅助不等式，原二维锐常数问题仍然开放。*

[响应恒等式](theory/full-response/response-schur.md) · [梯度修正反例](theory/full-response/density-gradient.md) · [计算记录](computations/full-response/r31_response_calibration.json)

## 6. 光学对应必须保持正确的色散与临界缩放

一个二阶时间方向与两个四阶横向方向，使三次模型在各向异性缩放下成为质量临界：

$$
i\partial_z u=(-\partial_\tau^2+\Delta_\perp^2)u-|u|^2u,
\qquad
u_\lambda(z,\tau,x_\perp)=\lambda^2u(\lambda^4z,\lambda^2\tau,\lambda x_\perp).
$$

这里 $L^2$ 质量对应归一化的积分光强；Hamilton 能量 $E$ 表示色散与聚焦的平衡。移除时间方向的漂移后，内禀能量为 $E_{\mathrm{int}}=E-|P_\tau|^2/(2M)$。质量间隙与定量残差已经推广到该模型，并对半正定横向二阶修正保持统一。

![混合色散几何、实际响应延拓和临界路径折返](figures/mixed-dispersion.svg)

*10 月 19 日保存的延拓数据。加密网格后，一个表面上的负响应变为正；另一条保持临界性的路径出现折返。辅助路径上最接近目标的已保存谱状态到达 $s=0.991015625$，尚未到达光学目标 $s=1$。目标模型中的负内禀能量行波存在性仍待解决。*

[混合模型定理](theory/coherent-radiation/anisotropic-gap.md) · [统一残差](theory/coherent-radiation/robust-mixed-extension.md) · [物理对应](theory/coherent-radiation/physical-bridge.md) · [延拓结果与运行方法](theory/mixed-dispersion-continuation/README.md) · [全部数值状态](computations/mixed-dispersion-continuation/)

## 最新研究文件

| 研究日期 | 内容 | 直接入口 |
|---|---|---|
| 10 月 19 日 | 混合光学方程的两条延拓路径 | [结果与方法](theory/mixed-dispersion-continuation/README.md) · [五个求解器及保存状态](computations/mixed-dispersion-continuation/core_continuation/) |
| 10 月 18 日 | 单核心与辐射、无矩残差、混合色散间隙、端点恒等式 | [论文 PDF](manuscripts/coherent-radiation/Negative-Energy-Coherent-Dynamics-Advances-20261018.pdf) · [十一份推导](theory/coherent-radiation/README.md) |
| 10 月 18 日 · R31 | 完整谱响应与密度梯度修正反例 | [推导](theory/full-response/README.md) · [计算](computations/full-response/) |
| 10 月 18 日 · R30 | 任意秩余项、密度转移、作用量约化 | [七份推导](theory/matrix-remainders/README.md) |
| 10 月 16 日 · R28 | 平方与三角晶格周期势搜索 | [分析](theory/periodic-potentials/README.md) · [数据](computations/periodic-potentials/) |
| 10 月 9—15 日 · R15—R25 | 占据阈值、核心动力学、尺度选择、分离核心理论 | [逐项成果](RESULTS.md) · [发展脉络](HISTORY.md) · [原文件索引](catalog/files.md) |

## 阅读与使用

| 您要查找什么 | 入口 |
|---|---|
| 整个工作的方程、原理与联系 | [中文研究总论](RESEARCH.zh-CN.md) |
| 每项结论的准确条件和证明 | [成果目录](RESULTS.md) |
| 论文、全部推导、代码与数据 | [完整目录](CONTENTS.md) |
| 以前交付的某个文件或资料包 | [原文件名索引](catalog/files.md) |
| 图的定义、数据和重绘方法 | [研究图](figures/README.md) |
| 计算环境与执行命令 | [计算说明](COMPUTATIONS.md) |
| 前人工作的关系及剩余问题 | [参考文献](references/README.md) · [开放问题](OPEN_PROBLEMS.md) |

本仓库整理了 32 个已恢复研究资料包及四份独立记录。此前命名的三份光学附件仍未找回，具体范围见[材料说明](catalog/README.md)。上述研究图由实际保留的数据和明确公式生成。

Copyright © 2026 Shuxing Yang. All rights reserved.
