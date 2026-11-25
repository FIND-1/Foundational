# 第 3 章 · 函数与方法完整速查（Python 3.11）

【必会】用于基础练习；【了解】可在读到例子时再查。签名与传参限制均已用 Python 3.11.9 的 `inspect.signature()` 与实际调用核对。

以下签名中，`/` 之前的参数只能按位置传入，`*` 之后的参数只能按关键字传入；无默认值的参数为必填参数。

前两章已讲的 API 不再重复，仅列出本章新增的重点：

- 见[第 1 章函数速查](../01-basic-syntax/functions.md)：`print()`、`input()`、`type()`、`len()`、`str()`、`int()`、`set()`。其中 **`int()` 在本章升为【必会】**：`int(x=0, /)` 对浮点数向零截断（`int(-3.9) == -3`），`int(x, /, base=10)` 按 2～36 进制或 `base=0`（按 `0b` / `0o` / `0x` 前缀）解析字符串；`int("3.5")` 抛 `ValueError`，`int(float("inf"))` 抛 `OverflowError`，`int(float("nan"))` 抛 `ValueError`。
- 见[第 2 章函数速查](../02-basic-data-types/functions.md)：`float()`、`complex()`、`bool()`、`list()`、`dict()`、`dict.items()`、`sorted()`、`ord()`、`bytes()`、`bytearray()`、`str.encode()`、`bytes.decode()`。其中 **`float()` 在本章升为【必会】**；`dict()` 接收重复键时以最后一次出现的值为准；`bytes([65, 66])` 与 `bytearray([65, 66])` 可由 0～255 的整数序列构造。

---

## 【必会】`tuple()`

- **函数用途**：创建空元组，或把可迭代对象按原顺序转换为不可变元组。
- **Python 3.11 完整签名**：`tuple(iterable=(), /)`
- **全部参数与默认值**：
  - `iterable`（可选位置参数，默认空元组 `()`）：任意可迭代对象（如字符串、列表、集合、字典）。省略时返回空元组 `()`。
- **参数限制**：`iterable` 位于 `/` 之前，只能按位置传入，`tuple(iterable=[1, 2])` 会抛 `TypeError`；最多传 1 个参数。
- **返回值及类型**：新的 `tuple`。传入字典时只取出键。
- **常见错误与异常**：`TypeError`：传入不可迭代对象（如 `tuple(123)`），或按关键字传参、传多个参数。
- **基础示例**：
  ```python
  print(tuple("abc"))       # ('a', 'b', 'c')
  print(tuple([1, 2, 3]))   # (1, 2, 3)
  print(tuple())            # ()
  ```
- **JS/TS 对照**：JS 没有内置元组，TS 的 `readonly [A, B]` 仅作编译期约束；运行时类似 `Object.freeze([...iterable])`。
- **实际项目 / 惯用建议**：写死已知元素直接用字面量 `(1, 2)` 或单元素 `(20,)`；`tuple(x)` 主要用于把列表或生成器冻结为可哈希对象（例如拼复合字典键或缓存键）。

---

## 【必会】`str.lower()`

- **方法用途**：把字符串中的所有大写字母转为小写，返回新字符串，原字符串不变。
- **Python 3.11 完整签名**：`str.lower(self, /)`；绑定到字符串后写 `s.lower()`
- **全部参数与默认值**：无额外参数（仅隐式接收字符串实例 `self`）。
- **参数限制**：不能传入额外参数；通过类型调用时 `self` 只能按位置传入。
- **返回值及类型**：新的 `str`。
- **常见错误与异常**：`TypeError`：传入额外参数；`AttributeError`：在非字符串对象上调用。
- **基础示例**：
  ```python
  flag = "False"
  print(flag.lower())            # false
  print(flag.lower() == "true")  # False
  ```
- **JS/TS 对照**：对应 `s.toLowerCase()`。
- **实际项目 / 惯用建议**：高频用于不区分大小写的文本匹配（如解析 `"TRUE"` / `"false"` 环境变量、统一邮箱或命令名）；处理含德语 `ß` 等多语种不区分大小写比较时，可使用更彻底的 `str.casefold()`。

