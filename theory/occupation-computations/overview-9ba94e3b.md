# 临界聚焦色散系统：接近单模态占据时的精确阈值
## R15 研究记录 — 2026-10-09

本轮具体对象是二维共同密度聚焦系统
$$
i\partial_tu_j=-\Delta u_j-\rho u_j,\qquad
\rho=\sum_j|u_j|^2.
$$
研究主线仍是“临界聚焦色散系统的阈值、相干结构与动力学”。本轮没有解决全部二维 Lieb–Thirring 最优常数问题，也没有解决等占据双模态端点。推进到的具体结论，是接近单模态占据的一整个区间内，精确常数对所有有限模态数一致；对应的动能不等式还可延伸到可数无穷秩。

## 1. 要证明的精确命题

令 $Q$ 是
$$
-\Delta Q+Q-Q^3=0,\qquad Q>0,\qquad Q\in H^1(\mathbb R^2)
$$
的径向基态，记 $M_c=\int Q^2$、$C_1=2/M_c$。

**接近单模态占据的动能不等式。** 存在只依赖二维标量基态的常数 $\tau_0>0$，使得对任意非零正迹类算子 $\gamma$，若
$$
\alpha=\|\gamma\|_{\mathrm{op}},\qquad
\operatorname{Tr}\gamma-\alpha\le\tau_0\alpha,\qquad
T(\gamma)=\operatorname{Tr}(-\Delta\gamma)<\infty,
$$
则
$$
\boxed{\quad
\int_{\mathbb R^2}\rho_\gamma^2\,dx
\le \frac{2}{M_c}\,\alpha\,T(\gamma).
\quad}
\tag{1}
$$
这里 $\rho_\gamma=\sum_j n_j|\phi_j|^2$，其中 $n_j$ 是占据数，$\phi_j$ 是正交归一模态。常数 $2/M_c$ 最优；同一个 $\tau_0$ 对有限秩和可数无穷秩均适用。不要求初态空间径向，也不要求给定初态接近某个固定 Townes 函数。

本记录证明的是 $\tau_0$ 的严格正性，尚未计算一个显式、可直接用于实验参数选择的数值。不能把“足够小”换成任意指定的占据百分比。

## 2. 对非线性演化的直接含义

先取有限个模态。共同的自伴 Hamiltonian 保持 Gram 矩阵
$$
\Gamma_{ij}=\int u_i\overline{u_j}
$$
不变。固定总质量（归一化模型中的总功率）$M=\operatorname{Tr}\Gamma$，令 $p_j$ 是 $\Gamma/M$ 的本征值，$\sum_jp_j=1$，并令 $p_{\max}=\max_jp_j$。

若
$$
\frac{1-p_{\max}}{p_{\max}}\le\tau_0,
$$
则固定整个占据谱 $p$ 的精确严格两侧边界为
$$
\boxed{\quad M_*(p)=\frac{M_c}{p_{\max}}.\quad}
\tag{2}
$$

准确含义如下：

* $M<M_*(p)$：该占据谱下的全部 $H^1$ 初态产生全局、梯度范数有界的解。
* $M>M_*(p)$：存在具有该精确占据谱的光滑紧支撑初态，其解有限时间塌缩。
* 这里没有完成 $M=M_*(p)$ 的全部动力学分类，也没有证明所有超阈值初态都塌缩。

证明只需将 (1) 用于场的密度算子：
$$
E=\tfrac12A-\tfrac14\int\rho^2
\ge \tfrac12\left(1-\frac{Mp_{\max}}{M_c}\right)A.
$$
严格下侧由能量守恒和局部适定性延拓。严格上侧由最优常数的近极值序列构造负能量；有限秩时可保持精确 Gram 矩阵作光滑紧支撑逼近，再用方差恒等式 $I''=16E<0$ 得到塌缩。

无穷秩动能不等式 (1) 不需要方差条件。无穷秩的有限方差塌缩构造另有占据数矩条件，不能从有限秩结论直接省略这一步。

## 3. 真正连接全局变分问题的机制

将最大占据归一化为 1，其余写成 $t_j$，令
$$
\tau=\sum_{j\ge2}t_j,\qquad
\rho=|\phi_1|^2+\sum_{j\ge2}t_j|\phi_j|^2.
$$
要排除的，是某个正交族满足
$$
\int\rho^2>C_1\left(\|\nabla\phi_1\|_2^2+
\sum_{j\ge2}t_j\|\nabla\phi_j\|_2^2\right).
$$

共同空间缩放使 $\|\nabla\phi_1\|_2=1$。设
$$
\delta=C_1-\int|\phi_1|^4,\qquad
B=\sum_{j\ge2}t_j\|\nabla\phi_j\|_2^2.
$$
标量 Gagliardo–Nirenberg 不等式首先强迫任何反例满足
$$
B<\frac{4\tau}{(1-\tau)^2},\qquad
\delta<\frac{C_1\tau}{1-\tau}.
\tag{3}
$$
因此主模态必须自动接近标量最优轨道。这个接近性质是反例假设推出的结论，不是附加在初态上的限制。

