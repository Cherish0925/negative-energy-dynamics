# 临界聚焦与正交模态：2026-10-12 研究记录

本轮仍未解决二维 Lieb–Thirring 端点，也未证明一般集体塌缩阈值。这里保存已推导的约束、实际计算及其文献归属，不把工作记录当作已经完成的原创论文。

## 科学问题

考虑二维共同密度聚焦系统

$$
i\partial_tu_j+\Delta u_j+\rho u_j=0,\qquad
\rho=\sum_j|u_j|^2.
$$

设 $-\Delta Q+Q-Q^3=0$，$M_c=\|Q\|_2^2$。对任意有限正交归一族 $\phi_j\in H^1(\mathbb R^2)$，问题是

$$
\int\left(\sum_j|\phi_j|^2\right)^2
\stackrel{?}{\le}\frac2{M_c}\sum_j\|\nabla\phi_j\|_2^2.
$$

这对应一个明确的物理竞争：不同正交模态的密度重叠增强吸引，维持正交所需的空间变化增加动能。能否由多个各自低于标量临界质量的等质量正交模态形成共同束缚核心，取决于这一竞争的精确常数。谱表述是 $L_{1,2}\stackrel{?}{=}1/(2M_c)$。这里的多分量模型与归一化已经固定，不意味着任意耦合波系统均服从相同结论。

## 已完成的推导

令 $C_N$ 为至多 $N$ 个正交模态的最优四次密度／动能比，$C_1=2/M_c$。借助已有有限秩优化器理论，可取实优化轨道。随机选取占据空间内的实 $k$ 维子空间，精确球面矩公式给出

$$
\mathbb E\rho_k^2=\frac{k(k+2)}{R(R+2)}\rho^2,
\qquad\mathbb ET_k=\frac{k}{R}T
$$

（$R$ 是优化器秩）。由此推出

$$
C_N\le\frac{N+2}{k+2}C_k.
$$

若 $N$ 是首次满足 $C_N>C_1$ 的秩，则

$$
0<\frac{C_N}{C_1}-1\le\frac1{N+1},
\qquad
\frac{N+1}{N+2}M_c\le\beta=\frac2{C_N}<M_c.
$$

这是最小违规秩与改善幅度的关系，不是统一的秩上界，也不排除任意微小改善。此处未建立其历史原创性。

同时逐项计算了完整正交约束下的二阶变分。若 $H=-\Delta-V$、$V=2\rho/C_N$、$H\phi_i=\lambda_i\phi_i$，则对全部外部变分 $\psi_i\perp\mathrm{Ran}P$，任何真实优化器必须满足

$$
\sum_i\langle\psi_i,(H-\lambda_i)\psi_i\rangle
\ge\frac4{C_N}\left\|\sum_i\phi_i\psi_i\right\|_2^2.
$$

平移、尺度与非平凡旋转变分的零方向已保留；占据空间修正没有丢掉。标准二阶变分本身不是新理论。完整推导、等价响应算子及一条不能用于证明的反向谱估计，见 [collective-hessian.md](../collective-threshold/collective-hessian.md)。

## 实际计算与前人工作

进行了 61 次二维 Hermite 全轨道优化，测试秩 1、2、3、4、6、8、12，总次数最高 40。不预设径向性或轨道的变量可分离性。所有结果均低于标量参考值；高值候选主要通过分裂成多个单核来接近它。20 次运行达到迭代上限，不能统称收敛驻点。

这一分裂现象不能算新发现。Levitt 2014 §4.2 已报告相同类型的二维数值分裂，其明确展示的例子为 $\gamma=1.1,1.2$。后来的 Frank–Gontier–Lewin 严格结果又证明二维 $\gamma>1$ 的单态常数确实可以被突破。这说明局部优化反复分裂，并不能排除遗漏的弱束缚。两项研究都不能代替本轮 $\gamma=1$ 端点的证明。

独立积分验证、全部系数和脚本保留在包中。浮点一致性不等于区间算术证明；本轮没有需要认证的超阈值候选。

## 尚未完成的核心一步

如果希望通过变分不稳定性解决问题，必须证明：每一个精确自洽、严格优于单核常数的最小违规秩候选，都存在违反上述二阶关系的允许变分。此命题尚未证明。另一方向是构造并严格认证一个四次密度／动能比超过 $2/M_c$ 的正交族；本轮也没有做到。

若仅继续提高分离峰的数值精度，不能填补这个缺口。后续有决定意义的进展应当控制真实的集体束缚增益，而非把已知碎裂现象重复计为支持性证据。

## 文件与来源

- [collective-hessian.md](../collective-threshold/collective-hessian.md)：随机子空间压缩、完整 Hessian、响应算子与未解决命题。
- [global-methods.md](../collective-threshold/global-methods.md)：独立推导与谱、节点、基态变换、共形方法的具体缺口。
- [orbital-search.md](../collective-threshold/orbital-search.md)：数值方法、结果、复现命令和历史归属。
- `r21_orbital_*.py/json/npz`：脚本、原始数据、全部正交轨道系数。
- `r21_orbital_densities.png`：实际密度图。

主要原始文献：

1. Antoine Levitt, *Best constants in Lieb–Thirring inequalities: a numerical investigation*, Journal of Spectral Theory 4 (2014), 153–175. https://ems.press/content/serial-article-files/33509
2. Rupert L. Frank, David Gontier, Mathieu Lewin, *The nonlinear Schrödinger equation for orthonormal functions: II. Application to Lieb–Thirring inequalities*. https://arxiv.org/abs/2002.04964
3. Rupert L. Frank, David Gontier, Mathieu Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*. https://arxiv.org/abs/2109.05984
