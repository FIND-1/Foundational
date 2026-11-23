# Foundational：Python 学习仓库

以 `source` 中的原始教程及其编号为唯一主线，按顺序阅读课程。课程中的【补充】是辅助理解，不是原教程新增章节。

四章的可阅读教程都位于 `source`。第 1～2 章已改为新结构（要点 + JS 对照 + demo + pytest 练习 + 笔记），03～04 章仍按旧方式把原教程实例整理在课程 Python 文件中，待迁移。可阅读 HTML 的互动脚本可能无法运行，外部链接与图片可能需要网络。

| 顺序 | 原始资料 | 学习目录 | 完成条件 |
| --- | --- | --- | --- |
| 1 | [基础语法](source/01-basic-syntax_files.html) | [基础语法教程](lessons/day01-python/01-basic-syntax/README.md) | 能说明变量、缩进、切片和输出，并独立完成基础练习 |
| 2 | [基本数据类型](source/02-basic-data-types.html) | [基本数据类型教程](lessons/day01-python/02-basic-data-types/README.md) | 能分辨主要类型与可变性，并完成本章练习 |
| 3 | [数据类型转换](source/03-type-conversion.html) | [数据类型转换教程](lessons/day01-python/03-type-conversion/README.md) | 能区分隐式和显式转换，并完成本章练习 |
| 4 | [解释器](source/04-interpreter.html) | [解释器教程](lessons/day01-python/04-interpreter/README.md) | 能进入并退出交互模式、运行脚本，并完成本章练习 |

在本地浏览器中打开上表的 HTML 文件，即可按章节标题阅读正文和代码示例。在线原文链接见 [source 索引](source/INDEX.md)。

## 怎么学习和运行

1. 按上表顺序阅读原始资料和对应课程 README；先阅读概念，再运行该章示例。
2. 在项目根目录打开 PowerShell，首次运行 `py -3.11 -m venv .venv` 创建虚拟环境。用 `.\.venv\Scripts\python.exe --version` 确认版本。
3. 安装测试工具（推荐在 `.venv` 中）：`.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt`（用法见 [pytest 教程](lessons/tooling/pytest/README.md)）。
4. 运行示例，例如：`.\.venv\Scripts\python.exe .\lessons\day01-python\01-basic-syntax\01_syntax_demo.py`。其他文件的运行方式见各章 README。
5. 练习：第 1～2 章完成对应 `exercises_NN.py` 后运行 `.\.venv\Scripts\python.exe -m pytest <章节目录> -m basic -v`（只测进阶题用 `-m advanced`，全部用例则去掉 `-m basic`）；03～04 章暂时仍使用 `practice.md`（待逐章迁移）。
6. 自由实验放在 `lessons/playground/`。

四章的完成条件全部满足后，再按实际新增的 `source` 学习后续内容。
