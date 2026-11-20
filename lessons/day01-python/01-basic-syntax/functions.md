# 第 1 章 · 函数与方法完整速查（Python 3.11）

【必会】用于基础练习；【了解】可在读到例子时再查。下半页的【补充】收录进阶验证所用的工具。

以下签名中，`/` 之前的参数只能按位置传入，`*` 之后的参数只能按关键字传入；无默认值的参数为必填参数。

---

## 【必会】`print()`

- **函数用途**：将零个或多个对象转为文本并输出到标准输出（默认终端屏幕）。
- **Python 3.11 完整签名**：`print(*objects, sep=' ', end='\n', file=None, flush=False)`
- **全部参数与默认值**：
  - `*objects`（位置可变参数，可传 0 个或多个）：要输出的任意对象，内部会先用 `str()` 转成字符串。
  - `sep`（仅关键字，默认 `' '`）：多个输出对象之间的分隔字符串；传 `None` 时使用默认值 `' '`。
  - `end`（仅关键字，默认 `'\n'`）：全部对象输出完毕后追加的结尾字符串；传 `None` 时使用默认值 `'\n'`。
  - `file`（仅关键字，默认 `None`）：具有 `write(string)` 方法的可写文本流对象；`None` 表示使用 `sys.stdout`。
  - `flush`（仅关键字，默认 `False`）：布尔值，为 `True` 时强制刷新输出缓冲区。
- **参数限制**：`objects` 只能按位置传入；`sep`、`end`、`file`、`flush` 位于 `*objects` 之后，只能按关键字传入。
- **返回值及类型**：总是返回 `None`（`NoneType`）。
- **常见错误与异常**：
  - `TypeError`：`sep` 或 `end` 传入非字符串且非 `None` 的值（如 `sep=1`）。
  - `AttributeError`：指定的 `file` 对象没有 `write` 方法。
  - `OSError`：底层输出流不可写。
- **基础示例**：
  ```python
  print("a", "b", sep=" | ", end="!\n")  # 输出: a | b!
  ```
- **JS/TS 对照**：类似 `console.log(...args)`。`console.log` 返回 `undefined`；Python 可通过 `sep` / `end` 定制格式。

---

## 【必会】`input()`

- **函数用途**：暂停程序运行，等待用户在标准输入中输入一行文本并返回（去掉末尾换行符）。
- **Python 3.11 完整签名**：`input(prompt='', /)`
- **全部参数与默认值**：
  - `prompt`（可选位置参数，默认 `''`）：等待输入前在终端显示的提示信息。
- **参数限制**：`/` 表示 `prompt` 只能按位置传入，不能写 `input(prompt="...")`。
- **返回值及类型**：总是返回 `str`（即使用户输入的是数字 `18`，返回的也是 `"18"`）。
- **常见错误与异常**：
  - `EOFError`：在未读取到任何输入时遇到文件结束符（如管道输入结束、Ctrl+Z 后回车）。
  - `KeyboardInterrupt`：用户在终端按 `Ctrl+C` 中断输入。
- **基础示例**：
  ```python
  name = input("请输入名字：")
  print("你好，", name)
  ```
- **JS/TS 对照**：类似浏览器环境的 `window.prompt(message)`，但浏览器取消时返回 `null`，而 Python 总是返回 `str`（空回车返回 `""`）；在 Node.js 中需要 `readline` 模块。

---

## 【必会】`type()`

- **函数用途**：单参数形式用于获取对象的运行时类型；三参数形式用于动态创建新类。
- **Python 3.11 完整签名（重载）**：
  1. `type(object, /)`（【必会】）
  2. `type(name, bases, dict, /, **kwds)`（【了解】动态建类，后续面向对象章节再看）
- **全部参数与默认值**：
  - 单参数形式：`object`（必填位置参数），任意 Python 对象。
  - 三参数形式：`name`（`str`，类名）、`bases`（`tuple`，基类元组）、`dict`（`dict`，类命名空间字典）、`**kwds`（可省略，无额外关键字时为空；用于类创建过程中的关键字参数）。
- **参数限制**：`object` 或 `name, bases, dict` 均在 `/` 之前，只能按位置传入；只能传 1 个或 3 个位置参数。
- **返回值及类型**：单参数返回对象的类型对象（`type`，例如 `<class 'int'>`）；三参数返回新创建的类（`type`）。
- **常见错误与异常**：
  - `TypeError`：传入 0 个、2 个或超过 3 个位置参数；或三参数形式参数类型不匹配。
