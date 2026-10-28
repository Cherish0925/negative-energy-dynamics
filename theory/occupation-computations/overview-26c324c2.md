# 临界聚焦色散系统的阈值、相干结构与动力学

## R17：临界解的长期分解、核心运动与一维推广

### 1. 本轮最主要的结果

对 R16 的二维共同密度聚焦系统

$$
i\partial_tu_j=-\Delta u_j-\rho u_j,
\qquad \rho=\sum_j|u_j|^2,
$$

现在可以描述有限方差初态在无限时间上的行为。记

$$
\Sigma=\{U\in(H^1)^k:\ |x|U\in L^2\},
\quad \Gamma=\int UU^*dx,
\quad M=\operatorname{Tr}\Gamma,
$$

并令 $p_1\ge p_2\ge\cdots$ 为 $\Gamma/M$ 的本征值。二维仍采用 R16 的条件 $p_2/p_1\le\varepsilon_0$，不限制次模态总占据或任意有限的模态数。其精确阈值为 $M_*=M_c/p_1$。

**阈值以下，有限方差解最终完全散射；阈值上的前向全局有限方差解，则有两个穷尽的可能：完全散射，或一个缩放基态核心加自由辐射。**

在第二种情形中，存在单位主本征向量 $c$、自由态 $F\in(H^1)^k$、固定向量 $v,x_0$、尺度 $0<\ell(t)\le C$、相位 $\theta(t)$，以及 $X(t)=vt+x_0+o(1)$，使沿全部 $t\to\infty$ 时刻都有

$$
\boxed{
U(t,x)=c\,e^{i\theta(t)+iv\cdot x/2}\ell(t)^{-1}
Q\!\left(\frac{x-X(t)}{\ell(t)}\right)
+e^{it\Delta}F(x)+R(t,x),
\qquad \|R(t)\|_{H^1}\to0.
}
$$

其中

$$
c^*F=0,\qquad
\int FF^*dx=\Gamma-M_ccc^*,\qquad
v=\frac2{M_c}\bigl(P(U)-P(F)\bigr),
$$

$P(f)=\operatorname{Im}\int\bar f\nabla f$，向量场的动量按分量求和。

这给出完整时间上的强 $H^1$ 分解，且核心运动的速度和位移常数已经确定。**尚未证明 $\ell(t)$ 收敛到正数，也未确定 $\theta(t)$ 的完整渐近规律。** 因而不能把它描述成“所有临界解最后变成一个固定尺度的精确行波”。允许宽度趋零的可能性仍是后续核心问题。

### 2. 有限时间爆破：整个主模态必须以受限速度收缩

R16 已证明在临界质量 $Mp_1=M_c$ 上，全寿命内成立

$$
0\le E_1(t)\le2E,
\qquad \sum_{j\ge2}\|\nabla u_j(t)\|_2^2\le64E.
$$

这里采用固定 Gram 本征基，$E_1$ 是主模态的标量临界能量，$E$ 是守恒的全系统能量。

本轮对主模态单独施加空间相位。因为它的质量恰为 $M_c$，标量 sharp GN 保证这种相位改变后的**标量**能量仍非负，得到

$$
\left|\int J_1\cdot\nabla\vartheta\right|^2
\le2E_1(t)\int |u_1|^2|\nabla\vartheta|^2.
$$

这一步不需要单独改变主模态相位时保持全系统 Gram 矩阵：使用的是标量能量的非负性，而不是全系统固定谱的能量非负性。结合主模态自身的连续性方程，得到其密度的二次运输距离界。

若在 $T$ 有有限时间爆破，R16 已识别唯一集中点 $x_*$。运输到点质量的代价恰好等于整个主模态的方差，因此

$$
\boxed{
I_1(t):=\int|x-x_*|^2|u_1(t,x)|^2dx
\le\left(\int_t^T\sqrt{8E_1(s)}\,ds\right)^2
\le16E(T-t)^2.
}
$$

没有预先假设初态有限方差。于是得到两个直接结论：

* 所有合格的有限时间临界爆破解，其整个主模态自动具有有限方差，并有 $\|\nabla u_1(t)\|_2\ge M_c/[4\sqrt E(T-t)]$。
* 若临界初态的主 Gram 本征模态具有无限方差，则解在正、负两个时间方向均全局存在。这里不声称梯度范数在无限时间上一致有界。

第二类初态非空。二维可以取归一化主模态 $u_1=\sqrt{M_c/(2\pi)}(1+|x|^2)^{-3/4}$，再选择与之精确正交的环状角向次模态，实现任意允许的有限占据谱。

### 3. 核心位置、动量与角动量的精确关系

设有限时间爆破的背景为 $W$，在 Gram 本征基中其第一分量为零。次模态的强 $H^{1/2}$ 收敛使其动量有极限。由总动量守恒，主模态动量趋于

$$
P_*=P(U)-P(W).
$$

利用新增的全主模态方差界，质心和定量基态逼近中的中心只相差 $O((T-t)^2)$。因此

$$
\boxed{x_c(t)=x_*-\frac{2P_*}{M_c}(T-t)+o(T-t).}
$$