---

## 【必会】`chr()`

- **函数用途**：把 Unicode 码点（整数）转换为对应的单个字符，是 `ord()` 的逆运算。
- **Python 3.11 完整签名**：`chr(i, /)`
- **全部参数与默认值**：
  - `i`（必填位置参数）：整数码点，有效范围 `0 <= i <= 0x10FFFF`（十进制 0～1114111）。
- **参数限制**：只能按位置传入，`chr(i=65)` 会抛 `TypeError`。
- **返回值及类型**：长度为 1 的 `str`。
- **常见错误与异常**：
  - `ValueError`：整数小于 0 或大于 `0x10FFFF`。
  - `TypeError`：传入非整数（如浮点数 `65.0`、字符串 `"65"`）或按关键字传参。
- **基础示例**：
  ```python
  print(chr(65))            # A
  print(chr(38632))         # 雨
  print(chr(ord("雨")))     # 雨
  ```
- **JS/TS 对照**：对应 `String.fromCodePoint(code)`（注意不要与只支持 16 位 UTF-16 码元的 `String.fromCharCode` 混淆）。
- **实际项目 / 惯用建议**：日常业务开发低频，主要见于编码转换、生成字母序列或算法题；和 `ord()` 成对记忆即可。

---

## 【必会】`bin()`、`oct()`、`hex()`

- **函数用途**：把整数分别格式化为带 `0b`（二进制）、`0o`（八进制）、`0x`（十六进制）前缀的字符串。
- **Python 3.11 完整签名**：`bin(number, /)`、`oct(number, /)`、`hex(number, /)`
- **全部参数与默认值**：
  - `number`（必填位置参数）：整数（`int`、`bool` 等实现了 `__index__` 的对象）。
- **参数限制**：均只能按位置传入，且恰好 1 个参数。
- **返回值及类型**：`str`。负数会在前缀前带负号，例如 `bin(-5)` 返回 `'-0b101'`；十六进制字母为小写。
- **常见错误与异常**：`TypeError`：传入浮点数（如 `bin(3.5)`）、字符串或按关键字传参。
- **基础示例**：
  ```python
  print(bin(10), oct(10), hex(10))  # 0b1010 0o12 0xa
  print(bin(-5), hex(-15))          # -0b101 -0xf
  ```
- **JS/TS 对照**：对应 `n.toString(2)`、`n.toString(8)`、`n.toString(16)`，但 JS 的结果不带 `0b` / `0o` / `0x` 前缀。
- **实际项目 / 惯用建议**：查看调试值时直接用 `bin()` / `hex()`；如果要去掉前缀、固定位数补零或输出大写十六进制，项目里常用 f-string 格式说明符（如 `f"{10:08b}"` 得 `'00001010'`，`f"{255:X}"` 得 `'FF'`）。

---

## 【了解】`repr()`

- **函数用途**：返回偏向代码/调试风格的对象表示字符串；对字符串等基础类型，结果常可直接作为合法 Python 表达式读回。
- **Python 3.11 完整签名**：`repr(obj, /)`
- **全部参数与默认值**：
  - `obj`（必填位置参数）：任意 Python 对象。
- **参数限制**：只能按位置传入，`repr(obj="hi")` 会抛 `TypeError`。
- **返回值及类型**：`str`。
- **常见错误与异常**：`TypeError`：缺少参数、多传参数或按关键字传参；对象自定义的 `__repr__` 内部出错时也可能抛异常。
- **基础示例**：
  ```python
  print(str("hi"), repr("hi"))  # hi 'hi'
  print(repr("a\nb"))           # 'a\nb'（转义符显式可见）
  ```
- **JS/TS 对照**：JS 没有同名内置函数，类似调试时用 `JSON.stringify(x)` 或 `util.inspect(x)` 查看带引号和转义符的原始形态。
- **实际项目 / 惯用建议**：写日志、报错信息或排查隐藏空格/换行时非常实用；在 f-string 中可简写为 `f"{value!r}"`。

