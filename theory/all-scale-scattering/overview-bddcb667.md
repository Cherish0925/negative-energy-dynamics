# 临界聚焦色散系统：基态谱结构、尺度分离与集体束缚

研究记录 R23，2026-10-15。

本轮完成了三个相互连接的解析推导：非显式径向基态的正伴随势恒等式、二维尺度悬殊双势阱的精确前两级谱展开、共同密度驻波的逐分量维里恒等式。它们服务于既定主线“临界聚焦色散系统的阈值、相干结构与动力学”。下文区分定理的适用范围与尚未解决的全局问题；不把独立推导自动等同于历史首创。

## 1. 当前主问题

二维共同密度系统为
$$
i\partial_tu_j+\Delta u_j+\rho u_j=0,
\qquad \rho=\sum_j|u_j|^2.
$$
设 Townes 基态满足
$$
-\Delta Q+Q-Q^3=0,
\quad M=\int_{\mathbb R^2}Q^2,
\quad q=Q/\sqrt M.
$$
任意有限正交族 $\langle\phi_i,\phi_j\rangle=\delta_{ij}$ 是否满足
$$
\int\left(\sum_j|\phi_j|^2\right)^2
\le\frac2M\sum_j\int|\nabla\phi_j|^2
\tag{G}
$$
仍是未完成的主目标。这等价于二维指数一 Lieb–Thirring 常数是否等于单态值 $1/(2M)$。本轮没有证明 (G)，也没有解决最初的非径向负能量 BNLS 爆破问题。

## 2. 基态方程直接给出谱结构

令 $p=Q'/Q$，在径向空间 $L^2(r\,dr)$ 中置
$$
A=\partial_r-p,\qquad h=-\Delta-Q^2.
$$
则 $A^*A=h_0+1$，而 $AA^*-1=-\partial_r^2-r^{-1}\partial_r+U$，其中
$$
\boxed{
U(r)=\frac1{rQ(r)^2}\int_r^\infty
\left(\frac{Q(s)^2}{s^2}+Q(s)^4\right)ds>0.
}
\tag{1}
$$
决定性的微分恒等式是
$$
(rQ^2U)'=-Q^2/r^2-Q^4.
$$
它只使用基态微分方程与无穷远衰减，不需要基态的闭式解或数值包络。

由正伴随势、物理径向定义域与零能方程，得到径向算子只有简单负本征值 $-1$，没有零能共振。再用角动量 Birman–Schwinger 迹界
$$
\operatorname{Tr}K_m(0)=\frac{M}{4\pi m}<1,\qquad m\ge1,
$$
完成二维全空间的排除。这里 $M<4\pi$ 由锐标量 GN 不等式与非最优高斯试探函数严格推出。因此
$$
\sigma(h)=\{-1\}\cup[0,\infty),\qquad
\langle f,hf\rangle\ge0\quad(f\perp Q),
\tag{2}
$$
且零能量没有本征态或有界共振。

这说明固定 Townes 自诱导势只能支持一个负能束缚模态。多个正交束缚模态若要共同存在，必须改变自洽密度；不能把额外负能模态直接放进不变的单核势中。

详细证明：[scattering-sign.md](../townes-spectral-structure/scattering-sign.md)、[partner-details.md](../townes-spectral-structure/partner-details.md)。

## 3. 推广到非纯幂次非线性

