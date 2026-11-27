# 第 5 章 · 函数速查（Python 3.11）

`print()` 见[第 1 章速查](../01-basic-syntax/functions.md#必会print)，`help()` 见[第 4 章速查](../04-interpreter/functions.md#了解help)。`__doc__` 是属性，读取时直接写 `对象.__doc__`，模块中的写法见[第 1 章示例](../01-basic-syntax/01_syntax_demo.py)。

## 【了解】`inspect.getdoc()`

- **用途**：获取对象的文档字符串，清除首行前导空白、后续各行共有的缩进和首尾空行，并将制表符展开为空格。类、方法、属性或描述符没有自己的文档时，会尝试沿继承层级获取。
- **完整签名**：`inspect.getdoc(object)`。只有这一种调用形式。`object` 必填、无默认值，可按位置或用 `object=` 传入，通常传模块、函数或类对象。
- **返回值**：清理后的 `str`。没有可用文档或 `__doc__` 不是字符串时，返回 `None`。
- **常见异常**：漏传、重复传入、传入过多参数或使用错误的参数名会抛 `TypeError`。
- **JS/TS 对照**：JSDoc 通常由编辑器或文档工具解析。Python 可以直接传入运行时对象读取文档。
- **实际项目**：终端里查文档可用 `help(对象)`。需要把清理后的文档作为文本使用时，用 `inspect.getdoc(对象)`。

下面的 `describe()` 只有文档字符串。把函数对象 `describe` 传给 `inspect.getdoc()` 时，得到的是两行清理后的文本。

```python
import inspect


def describe():
    """说明脚本的用途。

    这行缩进会在读取时被去掉。
    """


print(inspect.getdoc(describe))
```

[Python 3.11 `inspect.getdoc()` 文档](https://docs.python.org/3.11/library/inspect.html#inspect.getdoc)
