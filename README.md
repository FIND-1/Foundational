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

## 环境准备与通用流程

1. **创建并检查虚拟环境**（在仓库根目录打开 PowerShell；已有 Python 3.11 的 `.venv` 可跳过第一条）：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

2. **按顺序学习**：读 `source/` 原文 → 读本章 `README.md` 与 `functions.md` → 运行本章 Demo（如有）→ 完成练习或理解检查 → 记录复盘。
3. **运行示例**：例如 `.\.venv\Scripts\python.exe .\lessons\01-basic-syntax\01_syntax_demo.py`（激活 `.venv` 后可用 `python` 代替前缀）。各章具体命令见对应章节 `README.md`。
4. **阶段复习与自由实验**：每完成 3～5 章进入 [阶段复习目录](lessons/reviews/README.md) 做跨章综合实践与错题复盘；自由实验放在 `lessons/playground/`；pytest 进阶用法见 [pytest 教程](lessons/tooling/pytest/README.md)。

## 练习通用做法与 pytest 结果说明

含分层练习的章节均采用统一结构，各章 `exercises_NN.py` 与 `README.md` 不再重复以下说明：

1. **基础练习（必做）**：将待填占位 `...` 改为自己的表达式或语句，优先复用题目给定的变量，不写死结果（只用当前章节基础语法，无需 `def`；若含脚本入口题，将 `raise NotImplementedError("练习待完成")` 替换为自己的代码）。
2. **进阶练习（可选）**：需先了解 `def` / `return` / `if` 等前置知识，将函数体内的 `raise NotImplementedError("练习待完成")` 替换为实现。
3. **验证命令**（不要修改配套的 `test_exercises_NN.py`）：
   - 只测基础练习：`.\.venv\Scripts\python.exe -m pytest <章节目录> -m basic -v`
   - 只测进阶练习：`.\.venv\Scripts\python.exe -m pytest <章节目录> -m advanced -v`
   - 全章验证（含 Demo 自检与全部练习）：`.\.venv\Scripts\python.exe -m pytest <章节目录> -v`

| 测试结果 | 含义与下一步 |
| --- | --- |
| `PASSED` | 该用例符合预期；继续检查同题的其他输入或边界。 |
| `FAILED` | 查看实际值与期望值的差异，回到自己的练习代码修改后重跑。 |
| `SKIPPED` | 该项仍保留待填占位（`...` 或模板 `NotImplementedError`）；基础项须完成，进阶项可选。 |
| `deselected` | 使用 `-m basic` / `-m advanced` 筛选时，本次未选中的其他层级用例。 |
| `ERROR` | 通常是语法或缩进错误阻止了测试导入练习文件，先按报错定位文件和行号修复。 |

## 函数速查约定（`functions.md`）

各章 `functions.md` 均遵循以下约定，不再在每章顶部重复书写：

- **分级标签**：【必会】用于本章基础练习与高频日常操作；【了解】可在读到示例或拓展内容时再查。
- **签名核对**：所有签名、默认值与传参限制均已用 Python 3.11.9 的 `inspect.signature()` 与实际调用核实。
- **符号含义**：`/` 之前的参数只能按位置传入；`*` 之后的参数只能按关键字传入；方括号 `[ ]` 表示可省略的可选参数；无默认值的参数为必填参数。

## 笔记与验收约定

- **学习笔记（`notes.md`）**：统一采用五段式结构（核心知识点 / 最小代码示例 / 与 JS/TS 的差异 / 易错点与验证记录 / 待解决的问题）。学到哪一小节就记哪一小节，按需选填、不摘抄教材、不提前填未学内容。
- **验收勾选**：请按实际掌握程度勾选各章 `README.md` 的验收清单，不能仅凭跑通 Demo 或测试通过就勾选「本章完成」，须能用自己的话解释写法、边界与差异。
