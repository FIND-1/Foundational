# 【补充】第三章 Python 3.11 转换函数速查

`/` 前只能按位置传参；`*` 后只能按名字传参。没有默认值的参数必填。先掌握【必会】；【了解】不要求现在记住。

## 【必会】数字和字符串

- 【必会】`int("101", 2)` 按二进制解析得到 5。浮点数向零截断，无穷大转整数抛 `OverflowError`。`int` 和 `str` 的重载、默认值与关键字限制见[第 1 章函数速查](../01-basic-syntax/functions.md)。
- `float(x=0.0, /)`：接受数字或可解析的字符串等，返回浮点数；类型不合适抛 `TypeError`，文本格式错误抛 `ValueError`。例 `float("3.5")`。
- `str(12)` 得到文本 `"12"`；若指定编码，输入须是字节类对象。
- `bool("False")` 为 `True`。真假规则、参数和例子见[第 2 章函数速查](../02-basic-data-types/functions.md)。
- `complex(real=0, imag=0)`：【了解】数字表示实部和虚部；`real` 是字符串时不得同时提供 `imag`。返回复数；类型错误抛 `TypeError`，字符串格式错误抛 `ValueError`。例 `complex(2, 3)` 得 `(2+3j)`。
- `repr(obj, /)`：【了解】返回表示对象的字符串；缺少参数抛 `TypeError`，对象自定义表示也可能抛异常。例 `repr("hi")` 包含引号。

## 【了解】容器

- `tuple(iterable=(), /)`：省略时为空元组，否则从可迭代对象构造元组；返回元组，参数不可迭代抛 `TypeError`。例 `tuple([1, 2])`。
- `frozenset(iterable=(), /)`：省略时创建空的不可变集合，否则从可迭代对象构造并去重；返回 `frozenset`，输入不可迭代或元素不可哈希时抛 `TypeError`。例 `frozenset([1, 1])` 得 `frozenset({1})`。
- `dict([("a", 1)])` 接收键值对，若键重复，最后一个值生效。签名与限制见[第 2 章函数速查](../02-basic-data-types/functions.md)。
- `list`、`bytes`、`bytearray` 及编码和解码见[第 2 章速查](../02-basic-data-types/functions.md)；`set`、`len`、`type` 和 `print` 见[第 1 章速查](../01-basic-syntax/functions.md)。
- `dict.items()`：无参数，返回键值对视图；额外参数抛 `TypeError`。例 `list({"a": 1}.items())`。
- `str.lower()`：无参数，返回转换为小写的新字符串；额外参数抛 `TypeError`。例 `"FALSE".lower()` 得 `"false"`。

## 【了解】字符、进制和字面量

- `chr(i, /)`：必填整数码点，返回单字符字符串；范围为 0 到 0x10FFFF，越界抛 `ValueError`，类型不合适抛 `TypeError`。例 `chr(65)` 得 `"A"`。`ord(c, /)` 的完整说明见[第二章速查](../02-basic-data-types/functions.md)。
- `bin(number, /)`、`oct(number, /)`、`hex(number, /)`：均需一个整数或支持整数索引的对象，分别返回带 `0b`、`0o`、`0x` 前缀的字符串；类型不支持抛 `TypeError`。例 `hex(10)` 得 `"0xa"`。
- `ast.literal_eval(node_or_string)`：必填 Python 字面量文本或表达式 AST 节点；返回解析后的值，不执行任意代码。无效输入可抛 `ValueError`、`SyntaxError` 或 `TypeError`；不可信的大型或深层输入也可能耗尽资源。例 `literal_eval("[1, 2]")` 得列表，先写 `from ast import literal_eval`。
- `eval(source, globals=None, locals=None, /)`：`source` 是表达式字符串或代码对象；`globals` 为全局命名空间字典，`locals` 为局部命名空间映射，均可省略。两者都省略时使用调用处的命名空间；只提供 `globals` 时它也作为局部命名空间。返回表达式结果；语法错误抛 `SyntaxError`，执行中的错误会继续抛出。例 `eval("1 + 2")` 得 3。它会执行表达式，不能用于不可信输入；单纯解析数字用 `int()` 或 `float()`。
- `memoryview(object, /)`：`object` 必填且只能按位置传入，必须支持缓冲区协议，例如 `bytes` 或 `bytearray`；返回该对象的内存视图，不支持缓冲区的对象会抛 `TypeError`。例 `memoryview(b"AB")`。
- `ascii(obj, /)`：`obj` 必填且只能按位置传入，返回对象表示形式的字符串，其中非 ASCII 字符被转义；参数数量错误抛 `TypeError`，对象自定义表示也可能抛出异常。例 `ascii("雨")` 返回包含 `\\u96e8` 的表示字符串。
