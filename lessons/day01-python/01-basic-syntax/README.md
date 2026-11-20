# 第 1 章 · 基础语法

阅读材料：[source/01-basic-syntax_files.html](../../../source/01-basic-syntax_files.html)（菜鸟教程原文，在浏览器中打开）

## 学习步骤

1. **读原文**（约 15 分钟）：快速通读，不必记细节。
2. **读本页**：看「要点」「和 JS 的差异」「原教程勘误」三节。
3. **跑 demo**：运行 3 个 `demo_*.py`，再随手改错一个 `assert` 运行一次，熟悉 Python 的报错格式。
4. **做练习**：完成 `exercises_01.py`，用 pytest 验证（pytest 用法见 [pytest 教程](../../tooling/pytest/README.md)）。
5. **写笔记**：把疑问和踩坑写进 `notes.md`。

## 文件

| 文件 | 内容 |
| --- | --- |
| `demo_syntax.py` | 编码、标识符、关键字、注释、缩进、多行语句、代码组、空行 |
| `demo_strings.py` | 数字类型、字符串引号、拼接、索引、切片、转义与原始字符串 |
| `demo_io_import.py` | `print`、`input`、`sys.stdout.write`、`import` / `from...import`、命令行参数 |
| `exercises_01.py` | 4 组练习（函数体是 `TODO`） |
| `test_exercises_01.py` | 练习的自动测试，不要修改 |
| `notes.md` | 你自己的笔记 |

## 运行

在项目根目录的 PowerShell 中：

```powershell
python .\lessons\day01-python\01-basic-syntax\demo_syntax.py
python .\lessons\day01-python\01-basic-syntax\demo_strings.py
python .\lessons\day01-python\01-basic-syntax\demo_io_import.py Rain 123   # 带命令行参数
python .\lessons\day01-python\01-basic-syntax\demo_io_import.py --ask      # 体验 input()

python -m pytest lessons/day01-python/01-basic-syntax -v                  # 检查练习
```

demo 全部通过时，每个文件只打印一行 `xxx: all passed`。

## 要点（按原文顺序）

1. **编码**：源文件默认 UTF-8，无需声明。
2. **标识符**：字母或下划线开头，区分大小写，不允许 `$`；变量和函数用 `snake_case`，类用 `PascalCase`，常量用全大写（只是约定）。
3. **关键字**：3.11 共 35 个，可用 `keyword.kwlist` 查看；`True`、`False`、`None` 首字母大写。
4. **注释**：只有 `#`。三引号是字符串，放在模块、函数或类开头时是 docstring。
5. **缩进**：用 `:` + 缩进代替 `{}`，统一使用 4 个空格；空代码块写 `pass`；缩进错误在编译阶段就会报错。
6. **多行语句**：换行即语句结束；长表达式优先用括号续行，其次用 `\`；分号可以用，但不推荐。
7. **数字**：`int`（无上限）、`float`、`bool`、`complex`；`/` 的结果总是 float，`//` 向下取整。
8. **字符串**：单双引号等价，三引号表示多行；`+` 拼接、`*` 重复；没有隐式类型转换；索引越界会报错，切片越界不会；不可修改；`r"..."` 中的反斜杠不转义。
9. **空行**：不是语法；PEP 8 约定顶层定义之间空两行。
10. **input / print**：`input()` 总是返回 `str`；`print` 可以设置 `sep` 和 `end`，返回 `None`。
11. **代码组**：`if` / `elif` / `else`、`while`、`def`、`class` 等复合语句的首行以冒号结尾，后面是缩进的代码块。
12. **import**：`import m`、`from m import a, b`、`import m as n`；避免 `from m import *`。
13. **命令行参数**：`sys.argv[0]` 是脚本路径，之后都是 `str` 类型的参数。

## 和 JS 的差异

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
| 整数 | 超过 `2**53` 会丢失精度 | 任意精度 | |
| 整除 | `Math.floor(7 / 2)` | `7 // 2` | `-7 // 2 == -4` |
| 输出 | `console.log(a, b)` | `print(a, b)` | 可以设置 `sep`、`end` |
| 输入 | `prompt()` | `input()` | 都返回字符串 |
| 导入 | `import * as m from "m"` | `import m` | |
| 命名导入 | `import { a } from "m"` | `from m import a` | |
| 命令行参数 | `process.argv.slice(2)` | `sys.argv[1:]` | |

## 原教程勘误与不推荐写法

- **cp-1252**：原文说它适用于俄语、保加利亚语等语言，实际上 cp-1252 是**西欧语言**编码，西里尔字母对应的是 cp-1251。
- **`is_valid_identifier`**：用 `exec()` 执行拼接出来的代码，再用裸 `except:` 吞掉所有异常，既不安全，也是反面写法。正确做法：`name.isidentifier() and not keyword.iskeyword(name)`（见练习 1）。
- **`str = '123456789'`**：会覆盖内置的 `str` 类型，之后 `str(1)` 就会报错。不要用内置名称（`str`、`list`、`input`、`type` 等）作变量名。
- **`print ("x")`**：PEP 8 规定函数名和括号之间不加空格，应写成 `print("x")`。
- **“三引号多行注释”**：三引号其实是字符串表达式，只是没有被使用；Python 没有真正的多行注释。
- **“r 会自动将反斜杠转义”**：这个说法容易误解。准确地说，`r` 前缀让反斜杠**不被当作转义符处理**，按原样保留。
- **`from somemodule import *`**：会污染命名空间，也看不出名字从哪里来，实际项目中应避免使用。
- **章末测验**：用到了 `for`、`range` 等本章没有讲的语法，可以先跳过。
