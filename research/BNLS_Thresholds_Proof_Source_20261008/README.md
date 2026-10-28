# BNLS 主线研究，第十轮：证明源码与复核记录

日期：2026-10-08

主稿：BNLS_Thresholds_Spectral_Geometry_and_Radiation_20261008.tex
对应 PDF 共 28 页。

## 本轮内容

1. 负能量精确行波的最小质量紧致化：负能量取到，或有限个零能量精确剖面强分解；无弥散余项。
2. 完整作用量 Hessian 至少三个负方向，以及可微速度分支、各向同性响应下的加强；精确动量响应矩阵公式。
3. 严格凸密度范数的一阶等号机制，及其向正定 Hartree 非局域相互作用的统一质量间隙推广。
4. 同阶非齐次色散的双质量阈值、完整各向同性端点分类、低阈值精确尺度与剖面选择，以及弱扰动联合极限。
5. 原始 BNLS 全局有界负能量零动量解的弹道尺度外部梯度必要条件和梯度局域化刚性。

每个定理的完整假设以 TeX 主稿为准。研究笔记包含推导过程与已被正文精化的表述；出现措辞差异时以最终 TeX 为准。

## 检查与边界

- 独立代理交叉检查了阈值紧致化、Gamma 极限、谱指数与矩阵公式、梯度尾部动力学；主代理另行核对关键论证。
- 审查修正了归一化剖面与 Gamma 极限极小元的尺度区分，并消除了排版错误。
- 此次证明不依赖新的数值拟合或数值证书。负能量行波集合非空在紧致化定理中是明确前提。
- 本包不重新包含或重新验证较早四维构造的全部计算机辅助证书。
- round10_multisoliton_frontier.md 是对较早高质量双行波结果的连续性核对，未计入本轮新结果；不意味着近临界动力学已闭合。
- 一般近临界、零动量、负能量轨道的长期分类仍未完成。静态阈值定理、变分指数、动力学不稳定性和有限时间爆破是不同结论。
- 已进行有针对性的原始文献比较；没有声称完成外部同行评审或穷尽原创优先权核定。

## 复现 PDF

需要带有 amsmath、amsthm、mathtools、microtype、lmodern、hyperref 的 TeX Live：

```sh
pdflatex -interaction=nonstopmode -halt-on-error BNLS_Thresholds_Spectral_Geometry_and_Radiation_20261008.tex
pdflatex -interaction=nonstopmode -halt-on-error BNLS_Thresholds_Spectral_Geometry_and_Radiation_20261008.tex
```

主稿不需要其他轮次的 TeX 文件。输入文件均在本包根目录。
SHA256_MANIFEST.json 记录每个输入文件的 SHA-256。
