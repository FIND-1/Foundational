# 【补充】第三章 Python 3.11 转换函数速查

`/` 前只能按位置传参；`*` 后只能按名字传参。没有默认值的参数必填。先掌握【必会】；【了解】不要求现在记住。

## 【必会】数字和字符串

- `int([x])` 或 `int(x, base=10)`：方括号表示 `x` 可省略，省略得 0；`x` 只能按位置传入，`base` 可按位置或名称传入。数字转整数时向零截断。`base` 指定字符串、bytes 或 bytearray 的进制，范围为 2～36 或 0；显式提供 `base` 时 `x` 必须是前述文本形式。返回整数；类型错误抛 `TypeError`，内容或进制不合法抛 `ValueError`，无穷大转整数抛 `OverflowError`。例 `int("101", 2)` 为 5。
- `float(x=0.0, /)`：接受数字或可解析的字符串等，返回浮点数；类型不合适抛 `TypeError`，文本格式错误抛 `ValueError`。例 `float("3.5")`。
- `str(object='', /)` 或 `str(object=b'', encoding='utf-8', errors='strict')`：无参数返回空字符串；仅传对象返回可读字符串；提供编码时对象必须是字节类对象，按 `encoding` 解码，`errors` 为错误处理策略。返回字符串；类型错误抛 `TypeError`，编码未知抛 `LookupError`，解码失败可抛 `UnicodeDecodeError`。例 `str(12)` 得 `"12"`。
- `bool(x=False, /)`：根据对象的真假规则返回 `True` 或 `False`；无参数为 `False`。最多一个位置参数，传入过多或关键字参数抛 `TypeError`。例 `bool("False")` 为 `True`。
- `complex(real=0, imag=0)`：【了解】数字表示实部和虚部；`real` 是字符串时不得同时提供 `imag`。返回复数；类型错误抛 `TypeError`，字符串格式错误抛 `ValueError`。例 `complex(2, 3)` 得 `(2+3j)`。
- `repr(obj, /)`：【了解】返回表示对象的字符串；缺少参数抛 `TypeError`，对象自定义表示也可能抛异常。例 `repr("hi")` 包含引号。

## 【了解】容器

- `tuple(iterable=(), /)`：省略时为空元组，否则从可迭代对象构造元组；返回元组，参数不可迭代抛 `TypeError`。例 `tuple([1, 2])`。
- `frozenset(iterable=(), /)`：省略时创建空的不可变集合，否则从可迭代对象构造并去重；返回 `frozenset`，输入不可迭代或元素不可哈希时抛 `TypeError`。例 `frozenset([1, 1])` 得 `frozenset({1})`。
- `dict(**kwargs)`、`dict(mapping, **kwargs)` 或 `dict(iterable, **kwargs)`：可选一个映射或键值对序列，加任意关键字键值对；后提供的同名键覆盖前面的值。返回新字典；参数类型或键不可哈希抛 `TypeError`，键值对长度错误抛 `ValueError`。例 `dict([("a", 1)])`。
- `list`、`set`、`bytes`、`bytearray`、`len`、`type` 及字符串编码与字节解码的完整调用方式见[第二章速查](../02-basic-data-types/functions.md)；`print` 见[官方文档](https://docs.python.org/zh-cn/3.11/library/functions.html#print)。
- `dict.items()`：无参数，返回键值对视图；额外参数抛 `TypeError`。例 `list({"a": 1}.items())`。
- `str.lower()`：无参数，返回转换为小写的新字符串；额外参数抛 `TypeError`。例 `"FALSE".lower()` 得 `"false"`。

## 【了解】字符、进制和字面量

- `chr(i, /)`：必填整数码点，返回单字符字符串；范围为 0 到 0x10FFFF，越界抛 `ValueError`，类型不合适抛 `TypeError`。例 `chr(65)` 得 `"A"`。`ord(c, /)` 的完整说明见[第二章速查](../02-basic-data-types/functions.md)。
- `bin(number, /)`、`oct(number, /)`、`hex(number, /)`：均需一个整数或支持整数索引的对象，分别返回带 `0b`、`0o`、`0x` 前缀的字符串；类型不支持抛 `TypeError`。例 `hex(10)` 得 `"0xa"`。
- `ast.literal_eval(node_or_string)`：必填 Python 字面量文本或表达式 AST 节点；返回解析后的值，不执行任意代码。无效输入可抛 `ValueError`、`SyntaxError` 或 `TypeError`；不可信的大型或深层输入也可能耗尽资源。例 `literal_eval("[1, 2]")` 得列表，先写 `from ast import literal_eval`。
- `eval(source, globals=None, locals=None, /)`：`source` 是表达式字符串或代码对象；`globals` 为全局命名空间字典，`locals` 为局部命名空间映射，均可省略。两者都省略时使用调用处的命名空间；只提供 `globals` 时它也作为局部命名空间。返回表达式结果；语法错误抛 `SyntaxError`，执行中的错误会继续抛出。例 `eval("1 + 2")` 得 3。它会执行表达式，不能用于不可信输入；单纯解析数字用 `int()` 或 `float()`。
- `memoryview(object, /)`：`object` 必填且只能按位置传入，必须支持缓冲区协议，例如 `bytes` 或 `bytearray`；返回该对象的内存视图，不支持缓冲区的对象会抛 `TypeError`。例 `memoryview(b"AB")`。
- `ascii(obj, /)`：`obj` 必填且只能按位置传入，返回对象表示形式的字符串，其中非 ASCII 字符被转义；参数数量错误抛 `TypeError`，对象自定义表示也可能抛出异常。例 `ascii("雨")` 返回包含 `\\u96e8` 的表示字符串。
