四维质量临界 BNLS：非径向负能量全局行波的计算机辅助证明
2026-10-07，第二轮研究及完整认证

本次结论
对 i u_t = Δ²u − |u|²u（R⁴），存在 ε>0，以及对每个 0<|v|<ε 定义的非零剖面 Q_v，使
  u(t,x)=exp(it) Q_v(x−vt e₁)
是对所有实数时间存在的非径向解，且
  E(Q_v)<0，||u(t)||H²=||Q_v||H²<∞。
因此，“所有维数 N≥2 中，任意非径向 H² 负能量初值必然有限时间塌缩”的普遍断言不成立。
本证明给出 N=4 的反例，不声称同时裁决固定 N=2 或 N=3 的对应问题。

证明的决定性证书
存在精确实径向驻波 Q（Δ²Q+Q−Q³=0），距离冻结的紧支撑有理分段多项式 q 的 Z 范数小于 0.006；Z²=||f||₂²+||Δf||₂²。
在所需对称空间中线性化可逆，而且
  <∂₁Q,(Δ²+1−Q²)^−1 ∂₁Q>
  <= −24609689664617/140499437500 < −175。
隐函数定理、动量展开与截断 Pohozaev 恒等式推出负能量全局行波。
数值拟合不承担存在性证明；谱积分由 Arb 区间运算认证，其余关键积分和不等式用精确有理数认证。

从哪里开始
1. BNLS_Nonradial_Research_20261007.pdf：本轮完整证明稿。
2. round2_certificate/VERIFICATION_SUMMARY.json：独立全套重跑结果。
3. round2_certificate/run_verification.py：一键复核入口。
4. round2_notes/：推导、审计及研究过程记录。
5. round2_N4_reproduction_bundle.zip：数值发现和独立复现材料，包含不同网格/区域的行波剖面。
6. round1_archive/：上一轮阶段性研究。旧稿关于“尚未解决”的说明是当时状态，已被本轮证明稿更新。

复核命令
进入 round2_certificate 目录，使用 Python 3.12（本次运行环境）执行：
  python3 -m pip install -r requirements.txt
  python3 run_verification.py
精确算术部分仅用 Python 标准库；谱积分使用 python-flint 0.9.0 中的 Arb/acb。
验证器只读取冻结数据，不调用驻波数值求解器，不需要 NumPy/SciPy，也不重新生成输入。
通过时输出 ALL FINITE CERTIFICATES PASSED，并写入 VERIFICATION_SUMMARY.json。
完整运行约一分钟，依机器性能而异。

精确数据身份
核心剖面：round2_radial_H4_exact_h1_16.json
SHA256：c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627
文件通过有理网格节点及十六进制精确端点导数定义 C³ 分段七次多项式，r≥36 时为零。
根目录 SHA256.json 列出交付文件摘要。

结论的准确范围
定理证明的是“充分小的非零速度”这一存在族，并未认证某个明确速度上限。
v=0.02 的能量 −0.02704284764 是独立数值复现结果；此特定速度的数值并不被冒充为存在定理的已认证实例。
行波无需非线性稳定也足以反驳“所有负能量数据必爆破”。
本稿为本次研究产生的计算机辅助证明，已完成内部独立审查和重跑，尚未经外部同行评审或形式化证明助手验证。
