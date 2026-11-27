# 第 3 章 · 数据类型转换

阅读材料：[source/03-type-conversion.html](../../source/03-type-conversion.html)（菜鸟教程原文，在浏览器中打开）

## 学习步骤

1. **读原文**（约 10 分钟）：按「隐式类型转换 → 显式类型转换 → 内置转换函数表」顺序通读，了解有哪些转换函数，不必死记表格。
2. **读本页与函数速查**：看「要点」「和 JS 的差异」「原教程勘误」，本章新遇到的函数与方法查 [functions.md](functions.md)；前两章已讲的函数查[第 1 章速查](../01-basic-syntax/functions.md)和[第 2 章速查](../02-basic-data-types/functions.md)。
3. **跑 demo**：按下方顺序运行 5 个 `*_demo.py`，先预测再观察 `print()` 输出；标为 `# 拓展：` 的 `frozenset`、`memoryview`、`eval`、`ast.literal_eval` 和 `try...except` 只作观察，暂不要求手写。
4. **做基础练习**：完成 `exercises_03.py` 的「基础练习」（先写五组表达式，再独立写一段终端读入两行整数文本并求和的脚本），用 pytest 验证（用法见 [pytest 教程](../tooling/pytest/README.md)）。
5. **选做进阶练习**：若已了解 `def` / `return` / `try...except`，可继续挑战「进阶练习」（含异常捕获与安全字面量解析）。
6. **阶段复盘**：学到哪一小节就顺手把自己的理解、验证、JS 差异和易错点记进 `notes.md`（按需选填，不提前填未学内容，也不仅凭测试通过就标记掌握）。

## 学习验收标准

请按实际掌握情况勾选（不能仅凭跑通 demo 就勾选“本章完成”）：

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能预测整数与浮点数相加后的类型与原变量类型；能解释为什么字符串 `"12"` 不能直接与整数 `3` 相加、为什么 `int("3.5")` 会报 `ValueError`、`int(-3.9)` 为什么得 `-3`、`bool("False")` 为什么为 `True`，以及用同名覆盖与新变量保存（如 `"0456"`）的区别。
- [ ] 基础练习通过：独立完成六组题，`-m basic` 全部显示 `PASSED`，并能用自己的话说明每题用了什么转换函数、为什么这样写（并确认原变量未被误改）。
- [ ] 进阶练习通过（可选）
- [ ] 本章完成：读完原文、能解释示例、基础测试全过，并在 `notes.md` 记录易错点或自己的验证过程。

## 文件

| 文件 | 内容 |
| --- | --- |
| `01_implicit_demo.py` | 隐式类型转换（`int + float`）、原变量类型不变、字符串与数字不能直接相加 |
| `02_numbers_str_demo.py` | 显式转换：`int()`、`float()`、`str()`、保留原始输入、向零截断、`complex()`、`repr()`/`ascii()`、`bool()` 与 `str.lower()`、进制解析与 `bin()`/`oct()`/`hex()` |
| `03_containers_demo.py` | 容器转换：`list()`、`tuple()`、`set()` 去重、`frozenset()`、`dict()` 构造与重复键覆盖、字典转列表只取键 vs `items()` |
| `04_chars_bytes_demo.py` | 字符与字节：`chr()` 与 `ord()` 互转、`encode`/`decode` 复习、整数列表转 `bytes`/`bytearray`、`memoryview()` 零拷贝视图 |
| `05_errors_parse_demo.py` | 【补充】拓展：区分 `ValueError` 与 `TypeError`、`for` + `try/except/else`、`f"{value!r}"`、`eval()` 安全风险与 `ast.literal_eval()` |
| [functions.md](functions.md) | 本章首次引入的函数与方法完整速查（含签名、参数限制、异常与 JS 对照） |
| `exercises_03.py` | 基础练习（必做，写表达式和输入输出）+ 进阶练习（可选，写函数与异常处理） |
| `test_exercises_03.py` | 练习的自动测试，不要修改 |
| `test_demos_03.py` | 5 个 Demo 的自检；运行全章 pytest 时执行 |
| `notes.md` | 个人学习笔记与错题复盘（记录理解、验证、差异、易错点与待解问题） |

## 运行

