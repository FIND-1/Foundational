# 第 2 章 · 函数与方法完整速查（Python 3.11）

第 1 章已讲的 API 不再重复，见[第 1 章函数速查](../01-basic-syntax/functions.md)：`print()`、`input()`、`type()`、`len()`、`str()`、`int()`、`set()`、`isinstance()`。其中 `isinstance(obj, classinfo, /)` 在本章升为【必会】，重点是**子类实例也返回 `True`**：`isinstance(True, int)` 为 `True`，而 `type(True) is int` 为 `False`。

---

## 【必会】`issubclass()`

- **函数用途**：判断一个类是否为另一个类本身或其子类。
- **Python 3.11 完整签名**：`issubclass(cls, class_or_tuple, /)`
- **全部参数与默认值**：
  - `cls`（必填位置参数）：要检查的类，必须是类对象，不能是实例。
  - `class_or_tuple`（必填位置参数）：父类，也可以是类组成的元组或联合类型（如 `int | str`），满足其中之一即返回 `True`。
- **参数限制**：两项都在 `/` 之前，只能按位置传入。
- **返回值及类型**：`bool`。类和自身比较也返回 `True`。
- **常见错误与异常**：`TypeError`：`cls` 不是类（如 `issubclass(1, int)`），或第二项不是类、元组或联合类型。
- **基础示例**：
  ```python
  print(issubclass(bool, int))          # True
  print(issubclass(bool, (str, int)))   # True，元组中有一项满足即可
  ```
- **JS/TS 对照**：JS 没有同名函数，可用 `B.prototype instanceof A` 判断 `B` 是否继承自 `A`。
- **实际项目 / 惯用建议**：日常业务低频（多见于框架插件校验或类型工具）；判断实例类型时用 `isinstance()`。

---

## 【必会】`bool()`

- **函数用途**：按真值规则把任意对象转为 `True` 或 `False`。
- **Python 3.11 完整签名**：`bool(x=False, /)`
- **全部参数与默认值**：
  - `x`（可选位置参数，默认 `False`）：任意对象。省略时返回 `False`。
- **参数限制**：`x` 只能按位置传入，`bool(x=1)` 会抛 `TypeError`；最多传 1 个参数。
- **返回值及类型**：`bool`。`None`、`False`、数值零（`0`、`0.0`、`0j`）、空字符串、空列表、空元组、空字典、空集合、空 `bytes` 为 `False`，其余为 `True`。
- **常见错误与异常**：`TypeError`：按关键字传参或传入多个参数。
- **基础示例**：
  ```python
  print(bool([]), bool("False"), bool(0.0))  # False True False
  ```
- **JS/TS 对照**：类似 `Boolean(x)`，但 JS 中 `[]`、`{}` 为真，Python 中空容器为假。
- **实际项目 / 惯用建议**：只在需要保存或返回真正的 `bool`（如构造 JSON 字段、函数返回值）时显式调 `bool(x)`；在 `if` / `while` 中直接写 `if x:` 即可。

---

## 【补充】【了解】`float()`

- **函数用途**：把数字或数字文本转为浮点数。
- **Python 3.11 完整签名**：`float(x=0, /)`
- **全部参数与默认值**：`x`（可选位置参数，默认 `0`）：整数、浮点数、布尔值，或表示数字的字符串（可含首尾空白，也接受 `"inf"`、`"nan"`）。省略时返回 `0.0`。
- **参数限制**：只能按位置传入，最多 1 个参数。
- **返回值及类型**：`float`。`float(True)` 得到 `1.0`。
- **常见错误与异常**：`ValueError`：字符串不是有效数字（如 `float("abc")`）；`TypeError`：传入 `None`、列表等。
- **基础示例**：`print(float(True), float("3.5"))  # 1.0 3.5`
- **JS/TS 对照**：类似 `Number(x)` / `parseFloat(x)`，但 Python 对无效文本抛异常，不返回 `NaN`。第 3 章会继续使用。

---

## 【了解】`complex()`

- **函数用途**：创建复数。
- **Python 3.11 完整签名（重载）**：
  1. `complex(real=0, imag=0)`（【了解】）
  2. `complex(string, /)`（【了解】）
- **全部参数与默认值**：
  - `real`（可选，默认 `0`）：实部，可为整数、浮点数或复数。
  - `imag`（可选，默认 `0`）：虚部，可为整数、浮点数或复数。
  - `string`（必填位置参数）：形如 `"1+2j"` 的文本，加号两侧不能有空格。
