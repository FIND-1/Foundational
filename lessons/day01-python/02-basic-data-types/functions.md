# 【补充】第二章 Python 3.11 函数与方法速查

`/` 前的参数只能按位置传入；`*` 后的参数只能按名字传入。没有默认值的参数必填。先看【必会】，其他只需了解。

## 【必会】type 和 isinstance

- `type(object, /)` 返回对象的具体类型，例如 `type(1)` 为 `int`。另有【了解】形式 `type(name, bases, dict, **kwds)`：传入类名字符串、基类元组、属性字典及可选类创建关键字，返回新类；参数错误抛 `TypeError`。例如 `type("A", (), {})` 创建类。
- `isinstance(object, classinfo, /)` 判断对象是否属于类型或其子类，返回 `bool`；`classinfo` 可为类型、类型元组或类型联合。类型无效通常抛 `TypeError`。例如 `isinstance(1, int)` 为 `True`。两参数均必填。
- `issubclass(class, classinfo, /)`：【了解】判断第一个参数指定的类是否为第二个参数指定的类或其子类；`classinfo` 可为类、类型元组或类型联合。两个参数均必填且只能按位置传入，返回 `bool`；无效参数会抛 `TypeError`。例 `issubclass(bool, int)` 为 `True`。

## 【必会】列表和字符串

- `list(iterable=(), /)`：可选 `iterable` 是可迭代对象，省略创建空列表；返回新列表，非可迭代对象抛 `TypeError`。例 `list("ab")`。
- `list.append(object, /)`：必填 `object`，在原列表末尾添加一个对象，返回 `None`；参数数目不对抛 `TypeError`。例 `items.append("梨")`。
- `str.replace(old, new, count=-1, /)`：【了解】`old`、`new` 必须是字符串；`count` 为最多替换次数，默认 `-1` 表示全部；返回新字符串，类型不对抛 `TypeError`。例 `"aba".replace("a", "x", 1)` 得 `"xba"`。
- `len(obj, /)` 的参数、返回值和错误见[官方文档](https://docs.python.org/zh-cn/3.11/library/functions.html#len)。

## 【了解】集合、排序和字典

- `set(iterable=(), /)`：省略创建空集合；从可迭代对象得到集合并去重，返回新集合。不可迭代或元素不可哈希抛 `TypeError`；例 `set([1, 1, 2])`。
- `sorted(iterable, /, *, key=None, reverse=False)`：`iterable` 必填；`key` 默认 `None`，否则为接收一个元素并返回排序键的函数；`reverse` 默认 `False`，为真则倒序。返回新列表；对象不可迭代或键无法比较可抛 `TypeError`。例 `sorted([3, 1])` 得 `[1, 3]`。
- `dict.get(key, default=None, /)`：必填 `key`；没有该键返回 `default`，默认 `None`；键不可哈希抛 `TypeError`。例 `{"a": 1}.get("b", 0)` 为 `0`。
- `dict.keys()`、`dict.values()`、`dict.items()`：均无参数，分别返回动态的键、值、键值对视图，不是普通列表；传入参数抛 `TypeError`。例 `list({"a": 1}.items())` 得 `[("a", 1)]`。

## 【了解】字节与编码

- `bytes([source[, encoding[, errors]]])`、`bytearray([source[, encoding[, errors]]])`：方括号表示参数可省略；不提供 `source` 时创建空对象。`source` 可为非负整数、字节类对象、0～255 的整数可迭代对象或字符串。字符串必须指定 `encoding`；`errors` 指定编码错误处理策略，默认 `strict`；未提供字符串时不能单独指定编码。分别返回不可变 `bytes` 和可变 `bytearray`；类型或数值不合法抛 `TypeError`、`ValueError`，编码失败可抛 `UnicodeError`。例 `bytes("A", encoding="utf-8")` 得 `b'A'`。
- `str.encode(encoding='utf-8', errors='strict')`：编码名称和错误处理均可省略；返回 `bytes`。未知编码抛 `LookupError`，无法编码可抛 `UnicodeEncodeError`。例 `"A".encode()` 得 `b'A'`。
- `bytes.decode(encoding='utf-8', errors='strict')` 与 `bytearray.decode(encoding='utf-8', errors='strict')`：参数含义相同，返回字符串；未知编码抛 `LookupError`，字节无法解码可抛 `UnicodeDecodeError`。例 `b'A'.decode()` 得 `"A"`。
- `ord(c, /)`：`c` 必须是长度为 1 的字符串或字节对象；返回其 Unicode 码点或字节值的整数，参数不合要求抛 `TypeError`。例 `ord("A")` 为 65。

## 【了解】原文单词反转实例

- `str.split(sep=None, maxsplit=-1)`：`sep` 默认 `None` 时按连续空白分割，也可提供非空字符串作为分隔符；`maxsplit` 默认 `-1`，表示不限制分割次数，否则限制最多分割次数。返回字符串列表。空分隔符抛 `ValueError`，类型不合适抛 `TypeError`。例 `"I like Python".split(" ")` 得到三个单词的列表。
- `str.join(iterable, /)`：`iterable` 必填且只能按位置传入，必须是字符串组成的可迭代对象；返回用调用它的字符串连接后的新字符串。元素不是字符串或参数不可迭代时抛 `TypeError`。例 `" ".join(["I", "like", "Python"])` 得到 `"I like Python"`。
- `reverseWords(input)` 是原文自定义函数，`input` 必填、无默认值，可按位置或名字传入；示例传入字符串，返回以空格分隔且顺序反转后的字符串。参数不支持 `split` 时会抛 `AttributeError`。例 `reverseWords("I like runoob")` 返回 `"runoob like I"`。
