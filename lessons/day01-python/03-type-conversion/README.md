# Python3 数据类型转换

[打开本章教程原文](../../../source/03-type-conversion.html)（在 VS Code 中右键该文件，选择 Open with Live Server，或在浏览器中打开）。六个实例已按主题放进本章 Python 文件，原有扩展示例标为【补充】。

`01-implicit.py` 中字符串与整数相加的代码以注释保留；取消注释运行时会产生 `TypeError`，这是原教程的预期结果。`02-numbers-and-strings.py` 中的 `int`、`float`、`str` 三段原例只有赋值，不单独产生输出。

参考：[菜鸟教程：Python3 数据类型转换](https://www.runoob.com/python3/python3-type-conversion.html)

原文章节顺序为隐式转换 → 显式转换。先掌握这两节，再阅读下方【补充】。示例函数的完整参数和错误见 [函数速查](functions.md)，阅读后完成 [本章练习](practice.md)。

```powershell
.\.venv\Scripts\python.exe .\lessons\day01-python\03-type-conversion\example.py
```

在仓库根目录先运行以下主题脚本，再用 `example.py` 复习。将上面命令中的文件名换成对应脚本即可。

1. `01-implicit.py`：数字的隐式转换，以及字符串与数字不能直接相加。
2. `02-numbers-and-strings.py`：数字、字符串、布尔值与进制之间的转换。
3. `03-containers.py`：【补充】列表、元组、集合和字典之间的转换。
4. `04-characters-and-bytes.py`：【补充】字符、Unicode 码点、文本和字节。
5. `05-errors.py`：【补充】转换失败、异常处理和字面量解析。

每个文件都可以独立运行，例如：

```powershell
.\.venv\Scripts\python.exe .\lessons\day01-python\03-type-conversion\01-implicit.py
```

## 隐式转换

某些运算中 Python 会自动处理兼容的数字类型，例如 `1 + 2.5` 的结果是浮点数 `3.5`。字符串和数字不能直接用 `+` 相加，需要先显式转换。自动转换并不保证所有计算都没有精度损失。

## 显式转换

转换表达式返回一个值。观察 `example.py` 的两种赋值方式：原教程将转换结果写回同一个名字；【补充】示例同时保留原始输入和可计算的数量。试着预测哪一行输出会保留 `"0456"` 开头的零。

| 写法 | 作用 | 示例 |
| --- | --- | --- |
| `int(x)` | 转整数；浮点数向 0 截断 | `int(-3.8)` 得到 `-3` |
| `int(text, base)` | 按指定进制解析字符串 | `int("101", 2)` 得到 `5` |
| `float(x)` | 转浮点数 | `float("3.5")` 得到 `3.5` |
| `complex(x)` | 转复数 | `complex(2)` 得到 `(2+0j)` |
| `str(x)` | 转适合展示的字符串 | `str(123)` 得到 `"123"` |
| `repr(x)` | 转便于查看对象表示的字符串 | `repr("hi")` 包含引号 |
| `bool(x)` | 根据真假规则转换 | `bool(0)` 为 `False` |
| `list(x)`、`tuple(x)`、`set(x)` | 把可迭代对象转为对应容器 | `list("ab")` 得到 `['a', 'b']` |
| `dict(x)` | 根据键值对创建字典 | `dict([("a", 1)])` |
| `frozenset(x)` | 转为不可变集合 | `frozenset([1, 1])` 得到包含 `1` 的不可变集合 |
| `eval(source)` | 求 Python 表达式的值 | `eval("1 + 2")` 得到 `3`；不要用于不可信输入 |
| `chr(x)`、`ord(x)` | Unicode 码点与单个字符互转 | `chr(65)`、`ord("A")` |
| `bin(x)`、`oct(x)`、`hex(x)` | 整数转为带进制前缀的字符串 | `bin(5)` 得到 `"0b101"` |
| `bytes(x)`、`bytearray(x)` | 创建不可变或可变字节序列 | `bytes([65])` 得到 `b'A'` |
| `memoryview(x)` | 创建支持缓冲区对象的内存视图 | `memoryview(b'AB')` 创建一个视图 |
| `ascii(x)` | 返回对象的 ASCII 表示 | `ascii("雨")` 会把非 ASCII 字符转义 |

### 【补充】示例中补充的用法

- `"False".lower()` 返回小写字符串 `"false"`；与 `"true"` 比较的结果是 `False`。这种比较只演示如何识别 `true`，并没有验证所有其他输入。
- `person.items()` 提供字典键值对，`list(person.items())` 将它们变成列表；`list(person)` 只取键。集合会去重，而 `len()` 返回元素数量。
- 文本的 `.encode("utf-8")` 和字节的 `.decode("utf-8")` 分别进行编码和解码。`bytearray` 是可修改的字节序列，`bytes(mutable)` 转成不可变的字节序列；一个字节的整数值为 0 到 255。
- `chr(65)` 用 Unicode 码点得到字符 `"A"`，`ord("A")` 则得到码点 65；`ord()` 接受单个字符。

### 【补充】异常处理和字面量解析

`05-errors.py` 中的 `for value in (...)` 依次取出括号中的值。`try` 内的转换失败时，匹配的 `except ValueError` 或 `except TypeError` 会处理错误；没有发生异常时才执行 `else`。例如 `int("abc")` 的输入类型可以接受，但内容不是整数，因此引发 `ValueError`；`int(None)` 的输入类型不适合，因此引发 `TypeError`。

这些控制语句属于后续学习内容，在此仅为演示错误而提前使用，不是本章练习的要求。预期异常被相应的 `except` 捕获并输出说明；其他异常不会被捕获，应视为运行失败。

`f"{value!r}"` 是格式化字符串：把 `value` 的表示形式插入字符串，`!r` 使用类似 `repr(value)` 的形式，便于看清字符串的引号。`None` 表示没有值。

`ast` 是 Python 自带的标准库模块，`from ast import literal_eval` 从中导入 `literal_eval`。例如 `literal_eval("[1, 2, 3]")` 把表示列表字面量的字符串解析为列表；`literal_eval("1 + 2")` 不接受这个算术表达式，会引发 `ValueError`。这项内容是对源教程的补充。

## 【补充】常见问题

- `int("3.5")` 会报 `ValueError`：它不是整数字符串。可以先用 `float()`，再用 `int()`，但小数部分会被截去。
- `bool("False")` 是 `True`，因为它是非空字符串；若要解析用户输入，需要明确比较文本。
- `set()` 会去重，不能依赖集合的显示顺序；`dict()` 需要可用的键值对。
- 不要对不可信输入使用 `eval()`：它会执行表达式。只需解析数字时，使用 `int()` 或 `float()`。
- `ast.literal_eval()` 可解析字符串、数字、列表、字典等 Python 字面量，不能执行任意表达式；仍需限制不可信输入的大小和复杂度。
- 转换失败可能抛出 `ValueError` 或 `TypeError`，可以使用 `try` / `except` 处理。

## 学习验收

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能解释转换前后的值与类型。
- [ ] 基础练习通过：独立完成 [本章练习](practice.md)，按其中的验收条件核对结果。
- [ ] 进阶练习通过（可选，分层题待迁移）
- [ ] 本章完成：能回答理解检查中的问题，并独立得到基础练习要求的结果。