- **参数限制**：第一种形式的两项可按位置或关键字传入（`complex(real=3, imag=4)`）；第二种形式的 `string` 只能按位置传入，且不能再传第二个参数。
- **返回值及类型**：`complex`。实例属性 `z.real`、`z.imag` 分别返回实部和虚部，都是 `float`。
- **常见错误与异常**：`ValueError`：字符串格式错误（如 `complex("1 + 2j")`）；`TypeError`：第一个参数是字符串时又传了第二个参数。
- **基础示例**：
  ```python
  z = complex(3, 4)
  print(z, z.real, z.imag)  # (3+4j) 3.0 4.0
  ```
- **JS/TS 对照**：JS 没有内置复数类型，需要第三方库；可把 `complex(3, 4)` 类比成只读二维对象 `{ real: 3.0, imag: 4.0 }`（`real` 是不带 `j` 的实部，`imag` 是 `j` 前面的系数虚部）。
- **实际项目 / 惯用建议**：Web 后端、爬虫、自动化脚本和 AI 应用层开发中极少用到；主要用于科学计算与工程领域，如音视频/信号处理（傅里叶变换 FFT 同时表示振幅与相位）、电路/通信仿真（Python 沿用工程习惯用 `j` 而非 `i`）、物理/量子计算，以及算法题中用它充当轻量级二维坐标（加减即平移，乘 `1j` 即逆时针旋转 90°，`abs(z)` 即到原点的距离）。现阶段只需认得写法并能用 `.real` / `.imag` 取值即可。

---

## 【必会】`str.replace()`

- **方法用途**：返回把子串替换后的新字符串，原字符串不变。
- **Python 3.11 完整签名**：`str.replace(self, old, new, count=-1, /)`；绑定到字符串后写 `s.replace(old, new)`
- **全部参数与默认值**：
  - `old`（必填）：要被替换的子串。
  - `new`（必填）：替换成的字符串。
  - `count`（可选，默认 `-1`）：最多替换几处，`-1` 表示全部替换。
- **参数限制**：Python 3.11 中三项都只能按位置传入，`s.replace("a", "x", count=1)` 会抛 `TypeError`（3.13 起 `count` 才允许按关键字传入）。
- **返回值及类型**：新的 `str`。
- **常见错误与异常**：`TypeError`：`old` 或 `new` 不是字符串，或按关键字传参。
- **基础示例**：
  ```python
  print("Python".replace("P", "J"))    # Jython
  print("aba".replace("a", "x", 1))    # xba
  ```
- **JS/TS 对照**：JS 的 `s.replace("a", "x")` 只替换第一处，`replaceAll` 才替换全部；Python 默认替换全部。

---

## 【必会】`list()`

- **函数用途**：创建新列表，或把可迭代对象（字符串、元组、集合、字典视图等）转成列表。
- **Python 3.11 完整签名**：`list(iterable=(), /)`
- **全部参数与默认值**：`iterable`（可选位置参数，默认空元组）：任意可迭代对象。省略时得到空列表 `[]`。
- **参数限制**：只能按位置传入，最多 1 个参数。
- **返回值及类型**：新的 `list`。传入字典时只得到键。
- **常见错误与异常**：`TypeError`：传入不可迭代的对象（如 `list(1)`）。
- **基础示例**：
  ```python
  print(list("ab"))                    # ['a', 'b']
  print(list({"a": 1}.items()))        # [('a', 1)]
  ```
- **JS/TS 对照**：类似 `Array.from(iterable)` 或 `[...iterable]`。
- **实际项目 / 惯用建议**：创建空列表直接写 `[]`（比 `list()` 更简洁更快）；`list(x)` 主要用于把视图、集合、生成器转为列表或做浅拷贝。

---

## 【必会】`list.append()`

- **方法用途**：在原列表末尾添加一个元素。
- **Python 3.11 完整签名**：`list.append(self, object, /)`；绑定后写 `items.append(x)`
- **全部参数与默认值**：`object`（必填位置参数）：要添加的任意对象。传入列表时整体作为一个元素添加。
- **参数限制**：只能按位置传入，且只接收 1 个参数。
- **返回值及类型**：`None`，修改发生在原列表上。
- **常见错误与异常**：`TypeError`：不传或多传参数；`AttributeError`：在元组、字符串等不可变对象上调用。
- **基础示例**：
  ```python
  items = ["苹果"]
  items.append("梨")
  print(items)  # ['苹果', '梨']
  ```
