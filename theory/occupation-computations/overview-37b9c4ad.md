# 临界聚焦色散系统的阈值、相干结构与动力学

## R18：核心尺度与相位的闭合，以及无限模态推广

### 1. 主线与本轮实际推进

研究对象仍是临界聚焦波中，守恒的模态占据谱如何约束集中质量、相干核心和辐射，并最终确定解的动力学。R17 已在指定模型与占据范围内给出单核心及其背景，留下的主要缺口是：核心尺度能否继续缩小，以及相位究竟怎样演化。

本轮有三项主要推进：

1. 在原有能量空间条件下，给出明确归一化后的核心相位渐近式，无需预先知道尺度有正极限。
2. 对二维三次系统，在背景势曲率受到明确控制时，证明精确塌缩尺度；势和前两阶空间导数一致有界时，进一步证明共形主模态趋于固定尺度、确定渐近相位的驻波。
3. 将相应阈值与单核心动力学推广到可数无穷模态，并证明联合范数和迹范数中的结论。

这些结果的假设不同，不能合并成“任意背景、任意模型均已完全分类”。

### 2. 模型、符号与保留的限制

二维方程为

$$
i\partial_tu_j+\Delta u_j+\rho u_j=0,
\qquad \rho=\sum_j|u_j|^2.
$$

一维方程为

$$
i\partial_tu_j+\partial_x^2u_j+\rho^2u_j=0.
$$

记 $\Gamma=\int UU^*dx$，其本征值为 $m_1\ge m_2\ge\cdots$。$Q$ 是相应标量基态，$M_c=\|Q\|_2^2$。本轮的临界动力学均在 $m_1=M_c$ 上研究。

| 模型 | 临界单核心结论所用占据条件 | 本轮没有解除的条件 |
| --- | --- | --- |
| 二维三次共同密度系统 | $m_2/m_1\le\varepsilon_0$，沿用 R16 | 尚未覆盖全部二维占据谱 |
| 一维五次共同密度系统 | $m_2<m_1$，沿用 R17 | 最大占据须为单重 |

一维全部严格占据间隙的变分输入依赖 Read–Schulz 的 arXiv:2609.10478v2；这项锐不等式不是本项目证明的成果。二维 $\varepsilon_0$ 仍包含已有标量稳定性常数，未给出完全数值化的最终阈值。

### 3. 原有粗糙背景下，相位已能精确到收敛余项

设 $T$ 是有限时间爆破端点，写

$$
u_1(t,x)=e^{i\theta(t)}\lambda(t)^{-d/2}
\bigl(Q+\epsilon(t)\bigr)\!\left(\frac{x-a(t)}{\lambda(t)}\right).
$$

尺度由一个具体的振幅归一化固定：

$$
\langle\operatorname{Re}\epsilon,Q^{1+4/d}\rangle=0,
\quad \langle\operatorname{Im}\epsilon,Q\rangle=0,
\quad \langle\operatorname{Re}\epsilon,\partial_kQ\rangle=0.
$$

这不是把尺度定义成相位导数。先由隐函数定理固定振幅、中心和相位，再由方程推出

$$
|\lambda'(t)|+|a'(t)|\le C,
\qquad |\theta'(t)-\lambda(t)^{-2}|\le C.
$$

所以

$$
\boxed{\theta(t)-\int_{t_0}^{t}\lambda(r)^{-2}\,dr
=\theta_*+O(T-t).}
$$

共形时间 $s=(T-t)^{-1}$ 中，同一类归一化给出

$$
\boxed{\vartheta(s)-\int_{s_0}^{s}\mu(r)^{-2}\,dr
=\vartheta_*+O(s^{-1}).}
$$

第二式即使 $\mu(s)\to0$ 仍成立。其证明使用
$L_+Q=-(4/d)Q^{1+4/d}$ 消去相位方程的一阶误差，同时利用完整 Gram 正交性控制次模态在核心附近的作用。

本节的 $\lambda$ 是上述调制归一化的尺度，不能直接替换为梯度归一化尺度后沿用积分相位公式。证明和独立核查分别见 [scale-dynamics.md](../scale-and-phase/scale-dynamics.md) 与 [foundation-check.md](../scale-and-phase/foundation-check.md) 附录。

### 4. 背景曲率受控时，核心塌缩尺度得到闭合

本节直接适用于二维三次系统。把主模态方程写成

$$
i\partial_tu_1+\Delta u_1+|u_1|^2u_1+S(t,x)u_1=0,
\qquad S=\sum_{j\ge2}|u_j|^2.
$$

除原有临界假设外，假定

$$
\|\nabla_x^2 S(t)\|_\infty
\le K(T-t)^{-\alpha},\qquad 0\le\alpha<2,
$$