在仓库根目录打开 PowerShell。环境准备见[第 1 章 README 的「运行」](../01-basic-syntax/README.md#运行)。

```powershell
.\.venv\Scripts\python.exe .\lessons\03-type-conversion\01_implicit_demo.py
.\.venv\Scripts\python.exe .\lessons\03-type-conversion\02_numbers_str_demo.py
.\.venv\Scripts\python.exe .\lessons\03-type-conversion\03_containers_demo.py
.\.venv\Scripts\python.exe .\lessons\03-type-conversion\04_chars_bytes_demo.py
.\.venv\Scripts\python.exe .\lessons\03-type-conversion\05_errors_parse_demo.py

.\.venv\Scripts\python.exe .\lessons\03-type-conversion\exercises_03.py   # 手动体验基础题 6，分两行输入两个整数

.\.venv\Scripts\python.exe -m pytest lessons/03-type-conversion -m basic -v   # 只测基础练习
.\.venv\Scripts\python.exe -m pytest lessons/03-type-conversion -v            # 测全部练习和 Demo 自检
```

`PASSED`、`FAILED`、`SKIPPED` 和 `deselected` 的含义与处理方法见[第 1 章 README 的「运行」](../01-basic-syntax/README.md#运行)。

## 要点（按原文顺序）

1. **隐式类型转换**：兼容的数字类型参与运算时，Python 会自动把范围较小的类型提升为更大的类型（如 `int + float -> float`、`bool + int -> int`），返回新对象，不改变原变量的类型。字符串与数字不能隐式转换，直接用 `+` 会抛 `TypeError`。
2. **显式类型转换**：使用类型名或内置转换函数主动转换，返回转换结果，不会自动修改原变量（是否创建新对象取决于具体类型和转换方式，例如对已有元组调用 `tuple()` 可能直接返回原对象）。需要保留原始输入格式（如 `"0456"` 的前导零）时，应把结果赋给新变量名而不是覆盖原变量。
3. **常用内置转换函数总览**：

| 函数 | 作用 | 示例 | 说明 |
| --- | --- | --- | --- |
| `int(x)` / `int(text, base)` | 转整数；浮点向零截断；按进制解析字符串 | `int(-3.9)` 得 `-3`；`int("101", 2)` 得 `5` | `int("3.5")` 抛 `ValueError` |
| `float(x)` | 转浮点数 | `float("3.5")` 得 `3.5` | 无效文本抛 `ValueError` |
| `complex(real, imag)` | 创建复数 | `complex(2, 3)` 得 `(2+3j)` | 虚部默认 `0` |
| `str(x)` | 转适合展示的字符串 | `str(123)` 得 `"123"` | 面向阅读输出 |
| `repr(x)` | 转偏向代码/调试的字符串表示 | `repr("hi")` 得 `"'hi'"` | 可区分 `"42"` 与 `42` |
| `ascii(x)` | 转纯 ASCII 表示字符串 | `ascii("雨")` 得 `"'\\u96e8'"` | 非 ASCII 字符被转义 |
| `bool(x)` | 按真值规则转布尔值 | `bool(0)` 得 `False`；`bool("False")` 得 `True` | 解析真假文本需先 `.lower()` 再比较 |
| `list(s)`、`tuple(s)`、`set(s)` | 把可迭代对象转为对应容器 | `tuple("ab")` 得 `('a', 'b')` | `set()` 去重且无序 |
| `frozenset(s)` | 转为不可变集合 | `frozenset([1, 1])` 得 `frozenset({1})` | 可哈希，能作字典键 |
| `dict(d)` | 从键值对序列、映射或关键字创建字典 | `dict([("a", 1)])` 得 `{'a': 1}` | 重复键以后者覆盖前者 |
| `chr(i)`、`ord(c)` | Unicode 码点与单字符互转 | `chr(65)` 得 `'A'`；`ord("A")` 得 `65` | 互为逆运算 |
| `bin(n)`、`oct(n)`、`hex(n)` | 整数转带前缀的二、八、十六进制字符串 | `bin(10)` 得 `'0b1010'`；`hex(10)` 得 `'0xa'` | 只接受整数 |
| `bytes(...)`、`bytearray(...)` | 创建不可变或可变字节序列 | `bytes([65, 66])` 得 `b'AB'` | 整数须在 0～255 |
| `memoryview(obj)` | 创建支持缓冲区对象的零拷贝内存视图 | `memoryview(bytearray(b"AB"))` | 修改视图会直接改原缓冲区 |
| `eval(source)` | 执行 Python 表达式字符串并返回结果 | `eval("1 + 2")` 得 `3` | **严禁用于不可信输入**；安全解析字面量用 `ast.literal_eval()` |

## 【补充】和 JS 的差异

| 主题 | JS | Python | 注意 |
| --- | --- | --- | --- |
| 字符串与数字相加 | `"123" + 1 === "1231"` | `TypeError` | Python 是强类型，必须先显式写 `int()` 或 `str()` |
| 解析小数字符串为整数 | `parseInt("3.5", 10) === 3` | `int("3.5")` 抛 `ValueError` | 需先 `float("3.5")` 再 `int(...)` |
| 解析带垃圾后缀的文本 | `parseInt("42px", 10) === 42` | `int("42px")` 抛 `ValueError` | Python 严格校验整个字符串（允许首尾空白） |
| 浮点转整数 | `Math.trunc(-3.9) === -3` | `int(-3.9) == -3` | `int()` 向零截断；区分于 `//` 向下取整（`-7 // 2 == -4`） |
| 无效数字转浮点 | `Number("abc")` 得 `NaN` | `float("abc")` 抛 `ValueError` | 不会悄悄返回 `NaN` 污染后续计算 |
| 布尔文本转换 | `Boolean("False") === true` | `bool("False") is True` | 两边都按“非空即真”；解析文本需先 `s.lower() == "true"` |
| 进制格式化 | `(10).toString(16) === "a"` | `hex(10) == "0xa"` | Python 默认带 `0b` / `0o` / `0x` 前缀 |
| 字符与码点 | `String.fromCodePoint(65)` / `"A".codePointAt(0)` | `chr(65)` / `ord("A")` | Python 完整支持全部 Unicode 码点 |
| 调试表示 | `JSON.stringify(x)` / `util.inspect(x)` | `repr(x)` / `f"{x!r}"` | `str()` 给用户看，`repr()` 给开发者调试看 |
| 字典/对象与键值对 | `Object.fromEntries(pairs)` / `Object.entries(obj)` | `dict(pairs)` / `list(d.items())` | `list(d)` 只取键，不取键值对 |
| 零拷贝内存视图 | `DataView` / `Uint8Array` | `memoryview(buf)` | `memoryview` 不复制底层字节 |
| 表达式与安全解析 | `eval()` / `JSON.parse()` | `eval()` / `ast.literal_eval()` / `json.loads()` | 两者 `eval` 都危险；跨系统优先 JSON |
| 转换错误分类 | 多返回 `NaN` 或静默转换 | `ValueError`（值非法）/ `TypeError`（类型不符） | 如 `int("abc")` 抛 `ValueError`，`int(None)` 抛 `TypeError` |

## 【补充】原教程勘误与不推荐写法

- **输出多了一个冒号**：原文隐式转换代码写的是 `print("num_new 值为:", num_new)`，但下方示例输出误写成 `num_new: 值为: 124.23`（实际输出没有 `num_new` 后的冒号）。
- **“隐式转换以避免数据丢失”不够严谨**：`int` 任意精度，而 `float` 只有约 53 位有效二进制精度；超大整数（超过 `2**53`）转为 `float` 时反而会损失精度，且十进制小数转二进制浮点本身也有舍入误差（如 `0.1 + 0.2`）。
- **同名覆盖丢掉原输入**：原文将 `num_str = int(num_str)` 覆盖回原变量，导致名字叫 `num_str` 但值已是 `int`，且会丢掉原始文本格式（如 `"0456"` 的前导零）。实战中更推荐用新变量名保存转换结果（如 `quantity = int(quantity_text)`）。
- **`int()` / `float()` / `str()` 三段原例未打印**：原文仅写赋值并在注释中称“输出结果为 ...”，脚本直接运行时终端不会显示结果；本章 `02_numbers_str_demo.py` 补上了 `print()`。
- **“dict(d)：d 必须是一个 (key, value) 元组序列”偏窄**：实际上 `dict()` 还支持其他字典/映射、`dict(a=1, b=2)` 关键字参数，以及任意长度为 2 的可迭代对象组成的序列（如 `[["a", 1]]`）。
- **`eval(str)` 未提示安全风险**：原文表格直接列出 `eval(str)` 而未警告其会执行任意代码。日常解析数字用 `int()` / `float()`，解析 Python 字面量用标准库 `ast.literal_eval()`，解析 JSON 用 `json.loads()`，切勿对不可信输入使用 `eval()`。
