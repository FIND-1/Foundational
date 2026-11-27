# 第 6 章 · 运算符

学习模式：Core Learning（重点学习）

阅读材料：[source/06-operators.html](../../source/06-operators.html)（菜鸟教程原文，在浏览器中打开）

## 学习步骤

1. **读原文**（约 10 分钟）：按「算术 → 比较 → 赋值 → 位运算 → 逻辑 → 成员 → 身份 → 优先级」顺序通读，了解各类运算符的符号与大致用途，不必死记优先级表。
2. **读本页与函数速查**：看「要点」「和 JS 的差异」「原教程勘误」，本章新遇到的函数查 [functions.md](functions.md)；前几章已讲的 API 查[第 1 章速查](../01-basic-syntax/functions.md)、[第 2 章速查](../02-basic-data-types/functions.md)和[第 3 章速查](../03-type-conversion/functions.md)。
3. **跑 demo**：按下方顺序运行 4 个 `*_demo.py`，先预测再观察 `print()` 输出；标为 `拓展：` 的海象运算符、权限掩码和幂右结合只作观察，暂不要求手写。
4. **做基础练习**：完成 [exercises_06.py](exercises_06.py) 的「基础练习」（四组表达式与赋值题），用 pytest `-m basic` 验证（用法见 [pytest 教程](../tooling/pytest/README.md)）。
5. **选做进阶练习**：若已熟悉 `def` / `return` / `if`，可继续挑战「进阶练习」（保留列表合法假值、按位更新权限掩码）。
6. **阶段复盘**：学到哪一小节就顺手把本章理解、差异和易错点记进 [notes.md](notes.md)。

## 学习验收标准

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能解释 `int(-7 / 3)` 与 `-7 // 3`、`-7 % 3` 的区别，列表 `+=` 原地修改与 `+` 重新绑定的身份差异，`and` / `or` 的返回值与 `is None` 缺省值判断，`is` 与 `==` 的区别，以及优先级分组与短路求值顺序的差异。
- [ ] 基础练习通过：独立完成四组基础题，`-m basic` 全部显示 `PASSED`，并能用自己的话说明每题选用的运算符与边界条件。
- [ ] 进阶练习通过（可选）
- [ ] 本章完成：读完原文、能解释示例、基础测试全过，并在 `notes.md` 记录易错点或自己的验证过程。

## 文件

| 文件 | 内容 |
| --- | --- |
| [01_arith_compare_demo.py](01_arith_compare_demo.py) | 基本算术、`int()` 向零截断 vs `//` 与 `%`、六种比较、跨类型比较说明与链式比较 |
| [02_assignment_demo.py](02_assignment_demo.py) | 普通赋值、数值增量赋值、列表 `+=` 原地修改 vs `+` 重新绑定与身份对照、海象运算符（拓展） |
| [03_bitwise_logic_demo.py](03_bitwise_logic_demo.py) | 六种整数位运算、权限掩码与清除（拓展）、逻辑返回值与短路、`or` 与 `is None` 缺省值对照 |
| [04_member_id_demo.py](04_member_id_demo.py) | 列表/元组/集合/字符串/字典键与 `dict.values()` 成员判断、身份与 `id()`、优先级分组与求值顺序 |
| [functions.md](functions.md) | 本章首次引入的 `id()` 完整速查（含签名、参数限制、异常与 JS 对照）及前章 API 入口 |
| [exercises_06.py](exercises_06.py) | 基础练习（必做，四组题）+ 进阶练习（可选，两道函数题） |
| [test_exercises_06.py](test_exercises_06.py) | 练习的自动测试，不要修改 |
| [test_demos_06.py](test_demos_06.py) | 4 个 Demo 的自检；运行全章 pytest 时执行 |
| [notes.md](notes.md) | 个人学习笔记与错题复盘（记录理解、验证、差异、易错点与待解问题） |

## 运行

在仓库根目录打开 PowerShell 运行（环境准备、练习做法与 pytest 结果说明见[项目根目录 README](../../README.md)）：

```powershell
.\.venv\Scripts\python.exe .\lessons\06-operators\01_arith_compare_demo.py
.\.venv\Scripts\python.exe .\lessons\06-operators\02_assignment_demo.py
.\.venv\Scripts\python.exe .\lessons\06-operators\03_bitwise_logic_demo.py
.\.venv\Scripts\python.exe .\lessons\06-operators\04_member_id_demo.py

.\.venv\Scripts\python.exe -m pytest lessons/06-operators -m basic -v     # 只测基础练习
.\.venv\Scripts\python.exe -m pytest lessons/06-operators -m advanced -v  # 只测进阶练习
.\.venv\Scripts\python.exe -m pytest lessons/06-operators -v              # 测全部练习和 Demo 自检
```

## 要点（按原文顺序）