- **基础示例**：
  ```python
  print(type(42))      # <class 'int'>
  print(type("hi"))    # <class 'str'>
  ```
- **JS/TS 对照**：类似 JS 的 `typeof x`，但 JS 对数组、对象、`null` 都返回 `"object"`，而 Python 的 `type()` 返回精确的类对象（`<class 'list'>`、`<class 'dict'>`、`<class 'NoneType'>`）。

---

## 【必会】`len()`

- **函数用途**：返回容器或序列对象包含的元素（或字符）个数。
- **Python 3.11 完整签名**：`len(obj, /)`
- **全部参数与默认值**：
  - `obj`（必填位置参数，无默认值）：序列（如 `str`、`list`、`tuple`、`bytes`）或集合/映射（如 `dict`、`set`）等实现了 `__len__` 的对象。
- **参数限制**：`/` 表示 `obj` 只能按位置传入。
- **返回值及类型**：非负整数 `int`。
- **常见错误与异常**：
  - `TypeError`：传入没有长度概念的对象（如 `len(123)` 或 `len(None)`）。
- **基础示例**：
  ```python
  print(len("Python"))  # 6
  ```
- **JS/TS 对照**：JS 中数组和字符串是属性 `arr.length` / `str.length`，`Set` / `Map` 是 `size`；Python 统一使用内置函数 `len(x)`。

---

## 【必会】`str.isidentifier()`

- **方法用途**：判断字符串是否符合 Python 标识符（变量名、函数名等）的语法规则。注意：**不会**检查是否是保留关键字。
- **Python 3.11 完整签名**：`str.isidentifier(self, /)`；绑定到字符串后写 `s.isidentifier()`
- **全部参数与默认值**：无额外参数（仅隐式接收调用该方法的字符串对象 `self`）。
- **参数限制**：通过类型调用时 `self` 必填且仅限位置；通过实例调用时隐式传入。
- **返回值及类型**：布尔值 `bool`（拼写符合规则返回 `True`，空字符串或含非法字符返回 `False`）。
- **常见错误与异常**：
  - `AttributeError`：在非字符串对象（如整数 `123`）上调用 `.isidentifier()`。
- **基础示例**：
  ```python
  print("user_name".isidentifier())  # True
  print("2nd".isidentifier())        # False
  print("class".isidentifier())      # True（仍是关键字，需配合 keyword.iskeyword）
  ```
- **JS/TS 对照**：JS 没有内置方法判断合法标识符，通常需要正则或解析器；Python 自带此方法，但仍需配合 `keyword.iskeyword()` 排除关键字。

---

## 【补充】【必会】用 `keyword.iskeyword()` 判断保留关键字

- **基础练习 1**：传入一个字符串，读懂返回的布尔值。`isidentifier()` 检查名字的拼写，`keyword.iskeyword()` 检查它是否为保留关键字。
- 【了解】软关键字只在特定语境中有特殊含义，例如 `keyword.iskeyword("match")` 返回 `False`。
- **Python 3.11 完整签名**：`keyword.iskeyword(s, /)`（需先 `import keyword`）
- **全部参数与默认值**：`s`（必填位置参数，`str`）。
- **参数限制**：只能按位置传入。
- **返回值及类型**：布尔值 `bool`。
- **常见错误与异常**：传入不可哈希对象时可能抛 `TypeError`；正常传 `str` 不抛异常。
- **基础示例**：
  ```python
  import keyword
  print(keyword.iskeyword("class"))  # True
  ```
- **JS/TS 对照**：JS 没有标准库函数检查关键字，通常需要维护一份保留字数组。

---

## 【补充】【必会】用 `str()` 将数字转为字符串

把对象转为文本，或用指定编码把字节解码为文本。返回 `str`，类似 JS 的 `String(x)` 和 `TextDecoder.decode()`。

- **基础练习 3**：`str(42)` 得到字符串 `"42"`，可以用 `+` 与其他字符串拼接。直接用 `+` 拼接字符串和整数会抛 `TypeError`。
- 【了解】完整签名 `str(object='')` 返回对象的可读文本，省略参数得到空串。
- 【了解】字节解码形式为 `str(object=b'', encoding='utf-8', errors='strict')`。`object` 是字节类对象，`encoding` 是编码名，`errors` 是解码错误处理名。默认严格报错，`'replace'` 用替代字符继续解码。两种形式的显式参数都可按位置或关键字传入。
- 解码示例：`str(b'ABC', encoding='ascii')` 得到 `"ABC"`。给已有字符串再指定编码会抛 `TypeError`，未知编码会抛 `LookupError`，字节与编码不符可能抛 `UnicodeDecodeError`。

