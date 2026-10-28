# R30：二维锐正交 GN / Lieb–Thirring 主线证明记录

日期：2026-10-18。

## 目标与本轮结论

目标始终是对任意有限正交族证明

$$
T=\sum_j\|\nabla\phi_j\|_2^2\ge K_1\int\rho^2,
\qquad \rho=\sum_j|\phi_j|^2,\qquad K_1=M_c/2,
$$

其中 $M_c=\|Q_{\rm T}\|_2^2$，$-\Delta Q_{\rm T}+Q_{\rm T}-Q_{\rm T}^3=0$。这直接关系到临界聚焦向量 NLS 中由最大 Gram 特征值控制的预期质量阈值。

**本轮没有证明完整猜想，也没有改进无限制二维通用常数。** 本轮完成的是任意秩可积余项、物理密度转移、定量 action 约化，以及两个明确几何类别中的实际通道构造。下面各项均给出完整推导；它们没有被当作主猜想的替代品。

## 核心已证结果

令切片行 Gram 矩阵为 $\Gamma=WW^*$，$A(x)=\int_{-\infty}^x\Gamma$，$S=\int\operatorname{Tr}\Gamma^3$，$D_x=T_x-\pi^2S/4$。置

$$
\Theta=\frac\pi2(A-I/2),\quad X=\tan\Theta,
\quad R=\sec\Theta\,\Gamma\,\sec\Theta.
$$

1. **任意有限秩可积余项：**
   $$
   D_x\ge\frac{(4-\pi)^2}{2916}
   \int\frac{\|[X,R^{3/2}]\|_{\rm HS}^{4}}{\operatorname{Tr}R^3}\,dx.
   $$
   约定零分母处取零。常数不依赖秩；分母满足 $\operatorname{Tr}R^3\le8\operatorname{Tr}\Gamma^3$。证明处理了奇异矩阵与端点极限。正文使用字母 $Q$ 表示这里的 $R$，与 Townes 解 $Q_{\rm T}$ 无关。

2. **从算子误差到真实密度误差：** 若 $E=\int\|G-H\|_{\mathfrak S^3}^3$，$T_y^{\Sigma}=\int\operatorname{Tr}(-\partial_y^2)(G+H)$，则
   $$
   \|\sqrt{\rho_G}-\sqrt{\rho_H}\|_4
   \le(2/3)^{1/8}(ET_y^{\Sigma})^{1/8}.
   $$
   因而算子逼近确实可以传递到主不等式的二维密度项。

3. **实际构造，而非仅有等号分类：** 对固定正交横向通道，可构造归一化 sech 通道，误差为 $2048S^{1/4}D_x^{3/4}$。更进一步，对共同 Gram 形状 $\Gamma=a^2I_N$，允许横向框架随 $x$ 变化，仍可构造
   $$
   \gamma_0(x)=q_0(x)\sigma,\qquad
   0\le\sigma\le I,\quad\operatorname{Tr}\sigma=N,
   $$
   $$
   \int\|\gamma-\gamma_0\|_{\mathfrak S^3}^3
   \le16384S^{1/4}D_x^{3/4}.
   $$
   横向动能完全保持，纵向动能不增加。$\sigma$ 可以是无限秩迹类算子；构造所得是合法混合密度矩阵。没有把它误称为已经找到的正交纯态轨道族。

4. **一般框架的定量约化：** 对实框架，以 $\delta=D_x/T_x$ 表示小余项，变分选取保留子空间和尺度矩阵后，同时得到物理切片 $\mathfrak S^3$ 误差、总动能不超出原值加 $O(\delta^{1/4})T$、以及 action 的一阶、代数和对易子残差控制。此项仍需后续结构构造，不能直接调用第 3 项的额外假设。

## 主证明尚缺什么

一般矩阵路径中，不同轨道的尺度、中心与横向子空间会同时变化。现有证明没有从任意秩余项统一构造出保持所需动能和密度精度的空间通道块；共同 Gram 形状的构造还不能覆盖这一情形。

还有一个独立的、不能忽略的数值范围问题。设 $K_0=\sqrt3\pi$，候选反例满足 $T/F=K_1/(1+\delta_v)$。那么

$$
\frac{T-K_0F}{T}=1-\frac{K_0}{K_1}(1+\delta_v)
\longrightarrow 1-\frac{K_0}{K_1}\approx0.06992
\quad(\delta_v\downarrow0).
$$

因此，越来越小的主猜想违例不会自动使切片余项趋零。即使补全渐近稳定性，也还必须获得覆盖这一有限缺口的定量估计，或找到另一条直接排除优化子的论证。本轮没有完成这一步。

## 文件与依赖

| 文件 | 已证内容与适用范围 |
|---|---|
| [all-rank-stein-remainder.md](all-rank-stein-remainder.md) | 任意秩可积余项、近似 Riccati 估计、标量与固定框架构造、共同 Gram 形状的混合态构造 |
| [density-transfer.md](density-transfer.md) | 切片 Schatten 误差到二维物理密度误差 |
| [pruning-action.md](pruning-action.md) | 实框架的正性修剪、定量 action 约化和总动能控制 |
| [local-scale-mixing.md](local-scale-mixing.md) | 对数矩阵场的逐轨道尺度混合约束 |
| [centered-block-remainder.md](centered-block-remainder.md) | 中心化 Gaussian 二阶混沌给出的正块余项；明确限于 $\alpha<\pi$ |
| [optimizer-regularity.md](optimizer-regularity.md) | 实际自洽优化子的正则性和谱尺度估计；说明其对主证明的实际限制 |

本轮主要外部输入为 Read–Schulz 的一维等式及 Lemma 6，以及已有矩阵 action 定理：

- Larry Read and Marvin R. Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478, §2.2：<https://arxiv.org/html/2609.10478>。
- OpenAI, *Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials*, 2026-10-05，尤其 §§3–6：<https://www.emergentmind.com/openai-math-explorer/papers/526.pdf?v=adc7f12>。

包内没有用数值扫描替代任何证明。
