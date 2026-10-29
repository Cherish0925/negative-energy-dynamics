# 临界聚焦色散系统：全尺度散射符号与双核完整谱

研究记录 R24，2026-10-15。

本轮完成了此前未闭合的全尺度散射符号，并补上了双势阱的全部负能级计数。
二者结合，得到一个明确结论：任意固定正尺度比的两个 Townes 势阱，在距离
充分大时，其完整负谱迹严格低于单态 Lieb–Thirring 常数给出的势代价。
这包括真实本征函数的形变，也包括对任意接近零的额外负能级的排除。

这是一份给出解析推导、计算机辅助证明和复现程序的研究稿。历史首创性尚未

## 1. 主线与本轮回答的问题

固定主线仍是“临界聚焦色散系统的阈值、相干结构与动力学”。当前考察二维
共同密度聚焦系统
$$
i\partial_tu_j+\Delta u_j+\rho u_j=0,\qquad \rho=\sum_j|u_j|^2.
$$
令
$$
-\Delta Q+Q-Q^3=0,\qquad Q>0,\qquad M=\int Q^2.
$$
全局问题是：多个正交模态能否突破由单模态基态决定的锐常数？相应不等式为
$$
\int\left(\sum_j|\phi_j|^2\right)^2
\le\frac2M\sum_j\int|\nabla\phi_j|^2,
\qquad\langle\phi_i,\phi_j\rangle=\delta_{ij}.
$$
这条任意秩、任意非径向正交族的不等式，本轮仍未证明。最初的非径向负能量
BNLS 有限时间爆破问题也未解决。本轮解决的是其中具有精确表述的双核机制，
以及支撑该机制分析的全尺度散射问题。

## 2. 已完成：全尺度散射符号

置 $h=-\Delta-Q^2$，定义
$$
\mathcal A(k)=\int Q^2e^{2kx_1}
+\left\langle Q^2e^{kx_1},(h+k^2)^{-1}Q^2e^{kx_1}\right\rangle.
$$
现已得到带完整误差控制的计算机辅助证明：
$$
\boxed{\mathcal A(k)<-\frac{2\pi\cdot0.014}{\log(1/k)}<0
\quad\text{对每个 }0<k<1.}
$$

证明的解析核心是把 Townes 基态的一阶分解与 $B=K_0$ 的显式分解比较。
Wronskian 恒等式使 $Q/B$ 严格递增，继而使两个伴随势严格有序。正解比较
直接给出径向散射系数
$$
a_0(k)<-1/\log(1/k).
$$
这一步不需要数值基态。对全部非零角动量，则利用零能 Birman–Schwinger
算子的 Hilbert–Schmidt 范数统一控制。

剩余数值部分已实际完成，不是负值采样：

| 参数区间 | 包含全部角向模式后的相对上界 |
|---|---:|
| $0<k\le0.02$ | $<0.005769$，解析界 |
| $0.02\le k\le0.991$ | $<0.985344$，971 个完整参数区间 |
| $0.991\le k<1$ | $<0.950198$，解析界 |

严格基态包络由区间射击和逐步 Taylor 余项得到；径向积分、Bessel 级数、
无限空间尾部和无限角动量尾部均有上界。表中每项小于 0.986，遂得到上式。

主证明：[scattering-2cc19db4.md](scattering-2cc19db4.md)、[certified-angular.md](certified-angular.md)。
基态计算证明：[validated-profile.md](validated-profile.md)。
独立核对：[radial-scattering-verification.md](radial-scattering-verification.md)、[angular-verification.md](angular-verification.md)。

## 3. 已完成：固定尺度比双核的完整负谱结论

对任意固定 $k>0$，置
$$
V_{k,R}(x)=Q(x)^2+k^2Q(k(x-Re_1))^2,\qquad H_{k,R}=-\Delta-V_{k,R}.
$$
存在依赖 $k$ 的 $R_0(k)$，使所有 $R>R_0(k)$ 满足：

1. $H_{k,R}$ 恰有两个负本征值，零能没有非零有界解。
2. 完整负谱迹满足
   $$
   \boxed{\operatorname{Tr}(H_{k,R})_-<\frac1{2M}\int V_{k,R}^2.}
   $$

对 $0<k<1$，更精确地，令 $q=Q/\sqrt M$、
$q(r)\sim A_qr^{-1/2}e^{-r}$，则
$$
\operatorname{Tr}(H_{k,R})_--\frac1{2M}\int V_{k,R}^2
=\varepsilon_R^2\mathcal A(k)+o_k(\varepsilon_R^2),
\quad \varepsilon_R=A_q\sqrt{k}\,R^{-1/2}e^{-kR}.
$$
等尺度情形使用 R22 的独立展开；大于一的比值通过交换和缩放归约。
这里每个尺度比固定后距离趋于无穷，未证明 $k=k(R)$ 的联合极限一致性。

物理上，这回答了指定双核势中正交束缚模态的一个能量问题：在上述极限下，
两核结合不能使“总束缚能／势强度的二次积分”超过单核值。它没有推出任意
强重叠自洽状态的结论，也没有把谱结论当成时间演化稳定性定理。