## 【补充】【了解】`int()`

- `int(x=0, /)` 返回整数（`int`）。省略 `x` 得到零；给数字时向零截断，给文本时按十进制读取。这里的 `x` 只能按位置传入。
- `int(x, /, base=10)` 按进制解析文本。`x` 必填且必须是 `str`、`bytes` 或 `bytearray`；`base` 可按位置或关键字传入，取 2～36，或用 0 根据前缀判断进制。
- `int("18") + 1` 得到 `19`，`int("ff", base=16)` 得到 `255`。格式或进制错误会抛 `ValueError`，例如 `int("3.5")`；传入 `None` 或给数值指定进制会抛 `TypeError`。JS 的 `parseInt("3.5", 10)` 会读到小数点为止。

## 【补充】【了解】用 Decimal 保存十进制数

在 `from decimal import Decimal` 后调用 `Decimal(value='0', context=None)`，得到不可变的 `Decimal` 对象。两个参数均可省略，可按位置或关键字传入。

- `value` 是初始值，支持整数、十进制字符串、浮点数、另一个 `Decimal`，或表示符号、数字序列和指数的三元组。省略时得到十进制零。
- `context` 可传 `decimal.Context`，默认使用当前上下文。构造时保留字符串中的有效数字。在默认上下文中，无效数字文本会抛 `decimal.InvalidOperation`；将 `None` 作为数值会抛 `TypeError`。
- `Decimal("0.1") + Decimal("0.2")` 得到 `Decimal('0.3')`。JS 的 `Number` 和 Python 的 `float` 都用二进制浮点表示这两个小数。

## 【补充】【了解】`sys.stdout.write()`

- **方法用途**：向标准输出流直接写入字符串，不会像 `print()` 那样自动添加空格和换行。
- **Python 3.11 完整签名**：`sys.stdout.write(text, /)`（需先 `import sys`）
- **全部参数与默认值**：`text`（必填位置参数，无默认值），必须是 `str`。
- **参数限制**：只能按位置传入，且只接收 1 个字符串参数。
- **返回值及类型**：`int`，表示成功写入的字符数。
- **常见错误与异常**：`TypeError`（传入非 `str`，例如整数 `123`）；`OSError`（底层写入失败）。
- **基础示例**：
  ```python
  import sys
  count = sys.stdout.write("runoob\n")  # 输出 runoob 并换行，count 为 7
  ```
- **JS/TS 对照**：对应 Node.js 的 `process.stdout.write(str)`。

---

## 【补充】【了解】`compile()`

- **函数用途**：将源码字符串编译为代码对象（code object），后续可交给 `exec()` 或 `eval()` 执行，常用于在不运行文件的情况下检查语法/缩进错误。
- **Python 3.11 完整签名**：`compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, *, _feature_version=-1)`
- **全部参数与默认值**：
  - `source`（必填）：源码字符串、字节串或 AST 对象。
  - `filename`（必填，`str`）：报错信息中显示的文件名（非文件源码常写 `"<string>"`）。
  - `mode`（必填，`str`）：编译模式，`'exec'`（多条语句）、`'eval'`（单个表达式）、`'single'`（单条交互语句）。
  - `flags=0` 是编译选项的整数位掩码，默认不额外启用选项。`dont_inherit=False` 表示继承调用处的编译标志，设为真则只采用显式标志。
  - `optimize=-1` 沿用解释器优化级别；0 不优化，1 省略断言，2 还会省略文档字符串。
  - `_feature_version=-1` 是 CPython 3.11.9 的内部仅关键字参数，用于 AST 解析时选择语法特性版本，示例保持默认。
- **参数限制**：前 3 个为必填参数，允许按位置或关键字传入；`flags`、`dont_inherit`、`optimize` 可按位置或关键字传入。
- **返回值及类型**：默认返回代码对象（`code`）；启用 `ast.PyCF_ONLY_AST` 标志时返回语法树（`ast.AST`）。
- **常见错误与异常**：语法或缩进错误时抛 `SyntaxError`（或其子类 `IndentationError`）；`mode` 非法时抛 `ValueError`。
- **基础示例**：
  ```python
  code_obj = compile("x = 1 + 2", "<demo>", "exec")
  ```
