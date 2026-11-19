# Python3 数据类型转换

参考：[菜鸟教程：Python3 数据类型转换](https://www.runoob.com/python3/python3-type-conversion.html)

```powershell
python .\lessons\day01-python\03-type-conversion\example.py
```

`example.py` 是汇总示例。下面的文件按知识点分别练习，在项目根目录运行时，将命令中的文件名替换为相应文件即可：

1. `01-implicit.py`：数字的隐式转换，以及字符串与数字不能直接相加。
2. `02-numbers-and-strings.py`：数字、字符串、布尔值与进制之间的转换。
3. `03-containers.py`：列表、元组、集合和字典之间的转换。
4. `04-characters-and-bytes.py`：字符、Unicode 码点、文本和字节。
5. `05-errors.py`：转换失败、异常处理和安全解析字面量。

每个文件都可以独立运行，例如：

```powershell
python .\lessons\day01-python\03-type-conversion\01-implicit.py
```

## 隐式转换

某些运算中 Python 会自动处理兼容的数字类型，例如 `1 + 2.5` 的结果是浮点数 `3.5`。字符串和数字不能直接用 `+` 相加，需要先显式转换。自动转换并不保证所有计算都没有精度损失。

## 显式转换

通过类型名调用构造函数，转换后通常得到新对象，原变量不会自动改变。

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
| `chr(x)`、`ord(x)` | Unicode 码点与单个字符互转 | `chr(65)`、`ord("A")` |
| `bin(x)`、`oct(x)`、`hex(x)` | 整数转为带进制前缀的字符串 | `bin(5)` 得到 `"0b101"` |

### 示例中补充的用法

- `"False".lower()` 返回小写字符串 `"false"`；与 `"true"` 比较的结果是 `False`。这种比较只演示如何识别 `true`，并没有验证所有其他输入。
- `person.items()` 提供字典键值对，`list(person.items())` 将它们变成列表；`list(person)` 只取键。集合会去重，而 `len()` 返回元素数量。
- 文本的 `.encode("utf-8")` 和字节的 `.decode("utf-8")` 分别进行编码和解码。`bytearray` 是可修改的字节序列，`bytes(mutable)` 转成不可变的字节序列；一个字节的整数值为 0 到 255。
- `chr(65)` 用 Unicode 码点得到字符 `"A"`，`ord("A")` 则得到码点 65；`ord()` 接受单个字符。

### 异常处理和字面量解析

`05-errors.py` 中的 `for value in (...)` 依次取出括号中的值。`try` 内的转换失败时，匹配的 `except ValueError` 或 `except TypeError` 会处理错误；没有发生异常时才执行 `else`。例如 `int("abc")` 的输入类型可以接受，但内容不是整数，因此引发 `ValueError`；`int(None)` 的输入类型不适合，因此引发 `TypeError`。

`f"{value!r}"` 是格式化字符串：把 `value` 的表示形式插入字符串，`!r` 使用类似 `repr(value)` 的形式，便于看清字符串的引号。`None` 表示没有值。

`ast` 是 Python 自带的标准库模块，`from ast import literal_eval` 从中导入 `literal_eval`。例如 `literal_eval("[1, 2, 3]")` 把表示列表字面量的字符串解析为列表；`literal_eval("1 + 2")` 不接受这个算术表达式，会引发 `ValueError`。这项内容是对源教程的补充。

## 常见问题

- `int("3.5")` 会报 `ValueError`：它不是整数字符串。可以先用 `float()`，再用 `int()`，但小数部分会被截去。
- `bool("False")` 是 `True`，因为它是非空字符串；若要解析用户输入，需要明确比较文本。
- `set()` 会去重，不能依赖集合的显示顺序；`dict()` 需要可用的键值对。
- 不要对不可信输入使用 `eval()`：它会执行表达式。只需解析数字时，使用 `int()` 或 `float()`。
- `ast.literal_eval()` 可解析字符串、数字、列表、字典等 Python 字面量，不能执行任意表达式；仍需限制不可信输入的大小和复杂度。
- 转换失败可能抛出 `ValueError` 或 `TypeError`，可以使用 `try` / `except` 处理。