## 4. 已完成：尺度分离的全谱计数及同心双核

计数证明还适用于固定有限个一般非径向势阱。若 $W_j\ge0$ 非零、有界、
指数衰减，各自有 $n_j$ 个负能级且没有非零有界零能解，则固定缩放坐标
中心 $z_j$，相邻尺度充分分离时，
$$
\boxed{N_-\left(-\Delta-\sum_{j=1}^N k_j^2W_j(k_jx-z_j)\right)
=\sum_{j=1}^N n_j.}
$$
没有径向假设；$N$、势形状与缩放坐标中心固定。

关键是先在每个固定尺度组下令谱参数趋零，再处理尺度分离。二维对数核的
相对质量块满足
$$
-\sum_{i,j}\max(L_i,L_j)\overline{c_i}c_j
=\sum_{j<N}(L_{j+1}-L_j)\left|\sum_{i\le j}c_i\right|^2,
\qquad \sum_jc_j=0.
$$
它确定了全部负方向，因而没有遗漏极浅的负能级。

对固定 $z$ 的双尺度 Townes 势 $V_k=Q^2+k^2Q(kx-z)^2$，R23 的两级
展开由此成为完整谱迹展开：
$$
\operatorname{Tr}(-\Delta-V_k)_--\frac1{2M}\int V_k^2
=-\frac{2\pi k^2q(z)^2}{|\log k|}
+O_z\!\left(\frac{k^2}{|\log k|^2}\right)<0.
$$
这允许 $z=0$，即两核同心。一般多井计数定理本身不确定所有多核谱迹差的符号。
完整证明：[full-spectrum.md](full-spectrum.md)、[count-verification.md](count-verification.md)。

## 5. 强重叠部分得到什么、还缺什么

对于径向自洽多分量驻波，已推导一个保持剩余分量质量与正交性的精确变换。
若最低态 $u_1=w>0$，置
$$
v_j=\frac{u_j'-(w'/w)u_j}{\sqrt{e_1-e_j}},\quad
S=\sum_{j\ge2}v_j^2,
$$
则剩余分量满足
$$
-\Delta_{\rm rad}v_j+Wv_j-Sv_j=-e_jv_j,
\quad
W(r)=\frac1{rw(r)^2}\int_r^\infty w(s)^2[\rho(s)+S(s)+s^{-2}]\,ds>0.
$$
一维对应余项为零；二维、三维出现正的曲率修正。这把一维的非线性分解与
高维径向结构具体联系起来。

但 $W>0$ 还不能完成降秩归纳：剩余能量等于
$\tfrac12\int rW'S$，此积分的普遍非正性尚未证明。实际计算的驻波分支
表明不能用更强的逐点条件 $W'\le0$ 或 $\rho\ge S$ 代替它。非径向
紧致多模态的排除也尚未完成。这是当前全局问题仍缺少的实质步骤。

见 [global-route.md](global-route.md)；相关数值分支清楚标为浮点探索。它们不是全局结论的证明。

## 6. 与已有工作的关系

Frank–Gontier–Lewin 的正交函数 NLS／Lieb–Thirring 工作通过远离的基态核研究
绑定，其二维严格改善单态常数的结论要求指数 $\gamma>1$。本轮研究的是
$\gamma=1$ 的端点及指定势族，两种结论并不矛盾：
https://arxiv.org/html/2002.04964v3 。

经典 Darboux 分解、Birman–Schwinger 理论、二维对数预解算子及 Kwong 的
正基态唯一性是已有工具。这里记录的是本次推导的具体比较公式、全尺度符号
及全谱后果，不将这些经典工具归为原创，也不将未完成的历史检索当成优先权证明。

## 7. 阅读与复现

建议依次阅读本文件、[scattering-2cc19db4.md](scattering-2cc19db4.md)、[certified-angular.md](certified-angular.md)、
[full-spectrum.md](full-spectrum.md)。数学依赖的 R22、R23 笔记保留在包内；其旧版中关于
“全尺度符号未定”“可能还有极浅能级”的状态描述已被本轮相应定理更新。

复现全尺度计算只需 Python、mpmath、NumPy：

```bash
cd computations/all-scale-scattering  # from the repository root
python3 r24_validated_profile.py --mode shoot --a-low 2.20620086465074 --a-high 2.20620086465075 --stop 24 --output r24_validated_shooting_tight.json
python3 r24_validated_profile.py --mode profile --a-low 2.20620086465074 --a-high 2.20620086465075 --step 0.005 --output r24_validated_profile_tight.json
python3 r24_certified_angular.py --profile r24_validated_profile_tight.json --shooting r24_validated_shooting_tight.json --C 2.82 --output r24_certified_angular.json
```

最终输出应为 `all_k_bound_closes: true`。算术假设、逐项余项及射击识别的证明
在对应笔记中列明。径向驻波探索另需 SciPy；它不参与全尺度定理的计算机辅助证明。