---

## 【了解】`ascii()`

- **函数用途**：返回类似 `repr()` 的对象表示字符串，但把所有非 ASCII 字符转义为 `\x`、`\u` 或 `\U` 序列。
- **Python 3.11 完整签名**：`ascii(obj, /)`
- **全部参数与默认值**：
  - `obj`（必填位置参数）：任意 Python 对象。
- **参数限制**：只能按位置传入，`ascii(obj="雨")` 会抛 `TypeError`。
- **返回值及类型**：只含 ASCII 字符的 `str`。
- **常见错误与异常**：`TypeError`：参数数量错误或按关键字传参；自定义 `__repr__` 出错时也可能抛异常。
- **基础示例**：
  ```python
  print(repr("雨"))   # '雨'
  print(ascii("雨"))  # '\u96e8'
  ```
- **JS/TS 对照**：JS 没有同名内置函数，类似手动把非 ASCII 字符转为 `\uXXXX` 转义串。
- **实际项目 / 惯用建议**：低频 API，仅在目标日志、协议或终端只允许纯 ASCII 字符时使用。

---

## 【了解】`frozenset()`

- **函数用途**：创建不可变集合；创建后不能增删元素，但支持 `in`、`|`、`&`、`-`、`^` 等只读集合运算。
- **Python 3.11 完整签名（重载）**：
  1. `frozenset()`（创建空不可变集合）
  2. `frozenset(iterable, /)`（从可迭代对象去重构造）
- **全部参数与默认值**：
  - `iterable`（可选位置参数）：元素必须全部可哈希的可迭代对象。省略时返回空的 `frozenset()`。
- **参数限制**：只能按位置传入，最多 1 个参数；`frozenset(iterable=[1])` 会抛 `TypeError`。
- **返回值及类型**：`frozenset`。
- **常见错误与异常**：`TypeError`：参数不可迭代、包含不可哈希元素（如列表 `frozenset([[1]])`），或按关键字传参、传多个参数。
- **基础示例**：
  ```python
  editor_perms = frozenset(["read", "read", "write"])
  role_map = {editor_perms: "编辑者"}       # 不可变且可哈希，能作字典键
  query_perms = frozenset(["write", "read"]) # 新建查询键（未修改原集合）
  print(editor_perms == query_perms)         # True（集合无序，值相等）
  print(role_map[query_perms])               # 编辑者
  ```
- **JS/TS 对照**：JS 没有内置不可变 `Set`，需借助第三方库或自行封装。
- **实际项目 / 惯用建议**：低频 API，只在需要“无序去重集合”作为字典键、缓存键或集合嵌套元素（如 `set[frozenset]`）时使用；常规去重用 `set` 即可。

---

## 【了解】`memoryview()`

- **函数用途**：为支持缓冲区协议的对象（如 `bytes`、`bytearray`）创建内存视图，无需复制底层字节即可读取、切片或修改。
- **Python 3.11 完整签名**：`memoryview(object)`
- **全部参数与默认值**：
  - `object`（必填）：支持缓冲区协议的对象（如 `bytes`、`bytearray`）。
- **参数限制**：在 Python 3.11.9 中 `object` 可按位置传入，也允许按关键字 `memoryview(object=b"AB")` 传入；但习惯上几乎都按位置传入。
- **返回值及类型**：`memoryview`。对 `bytearray` 创建的视图可写入（修改直接反映到原对象），对 `bytes` 创建的视图只读。
- **常见错误与异常**：
  - `TypeError`：对象不支持缓冲区协议（如 `memoryview("AB")`），或向只读视图写入。
  - `ValueError`：写入的字节值超出 0～255，或切片长度不匹配。
- **基础示例**：
  ```python
  buf = bytearray(b"AB")
  view = memoryview(buf)
  view[0] = 67
  print(buf, list(view))  # bytearray(b'CB') [67, 66]
  ```
