# R25：二维 Townes 双势阱的全尺度散射符号

2026-10-15

本资料包给出一个解析证明与区间计算结合的结果：对每个 0<k<1，完整散射系数满足

    A(k) < -2π / [25 log(1/k)] < 0.

因此，对每个固定的尺度比 k，两个充分远离的 Townes 势阱，其全部负本征值绝对值之和严格小于 (1/(2M))∫V²。证明包括全部角向模式、无穷远尾项，以及恰有两个负本征值的阈值计数。

这不是任意势、任意秩的锐 Lieb–Thirring 不等式证明，也不覆盖尺度比随距离变化的联合极限。结果的历史优先权尚未确认。

## 阅读顺序

1. [main-theorem.md](main-theorem.md)：精确命题、全部量词及证明结构。
2. [radial-scattering-verification.md](radial-scattering-verification.md)：径向散射负项的解析比较。
3. [uniform-bound.md](uniform-bound.md)：正角向项的全参数区间上界。
4. [certificate-details.md](certificate-details.md)：独立推导检查和程序重跑记录。
5. [separated-count.md](separated-count.md)：完整负谱计数，包含任意浅能级。

[partner-details.md](../townes-spectral-structure/partner-details.md) 提供单势阱谱输入，[relaxed-unequal-wells.md](../separated-cores/relaxed-unequal-wells.md) 提供远离势阱的首阶展开。旧文中的阶段性限制和浮点探索仅记录当时状态；R25 的最终结论以主定理及区间证书为准。归档的 [scattering-2cc19db4.md](scattering-2cc19db4.md) 明确标为解析节选，仅保留本证明需要的第 1–2 节。

## 复现

依赖 Python 3 与 mpmath 1.3.0。从仓库根目录开始，进入计算目录后依次运行：

```sh
cd computations/all-scale-scattering  # from the repository root
python r25_interval_shoot.py
python r25_interval_shoot.py 2.2062008646507,2.2062008646508 8 --enclose
python r25_uniform_certificate.py
```

第三个程序也可直接读取包内已保存的精确二进制区间端点，复核最终证书。它会断言全区间上界小于有理数 24/25；记录的最大区间上界小于 0.959318。此结果由连续区间覆盖和解析端点控制给出，不是离散采样推断。

程序重跑会更新相应 JSON 输出；`SHA256SUMS.txt` 标识本次归档时的文件快照。数学证明依赖所述解析输入及区间算术实现，不是形式化证明系统的验证产物。