- **JS/TS 对照**：类似 `arr.push(x)`，但 `push` 可一次传多个且返回新长度。

---

## 【了解】`str.split()`

- **方法用途**：按分隔符把字符串拆成列表。
- **Python 3.11 完整签名**：`str.split(self, /, sep=None, maxsplit=-1)`
- **全部参数与默认值**：
  - `sep`（可选，默认 `None`）：分隔字符串。为 `None` 时按连续空白拆分，并忽略首尾空白；指定字符串时每遇到一次就切一刀，连续分隔符之间会产生空字符串。
  - `maxsplit`（可选，默认 `-1`）：最多拆分几次，`-1` 表示不限制。
- **参数限制**：两项都可按位置或关键字传入。
- **返回值及类型**：`list[str]`。
- **常见错误与异常**：`ValueError`：`sep` 为空字符串；`TypeError`：`sep` 不是字符串或 `None`。
- **基础示例**：
  ```python
  print("a  b".split(" "))     # ['a', '', 'b']
  print(" a  b ".split())      # ['a', 'b']
  ```
- **JS/TS 对照**：JS 的 `s.split()` 不传参数时返回 `[s]`；按空白拆分要写 `s.trim().split(/\s+/)`。
- **实际项目 / 惯用建议**：高频用于文本清洗与分词预处理；按空白拆单词时优先用无参 `s.split()`，避免 `s.split(" ")` 遇连续空格产生空串。

---

## 【了解】`str.join()`

- **方法用途**：用调用它的字符串作分隔符，把多个字符串连成一个。
- **Python 3.11 完整签名**：`str.join(self, iterable, /)`
- **全部参数与默认值**：`iterable`（必填位置参数）：元素全是字符串的可迭代对象。
- **参数限制**：只能按位置传入。
- **返回值及类型**：新的 `str`。传入空列表得到空字符串。
- **常见错误与异常**：`TypeError`：有元素不是字符串（如 `" ".join([1])`），或参数不可迭代。
- **基础示例**：`print(" ".join(["I", "like", "Python"]))  # I like Python`
- **JS/TS 对照**：JS 写 `arr.join(" ")`，分隔符是参数；Python 把分隔符放在点号前，且不会自动把数字转成字符串。
- **实际项目 / 惯用建议**：高频用于拼接多段文本（如拼 Prompt 片段、生成 CSV 行），比在循环里反复用 `+=` 拼接字符串性能高得多。

---

## 【必会】`sorted()`

- **函数用途**：返回把元素排好序的新列表，不修改原对象。
- **Python 3.11 完整签名**：`sorted(iterable, /, *, key=None, reverse=False)`
- **全部参数与默认值**：
  - `iterable`（必填位置参数）：任意可迭代对象，如集合、列表、字符串。
  - `key`（可选，仅关键字，默认 `None`）：接收一个元素、返回排序依据的函数；`None` 表示直接比较元素。（【了解】）
  - `reverse`（可选，仅关键字，默认 `False`）：为 `True` 时降序。
- **参数限制**：`iterable` 只能按位置传入；`key`、`reverse` 位于 `*` 之后，只能按关键字传入。
- **返回值及类型**：新的 `list`。
- **常见错误与异常**：`TypeError`：参数不可迭代，或元素之间无法比较（如 `sorted([1, "a"])`）。
- **基础示例**：
  ```python
  print(sorted({3, 1, 2}))              # [1, 2, 3]
  print(sorted("cab", reverse=True))    # ['c', 'b', 'a']
  ```
- **JS/TS 对照**：JS 的 `arr.sort()` 原地修改，且默认按字符串比较；`toSorted()` 才返回新数组。
- **实际项目 / 惯用建议**：高频用于给接口数据或检索结果按分数排序（配合 `key=` 和 `reverse=True`）；不想改动原列表时用 `sorted()`，允许原地排才用 `list.sort()`。

---

## 【必会】`dict()`

- **函数用途**：创建新字典。
- **Python 3.11 完整签名（重载）**：
  1. `dict(**kwargs)`
  2. `dict(mapping, /, **kwargs)`（【了解】）
  3. `dict(iterable, /, **kwargs)`
- **全部参数与默认值**：
  - `**kwargs`（可省略）：`名字=值` 形式的关键字参数，名字成为字符串键。不传任何参数得到 `{}`。
  - `mapping`（位置参数）：另一个字典等映射对象，复制其键值对。
  - `iterable`（位置参数）：每个元素都是长度为 2 的可迭代对象（如二元组），第一项作键、第二项作值。
