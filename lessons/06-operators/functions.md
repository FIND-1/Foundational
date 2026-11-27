# 第 6 章 · 函数与方法完整速查（Python 3.11）

前几章已讲的 API 不再重复，可按需回查：

- 见[第 1 章函数速查](../01-basic-syntax/functions.md)：`print()`、`len()`。
- 见[第 2 章函数速查](../02-basic-data-types/functions.md)：[`bool()`](../02-basic-data-types/functions.md#必会bool)（真假值规则）、`dict.values()`（字典值视图，可用于 `v in d.values()`）。
- 见[第 3 章函数速查](../03-type-conversion/functions.md)：`int()`（向零截断）、`repr()`（带引号的调试表示）。

---

## 【了解】`id()`

- **函数用途**：读取对象的唯一标识。对象存活期间，标识保持固定；同时存活的不同对象拥有不同标识。
- **Python 3.11 完整签名**：`id(obj, /)`
- **全部参数与默认值**：
  - `obj`（必填位置参数，无默认值）：任意 Python 对象。
- **参数限制**：`obj` 位于 `/` 之前，只能按位置传入，`id(obj=items)` 会抛 `TypeError`；必须恰好传 1 个参数。
- **返回值及类型**：`int`。生命周期互不重叠的对象可能复用同一个标识；CPython 把对象内存地址作为标识值。
- **常见错误与异常**：`TypeError`：漏传、多传参数，或按关键字传参。
- **基础示例**：
  ```python
  items = []
  alias = items
  print(id(items) == id(alias))  # True
  ```
- **JS/TS 对照**：JS 比较两个对象引用直接用 `===`，没有内置的对象标识整数 API。
- **实际项目 / 惯用建议**：日常业务判断两个变量是否指向同一对象直接写 `a is b`（判空固定写 `x is None`）；`id()` 仅在调试或学习对象绑定时用来观察引用身份。

---

更多示例见 Python 3.11 官方文档的 [`id()`](https://docs.python.org/zh-cn/3.11/library/functions.html#id) 和[表达式与运算符](https://docs.python.org/zh-cn/3.11/reference/expressions.html)。
