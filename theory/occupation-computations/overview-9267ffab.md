# 临界聚焦色散系统的阈值、相干结构与动力学

## R16：多模态精确阈值、临界塌缩构造与相干核心

2026-10-09。本记录汇总本轮实际完成的推导及项目内独立复核。它承接 R15；`README_R15.后两项尚未完成。

### 1. 模型与本轮的核心进展

研究二维共同密度聚焦系统

$$
i\partial_tu_j=-\Delta u_j-\rho u_j,
\qquad \rho=\sum_{j=1}^k|u_j|^2,
\qquad U=(u_1,\ldots,u_k).
$$

这里各分量具有相同色散系数和同一个由总密度产生的非线性势。有限分量演化采用标准局部 $H^1$ 适定性及质量、Gram 矩阵、能量守恒。$t$ 在光学解释中对应归一化传播坐标。结论不要求初态径向，不要求初态接近预先给定的基态波形。

记

$$
\Gamma=\int UU^*dx,
\quad M=\operatorname{Tr}\Gamma,
\quad p_1\ge p_2\ge\cdots\ge0,
\quad \sum_jp_j=1,
$$

其中 $Mp_j$ 是守恒 Gram 矩阵的本征值。令 $Q>0$ 为二维 Townes 基态，

$$
-\Delta Q+Q-Q^3=0,
\qquad M_c=\int Q^2,
\qquad C_1=2/M_c.
$$

**本轮的主要推广：存在与模态数无关的 $\varepsilon_0>0$，只要 $p_2/p_1\le\varepsilon_0$，固定占据谱的精确塌缩阈值为**

$$
\boxed{M_*(p)=M_c/p_1.}
$$

R15 要求全部次模态的总占据相对主模态很小；R16 只要求其中每个次模态相对主模态很小。次模态的总功率可以任意大，有限模态数可以任意大。因而本轮结论已经覆盖远离纯态的多模态谱。

例如，固定 $0<\varepsilon\le\varepsilon_0$，取

$$
p=\frac{(1,\varepsilon,\ldots,\varepsilon)}{1+N\varepsilon}.
$$

随着次模态数 $N$ 增加，$p_1\to0$，而

$$
M_*(p)=M_c(1+N\varepsilon).
$$

这是对指定共同密度模型的结论，不直接外推至具有不同交叉相位系数、饱和项、耗散项或不同色散算子的介质。

### 2. 阈值的严格含义：两侧及等号都已有结论

对每个满足上述条件的有限占据谱：

| 总质量 | 已证明的动力学陈述 |
| --- | --- |
| $M<M_*(p)$ | 全部具有该占据谱的 $H^1$ 初态产生全局解，梯度范数保持有界。 |
| $M=M_*(p)$ | 存在具有该精确占据谱的有限时间爆破解；也存在同一占据谱的前向全局有界解。 |
| $M>M_*(p)$ | 存在具有该精确占据谱的光滑紧支撑负能量初态，产生有限时间爆破。 |

这里的阈值划定了“所有初态都不会塌缩”的范围。处于阈值上或超过阈值，不能只凭总功率决定一个具体初态的最终行为。

严格下侧由精确动能不等式及能量守恒得到；严格上侧由保持精确 Gram 矩阵的近极值构造、光滑紧支撑逼近和方差恒等式得到。等号处的存在性在本轮补齐，详见第 4 节。

### 3. 支撑推广的数学结构与全局能量余项

在固定的 Gram 本征基中，将占据归一化为 $n_1=1$、$n_j=p_j/p_1$，令 $\phi_j$ 正交归一。新的推导利用整个正交族：

$$
\sum_{j\ge2}n_j|\langle\eta,\phi_j\rangle|^2
\le \varepsilon\|\eta\|_2^2,
\qquad \varepsilon=\max_{j\ge2}n_j.
$$

结合 Fourier 截断直接证明的次模态密度估计

$$
\int S^2\le\frac{3\varepsilon}{2\pi}B,
\quad S=\sum_{j\ge2}n_j|\phi_j|^2,
\quad B=\sum_{j\ge2}n_j\|\nabla\phi_j\|_2^2,
$$

以及标量 GN 稳定性和 Townes 齐次谱估计，得到全局余项。若 $\|\nabla\phi_1\|_2=1$，记 $\delta=C_1-\|\phi_1\|_4^4$，则对所有合格正交族均有

$$
\boxed{
C_1(1+B)-\int(|\phi_1|^2+S)^2
\ge\frac12\delta+\frac{C_1}{32}B.
}
$$

不需要预先假设接近极值。证明通过假定该余项失效，强迫主模态进入标量稳定性邻域，再推出矛盾。这是把局部谱信息转为全局多模态结论的关键步骤。

在临界质量 $Mp_1=M_c$ 上，定义

$$
E(U)=\frac12\sum_j\|\nabla u_j\|_2^2-\frac14\int\rho^2,
\quad E_1=\frac12\|\nabla u_1\|_2^2-\frac14\int|u_1|^4.
$$

上式化为

$$
\boxed{E(U)\ge\tfrac12E_1+\tfrac1{64}\sum_{j\ge2}\|\nabla u_j\|_2^2.}
$$

由于 $E_1\ge0$，整个存在区间内都满足

$$
\sum_{j\ge2}\|\nabla u_j(t)\|_2^2\le64E(U(0)).
$$

因此，临界塌缩中所有发散的动能只能来自主本征模态；全部次模态的总动能保持有界，即便它们的总功率很大。

动能不等式及其全局余项也适用于有限动能的正迹类无穷秩算子。无穷分量的动力学结论还需要相应解的适定性与守恒定理；本记录完整的动力学陈述限于任意有限分量数。

### 4. 等号处：保持精确占据谱的真实爆破与全局解

本轮逐项验证了 Bourgain–Wang 构造在该向量系统中的延伸。任取有限个 $m_2,\ldots,m_k\ge0$，可构造精确解，保持

$$
\Gamma=\operatorname{diag}(M_c,m_2,\ldots,m_k),
$$

并在 $t\uparrow0$ 时满足

$$
U(t)=S(t)e_1+Z(t)+O_{H^1}(|t|^5),
\qquad \|\nabla U(t)\|_2\sim\frac{\sqrt{M_c}}{|t|}.
$$

这里 $S$ 是伪共形 Townes 核，$Z$ 是穿过 $t=0$ 的光滑向量解，且 $Z_1=0$。所有负时间截面的解光滑且有有限方差。次模态质量无须小；较大的尾部只改变构造所需的时间区间。

证明使用经典的标量线性化流定理；新增横向分量是自伴 $L_-=-\Delta+1-Q^2$ 流。对增长子空间必须使用局域化的非线性估计，而不是把粗略的全空间估计直接乘上三次时间增长。独立复核修正了实线性传播子中 $i$ 的位置，并补齐伪共形变换所需的高阶矩控制。

经伪共形变换，同一构造还给出前向全局解：主分量在 $H^1$ 中趋近 $e^{is}Q$，其余分量分别趋近自由波 $e^{is\Delta}f_j$。它保持同一个精确 Gram 矩阵。

取 $m_j=M_cp_j/p_1$，便得到第 2 节的等号处两类解。构造本身适用于任意有限占据谱；在已证明的占据比范围之外，它仅给出 $M_c/p_1$ 处的爆破实例，不能据此断言那就是最小爆破质量。

### 5. 每一个临界爆破解的相干核心与固定背景

本节的普遍结论适用于 $p_2/p_1\le\varepsilon_0$、$M=M_*(p)$ 下的所有有限时间 $H^1$ 爆破解，不要求径向性或有限方差。

设爆破时间为 $T$。存在唯一集中点 $x_*$、单位主本征向量 $c$、尺度 $\lambda(t)\to0$、相位 $\theta(t)$，以及固定背景 $W\in(H^1)^k$，使全部趋近 $T$ 的时刻满足

$$
U(t,x)=c\,e^{i\theta(t)}\lambda(t)^{-1}
Q\!\left(\frac{x-x(t)}{\lambda(t)}\right)+W(x)+R(t,x),
$$

$$
\|R(t)\|_{H^\sigma}\to0\quad(0\le\sigma<1),
\qquad \sup_{t\text{ 近 }T}\|R(t)\|_{H^1}<\infty,
$$

$$
c^*W=0,\qquad \int WW^*dx=\Gamma-M_ccc^*.
$$

这是完整时间趋近中的分解，不只是选择某个时间子序列。其物理内容是：局部塌缩核完全相干，集中质量恰为一个 Townes 质量；其余占据谱完整地保留在有限动能背景中。总密度满足

$$
\rho(t,x)dx\rightharpoonup M_c\delta_{x_*}+|W(x)|^2dx.
$$

进一步有

$$
\lambda(t)\le C(T-t),\quad |x(t)-x_*|\le C(T-t),
\quad \|\nabla u_1(t)\|_2\ge\frac{c_0}{T-t}.
$$

证明由保持完整 Gram 矩阵的共同空间相位变换得到流量估计，再控制密度之间的二次运输代价。截断代价和有界 Lipschitz 对偶允许初态的单独二阶矩无限。这里的速度是单侧界；尚未证明所有解都满足 $\lambda(t)\sim a(T-t)$，也未证明全部背景强 $H^1$ 收敛。

### 6. 量子谱方面的直接推论

对 $V\ge0$、$V\in L^2(\mathbb R^2)$，令 $e_1\ge e_2\ge\cdots\ge0$ 是 $-\Delta-V$ 负本征值的绝对值。新的全局占据不等式通过经典谱对偶给出

$$
\boxed{e_1(V)+\varepsilon_0\sum_{j\ge2}e_j(V)
\le\frac1{2M_c}\int V^2.}
$$

它把全部激发束缚态的结合能之和，控制在最优单态估计留下的余量内。系数为 $\varepsilon_0$，不是 1；因此这还不是完整的二维 Lieb–Thirring 最优常数结论。

本轮另用倾斜 Yukawa 核的精确 $L^2$ 积分，排除了正交化双 Townes 试探族中远分离、极端尺度比等逃逸参数区间。等占据双模态的一般问题仍未完成，不能将试探族排除结果当作全空间证明。

### 7. 已定量的常数与仍待推进的事项

由 R15 已保存并审核的区间证书，本轮严格提取出

$$
Q(r)^2\le\frac{81}{16(1+r^2)^2},
\qquad
\int Q^2|v|^2\le\frac{128}{175}\int|\nabla v|^2
\quad(v\perp Q).
$$

因此齐次谱间隙可取 $47/175$。这是有理数比较和球面均值消去的推论，不是重新拟合谱数据。

占据比范围则为

$$
\varepsilon_0=\min\left\{\frac1{96},\frac{\delta_0}{8C_1},
\frac{28}{6795C_1K}\right\}>0,
$$

其中 $K,\delta_0$ 是 R15 附录完整证明其存在的标量 GN 稳定性常数，尚未数值认证。因而目前不能为实验指定某个已保证有效的占据百分比。

重要的后续数学问题是：扩展至 $p_2=p_1$ 的等占据端点；确定最优占据范围；分类一般临界解的精确尺度和相位演化。工程应用还需把归一化参数转换为具体材料与光束参数，并研究有限孔径、耗散、饱和等物理修正。原始四阶 BNLS 的一般非径向负能量爆破命题仍需要独立证明，本记录的二阶多分量结论不解决它。

### 8. 与前人工作的联系及研究状态

共同密度模型可表达若干部分相干、多模态自聚焦情形。相干性改变临界功率的物理问题已有长期研究，例如 Bang、Edmundson、Krolikowski（1999）。本轮研究针对守恒占据谱，给出所述数学模型中的精确阈值和临界结构；未进行新的实验或器件验证。

使用的经典基础包括标量 sharp GN 与 Townes 理论、线性化算子非退化性、占据数与 Lieb–Thirring 谱对偶、Bourgain–Wang 爆破构造及临界质量中的相位流量思想。本轮具体增加的是：不限制次模态总占据的精确区间、全局能量余项、精确 Gram 约束的临界构造、无方差假设的完整时间核心—背景分解及单侧速率界。它们在本项目内经过独立数学复核；没有将其标为已经确认历史首创或已经解决某个完整著名猜想。

主要原始文献：

1. Bourgain–Wang (1997), *Construction of blowup solutions for the nonlinear Schrödinger equation with critical nonlinearity*. 本轮逐项核对 Proposition 2.8：<https://www.numdam.org/item/ASNSP_1997_4_25_1-2_197_0.pdf>。
2. Chang–Gustafson–Nakanishi–Tsai (2007), *Spectra of Linearized Operators for NLS Solitary Waves*, DOI <https://doi.org/10.1137/050648389>。R15 标量稳定性使用其线性非退化事实。
3. Dolbeault–Felmer–Loss–Paturel (2006), *Lieb–Thirring type inequalities and Gagliardo–Nirenberg inequalities for systems*, DOI <https://doi.org/10.1016/j.jfa.2005.11.008>。
4. Frank–Gontier–Lewin (2021), *The Nonlinear Schrödinger Equation for Orthonormal Functions II*, DOI <https://doi.org/10.1007/s00220-021-04039-5>。该文相关秩一非最优性结果的严格指数范围不包含这里的二维端点。
5. Banica (2004), *Remarks on the blow-up for the Schrödinger equation with critical mass on a plane domain*, <https://numdam.org/item/ASNSP_2004_5_3_1_139_0/>。标量临界质量的相位流量与速率方法是既有基础。
6. Bang–Edmundson–Krolikowski (1999), *Collapse of Incoherent Light Beams in Inertial Bulk Kerr Media*, DOI <https://doi.org/10.1103/PhysRevLett.83.5479>。

### 9. 证明文件与复算

| 文件 | 内容 |
| --- | --- |
| [occupation-gap.md](../occupation-thresholds/occupation-gap.md) | 完整占据推广、全局余项、无穷秩变分延伸及谱推论。 |
| [occupation-gap-details.md](../occupation-thresholds/occupation-gap-details.md) | 上述证明和常数的独立核查。 |
| [endpoint-construction.md](../occupation-thresholds/endpoint-construction.md) | 临界爆破与同谱前向全局解的详细构造。 |
| [endpoint-details.md](../occupation-thresholds/endpoint-details.md) | 原论文输入、实线性传播、矩估计及精确 Gram 的独立核查。 |
| [threshold-rigidity.md](../occupation-thresholds/threshold-rigidity.md) | 所有合格临界爆破解的结构、背景极限和速率界。 |
| [dynamics-details.md](../occupation-thresholds/dynamics-details.md) | 全时间分解、运输代价及无方差步骤的独立核查。 |
| [quantitative-gap.md](../occupation-thresholds/quantitative-gap.md) / `.py` | 显式齐次谱间隙与有理数复算。 |
| [dual-search.md](../occupation-thresholds/dual-search.md) | 双 Townes 试探族的参数逃逸区域排除。 |
| [rank2-global.md](../occupation-thresholds/rank2-global.md) | 等占据问题的剩余结构及受限角向族排除。 |
| [imbalanced.md](../occupation-thresholds/imbalanced.md) | 继承的标量 GN 稳定性完整附录。 |
| [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py) / [spectral-details.md](../occupation-thresholds/spectral-details.md) | Townes 包络区间计算及解析连接。 |

在解压目录运行：

```bash
python3 research/r16_quantitative_gap.py
```

它读取保存的 R15 证书，用精确有理数检查本轮包络和间隙；输出 `passed: true`。如需从头复算原区间 ODE 证书：

```bash
python3 research/r15_validated_townes.py --certificate
```

两份脚本仅使用 Python 标准库。原区间积分依赖 IEEE-754 binary64 与逐运算向外舍入，具体假设在 R15 区间算法说明中说明；有理数检查本身不独立替代该 ODE 证书。探索性浮点数值文件保留为历史记录，未作为严格证明的替代。

`MANIFEST_R16_SHA256.json` 记录本包其余文件的哈希；R15 的旧清单保留为历史记录。本轮未对旧探索性数值重复运行无关测试。