- **JS/TS 对照**：类似 `new Function(...)` 或在编译阶段检查语法的 `vm.Script`，日常业务极少直接使用。
- **官方文档**：[compile](https://docs.python.org/zh-cn/3.11/library/functions.html#compile)

## 【补充】【了解】字符串方法

下表使用绑定方法签名。`s` 是必需的字符串实例，调用时已隐式传入。省略的 `start`、`end` 分别表示从头、到末尾，索引范围左闭右开。

| 完整调用形式 | 用途、参数、返回值 | 示例与常见错误 | JS 对照 |
| --- | --- | --- | --- |
| `s.count(sub[, start[, end]], /)` | 在指定范围统计不重叠的子串，返回 `int`。`sub` 必填，范围可选，均仅限位置。 | `"banana".count("an")` 得到 2。给非字符串子串或非整数索引会抛 `TypeError`。 | JS 没有同名计数方法。 |
| `s.startswith(prefix[, start[, end]], /)` | 检查指定范围的开头，返回 `bool`。`prefix` 必填，可为字符串或字符串元组；范围可选，均仅限位置。 | `"abc".startswith("b", 1)` 得到 `True`。把列表用作前缀会抛 `TypeError`。 | `startsWith(prefix, position)` 只接受一个前缀。 |
| `s.splitlines(keepends=False)` | 按行边界拆成 `list[str]`；可选的 `keepends` 可按位置或关键字传入，为真时保留行尾。 | `"a\nb\n".splitlines()` 得到 `["a", "b"]`。多传一个参数会抛 `TypeError`。 | JS 的 `split("\n")` 在末尾换行时还会留下空串。 |

## 【补充】【了解】进阶断言用到的类型与输出工具

| 完整调用形式 | 参数、限制与返回值 | 基础示例与常见错误 | JS 对照 |
| --- | --- | --- | --- |
| `set()`、`set(iterable, /)` | 返回去重后的可变集合 `set`；省略参数得到空集合，传入时只接受一个位置参数，元素须可哈希。 | `set("aba")` 包含 `"a"` 和 `"b"`。不可迭代的输入或列表元素不可哈希时抛 `TypeError`。 | `new Set(iterable)` |
| `isinstance(obj, classinfo, /)` | 两项均必填且仅限位置。检查对象是否属于指定类型或其子类，返回 `bool`；`classinfo` 也可为类型元组或联合类型。 | `isinstance("18", str)` 得到 `True`。把字符串 `"str"` 当类型会抛 `TypeError`。 | 类似 `instanceof`，也能检查字符串等内置类型。 |
| `io.StringIO(initial_value='', newline='\n')` | 创建内存文本流并返回 `StringIO` 对象。初始文本默认空串；换行参数控制换行识别与写入转换，可取 `None`、空串、换行、回车或回车换行。两项均可选，可按位置或关键字传入。 | `import io` 后，`io.StringIO("Hi").getvalue()` 得到 `"Hi"`。传入字节会抛 `TypeError`，无效换行设置会抛 `ValueError`。 | 内存里收集文本，类似用数组收集输出再拼接。 |
| `buffer.getvalue()`（`io.StringIO.getvalue(self, /)`） | 取出流中的全部文本，返回 `str`；唯一必需的位置参数是隐式传入的流实例，不改变当前位置。 | `io.StringIO().getvalue()` 得到空串。流已关闭时抛 `ValueError`。 | 类似取出缓冲的文本。 |
| `contextlib.redirect_stdout(new_target)` | 必填的 `new_target` 可按位置或关键字传入。返回上下文管理器；进入 `with` 后临时把标准输出指向目标，退出后恢复。 | 见下例。目标缺少 `write` 方法时，块内的 `print` 会抛 `AttributeError`。 | 类似测试里临时替换输出并在结束后恢复。 |

```python
import contextlib
import io

buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    print("Hi")
print(buffer.getvalue() == "Hi\n")  # True
```

更多示例见 Python 3.11 官方文档的[字符串方法](https://docs.python.org/3.11/library/stdtypes.html#string-methods)、[文本流](https://docs.python.org/3.11/library/io.html#io.StringIO)和[输出重定向](https://docs.python.org/3.11/library/contextlib.html#contextlib.redirect_stdout)。