且势的局部正则性足以使文中能量、动量及维里恒等式成立。令这里的 $\lambda(t)=\sqrt{M_c}/\|\nabla u_1(t)\|_2$ 为原来的梯度归一化尺度，则

$$
\boxed{\lambda(t)=\mu_*(T-t)+O((T-t)^{3-\alpha}),
\qquad \mu_*>0.}
$$

这个结论确定的是实际基态集中尺度，不只是均方根半径。

若进一步有 $\sup_{t<T}\|S(t)\|_{W^{2,\infty}}<\infty$，定义

$$
v_1(s,y)=h\,e^{ih|y|^2/4}u_1(T-h,x_*+hy),
\quad h=s^{-1},
$$

则存在固定 $\mu_*>0,y_*,\vartheta_*$，使

$$
\boxed{
v_1(s,y)=e^{i(s/\mu_*^2+\vartheta_*)}
\mu_*^{-1}Q\!\left(\frac{y-y_*}{\mu_*}\right)
+O_{H^1}(s^{-1}).}
$$

其调制尺度误差为 $O(s^{-2})$，调制后的场残差为 $O_{H^1}(s^{-2})$。这补上了 R17 在这类背景中的尺度与相位缺口；并未证明给定背景的全向量解唯一。

### 5. 证明为什么能够闭合

只知道主模态能量有界以及方差为 $O((T-t)^2)$，不足以确定核心尺度：微小质量尾部可能承担不可忽略的方差。本轮对整个密度作了更强的控制。

去掉质心平动后，定义

$$
e(t)=E_{\rm scalar}(u_1(t))-\frac{|P_1(t)|^2}{2M_c},
\qquad I(t)=\int|x-b_1(t)|^2|u_1|^2dx.
$$

相位改变后的标量能量非负性与连续性方程给出

$$
I(t)\le8\left(\int_t^T\sqrt{e(r)}\,dr\right)^2,
\qquad |(\sqrt e)'|\le\|\nabla^2S(t)\|_\infty\sqrt{I/2}.
$$

这两式先推出严格正的终端内能 $e_*>0$。有界曲率时，中心化维里恒等式进一步给出

$$
e=e_*+O(h^2),\quad I=8e_*h^2+O(h^4),
\quad I'=-16e_*h+O(h^3).
$$

共形标量能量中的主要项因而抵消，剩下 $O(s^{-4})$。其平方根可积，使全部主模态密度在二次输运距离中收敛，方差也随之收敛。这排除了核心变成点质量而方差逃向空间无穷远的可能，进而确定

$$
\mu_*^2\int |y|^2Q(y)^2dy=8e_*.
$$

曲率允许 $h^{-\alpha}$ 增长时，同一推导产生 $O(s^{-4+\alpha})$ 的中心化共形能量；$\alpha<2$ 保证其平方根仍可积。$\alpha=2$ 的端点没有被本轮证明覆盖。

完整证明见 [regular-background.md](../scale-and-phase/regular-background.md)；维度一般的条件性推导及独立核查见 [potential-details.md](../scale-and-phase/potential-details.md)。一维五次向量系统有额外混合非线性 $2S|u_1|^2u_1+S^2u_1$，不能把本节结论直接照搬过去。

### 6. 正则背景下，塌缩系数还可由能量分配确定

若二维次模态在整个终端时间区间一致有 $H^k$ 正则性，$k>3$，则本轮额外证明

$$
w_j(x_*)=0\quad(j\ge2),
$$

其中 $W$ 是次模态终态。这不是仅凭二维 $H^1$ 点值推理：证明使用改进后的主模态 $L^2$ 误差、保留二次相位的精确正交性，以及次模态的一致 Lipschitz 控制。

此时次模态在物理变量中强 $H^1$ 收敛，核心与背景的交叉势能趋零。因此

$$
\boxed{\mu_*^2=\frac8{\int|y|^2Q^2}
\left(E-E_{\rm sec}(W)-\frac{|P_*|^2}{2M_c}\right)>0.}
$$

这里 $P_*=P(U)-P(W)$，$E_{\rm sec}$ 是同一二维方程的次模态子系统能量。它说明，在指定模型中，扣除背景能量和核心平动动能后的能量决定塌缩系数。不能把“光滑初态”直接等同于“次模态一直满足上述一致高阶正则性”。

### 7. 无限模态推广补足了什么

现在可取任意可分 Hilbert 空间 $\mathcal H$，研究

$$
iU_t+\Delta U+\|U\|_{\mathcal H}^{4/d}U=0,
\qquad U\in H^1(\mathbb R^d;\mathcal H).
$$

总质量、总动能均有限，$\Gamma$ 是正迹类算子，沿用第 2 节的占据范围。有限端点的主核心、唯一背景、自动主模态方差和一维背景共同零点，在联合 Hilbert 范数中继续成立。

