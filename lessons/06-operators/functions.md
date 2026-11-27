# 第 6 章 · 函数速查（Python 3.11）

`print()` 和 `len()` 已在[第 1 章速查](../01-basic-syntax/functions.md)中讲过。`bool()` 的真值规则见[第 2 章速查](../02-basic-data-types/functions.md#必会bool)。

## 【了解】`id()`

- **用途**。读出对象的标识。对象存活期间，标识保持固定，同时存活的不同对象拥有不同标识。
- **完整签名**。`id(obj, /)`，只有一种调用形式。`obj` 必填，可传入任意 Python 对象，无默认值。`/` 表示只能按位置传入。
- **返回值**。对象标识的整数（`int`）。生命周期互不重叠的对象可以复用同一个标识。CPython 把对象地址用作标识。
- **常见异常**。漏传、多传，或写作 `id(obj=某对象)` 会抛 `TypeError`。
- **JS/TS 对照**。JS 比较两个对象引用可用 `===`，没有对应的对象标识整数 API。Python 日常用 `is` 判断是否为同一对象，`id()` 多用于观察和调试。

下面两个变量引用同一个列表，读取两次标识并比较，结果为 `True`。

```python
items = []
alias = items
print(id(items) == id(alias))
```

[Python 3.11 `id()` 文档](https://docs.python.org/3.11/library/functions.html#id)