设二维或三维存在正的、递减的、光滑指数衰减径向剖面
$$
-\Delta Q+\omega Q-V(Q)Q=0,\quad \omega>0,
$$
其中 $V(0)=0$、$V\ge0$、$sV'(s)\ge2V(s)$。令 $a=d-1$、$p=Q'/Q$。对应伴随势满足
$$
\boxed{
(r^aQ^2U)'=r^aQ^2
\left[\frac{a(a-2)}{r^3}-\frac{aV(Q)}r
+p\bigl(QV'(Q)-2V(Q)\bigr)\right]\le0.
}
\tag{3}
$$
由此得到径向 $-\Delta-V(Q)$ 只有基态负能级 $-\omega$，并排除相应的径向阈值共振。纯幂次 $V(s)=s^\sigma$、$\sigma\ge2$ 是其中一类；定理以所述基态存在为前提，不额外声称任意维数、指数下都有基态。

这是对一类剖面的同一解析论证。它只涉及标量 $L_-$ 及其径向谱，不能转述成完整矩阵线性化或非线性动力学的稳定性定理。详细证明见 [general-partner.md](../townes-spectral-structure/general-partner.md)。

## 4. 尺度悬殊双核：包括同心构型

固定 $z\in\mathbb R^2$，令
$$
V_k(x)=Q(x)^2+k^2Q(kx-z)^2,\qquad k\downarrow0,
\quad H_k=-\Delta-V_k.
$$
上述单核谱结论使我们能够完整分离宽核的基态极点，并证明第二个负能级满足
$$
\boxed{
\lambda_2(H_k)=-k^2+
\frac{2\pi k^2q(z)^2}{|\log k|}
+O_z\!\left(\frac{k^2}{|\log k|^2}\right).
}
\tag{4}
$$
同时
$$
\lambda_1(H_k)=-1-k^2Q(z)^2+O_z(k^4).
$$
定义 $S_2=-\lambda_1-\lambda_2$，精确抵消直接交叉吸引项后得到
$$
\boxed{
S_2(H_k)-\frac1{2M}\int V_k^2
=-\frac{2\pi k^2q(z)^2}{|\log k|}
+O_z\!\left(\frac{k^2}{|\log k|^2}\right)<0.
}
\tag{5}
$$

该结果允许 $z=0$，即两个不同尺度的核完全同心。它处理此前固定尺度比、中心远离的展开没有覆盖的联合极限。证明包含压缩算子的严格正性、预解算子范数余项、极点处的精确消元，以及保证所求能级确为第二级的计数步骤。

主导系数 $2\pi$ 来自二维 Green 函数的对数奇性。相同第二能级展开也适用于满足明确谱假设的非 Townes 窄势阱和宽势阱，见 [hierarchical-wells.md](../townes-spectral-structure/hierarchical-wells.md) 第 7 节。对 Townes 势，(5) 还利用了其 Pohozaev 归一化；一般势不自动享有这个谱和与势代价的抵消。

一致性范围：$z$ 在固定紧集内；没有声称对 $z=z(k)\to\infty$ 一致，也没有声称对该势族的任意形变稳定。

## 5. 逐分量结构与非径向项

对于实值、光滑、指数衰减的二维径向驻波
$$
-\Delta u_i-\rho u_i=-e_i u_i,\qquad \rho=\sum_j u_j^2,
$$
非零分量频率互异时，证明每一个分量分别满足
$$
\boxed{
\int|\nabla u_i|^2=e_i\int u_i^2,
\qquad \int\rho u_i^2=2e_i\int u_i^2.
}
\tag{6}
$$
正交径向分量自动具有互异频率。证明使用 Wronskian 修正量；不是把总 Pohozaev 等式任意分摊给各分量。

去掉径向性后，等式的修正项可以精确写出。置
$J_{ij}=u_i\nabla u_j-u_j\nabla u_i$，则
$$
T_i-e_iM_i=
\sum_{j\ne i}\frac1{e_i-e_j}
\int(x_1J_{ij,2}-x_2J_{ij,1})\,\operatorname{curl}J_{ij}.
\tag{7}
$$
该角向项尚无所需的普遍符号控制。完整推导及相对平移的二阶形式见 [compact-states.md](../townes-spectral-structure/compact-states.md)。

## 6. 对主目标的准确影响

- R22 的单核谱次序假设现在已被证明，对所有固定 $0<k<1$ 自动成立。
- 原双核散射系数满足 $\mathcal A(k)=-2\pi/\log(1/k)+O(\log^{-2}(1/k))$，故小尺度比端的符号已明确；中间尺度区间尚未完成。
- 新的 (5) 排除了固定宽核坐标下的尺度悬殊双核族，包括同心核。
- 对假设存在的首个改善常数的秩，[global-bridge.md](../townes-spectral-structure/global-bridge.md) 给出任意占据子空间分裂的重叠下界及占据频率比限制。这些是已有下秩不等式的推论，没有单独解决全局集体束缚问题。
- 强重叠、同量级尺度、任意非径向自洽多模态结构仍是主问题的核心；(1)–(7) 尚不能排除它们或构造反例。

## 7. 与前人工作的关系

Darboux 一阶分解是经典方法，Chang–Gustafson–Nakanishi–Tsai 的 NLS 谱论文有明确应用。三维三次径向 $L_\pm$ 谱隙由 Costin–Huang–Schlag 严格证明；Li–Yang 后来完成相应的非径向标量谱结果。本轮没有“新解决”这些已有结论。这里整理的是正伴随势的直接积分表达、非线性推广及其对双尺度集体束缚的应用，历史首创性仍需进一步比对。

二维对数预解算子展开的背景包括 Jensen–Nenciu 的工作。谱计算本轮包含自己的压缩块和谱次序论证，并不把标准预解算子工具归为原创。

新检索到的 Chen–Guo–Luo–Wei 预印本（2026-10-13）研究一维任意分量三次系统的分类和邻近指数的存在性转变。其一维守恒量与本轮 Wronskian 修正量有关；它不解决这里的二维端点问题。我们核对了相关恒等式与论文范围，尚未独立复核该预印本全部证明。

主要原始文献链接及具体关系见各技术笔记末尾。

## 文件与复现

本包包括上述解析笔记、独立数学核对、符号验证脚本、径向搜索代码与原始浮点结果，以及作为背景的 R22 笔记。[r23_symbolic_identities.py](../../computations/all-scale-scattering/r23_symbolic_identities.py) 精确核对一般伴随势、径向 Wronskian、逐分量维里三条恒等式；其结果全部为零余项。定义域与谱结论由笔记中的解析证明承担。

径向 Galerkin 搜索未找到合格的紧致反例：六次运行都向窄核心加扩散模态发展，且第二乘子仍为正。数据没有被当成不存在定理。无需重跑这些实验即可阅读解析成果。

```bash
python3 research/r23_symbolic_identities.py
```