对前向全局的临界解，若还有有限**总**方差，则仍是完全散射，或

$$
U(t)=c\,S_t+e^{it\Delta}F+o_{H^1(\mathcal H)}(1),
\qquad F(x)\perp c,
$$

其中 $S_t$ 是 R17 所述宽度有界的移动基态核心。一般背景下仍未证明这个宽度的正极限。

无限维推广有两个必须解决的问题：

* Hilbert 值 $H^1$ 有界集并不自动局部紧。本轮用守恒关系
  $\|(1-P_N)U(t)\|_2^2=\sum_{j>N}m_j\to0$，将有限坐标紧性提升为联合紧性。
* 每个坐标分别加权收敛不允许直接交换无穷求和与极限。本轮控制总次模态密度的输运和总方差，得到联合加权收敛，再得到联合强 $H^1$ 辐射。

若用空间相干算子 $\gamma_U=\sum_j|u_j\rangle\langle u_j|$ 表述，非散射分支还有

$$
\gamma_U(t)=|S_t\rangle\langle S_t|
+e^{it\Delta}\gamma_F e^{-it\Delta}+o_{\mathfrak S_1}(1).
$$

这里是迹范数，不是动能加权迹范数。它把有限模态近似后的结论，提升为模型本身的无限相干模态结论。无限总质量和任意无穷占据谱的爆破解构造不在证明范围内。完整推导与独立核查见 [hilbert-extension.md](../scale-and-phase/hilbert-extension.md)、[hilbert-details.md](../scale-and-phase/hilbert-details.md)。

### 8. 辐射与核心的精确关系

本轮还从共形恒等式得到全局非散射分支的精确能量关系

$$
E(U)=\frac{M_c|v|^2}{8}+\frac12\|\nabla F\|_2^2.
$$

动量、质心、伸缩量及二维角动量也有相应精确分解。证明没有把能量连续性错误地用于梯度可能无界的核心。

一维终端背景的共同零点转化为自由辐射的频谱零点：

$$
\widehat F_j(v/2)=0.
$$

本方程自由波的群速度是 $2\xi$，所以这恰是与核心同速的辐射频率。该结论来自动力学与正交性，不是额外施加在初态上的频谱假设。推导见 [foundation-check.md](../scale-and-phase/foundation-check.md)。

### 9. 前人工作、归属和下一处实质缺口

已核对的原始文献包括：

* Hong–Kwon–Yoon 的无限共同密度三维三次系统及占据谱动力学：<https://arxiv.org/pdf/1712.06811>。无限模态、密度算子和占据谱方法本身已有明确先驱。
* Banica–Carles–Duyckaerts 的带势临界爆破解构造：<https://arxiv.org/pdf/0904.1317>。其主要定理是构造性结果，文中明确未处理分类。
* Matsui 的较弱势假设下的临界爆破解构造：<https://arxiv.org/html/2007.15968v4>、<https://arxiv.org/html/2108.06205v2>。
* Read–Schulz 的一维锐 Lieb–Thirring 不等式：<https://arxiv.org/html/2609.10478v2>。

本轮项目内推进在于相位误差的抵消、曲率控制到完整尺度渐近的证明、以及无限模态所需联合紧性与输运论证。检索和内部复核尚不能替代全面的历史优先权核查。

最直接的后续难点，是从原有次模态 $H^1$ 控制出发，证明足够的背景曲率或找到可以替代它的局部估计，进而消除附加正则性条件。这比继续给结论增加模型名称更接近完整的动力学分类。其他未解决项仍包括二维等占据锐常数、无有限方差的全部次阈值散射，以及最初的非径向 BNLS 负能量爆破命题。

### 10. 文件索引

| 文件 | 内容 |
| --- | --- |
| [scale-dynamics.md](../scale-and-phase/scale-dynamics.md) | 粗糙背景下明确归一化的相位与可微参数 |
| [regular-background.md](../scale-and-phase/regular-background.md) | 曲率控制下的尺度、驻波相位和正则背景能量系数 |
| [potential-details.md](../scale-and-phase/potential-details.md) | 独立推导、符号核查、尺度转换和适用范围 |
| [hilbert-extension.md](../scale-and-phase/hilbert-extension.md) | 无限模态局部理论、联合紧性、单核心及辐射 |
| [hilbert-details.md](../scale-and-phase/hilbert-details.md) | 无限维推广的独立核查 |
| [foundation-check.md](../scale-and-phase/foundation-check.md) | R17 结构复核、精确守恒量分解、相位推导复核 |
| [literature.md](../scale-and-phase/literature.md) | 外部文献与模型逐项对应 |

归档保留 R15–R17 的全部依赖；旧阶段文件没有被改写。R18 的新结论、假设和范围以本文件及相应证明为准。
