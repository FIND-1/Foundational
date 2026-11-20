# 【补充】第二章 Python 3.11 函数与方法速查

`/` 前的参数只能按位置传入；`*` 后的参数只能按名字传入。没有默认值的参数必填。先看【必会】，其他只需了解。

## 【必会】类型和真假判断

- `type`、`isinstance`、`len` 和 `set` 的完整签名见[第 1 章函数速查](../01-basic-syntax/functions.md)。本章用 `type(1) is int` 检查精确类型。
- `isinstance(1, int)` 和 `isinstance(True, int)` 都为真。前者是 `int` 实例，后者所属的 `bool` 继承自 `int`。
- 【了解】`issubclass(cls, classinfo, /)` 判断类 `cls` 是否为 `classinfo` 本身或其子类。两项均必填且仅限位置，`classinfo` 可为类、类型元组或联合类型。返回 `bool`，无效类型会抛 `TypeError`。`issubclass(bool, int)` 得到 `True`。JS 可沿原型链判断继承关系。
- `bool(x=False, /)` 返回布尔值，省略 `x` 得到 `False`。非空字符串为真，`bool("False")` 得到 `True`。多传参数或按名称传参会抛 `TypeError`。与 JS 的 `Boolean()` 相比，Python 的空列表和空字典为假。

## 【必会】列表和字符串

- `list(iterable=(), /)`：可选 `iterable` 是可迭代对象，省略创建空列表；返回新列表，非可迭代对象抛 `TypeError`。例 `list("ab")`。
- `list.append(object, /)`：必填 `object`，在原列表末尾添加一个对象，返回 `None`；参数数目不对抛 `TypeError`。例 `items.append("梨")`。
- `str.replace(old, new, count=-1, /)`：【了解】`old`、`new` 必须是字符串；`count` 为最多替换次数，默认 `-1` 表示全部；返回新字符串，类型不对抛 `TypeError`。例 `"aba".replace("a", "x", 1)` 得 `"xba"`。
- 【补充】JS 的数组 `push` 返回新长度，Python 的 `append` 返回 `None`。JS 的 `replace` 使用普通字符串匹配时默认只替换第一处，Python 默认替换所有匹配。

## 【了解】集合、排序和字典

- `set([1, 1, 2])` 去重后包含两个整数，可与 JS 的 `new Set([1, 1, 2])` 对照。
- `sorted(iterable, /, *, key=None, reverse=False)`：`iterable` 必填；`key` 默认 `None`，否则为接收一个元素并返回排序键的函数；`reverse` 默认 `False`，为真则倒序。返回新列表；对象不可迭代或键无法比较可抛 `TypeError`。例 `sorted([3, 1])` 得 `[1, 3]`。
- `dict(**kwargs)`、`dict(mapping, /, **kwargs)`、`dict(iterable, /, **kwargs)` 创建新字典。不传参数得到 `{}`；可按位置传入一个映射或键值对序列，再用可选的关键字增加或覆盖同名键。键不可哈希时抛 `TypeError`，键值对长度错误抛 `ValueError`。`dict([("a", 1)])` 得到 `{"a": 1}`，类似 JS 的 `Object.fromEntries()`。
- `d.get(key, default=None, /)` 从字典 `d` 按键读取。必填的 `key` 和可选的 `default` 仅限位置；返回对应的值，缺键时返回默认值（默认 `None`），结果类型取决于该值。键不可哈希抛 `TypeError`。`{"a": 1}.get("b", 0)` 得到 `0`。
- `dict.keys()`、`dict.values()`、`dict.items()`：均无参数，分别返回动态的键、值、键值对视图，不是普通列表；传入参数抛 `TypeError`。例 `list({"a": 1}.items())` 得 `[("a", 1)]`。

## 【了解】字节与编码

- `bytes([source[, encoding[, errors]]])`、`bytearray([source[, encoding[, errors]]])`：方括号表示参数可省略；不提供 `source` 时创建空对象。`source` 可为非负整数、字节类对象、0～255 的整数可迭代对象或字符串。字符串必须指定 `encoding`；`errors` 指定编码错误处理策略，默认 `strict`；未提供字符串时不能单独指定编码。分别返回不可变 `bytes` 和可变 `bytearray`；类型或数值不合法抛 `TypeError`、`ValueError`，编码失败可抛 `UnicodeError`。例 `bytes("A", encoding="utf-8")` 得 `b'A'`。
- `str.encode(encoding='utf-8', errors='strict')`：编码名称和错误处理均可省略；返回 `bytes`。未知编码抛 `LookupError`，无法编码可抛 `UnicodeEncodeError`。例 `"A".encode()` 得 `b'A'`。
- `bytes.decode(encoding='utf-8', errors='strict')` 与 `bytearray.decode(encoding='utf-8', errors='strict')`：参数含义相同，返回字符串；未知编码抛 `LookupError`，字节无法解码可抛 `UnicodeDecodeError`。例 `b'A'.decode()` 得 `"A"`。
- `ord(c, /)`：`c` 必须是长度为 1 的字符串或字节对象；返回其 Unicode 码点或字节值的整数，参数不合要求抛 `TypeError`。例 `ord("A")` 为 65。

## 【了解】原文单词反转实例

- `text.split(sep=None, maxsplit=-1)`：两个选项均可按位置或名字传入。默认按连续空白分割并忽略首尾空白，也可指定非空分隔字符串。`maxsplit` 默认不限制分割次数。返回字符串列表；空分隔符抛 `ValueError`，参数类型不合适抛 `TypeError`。`"I like Python".split(" ")` 得到三个单词。JS 的 `split()` 省略分隔符时会保留整段文本。
- `str.join(iterable, /)`：`iterable` 必填且只能按位置传入，必须是字符串组成的可迭代对象；返回用调用它的字符串连接后的新字符串。元素不是字符串或参数不可迭代时抛 `TypeError`。例 `" ".join(["I", "like", "Python"])` 得到 `"I like Python"`。
- 教程函数 `reverseWords(input)` 和课程中的 `reverse_words(text)` 接受一个必填字符串，可按位置或对应的参数名传入，返回单词倒序后的字符串。不支持 `split` 的输入会抛 `AttributeError`。例 `reverse_words("I like runoob")` 返回 `"runoob like I"`。
