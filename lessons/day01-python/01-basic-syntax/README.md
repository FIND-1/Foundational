# 第 1 章 · 基础语法

阅读材料：[source/01-basic-syntax_files.html](../../../source/01-basic-syntax_files.html)（菜鸟教程原文，在浏览器中打开）

## 学习步骤

1. **读原文**（约 15 分钟）：快速通读，不必记细节。
2. **读本页与函数速查**：看「要点」「和 JS 的差异」「原教程勘误」，首次遇到的函数与方法查 [functions.md](functions.md)。
3. **跑 demo**：运行 3 个 `*_demo.py`，观察终端的 `print()` 输出；`# 拓展：` 部分的 `compile()` / `try...except` 只作验证，暂不要求手写。
4. **做基础练习**：完成 `exercises_01.py` 的「基础练习」部分（先写变量表达式，再独立写一段带缩进的输入输出代码），用 pytest 验证（用法见 [pytest 教程](../../tooling/pytest/README.md)）。
5. **选做进阶练习**：若已了解 `def` / `return` / `if-elif-else`，可继续挑战「进阶练习」。
6. **阶段复盘**：学到哪一小节就顺手把自己的理解、验证、JS 差异和易错点记进 `notes.md`（按需选填，不提前填未学内容，也不仅凭测试通过就标记掌握）。

## 学习验收标准

请按实际掌握情况勾选（不能仅凭跑通 demo 就勾选“本章完成”）：

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能预测切片和换行的结果，改动下标或 `end` 后能解释差异。能指出两种续行写法各靠什么识别下一行，并解释显式拼接和 f-string 为什么得到相同的问候语。
- [ ] 基础练习通过：独立完成四组题，`-m basic` 全部显示 `PASSED`，并能用自己的话说明每题用了什么语法、为什么这样写。例如，做完题 1 后，能解释两项检查分别回答什么问题。
- [ ] 进阶练习通过（可选）
- [ ] 本章完成：读完原文、能解释示例、基础测试全过，并在 `notes.md` 记录易错点或自己的验证过程。

## 文件

| 文件 | 内容 |
| --- | --- |
| `01_syntax_demo.py` | 编码、标识符、关键字、注释、缩进、多行语句 |
| `02_strings_demo.py` | 数字类型、字符串引号、拼接、索引、切片、转义与原始字符串 |
| `03_io_import_demo.py` | 空行、`input`、同行语句、代码组、`print`、`sys.stdout.write`、`import` / `from...import`、命令行参数 |
| [functions.md](functions.md) | 本章首次引入的函数与方法完整速查（含签名、参数限制、异常与 JS 对照） |
| `exercises_01.py` | 基础练习（必做，写表达式和输入输出）+ 进阶练习（可选，写函数） |
| `test_exercises_01.py` | 练习的自动测试，不要修改 |
| `test_demos_01.py` | 语法和字符串 Demo 的自检；运行全章 pytest 时执行 |
| `notes.md` | 个人学习笔记与错题复盘（记录理解、验证、差异、易错点与待解问题） |

## 运行

在仓库根目录打开 PowerShell。首次使用时执行以下两条命令。已有 Python 3.11 的 `.venv` 可以跳过第一条。

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

```powershell
.\.venv\Scripts\python.exe .\lessons\day01-python\01-basic-syntax\01_syntax_demo.py
.\.venv\Scripts\python.exe .\lessons\day01-python\01-basic-syntax\02_strings_demo.py
.\.venv\Scripts\python.exe .\lessons\day01-python\01-basic-syntax\03_io_import_demo.py Rain 123   # 带命令行参数
.\.venv\Scripts\python.exe .\lessons\day01-python\01-basic-syntax\03_io_import_demo.py --ask      # 输入 18 后应看到「明年： 19」

.\.venv\Scripts\python.exe -m pytest lessons/day01-python/01-basic-syntax -m basic -v   # 只测基础练习
.\.venv\Scripts\python.exe -m pytest lessons/day01-python/01-basic-syntax -v            # 测全部练习
```

前两个 Demo 直接展示结果；第三个 Demo 在「拓展」部分介绍 `assert`，末尾的 `all passed` 表示该示例自检通过。前两个 Demo 的检查随全章 pytest 一起运行。练习进度看标记为 `basic` 或 `advanced` 的用例。

| 结果 | 下一步 |
| --- | --- |
| `PASSED` | 该用例符合预期；继续检查同题的其他输入。 |
| `FAILED` | 看失败项的实际值和期望值，回到自己的代码修改后重跑。 |
| `SKIPPED` | 该项保留了待填标记。基础项仍需完成，进阶项可留到学过函数后。 |

`-m basic` 只选择基础题；摘要里的 `deselected` 是本次未选择的用例。若出现 `ERROR`，先按报错定位文件和行号，例如缩进错误会阻止测试导入练习文件。

## 要点（按原文顺序）

