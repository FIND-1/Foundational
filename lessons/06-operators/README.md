# 第 6 章 · Python3 运算符

学习模式：Core Learning（重点学习）

阅读材料：[菜鸟教程原文 HTML](../../source/06-operators.html)（在浏览器中打开）

## 学习步骤

1. 按原文正文顺序阅读「算术 → 比较 → 赋值 → 位运算 → 逻辑 → 成员 → 身份 → 优先级」。把运算符作用的值称为操作数，例如 `4 + 5` 中的 `4` 和 `5`。
2. 根据下方要点预测 4 个 Demo 的输出，再按顺序运行。重点留意负数整除、逻辑运算的返回值和列表的对象身份。
3. 完成 `exercises_06.py` 的基础题，用 `-m basic` 检查结果。选做函数题时，回顾 `def`、`return` 和 `if`。
4. 在 [notes.md](notes.md) 记录一处结果和自己原先预测不同的地方，以及验证方法。

## 要点（按原文正文顺序）

| 主题 | 本章要会解释 |
| --- | --- |
| 算术 | `+`、`-`、`*`、`/`、`%`、`**`、`//`。`7 / 3` 得到小数，`-7 // 3` 向下取整得到 `-3`，`-7 % 3` 得到 `2`。对于整数，`被除数 = 整除商 * 除数 + 余数`。 |
| 比较 | `==`、`!=`、`<`、`<=`、`>`、`>=`。对本章使用的内置值，结果是 `bool`。`下界 <= 值 < 上界` 同时检查两侧，中间表达式只求值一次。不支持排序的值用大小运算符比较时可能抛 `TypeError`，例如 `3 < "4"`。 |
| 赋值 | `=` 把右侧求出的值绑定到左侧。`+=`、`-=`、`*=`、`/=`、`%=`、`**=`、`//=` 先运算再写回，列表 `+=` 还会原地扩展。`:=` 在表达式里给名字赋值，并产生该值。比较长度时用 `(n := len(items)) > 2` 明确分组，日常可先写一行常规赋值。 |
| 位运算 | `&` 与、`\|` 或、`^` 异或、`~` 取反、`<<` 左移、`>>` 右移。对整数，`~x` 等于 `-x - 1`，右移 `n` 位相当于整除 `2 ** n`。 |
| 逻辑 | `and` 遇到假值就返回左操作数，`or` 遇到真值就返回左操作数。否则两者都会求值并返回右操作数。`not` 返回反转后的布尔值。真假值规则见[第 2 章 `bool()` 速查](../02-basic-data-types/functions.md#必会bool)。 |
| 成员 | `in`、`not in` 检查成员。字符串查子串，列表和元组查元素，字典默认查键。 |
| 身份 | `is`、`is not` 检查两个引用是否指向同一对象。`==` 检查值是否相等。可用 `id()` 观察对象标识，判空用 `is None`。 |
| 优先级 | 本章常用顺序从高到低为乘除取模组 → 加减 → 移位 → `&` → `^` → `\|` → 比较、成员与身份 → `not` → `and` → `or`。幂运算向右分组，`-2 ** 2` 得到 `-4`。条件表达式也向右分组。完整表包括调用、下标、`await`、`@`、`lambda` 和 `:=`。[Python 3.11 优先级表](https://docs.python.org/3.11/reference/expressions.html#operator-precedence) |

## 【补充】JS/TS 对照与原文勘误

- JS/TS 的 `//` 开始注释。整除可类比 `Math.floor(a / b)`。整数取模时，Python 的非零余数与除数同号，JS 的 `%` 与被除数同号。例如 Python `-7 % 3` 得 `2`，JS 得 `-1`。
- Python 用 `and`、`or`、`not` 表达 JS 的 `&&`、`||`、`!`。两边的短路方式相近，空列表和空字典在 Python 中是假值，JS 的空数组和空对象是真值。默认值只应替换 `None` 时，用 `默认值 if 值 is None else 值` 保留 `0` 和空字符串。
- Python 列表的 `==` 会比较内容。`is` 检查对象身份，类似 JS 对对象做 `===`；JS 的 `in` 查对象属性，Python 的列表成员判断更接近 `includes()`。Python 的 `==` 不会把数字文本自动转换为数字，`3 == "3"` 得到 `False`。
- 原文把 Python 左移描述为丢弃高位。Python 的整数可按需增加位数，左移等价于乘 `2 ** 位数`。JS 的普通 `Number` 按位运算会转成 32 位整数。两边都应区别按位与 `&` 和短路逻辑与。
- 原文比较表将结果写作 `1` 和 `0`，本章的内置值比较得到 `True` 或 `False`。原文的整数身份示例受对象复用影响，课程改用列表别名和切片副本。`id()` 的语言语义是对象标识，CPython 用地址实现。原文优先级示例把分组写成「先算 and」。当 or 左侧为真时，右侧的 and 子表达式会被跳过。日常不等判断用 `!=`。[Python 3.11 表达式参考](https://docs.python.org/3.11/reference/expressions.html)

## 文件

| 文件 | 内容 |
| --- | --- |
| [01_arith_compare_demo.py](01_arith_compare_demo.py) | 四则、乘方、整除和取模、六种比较、链式区间 |
| [02_assignment_demo.py](02_assignment_demo.py) | 增量赋值、列表别名、常规赋值与海象运算符 |
| [03_bitwise_logic_demo.py](03_bitwise_logic_demo.py) | 位运算、权限位、逻辑短路 |
| [04_member_id_demo.py](04_member_id_demo.py) | 字符串、列表和字典成员，身份、分组 |
| [functions.md](functions.md) | 本章首次引入的 `id()`，以及前章 API 的入口 |
| [exercises_06.py](exercises_06.py) | 四组基础题、两道选做函数题 |
| [test_demos_06.py](test_demos_06.py)、[test_exercises_06.py](test_exercises_06.py) | Demo 自检与分层练习验收 |
| [notes.md](notes.md) | 个人验证和错题复盘 |

## 运行

在仓库根目录打开 PowerShell。环境准备见[第 1 章「运行」](../01-basic-syntax/README.md#运行)。

```powershell
.\.venv\Scripts\python.exe .\lessons\06-operators\01_arith_compare_demo.py
.\.venv\Scripts\python.exe .\lessons\06-operators\02_assignment_demo.py
.\.venv\Scripts\python.exe .\lessons\06-operators\03_bitwise_logic_demo.py
.\.venv\Scripts\python.exe .\lessons\06-operators\04_member_id_demo.py

.\.venv\Scripts\python.exe -m pytest lessons/06-operators -m basic -v
.\.venv\Scripts\python.exe -m pytest lessons/06-operators -m advanced -v
.\.venv\Scripts\python.exe -m pytest lessons/06-operators -v
```

练习占位未填写时显示 `SKIPPED`。基础题通过后，能说明选用哪个运算符以及取值边界，才勾选基础验收。

## 学习验收标准

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成，能解释负数整除和取模、逻辑短路、`is` 与 `==`，并用括号表示一条混合表达式的分组。
- [ ] 基础练习通过，独立完成四组基础题，`-m basic` 全部通过并能说明写法。
- [ ] 进阶练习通过（可选），能保留列表中的假值，并更新单个权限位。
- [ ] 本章完成
