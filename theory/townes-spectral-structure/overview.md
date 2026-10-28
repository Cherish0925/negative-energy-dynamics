# 临界聚焦中的正交代价与集体束缚：R22

## 问题及其物理内容

沿用二维共同密度聚焦系统的归一化。Townes 基态满足
$$
-\Delta Q+Q-Q^3=0,\qquad M=\int Q^2,
\qquad q=Q/\sqrt M,\qquad C_1=2/M.
$$
任意有限正交族的锐不等式是否为 $F\le C_1T$，仍是目标。物理上的竞争是密度重叠增强吸引与空间正交增加动能。这里直接计算这两种效应，尤其保留此前数值搜索不易分辨的指数小量。

## 1. 等尺度分离核：主导项的符号已经推导清楚

设 $q_i=q(\cdot-a_i)$，$P$ 为这些函数张成空间的正交投影，$R_{ij}=|a_i-a_j|$，$R=\min R_{ij}$。若 $q(r)\sim A r^{-1/2}e^{-r}$，则任意固定 $N$ 下，随 $R\to\infty$，
$$
C_1T(P)-F(P)
=\frac{16\pi A^4}{M}\sum_{i<j}e^{-2R_{ij}}[1+o_N(1)]>0.
$$
最初固定形状中心配置的展开在 [multicore.md](../separated-cores/multicore.md)；对任意最小距离趋于无穷的配置的统一性，见 [transverse-coercivity.md](../separated-cores/transverse-coercivity.md) 第 6.2 节。

证明不能只计算密度重叠：Gram 正交化产生的表面上更大项先精确抵消，然后留下正的主导项。直接吸引项仅为 $O(R_{ij}^{-1/2}e^{-2R_{ij}})$，不足以压过它。

对固定势 $V=\sum_iQ(\cdot-a_i)^2$，其精确前 $N$ 个负特征值和也不能突破单态常数。IMS 分解给出占据空间外的统一谱隙，Ritz 误差被控制在 $O_N(R^{-1}e^{-2R})$，低于主导相互作用。这个结论涉及前 $N$ 个特征值，不声称控制全部负谱。

## 2. 允许无限维小形变，但准确固定范围

令 $\Phi$ 是上述子空间的正交归一基，使用精确图表
$$
\Phi(\eta)=(\Phi+\eta)(I+\eta^*\eta)^{-1/2}.
$$
要求 $\Phi^*\eta=0$，并令各对角形变与相应核的平移、缩放方向正交。对该固定调制切片内任意充分小的实 $H^1$ 形变，证明
$$
C_1T(P(\eta))-F(P(\eta))
\ge c_N\sum_{i<j}e^{-2R_{ij}}>0.
$$

证明使用已知标量基态的谱非退化性，区分对角分量的 $L_+$ 和交叉分量的 $L_-$，再以 IMS 得到横向一致强制性。完整残差满足
$$
\|\text{normal residual}\|^2\le C_N\sum_{i<j}R_{ij}^{-1}e^{-2R_{ij}},
$$
故形变的最大改善低于正的主导亏损。详见 [transverse-coercivity.md](../separated-cores/transverse-coercivity.md)，包括非临界点的完整乘子矩阵与非线性余项。

该结论控制指定切片内无限维形状变化。它不是允许各核任意改变尺度的完整邻域定理，常数也不对 $N\to\infty$ 一致。

## 3. 不等尺度：完整响应化为一个单核散射量

置 $h=-\Delta-Q^2$。固定 $0<k<1$，并明确要求 $\lambda_2(h)>-k^2$，其中第二个负能级不存在时按零解释。研究
$$
V_R=Q^2+k^2Q^2(k(\cdot-Re_1)),\qquad
\epsilon_R=A\sqrt{k}\,R^{-1/2}e^{-kR}.
$$
在这个谱次序条件下，完整前两个负特征值和满足
$$
S_2(V_R)-\frac1{2M}\int V_R^2
=\epsilon_R^2\mathcal A(k)+o(\epsilon_R^2),
$$
$$
\mathcal A(k)=\int Q^2e^{2kx_1}
+\langle Q^2e^{kx_1},(h+k^2)^{-1}Q^2e^{kx_1}\rangle.
$$
注意这里 $A$ 是归一化 $q$ 的尾系数。两份独立推导分别见 [relaxed-unequal-wells.md](../separated-cores/relaxed-unequal-wells.md)（准模态）与 [unequal-potential.md](../separated-cores/unequal-potential.md)（Schur 补；采用未归一化尾系数，等价公式多一个 $1/M$）。两者的量纲和符号已对照。

必须保留完整预解算子的负基态方向：它正是局部宽核与窄核保持正交的贡献。只保留正补空间会错误地改变结合符号。不等尺度下，波形调整与原始相互作用同阶，不能视为小余项。

已解析证明 $k<1$ 充分接近 1 时 $\mathcal A(k)<0$。此外，实际角动量计算至 $m=40$ 得到：

| k | A(k)，浮点近似 |
|---:|---:|
| 0.10 | -2.8723616721 |
| 0.30 | -5.1109586391 |
| 0.50 | -8.4706010788 |
| 0.70 | -17.1605054973 |
| 0.85 | -43.3566559336 |
| 0.90 | -73.0791275967 |

这些离散计算未进行区间认证，不能证明全部 $k$ 的符号，也没有替代各 $k$ 的谱次序假设。脚本保留各通道系数与截断序列。对所有允许 $k$ 的解析符号仍未知于本轮推导。

## 4. 与前人工作及主目标的关系

Frank–Gontier–Lewin 的相关结合构造在二维要求 $\gamma>1$，相应非线性指数 $p<2$。其 Lemma 12 使用 $EB=o(A_{\rm overlap})$。在本轮 $p=2$ 端点，恰有 $EB\asymp e^{-2R}$、$A_{\rm overlap}\asymp R^{-1/2}e^{-2R}$，次序倒转。这解释了为何不能简单把已有结合证明取极限。

本轮没有证明前人错误，也没有宣布端点猜想已经解决。所得结论是指定分离构型的解析控制，以及不同尺度下可以继续研究的完整相互作用系数。全局问题仍包括强重叠核心、任意尺度结构及任意秩；上述局部结果没有覆盖它们。

主要原始文献：

- Frank–Gontier–Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb–Thirring inequalities*, Theorem 2, Proposition 11, Lemma 12. https://arxiv.org/html/2002.04964v3
- Frank–Gontier–Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, Theorems 3–4. https://arxiv.org/html/2109.05984v2
- Weinstein, *Modulational Stability of Ground States of Nonlinear Schrödinger Equations*. https://doi.org/10.1137/0516034

## 复现与文件

在本目录上级运行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research/r22_interaction_check.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research/r22_scattering_check.py
```

依赖 NumPy、SciPy。两个 JSON 保存实际运行结果；计算只作解析推导的一致性检查。[orientation.md](../separated-cores/orientation.md) 另保存方向场方法的准确重述及未闭合之处，不将其计为全局问题的解决。