| 运算符分类 | 常用运算符 | 核心规则与示例 |
| --- | --- | --- |
| 算术运算符 | `+` `-` `*` `/` `//` `%` `**` | `7 / 3` 总得 `float`；`int(-7 / 3)` 向零截断得 `-2`，`-7 // 3` 向下取整得 `-3`，`-7 % 3` 得 `2`（满足 `被除数 == 整除商 * 除数 + 余数`，非零余数与除数同号） |
| 比较运算符 | `==` `!=` `<` `<=` `>` `>=` | 内置值比较返回 `bool`；`==` 跨类型不隐式转换（`3 == "3"` 为 `False`），跨类型大小比较（如 `3 < "4"`）抛 `TypeError`；链式比较 `3 <= 7 < 10` 中间表达式只求值一次 |
| 赋值运算符 | `=` `+=` `-=` `*=` `/=` `//=` `%=` `**=` `:=` | 列表 `a += [x]` 原地修改原对象（别名可见），`a = a + [x]` 生成新列表并重新绑定（原别名不变）；`:=`（拓展）在表达式内赋值并返回该值，如 `(n := len(items)) > 2` |
| 位运算符 | `&` `\|` `^` `~` `<<` `>>` | 按整数二进制位运算；Python 中 `~x == -x - 1`，右移 `n` 位等价于向下整除 `2 ** n`；权限掩码与清除见 Demo 03 拓展段 |
| 逻辑运算符 | `and` `or` `not` | `and` / `or` 短路并返回决定结果的**操作数本身**，`not` 恒返回 `bool`；`值 or 默认值` 会误覆盖 `0`、`""`、`False`，仅在 `None` 时回退写 `默认值 if 值 is None else 值` |
| 成员运算符 | `in` `not in` | 字符串查子串，列表/元组/集合查元素，字典默认查键；查字典值用 `值 in 字典.values()` |
| 身份运算符 | `is` `is not` | 检查两个变量是否引用同一对象，`==` 检查值是否相等；判空固定写 `is None` / `is not None`，调试观察标识可用 `id()` |
| 运算符优先级 | 见下方常用顺序 | 高到低：乘除取模组 → 加减 → 移位 → `&` → `^` → `\|` → 比较/成员/身份 → `not` → `and` → `or`。**优先级只决定语法分组，实际求值从左到右并受短路控制**；拓展：`2 ** 3 ** 2` 向右分组，`-2 ** 2 == -4`。完整表见 [Python 3.11 优先级表](https://docs.python.org/3.11/reference/expressions.html#operator-precedence) |

## 【补充】和 JS 的差异

| 主题 | JS | Python | 注意 |
| --- | --- | --- | --- |
| 整除运算符 | `//` 是单行注释；用 `Math.floor(a / b)` | `a // b` 向下取整 | `int(a / b)` 向零截断，类似 JS 的 `Math.trunc(a / b)` |
| 负数取模 `%` | `-7 % 3 === -1`（与被除数同号） | `-7 % 3 == 2`（与除数同号） | Python 保证 `a == (a // b) * b + (a % b)` |
| 跨类型比较 | `3 == "3"` 为 `true`，`3 < "4"` 为 `true` | `3 == "3"` 为 `False`，`3 < "4"` 抛 `TypeError` | Python 没有 `===`，`==` 也不做跨类型隐式转换 |
| 链式比较 | `3 <= 7 < 10` 先得 `true` 再算 `1 < 10` | `3 <= 7 < 10` 等价于 `3 <= 7 and 7 < 10` | Python 原生支持链式区间，且中间表达式只求值一次 |
| 列表拼接赋值 | `arr.push(...other)` 原地修改 | `a += [x]` 原地修改，`a = a + [x]` 重新绑定 | 存在列表别名时，两种写法的对象身份结果相反 |
| 逻辑运算符与空容器 | `&&` `\|\|` `!`；`[]`、`{}` 为真 | `and` `or` `not`；`[]`、`{}` 为假 | 两边都短路且返回原操作数，但空容器真假值相反 |
| 仅空值回退默认值 | `val ?? fallback`（空值合并） | `fallback if val is None else val` | 用 `or` 会像 JS `\|\|` 一样误盖 `0`、`""`、`False` |
| 成员判断 | `arr.includes(x)`；`k in obj` 查属性 | `x in seq`；`k in d` 查键，`v in d.values()` 查值 | 字符串用 `in` 查子串，类似 `str.includes(sub)` |
| 值相等 vs 对象身份 | 对象 `===` 仅比引用，不比内容 | `==` 比较内容，`is` 比较对象身份 | 比较列表/字典内容用 `==`，判空用 `is None` |
| 整数位运算位数 | 普通 `Number` 先转 32 位有符号整数 | `int` 任意精度，左移不丢弃高位 | 两边均须区分按位与 `&` 与逻辑与 `and` / `&&` |

## 【补充】原教程勘误与不推荐写法

- **比较表称返回 `1` 和 `0`**：原文描述“所有比较运算符返回 1 表示真，返回 0 表示假”，实际 Python 3 内置值比较返回的是布尔值 `True` 和 `False`（只是 `bool` 是 `int` 子类）。
- **左移“高位丢弃”不适用于 Python 整数**：Python 的 `int` 是任意精度整数，左移会按需扩展位数，不会截断丢弃高位，等价于乘 `2 ** 位数`。
- **用小整数演示 `is` 容易误导**：原文用 `a = 20; b = 20` 演示 `a is b`，该结果依赖 CPython 的小整数缓存细节；验证值相等与对象身份应改用列表别名和切片副本（`a[:]`）。
- **`id()` 的语言语义**：原文称 `id()` “获取对象内存地址”，这是 CPython 的具体实现细节；语言规范定义 `id()` 返回的是对象在存活期内唯一且不变的整数标识。
- **优先级示例把“分组”误写成“先算 `and`”**：原文注释称 `x or y and z` 是“先算 `y and z`”。准确来说，`and` 优先级高于 `or` 决定了语法分组为 `x or (y and z)`；但实际从左到右求值，当 `x` 为 `True` 时，右侧整个 `and` 子表达式会被短路跳过，根本不会执行。
- **代码格式与废弃写法**：原文多处写有 `print (...)`、`if ( a == b ):`、用内置名 `list` 做变量名以及提及 Python 2 的 `<>`；日常应遵守 PEP 8（`print(...)`、`if a == b:`、不用内置名作变量名、不等统一写 `!=`）。参考 [Python 3.11 表达式参考](https://docs.python.org/3.11/reference/expressions.html)。