这是位置的一阶渐近式，不额外宣称任意选取的调制中心可微。若次模态有有限方差，总角动量还满足

$$
L(U)=x_*\times P_*+L(W),
\qquad L_{x_*}(u_1(t))\to0.
$$

即关于塌缩点的角动量留在规则背景中；核心关于该点的内禀角动量趋零。这里必须保留有限方差条件，以保证所有角动量量有定义。

### 4. 为什么现在能得到完整时间的强分解

首先，次模态的有界动能与其自身连续性方程控制其密度运输速度。若它有有限方差，终态不仅是强 $L^2$ 极限，也是强加权 $L^2$ 极限。这处理了空间尾部，而不只处理局部密度。

其次，用伪共形对称把无限时间变换为有限时间端点。对次模态，空间权重恰好转化为变换后的梯度控制，因此全部次模态在原来的无限时间方向上强 $H^1$ 散射为自由波。

对主模态，R16 的误差具有 $L^2$ 范数 $O(\lambda)$ 和有界梯度；本轮又得到其位置加权范数为 $O(T-t)$。这些估计结合后，使共形像到缩放基态族的**绝对 $H^1$ 距离为 $O(1/t)$**，即便共形后的核心宽度趋零仍成立。移除二次相位时，把相位锚定在核心中心，避免了错误地产生一个无法控制的宽度倒数。

最后，变换后的有限端点要么能延拓，要么爆破。可延拓对应原解完全散射；爆破对应第 1 节的一个核心加自由辐射。此步骤没有借用一般孤子分解猜想。

二维阈值以下的有限方差散射还具有定量尾部：

$$
\|U(t)-e^{it\Delta}U_+\|_2=O(t^{-3/4}),
\quad
\|U(t)-e^{it\Delta}U_+\|_{H^1}=O(t^{-1/2}).
$$

在相互作用表象中实际有 $e^{-it\Delta}U(t)\to U_+$ 于 $\Sigma$；这里的两条显式速率仅针对未加权范数。去掉初始有限方差后的全部 $H^1$ 散射尚未完成。

### 5. 真正跨到另一个临界模型：一维五次系统

本轮研究了

$$
i\partial_tu_j=-\partial_x^2u_j-\rho^2u_j,
\qquad Q(x)=3^{1/4}\sqrt{\operatorname{sech}(2x)},
\qquad M_c=\frac{\pi\sqrt3}{2}.
$$

文献核对发现 Read–Schulz 的 2026 年 9 月 14 日预印本已给出一维完整锐 Lieb–Thirring 不等式。由该外部定理可推出所有有限占据谱的精确阈值 $M_*=M_c/p_1$。**这部分须归属于他们的锐不等式及其应用，不能算作我们解决了一维 Lieb–Thirring 猜想。**

本轮补充的推导是：先从显式基态和 Legendre 谱得到

$$
\langle f,(-\partial_x^2-Q^4)f\rangle
\ge\frac{10}{21}\|f'\|_2^2,\qquad f\perp Q,
$$

再建立带次模态动能正余项的不等式。利用密度幂关于占据数的凸性，余项可以从小占据区间传播到**每一个严格分离的最大占据谱 $p_2<p_1$**。无需主模态占绝大多数功率。

在临界质量处，得到

$$
E(U)\ge a_\varepsilon E_1(u_1)+b_\varepsilon A_{\rm sec},
\qquad a_\varepsilon,b_\varepsilon>0,
\quad \varepsilon=p_2/p_1<1.
$$

因此同样能识别全部有限时间爆破解的单个主模态核心，并证明自动主模态有限方差、无限方差主模态的双向全局存在，以及唯一规则背景。此处的次模态时间极限使用独立的一维论证：在爆破点之外测试方程，再利用一维 $H^1$ 连续性、紧性和运输尾部控制；没有错误套用二维的全空间非线性估计。

一维还有一个明确的空间结构：全部背景分量在爆破点为零，$W(x_*)=0$。有限方差时，同样得到强 $H^1$ 共形辐射，以及前向全局解的一个缩放基态核心加自由波的分解；具体声明见 [quintic-dynamics.md](../critical-core/quintic-dynamics.md)。

这一推广的范围对照如下：

| 模型 | 临界核心及长期分解所用占据条件 | 锐常数的输入 |
| --- | --- | --- |
| 二维三次共同密度系统 | $p_2/p_1\le\varepsilon_0$ | R16 的区间证书、齐次谱估计和非线性证明 |
| 一维五次共同密度系统 | $p_2<p_1$ | Read–Schulz 2026 锐不等式，加本轮正余项推导 |

两行的无限时间强分解均针对前向全局、有限方差、精确临界质量的有限分量解。核心尺度的正极限和精确相位律仍未证明。外部一维输入目前以预印本形式存在；其使用与本项目推导分别记录。

### 6. 二维最优常数问题：本轮排除了什么

二维等占据双态的具体目标仍是

$$
\int(|\phi_1|^2+|\phi_2|^2)^2
\stackrel{?}{\le}\frac2{M_c}
(\|\nabla\phi_1\|_2^2+\|\nabla\phi_2\|_2^2)
$$