1. **编码**：源文件默认 UTF-8，无需声明。
2. **标识符**：字母或下划线开头，区分大小写，不允许 `$`；变量和函数用 `snake_case`，类用 `PascalCase`，常量用全大写（只是约定）。
3. **关键字**：3.11 共 35 个，可用 `keyword.kwlist` 查看；`True`、`False`、`None` 首字母大写。
4. **注释**：只有 `#`。三引号是字符串，放在模块、函数或类开头时是 docstring。
5. **缩进**：用 `:` + 缩进代替 `{}`，统一使用 4 个空格；空代码块写 `pass`；缩进错误在编译阶段就会报错。
6. **多行语句**：换行即语句结束；长表达式优先用括号续行，其次用反斜杠。
7. **数字**：`int`（无上限）、`float`、`bool`、`complex`；两个整数用 `/` 相除得到 `float`，`//` 向下取整。
8. **字符串**：单双引号等价，三引号表示多行；`+` 拼接、`*` 重复；没有隐式类型转换；索引越界会报错，切片越界不会；不可修改；`r"..."` 中的反斜杠不转义。
9. **空行**：不是语法；PEP 8 约定顶层定义之间空两行。
10. **等待用户输入**：`input()` 读入一行，去掉行尾换行后返回 `str`。
11. **同行多条语句**：分号可以分隔语句，日常优先分行写。
12. **代码组**：`if` / `elif` / `else`、`while`、`def`、`class` 等复合语句的首行以冒号结尾，后面是缩进的代码块。
13. **print 输出**：`print` 可以设置 `sep` 和 `end`，返回 `None`。
14. **import**：`import m`、`from m import a, b`、`import m as n`；避免 `from m import *`。
15. **命令行参数**：`sys.argv[0]` 是脚本路径，之后都是 `str` 类型的参数。

## 【补充】和 JS 的差异

| 主题 | JS | Python | 注意 |
| --- | --- | --- | --- |
| 代码块 | `{ }` | `:` + 缩进 | 混用 Tab 和空格会报 `IndentationError` |
| 语句结束 | `;` / 自动分号插入（ASI） | 换行 | 没有 ASI 的坑 |
| 空值 | `null` / `undefined` | `None` | 只有一个空值 |
| 布尔值 | `true` / `false` | `True` / `False` | 首字母大写 |
| 逻辑运算 | `&&` `\|\|` `!` | `and` `or` `not` | |
| 否则如果 | `else if` | `elif` | |
| 函数 | `function f() {}` / `() => {}` | `def f():` / `lambda: ...` | `lambda` 只能写一个表达式 |
| 命名 | `camelCase` | `snake_case` | 类名两者都是 `PascalCase` |
| 私有成员 | `#field`（强制） | `_name`（约定） | |
| 模板字符串 | `` `${x}` `` | `f"{x}"` | |
| 多行字符串 | `` `...` `` | `"""..."""` | |
| 原始字符串 | ``String.raw`...` `` | `r"..."` | |
| 拼接数字 | `"a" + 1 === "a1"` | `TypeError` | 需要写 `"a" + str(1)` |
| 重复字符串 | `"ab".repeat(3)` | `"ab" * 3` | |
| 负数索引 | `s.at(-1)` | `s[-1]` | JS 中 `s[-1]` 是 `undefined` |
| 越界索引 | `undefined` | `IndexError` | 切片越界不会报错 |
| 截取 | `s.slice(1, 5)` | `s[1:5]` | Python 还可以加步长 `s[1:5:2]` |
| 整数 | `Number` 超过最大安全整数后无法保证精确，`BigInt` 可表示更大整数 | 任意精度 | |
| 整除 | `Math.floor(7 / 2)` | `7 // 2` | `-7 // 2 == -4` |
| 输出 | `console.log(a, b)` | `print(a, b)` | 可以设置 `sep`、`end` |
| 输入 | `prompt()` | `input()` | 正常输入都返回字符串；浏览器取消时返回 `null` |
| 导入 | `import * as m from "m"` | `import m` | |
| 命名导入 | `import { a } from "m"` | `from m import a` | |
| 命令行参数 | `process.argv.slice(2)` | `sys.argv[1:]` | |

## 【补充】原教程勘误与不推荐写法

- **cp-1252**：原文说它适用于俄语、保加利亚语等语言，实际上 cp-1252 是**西欧语言**编码，西里尔字母对应的是 cp-1251。
- **`is_valid_identifier`**：用 `exec()` 执行拼接出来的代码，再用裸 `except:` 吞掉所有异常，既不安全，也是反面写法。做进阶练习时要分别考虑拼写规则和保留字，可查本章的函数速查。
- **`str = '123456789'`**：会覆盖内置的 `str` 类型，之后 `str(1)` 就会报错。不要用内置名称（`str`、`list`、`input`、`type` 等）作变量名。
- **`print ("x")`**：PEP 8 规定函数名和括号之间不加空格，应写成 `print("x")`。
- **“三引号多行注释”**：三引号其实是字符串表达式，只是没有被使用；Python 没有真正的多行注释。
- **“r 会自动将反斜杠转义”**：这个说法容易误解。准确地说，`r` 前缀让反斜杠**不被当作转义符处理**，按原样保留。
- **`from somemodule import *`**：会污染命名空间，也看不出名字从哪里来，实际项目中应避免使用。
- **章末测验**：用到了 `for`、`range` 等本章没有讲的语法，可以先跳过。
