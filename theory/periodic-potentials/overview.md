# R28：二维端点的周期势直接检验

本轮未证明完整猜想，未构造反例，也未改善一般二维态的已知通用常数。
本文件记录可复用的直接数值检验，不宣称新的数学突破或历史首创。

## 固定目标与主线关系

目标仍为任意有限正交族的锐不等式

$$
\sum_j\|\nabla\phi_j\|_2^2\ge\frac{M_c}{2}\int\left(\sum_j|\phi_j|^2\right)^2,
\qquad \langle\phi_i,\phi_j\rangle=\delta_{ij}.
$$

谱形式的候选常数为 $L_*=1/(2M_c)\approx0.04273176846$。
Frank–Gontier–Lewin 的周期 LT 定理说明，允许所有晶格与周期势时，周期问题和全空间问题具有同一个最优常数。因此本次直接搜索周期反例与原猜想严格相关。该等价定理不意味着某个有限参数周期类足以证明全空间猜想。

主来源：<https://arxiv.org/html/2010.02981v2>，Theorem 1.1。

## 计算内容

- 平方与三角晶格，完整的分数倒格胞中点积分；不使用单独的零准动量替代整个能带积分。
- 在有限平面波空间内保留全部负本征值。密度更新保留全部 Fourier 模式，得到连续空间中非负的三角多项式势。
- 固定 $D=\int_CV^2$，用占据态密度更新势。在固定 Galerkin 空间与准动量网格内，该更新使谱负和不下降。
- 10 个初始单阱计算、8 个提高截断阶数的单阱计算，以及 18 个平坦背景/双阱/三阱起点；部分平坦背景计算在所设步数内未完全收敛。
- 独立核对面积因子、密度归一化、FFT 无混叠条件，并对首批 10 个最终势计算完整 Galerkin 谱、优化常数位移。
- 对最接近目标的平方晶格势保持势本身固定，提高 Fourier 截断与准动量分辨率。

单阱优化使用 $|n_1|,|n_2|\le m$。其密度频率范围为 $[-2m,2m]^2$，故 $(4m+1)^2$ 网格能完整表示密度；分母由 Parseval 公式直接计算。随机初始网格的插值不保证处处非负，但完成一次密度更新后的势具有上述严格非负表示。

## 实际结果

最接近目标的固定试探势来自平方晶格、$D=48$、$m=10$ 的优化。随后只改变数值求谱空间，得到：

| Fourier 截断 $m$ | 每方向准动量点数 | 中点积分试探值 |
|---:|---:|---:|
| 10 | 10 | 0.042731395013480 |
| 10 | 16 | 0.042731394832933 |
| 12 | 10 | 0.042731718210367 |
| 14 | 8 | 0.042731734636072 |

候选目标约为 **0.04273176846**。这些计算没有给出超过目标的候选。
大 $D$ 势阱的粗截断数值明显偏低，因此不能把粗网格上的下降解释为真实变分单调性。
已测试的多带起点最高中点积分值约为 0.042232294，仍低于单阱候选；这不是多带势的普遍上界。

这些都是双精度试探计算，既非全局优化证书，也非原问题的上界。
Galerkin 负谱和从下方逼近真实负谱和，因此低于候选目标不能证明该势满足所猜锐界，更不能证明所有势满足它。

## 可以严谨使用的积分下界公式

若倒格矩阵为 $B$，将分数倒格胞分为 $n_q^2$ 个小方格，
其中点为 $q_\alpha$，则

$$
R(V)\ge\frac{n_q^{-2}\sum_{\alpha,j}
[-\varepsilon_j^G(q_\alpha)-c_{n_q}]_+}{\int_CV^2},
\qquad c_{n_q}=\frac{\operatorname{tr}(B^TB)}{12n_q^2}.
$$

证明是在每个小格内使用固定 Ritz 投影；平均后线性动量项为零，二次动量项正好是 $c_{n_q}I$。它不要求谱带光滑或固定占据带数。详见 [periodic-trial-details.md](periodic-trial-details.md)。
公式是严格的，但 JSON 中的 `patch_lower` 仍由浮点本征值计算；本轮没有完成区间算术认证，也没有任何试探下界越过目标。

## 文件与复现

- [r28_periodic_search.py](../../computations/periodic-potentials/r28_periodic_search.py)：单阱起点及固定范数密度迭代。
- [r28_periodic_multistart.py](../../computations/periodic-potentials/r28_periodic_multistart.py)：平坦背景、双阱、三阱起点。
- [r28_periodic_baseline.py](../../computations/periodic-potentials/r28_periodic_baseline.py)：固定势的常数位移独立优化。
- [r28_periodic_verify.py](../../computations/periodic-potentials/r28_periodic_verify.py)：固定最佳试探势的分辨率复核。
- 同名前缀 JSON 保存结果，NPZ 保存全部试探势 Fourier 系数。

从仓库根目录开始，例如：

```bash
cd computations/periodic-potentials  # from the repository root
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r28_periodic_search.py --cutoff 10 --nq 10 --steps 25 --lattice square --norms 12 24 48 96 --output r28_periodic_square_refined
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r28_periodic_verify.py
```

依赖：Python、NumPy、SciPy。本轮环境 NumPy 2.3.5、SciPy 1.17.0。

此前的局部化、Townes 配平方及矩阵稳定性尝试本轮未产生新的普遍估计；没有把尚未证明的辅助命题记作成果。