对任意正交归一函数对成立。它对应二维、谱矩指数一的最优 Lieb–Thirring 问题的秩二部分。

R16 已排除双 Townes 试探族的远分离和极端尺度比。本轮将两份波包趋于重合时的所有尺度和平移切向方向，精确化为三个四次多项式系数；408 个完整区间积分管和解析无穷尾界证明三个系数严格为负。由此得到所有切向方向的一致商间隙 $1/105$，以及整个近重合穿孔邻域的间隙 $1/210$。该计算已由另一分支独立执行并复核。

因此，这一试探族的潜在反例被限制在真正非退化的紧参数集内。**尚未排除这个剩余紧集，更没有排除任意正交函数对。** 不能将试探族的边界排除称为解决完整秩二问题。

### 7. 文献关系与尚未闭合的部分

本轮找到一个更短的二维谱证明：Carlen–Frank–Lieb（2014）的最低本征值稳定性，加上 R16 的齐次谱估计，通过余维一压缩和普通 Lieb–Thirring 不等式，推出

$$
e_1(V)+\varepsilon\sum_{j\ge2}e_j(V)
\le\frac1{2M_c}\int V^2.
$$

这个证明加强了与前人理论的联系，也明确说明标量稳定性不是本项目的新发明。新的项目内推导涉及上述输入的结合、全局动能余项，以及由它得到的固定占据谱动力学。其组合是否已有完全相同的发表版本仍待更广泛核查。

本轮未解决的核心问题是：二维等占据锐常数；临界核心尺度与相位的完整渐近律；无有限方差假设的全部次阈值散射；最初提出的四阶 BNLS 一般非径向负能量爆破命题。也没有证明一个覆盖所有维数的同一阈值公式：Frank–Gontier–Lewin 的结果说明，在更高维的相应指数下，单态常数确实会失去最优性。

从物理上，本轮推进的是指定模型中多模态自聚焦的最终形态、塌缩质量、规则辐射及动量分配。没有新的实验或器件性能验证。占据数谱、相干性与塌缩的联系有既有理论基础，不能把这一物理联系本身称为首次发现。

### 8. 阅读、复算与来源

| 文件 | 作用 |
| --- | --- |
| [independent-foundation.md](../critical-core/independent-foundation.md) | 二维定量背景极限、次阈值散射、临界全局解的强分解完整证明 |
| [critical-rate.md](../critical-core/critical-rate.md) | 主模态自动方差、临界全局初态族、加权背景与共形辐射 |
| [primary-variance-details.md](../critical-core/primary-variance-details.md) | 单模态相位与无方差运输步骤独立复核 |
| [momentum-details.md](../critical-core/momentum-details.md) | 本轮核心速度和角动量分配的完整推导及复核 |
| [global-dynamics-details.md](../critical-core/global-dynamics-details.md) | 无限时间强分解及共形变换独立复核 |
| [variational-extension.md](../critical-core/variational-extension.md) / `_audit.md` | 一维显式齐次谱隙、正余项及全部严格占据间隙推广 |
| [quintic-dynamics.md](../critical-core/quintic-dynamics.md) / `_audit.md` | 一维核心、节点背景和动力学推广及复核 |
| [rank2-endpoint.md](../critical-core/rank2-endpoint.md) | 二维重合双 Townes 族的全方向排除 |
| [r17_tangent_certificate.py](../../computations/occupation-computations/r17_tangent_certificate.py) / `.json` | 完整区间积分和已保存证书 |
| [tangent-details.md](../critical-core/tangent-details.md) | 区间代码、解析尾部及参数邻域独立复核 |
| [literature-status.md](../critical-core/literature-status.md) | 原始文献对应、替代谱证明及准确归属 |

解压后可以运行：

```bash
python3 research/r17_tangent_certificate.py
```

其成功输出为 `certificate_passed: true`。原 Townes 射击证书可用 `python3 research/r15_validated_townes.py --certificate` 重新生成。本轮独立分支已运行两者并通过；这些是同一实现的独立执行与数学核查，不是两个独立编写的积分器。计算依赖 R15 文档声明的 binary64 向外舍入假设。

主要原始文献：

* Carlen–Frank–Lieb, *Stability estimates for the lowest eigenvalue of a Schrödinger operator*, GAFA 24 (2014), 63–84：<https://arxiv.org/html/1301.5032v2>。
* Read–Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478v2, 2026-09-14：<https://arxiv.org/html/2609.10478v2>。
* Frank–Gontier–Lewin, *The Nonlinear Schrödinger Equation for Orthonormal Functions II*, CMP 384 (2021)：<https://doi.org/10.1007/s00220-021-04039-5>。
* Bourgain–Wang, *Construction of blowup solutions for the nonlinear Schrödinger equation with critical nonlinearity* (1997)：<https://numdam.org/item/ASNSP_1997_4_25_1-2_197_0/>。

其余模型匹配、既有向量爆破工作和光学来源见文献核对文件及 R16。包内保留 R15、R16 全部依赖；旧 README 反映各自阶段状态，以本文件和 R17 证明为本轮更新。`MANIFEST_R17_SHA256.json` 给出归档文件的哈希清单。