- **JS/TS 对照**：类似 JS 中基于同一个 `ArrayBuffer` 创建的 `Uint8Array` / `DataView` 视图，共享底层内存。
- **实际项目 / 惯用建议**：普通业务开发极少直接使用；主要见于网络协议解析、大文件流式分片、音视频或科学计算（如 NumPy）中避免内存拷贝的场景。

---

## 【了解】`eval()`

- **函数用途**：把字符串当作单个 Python 表达式求值，并返回计算结果。
- **Python 3.11 完整签名**：`eval(source, globals=None, locals=None, /)`
- **全部参数与默认值**：
  - `source`（必填位置参数）：单个 Python 表达式字符串，或 `compile(..., "eval")` 生成的代码对象。
  - `globals`（可选位置参数，默认 `None`）：全局命名空间字典；省略时使用调用处的全局命名空间。
  - `locals`（可选位置参数，默认 `None`）：局部命名空间映射；只传 `globals` 时 `locals` 默认与 `globals` 相同。
- **参数限制**：三项都在 `/` 之前，只能按位置传入，`eval(source="1 + 2")` 会抛 `TypeError`。
- **返回值及类型**：表达式求值结果，类型取决于表达式本身。
- **常见错误与异常**：`SyntaxError`：源码不是合法表达式（如空字符串、赋值语句 `x = 1`）；`TypeError`：`source` 类型不对或按关键字传参；表达式运行期产生的任何异常（如 `NameError`、`ZeroDivisionError`）都会直接抛出。
- **基础示例**：
  ```python
  print(eval("1 + 2"))                 # 3
  print(eval("x * 2", {"x": 10}))      # 20
  ```
- **JS/TS 对照**：对应 JS 的 `eval(code)`，具有同样的代码注入风险。
- **实际项目 / 惯用建议**：**严禁对用户输入、接口参数、配置文件等不可信内容调用 `eval()`**；解析数字用 `int()` / `float()`，解析 JSON 用标准库 `json.loads()`，解析 Python 字面量用 `ast.literal_eval()`。

---

## 【了解】`ast.literal_eval()`

- **函数用途**：安全解析只包含 Python 字面量的字符串（或 AST 节点），支持字符串、字节、数字、元组、列表、字典、集合、布尔值和 `None`，不执行函数调用或任意代码。
- **Python 3.11 完整签名**：`ast.literal_eval(node_or_string)`（需先 `import ast` 或 `from ast import literal_eval`）
- **全部参数与默认值**：
  - `node_or_string`（必填）：表示 Python 字面量的字符串或 AST 节点。
- **参数限制**：可按位置或关键字（`literal_eval(node_or_string="[1, 2]")`）传入。
- **返回值及类型**：解析后的 Python 对象（如 `list`、`dict`、`tuple`、`int` 等）。
- **常见错误与异常**：
  - `ValueError`：包含非字面量结构（如 `"1 + 2"`、函数调用 `"print(1)"`）或传入非字符串/非 AST 对象（如 `None`、`123`）。
  - `SyntaxError`：字符串语法不完整（如 `"[1,"`）。
  - `MemoryError` / `RecursionError`：极端巨大或超深嵌套的不可信输入仍可能耗尽资源。
- **基础示例**：
  ```python
  from ast import literal_eval

  print(literal_eval("[1, 2, 3]"))      # [1, 2, 3]
  print(literal_eval("{'a': True}"))    # {'a': True}
  ```
- **JS/TS 对照**：定位类似 `JSON.parse()`，但解析的是 Python 字面量语法（允许单引号、元组、`True`/`False`/`None`、集合）。
- **实际项目 / 惯用建议**：跨系统数据交换优先用 `json.loads()`；仅当历史日志或配置里存的是 Python 风格字面量（如单引号字典、元组）时才用 `ast.literal_eval()`，并限制输入长度。

---

更多示例见 Python 3.11 官方文档的[内置函数](https://docs.python.org/zh-cn/3.11/library/functions.html)、[内置类型](https://docs.python.org/zh-cn/3.11/library/stdtypes.html)和 [ast.literal_eval](https://docs.python.org/zh-cn/3.11/library/ast.html#ast.literal_eval)。