- **参数限制**：`mapping` / `iterable` 最多传 1 个，只能按位置传入；可再加关键字参数，同名键以关键字为准；后出现的重复键覆盖先出现的。
- **返回值及类型**：新的 `dict`。
- **常见错误与异常**：`ValueError`：键值对长度不是 2（如 `dict([(1, 2, 3)])`）；`TypeError`：键不可哈希，或传入的对象不可迭代。
- **基础示例**：
  ```python
  print(dict([("Runoob", 1), ("Google", 2)]))  # {'Runoob': 1, 'Google': 2}
  print(dict(Runoob=1, Google=2))              # {'Runoob': 1, 'Google': 2}
  ```
- **JS/TS 对照**：第三种形式类似 `Object.fromEntries(pairs)` 或 `new Map(pairs)`。
- **实际项目 / 惯用建议**：字面量建字典优先用 `{...}`（更快且键不受变量名规则限制）；`dict()` 主要用于把键值对序列转字典或浅拷贝字典。

---

## 【必会】`dict.get()`

- **方法用途**：按键读取值；键不存在时返回默认值，不会报错，也不会新增键。
- **Python 3.11 完整签名**：`dict.get(self, key, default=None, /)`
- **全部参数与默认值**：
  - `key`（必填）：要读取的键。
  - `default`（可选，默认 `None`）：键不存在时的返回值。
- **参数限制**：两项都只能按位置传入，`d.get(key="a")` 会抛 `TypeError`。
- **返回值及类型**：键对应的值或 `default`，类型取决于存储的值。
- **常见错误与异常**：`TypeError`：键不可哈希（如列表），或按关键字传参。
- **基础示例**：`print({"a": 1}.get("b", 0))  # 0`
- **JS/TS 对照**：类似 `obj.b ?? 0` 或 `map.get("b") ?? 0`。用 `d["b"]` 读取缺失的键会抛 `KeyError`。
- **实际项目 / 惯用建议**：极高频，解析第三方 API / 大模型返回的 JSON 字典时，读取可选字段优先用 `d.get("key", 默认值)` 防止 `KeyError`。

---

## 【必会】`dict.keys()`、`dict.values()`、【了解】`dict.items()`

- **方法用途**：分别返回字典的键、值、`(键, 值)` 对的**视图**。视图随字典变化而变化，可用 `in`、`len()`、`list()`、`for` 使用。
- **Python 3.11 完整签名**：`dict.keys(self, /)`、`dict.values(self, /)`、`dict.items(self, /)`
- **全部参数与默认值**：无额外参数（仅隐式接收字典 `self`）。
- **参数限制**：不能传任何参数。
- **返回值及类型**：`dict_keys`、`dict_values`、`dict_items`，不是列表，不能用下标读取；需要列表时用 `list(...)` 转换。
- **常见错误与异常**：`TypeError`：传入参数，或对视图使用下标（如 `d.keys()[0]`）。
- **基础示例**：
  ```python
  d = {"name": "runoob", "code": 1}
  print(d.keys())          # dict_keys(['name', 'code'])
  print(list(d.items()))   # [('name', 'runoob'), ('code', 1)]
  ```
- **JS/TS 对照**：类似 `Object.keys(obj)` / `Object.values(obj)` / `Object.entries(obj)`，但 JS 返回的是普通数组。
- **实际项目 / 惯用建议**：遍历键直接写 `for k in d:`，同时取键值写 `for k, v in d.items():`；只在需要下标访问或“边遍历边删键”时才套一层 `list(...)`。

---

## 【必会】`bytes()`、【了解】`bytearray()`

- **函数用途**：`bytes()` 创建不可变字节序列；`bytearray()` 创建可修改的字节序列。
- **Python 3.11 完整签名（重载，两者相同）**：
  1. `bytes(source=b'')`
  2. `bytes(source, encoding, errors='strict')`
- **全部参数与默认值**：
  - `source`（可选，默认 `b''`）：非负整数 n（创建 n 个零字节）、字节类对象（复制）、0～255 的整数组成的可迭代对象，或字符串（必须同时给 `encoding`）。省略时得到空对象。
  - `encoding`（`source` 为字符串时必填）：编码名，如 `"utf-8"`。
  - `errors`（可选，默认 `'strict'`）：编码失败时的处理方式，`'strict'` 报错，`'replace'` 用 `?` 代替，`'ignore'` 跳过。