固定质量和梯度归一化以后，标量不等式的二次稳定性给出
$$
\phi_1=q+\eta,\qquad q=Q/\sqrt{M_c},\qquad
\|\eta\|_{H^1}^2\le K\delta
$$
（已调整整体相位和空间中心）。标量线性化的缩放零方向由梯度约束排除；相位、平移方向由调制排除。这一标准输入及其推导见 r15_imbalanced.md。

新的证明链需要下面的齐次谱强制性：
$$
\int Q^2|v|^2\le(1-\kappa)\int|\nabla v|^2,
\qquad \langle v,Q\rangle=0,\qquad \kappa>0.
\tag{4}
$$
它不是 $L^2$ 正谱隙；后者因连续谱从零开始而不可能成立。

正交条件使次模态的 $Q$ 投影只产生 $O(\delta\tau)$ 误差。用 (4) 吸收密度交叉项，最终得到
$$
\int\rho^2-C_1(1+B)
\le -(1-C\tau)\delta-C_1(\kappa/4-\tau)B.
\tag{5}
$$
对于一个与模态数无关的足够小 $\tau_0>0$，右侧非正。这是完整非线性估计，不是一阶或二阶形式展开。

最优性来自一个接近 Townes 的主模态，以及彼此正交、逐渐稀释到远处的其余模态。进一步，同一估计证明了固定有限占据谱下全部优化序列的结构：共同缩放、相位与平移调整后，主模态强 H1 收敛到 Townes，所有正权重次模态的梯度、L4 范数和局部质量趋零。因此，只要次占据不为零，最优常数不由一个真正的有限正交族取到。这是变分优化序列的分类，未被当作时变解的孤子分解。无穷秩不等式由谱截断与单调收敛得到；详见 r15_density_matrix_extension.md。

## 4. 补上谱输入：基态包络与球面几何

本轮用可复算区间积分证明了一个刻意保留大余量的上界：
$$
\boxed{\quad Q(r)^2\le\frac6{(1+r^2)^2}\quad(r\ge0).\quad}
\tag{6}
$$

这不是将浮点采样当成全区间证明。证明包括三个部分：

1. 原点处利用复解析积分方程和 Cauchy 余项控制偶次幂级数。
2. 从 $r=1/128$ 到 $r=6$，用每步 Picard 包络和 16 阶 Taylor–Lagrange 区间余项覆盖全部区间。
3. 从 $r=6$ 到无穷远，用外域最大值原理给出指数上界，再与有理函数比较。

两个精确二进制有理初值（显示为 2.20620086 和 2.20620087）分别严格欠射、过射。所有步的区间包络还检查了首次退出的方向，排除漏掉中途振荡。连续依赖、首次退出分类和正基态唯一性将真正的 $Q(0)$ 夹在二者之间。

全初值区间传播给出的记录为：
$$
\sup_{1/128\le r\le6}Q(r)^2(1+r^2)^2
\le5.024647<6,\qquad Q(6)<0.004284<1/200.
$$
这些数值仅用于展示余量；严格端点和完整算术写在代码及 JSON 中。原点和外域均有独立解析控制。

立体投影保持二维 Dirichlet 积分，并把比较势变成球面常数势：
$$
\int_{\mathbb R^2}\left(|\nabla v|^2-\frac6{(1+r^2)^2}|v|^2\right)
=
\int_{\mathbb S^2}\left(|\nabla\widetilde v|^2-\tfrac32|\widetilde v|^2\right).
$$
球面 Laplacian 的前三个本征值是 $0,2,6$。因此右侧只有一个非正方向。

设 $H=-\Delta-Q^2$。由于 $HQ=-Q$，如果存在 $v\perp Q$ 且 $\langle v,Hv\rangle\le0$，则 $\operatorname{span}\{Q,v\}$ 会给出两个非正方向，与球面比较矛盾。这个论证也适用于锚定的有限 Dirichlet 能量空间，排除了零能共振。该空间紧嵌入 $L^2(Q^2dx)$，于是严格正性提升为统一的 (4)。

这一步将一个未知势的连续谱问题，化为一个带余量的基态包络和已知球面谱。解析推导详见 r15_spectral_audit.md，区间算法说明详见 r15_interval_code_audit.md。

## 5. 同时尝试但没有解决的端点

等占据双模态需要
$$
\int(|\phi_1|^2+|\phi_2|^2)^2
\le C_1(\|\nabla\phi_1\|_2^2+\|\nabla\phi_2\|_2^2)
$$
对全部正交对成立。它对应 $\tau=1$，并不由本轮的小占据量定理推出。

本轮进行了以下实质工作：

* 推导不同尺度、相距很远的两个 Townes 波包的精确正交化公式；严格排除了固定尺度比趋于 0 或 1 的两个端部反例机制，中间尺度比的整体符号尚未证明。
* 完全解析地排除精确 Townes 主核附近的非零角动量次模态一阶改进，并得到该受限族的有限振幅估计。
* 在 Dirichlet 正弦谱离散上搜索分离双阱、实偶极、非对称双阱、复涡旋及破对称候选。没有发现超过标量常数的候选。最接近的数值仍比标量值低约 $8.6\times10^{-8}$。

