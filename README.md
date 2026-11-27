# Foundational：Python 学习仓库

以 `source` 中的原始教程及其编号为唯一主线，按菜鸟教程顺序学习。`source` 与 `lessons/<NN-topic>/` 保持一一对应，不按实际学习天数拆建新 `day` 目录。课程中的【补充】是辅助理解，不是原教程新增章节。

为提高有 JS/TS 背景学习者的效率，仓库采用**差异化学习机制**（**Quick Review 速览学习** / **Delta Learning 差异学习** / **Core Learning 重点学习**），模式标明在各章 `README.md` 中、不写入目录名；并在 `lessons/reviews/` 独立规划跨章节阶段复习。完整路线规划与模式说明见 [课程索引](lessons/README.md) 与 [阶段复习机制](lessons/reviews/README.md)。

## 已导入原文的章节

可阅读 HTML 的互动脚本可能无法运行，外部链接与图片可能需要网络。在线原文链接见 [source 索引](source/INDEX.md)。

| 顺序 | 原始资料 | 学习目录 | 学习模式 | 完成条件 |
| --- | --- | --- | --- | --- |
| 1 | [基础语法](source/01-basic-syntax_files.html) | [基础语法教程](lessons/01-basic-syntax/README.md) | Core Learning | 能说明变量、缩进、切片和输出，并独立完成基础练习 |
| 2 | [基本数据类型](source/02-basic-data-types.html) | [基本数据类型教程](lessons/02-basic-data-types/README.md) | Core Learning | 能分辨主要类型与可变性，并完成本章练习 |
| 3 | [数据类型转换](source/03-type-conversion.html) | [数据类型转换教程](lessons/03-type-conversion/README.md) | Core Learning | 能区分隐式和显式转换，并完成本章练习 |
| 4 | [解释器](source/04-interpreter.html) | [解释器教程](lessons/04-interpreter/README.md) | Quick Review | 能进入并退出交互模式、运行脚本，并回答理解检查 |
| 5 | [注释](source/05-comments.html) | [注释教程](lessons/05-comments/README.md) | Quick Review | 能区分行注释、三引号字符串与文档字符串，并完成理解检查 |
| 6 | [运算符](source/06-operators.html) | [运算符教程](lessons/06-operators/README.md) | Core Learning | 能解释运算边界、短路与优先级，并独立完成基础练习 |

在本地浏览器中打开上表的 HTML 文件，即可按章节标题阅读正文和代码示例。后续第 07～15 章将在导入对应 `source/` 原文后再逐章编写，详见 [课程索引](lessons/README.md)。

## 怎么学习和运行

1. 按上表顺序阅读原始资料和对应课程 README；先看章节顶部的学习模式与概念要点，再按模式运行示例或直接速览。
2. 在项目根目录打开 PowerShell，首次运行 `py -3.11 -m venv .venv` 创建虚拟环境。用 `.\.venv\Scripts\python.exe --version` 确认版本。
3. 安装测试工具（推荐在 `.venv` 中）：`.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt`（用法见 [pytest 教程](lessons/tooling/pytest/README.md)）。
4. 运行示例，例如：`.\.venv\Scripts\python.exe .\lessons\01-basic-syntax\01_syntax_demo.py`。其他文件的运行方式见各章 README。
5. 练习与验证：含练习脚本的章节完成对应 `exercises_NN.py` 后运行 `.\.venv\Scripts\python.exe -m pytest <章节目录> -m basic -v`（只测进阶题用 `-m advanced`，全部用例则去掉 `-m basic`）；速览章节按该章 README 的理解检查或实操验收（如第 04 章包含 REPL 交互体验）。
6. 阶段复习：每完成 3～5 章进入 [阶段复习目录](lessons/reviews/README.md) 进行跨章节综合实践与错题复盘。
7. 自由实验放在 `lessons/playground/`。