- **参数限制**：三项都可按位置或关键字传入；`source` 不是字符串时不能指定 `encoding`。
- **返回值及类型**：`bytes` / `bytearray`。按下标读取单个元素得到 `int`。
- **常见错误与异常**：`TypeError`：字符串没给编码（`bytes("hi")`），或非字符串却给了编码；`ValueError`：整数不在 0～255；`UnicodeEncodeError`：字符无法用指定编码表示；`LookupError`：未知编码名。
- **基础示例**：
  ```python
  print(bytes("hello", encoding="utf-8"))   # b'hello'
  data = bytearray(b"hello")
  data[0] = 72
  print(data)                               # bytearray(b'Hello')
  ```
- **JS/TS 对照**：类似 `new TextEncoder().encode(text)` 得到的 `Uint8Array`；`Uint8Array` 可修改，接近 `bytearray`。
- **实际项目 / 惯用建议**：字符串转字节通常写 `text.encode("utf-8")`（比 `bytes(text, encoding="utf-8")` 更简洁）；写死纯 ASCII 常量用 `b"..."`；`bytearray` 多用于二进制协议或文件流处理。

---

## 【必会】`str.encode()`

- **方法用途**：用指定编码把字符串转为 `bytes`。
- **Python 3.11 完整签名**：`str.encode(self, /, encoding='utf-8', errors='strict')`
- **全部参数与默认值**：
  - `encoding`（可选，默认 `'utf-8'`）：编码名。
  - `errors`（可选，默认 `'strict'`）：无法编码时的处理方式，含义同 `bytes()`。
- **参数限制**：两项都可按位置或关键字传入。
- **返回值及类型**：`bytes`。UTF-8 中 ASCII 字符占 1 字节，常用汉字占 3 字节。
- **常见错误与异常**：`UnicodeEncodeError`：字符无法用该编码表示（如 `"你".encode("ascii")`）；`LookupError`：未知编码名。
- **基础示例**：`print(len("你好".encode("utf-8")))  # 6`
- **JS/TS 对照**：`new TextEncoder().encode(text)`，只支持 UTF-8。
- **实际项目 / 惯用建议**：高频用于文件读写、HTTP 请求体、哈希签名与编码转换；默认即 UTF-8，项目里常简写为 `text.encode()`。

---

## 【必会】`bytes.decode()`、`bytearray.decode()`

- **方法用途**：用指定编码把字节序列还原为字符串。
- **Python 3.11 完整签名**：`bytes.decode(self, /, encoding='utf-8', errors='strict')`，`bytearray.decode` 相同。
- **全部参数与默认值**：
  - `encoding`（可选，默认 `'utf-8'`）：编码名，必须与编码时一致。
  - `errors`（可选，默认 `'strict'`）：无法解码时的处理方式，`'replace'` 用替代字符 `�` 继续。
- **参数限制**：两项都可按位置或关键字传入。
- **返回值及类型**：`str`。
- **常见错误与异常**：`UnicodeDecodeError`：字节不符合该编码（如 `b"\xff".decode()`）；`LookupError`：未知编码名。
- **基础示例**：`print(b"\xe4\xbd\xa0\xe5\xa5\xbd".decode("utf-8"))  # 你好`
- **JS/TS 对照**：`new TextDecoder("utf-8").decode(bytes)`。

---

## 【必会】`ord()`

- **函数用途**：返回单个字符的 Unicode 码点（整数）。
- **Python 3.11 完整签名**：`ord(c, /)`
- **全部参数与默认值**：`c`（必填位置参数）：长度为 1 的字符串，或长度为 1 的 `bytes` / `bytearray`。
- **参数限制**：只能按位置传入。
- **返回值及类型**：`int`。`ord("h")` 得到 104，`ord("你")` 得到 20320。
- **常见错误与异常**：`TypeError`：长度不是 1（如 `ord("ab")`），或类型不对。
- **基础示例**：`print(ord("h"), b"hello"[0] == ord("h"))  # 104 True`
- **JS/TS 对照**：类似 `"h".codePointAt(0)`。反向操作 `chr()` 见第 3 章。
- **实际项目 / 惯用建议**：日常业务低频，主要见于底层编解码校验、字符范围判断和算法题，认得即可。

---

更多示例见 Python 3.11 官方文档的[内置函数](https://docs.python.org/zh-cn/3.11/library/functions.html)、[序列类型](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#sequence-types-list-tuple-range)、[集合类型](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#set-types-set-frozenset)、[映射类型](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#mapping-types-dict)和[二进制序列类型](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)。