数值最优序列逼近不等式常数不是全局证明。网格细化不消除有限计算域的尾误差，也不保证优化找到了全局极值。因此完整的秩二等式仍待解决。

## 6. 与既有研究的关系和物理意义

标量 Townes 基态、临界质量和线性化结构来自既有 NLS 理论。正交函数的非线性变分问题与 Lieb–Thirring 对偶也已有系统研究。本轮结果使用这些基础，目标是固定占据谱时的精确多模态常数。

Frank–Gontier–Lewin 的秩一非最优性论证要求
$\gamma>\max(0,2-d/2)$；它不包含 $d=2,\gamma=1$ 的等号端点。这说明本轮不能从他们的严格不等式定理直接读出答案，也不存在由本轮小占据量结论造成的逻辑冲突。

在这个二维共同密度模型中，占据谱可表达部分相干场的模态功率分布。结果 (2) 说明：在主模态占据足够高的范围内，任意数量弱次模态的共同聚焦，不会把负能量／可塌缩边界压低到主模态单独临界的数值以下。其余模态如何分配不再改变该边界。

这给出一个精确的模型级结论。要变成定量工程设计，还需要计算有效的占据区间常数，并核对物理系统的饱和、耗散、响应速度和归一化系数。这里没有宣称理想立方模型包含这些机制。

## 7. 文件与复算

* r15_imbalanced.md：非线性不等式、标量稳定性及最优性证明。
* r15_validated_townes.py：标准库区间 Taylor 内核。
* r15_validated_townes.py --certificate：以单一命令复算全部区间证明步骤。
* r15_townes_certificate.json：原始区间输出。
* r15_certificate.md：原点、首次退出、外域和谱比较的完整说明。
* r15_spectral_audit.md、r15_interval_code_audit.md：独立复核。
* r15_density_matrix_extension.md：无穷秩延伸及有限方差边界。
* r15_geometric.md：不同尺度双波包推导。
* r15_numerics_report.md 和相关脚本、JSON、NPZ：探索性反例搜索，与证明性区间计算分开记录。

完整区间证明的单一复算命令：
```sh
python3 r15_validated_townes.py --certificate
```
成功时输出 `certificate_passed: true`；失败的证明检查使程序以错误状态退出。请使用正常的 Python 运行模式，勿用会禁用断言的 `-O`。

也可以分别运行三个内核计算：
```sh
python3 r15_validated_townes.py --a 2.20620086 --R 16
python3 r15_validated_townes.py --a 2.20620087 --R 16
python3 r15_validated_townes.py --a 2.20620086 --b 2.20620087 --R 6 --envelope
```
这里的命令需在解压后的 research 目录运行。

## 8. 原始参考文献

1. M. I. Weinstein, Nonlinear Schrödinger equations and sharp interpolation estimates, Commun. Math. Phys. 87 (1983), 567–576. DOI: 10.1007/BF01208265.
2. S.-M. Chang, S. Gustafson, K. Nakanishi, T.-P. Tsai, Spectra of linearized operators for NLS solitary waves, SIAM J. Math. Anal. 39 (2007), 1070–1111. DOI: 10.1137/050648389. 作者版：https://personal.math.ubc.ca/~ttsai/publications/cgnt-sima07.pdf
3. J. Dolbeault, P. Felmer, M. Loss, E. Paturel, Lieb–Thirring type inequalities and Gagliardo–Nirenberg inequalities for systems, J. Funct. Anal. 238 (2006), 193–220. DOI: 10.1016/j.jfa.2005.11.008.
4. R. L. Frank, D. Gontier, M. Lewin, The nonlinear Schrödinger equation for orthonormal functions II: Application to Lieb–Thirring inequalities, Commun. Math. Phys. 384 (2021), 1783–1828. DOI: 10.1007/s00220-021-04039-5. https://arxiv.org/abs/2002.04964
5. R. L. Frank, D. Gontier, M. Lewin, Optimizers for the finite-rank Lieb–Thirring inequality. https://arxiv.org/abs/2109.05984

## 9. 证明所用的谱与区间输入

2026-10-09 完成本轮复核：

* 非线性估计及其常数对秩的一致性经过另一研究分支核查；临界缩放退化的处理已补成完整附录。
* 射击括号、原点余项、外域比较、球面非正指标和锚定空间紧性均经过数学推导。
* 区间算术、Taylor 递推、整步 Picard 包络、首次退出的全程检查经过算法推导。最终内核 SHA256 为 d5bd62d276b0decd65eadca0c198610289fdb06f8ca33aad7606178edfc25b34。
* 主研究分支再次执行最终 `--certificate`，成功。复核属于独立审码和同一程序重跑，没有声称另写了第二套区间积分器，也没有声称经过证明助手形式化。

在记录的标准 IEEE-754 算术语义和已注明经典定理输入下，本轮没有剩余的未证明谱假设；所得是 (1)–(2) 及有限秩优化序列分类的计算机辅助证明。完整等占据双模态端点、显式占据区间以及阈值处全部动力学仍未由本轮解决。

