# 第 3 章笔记

> 定位：只记录**我理解了什么、验证了什么、踩了什么坑**（不摘抄教材）。
> 阶段性记录：学到哪一小节就记哪一小节，按需选填，不必每节写满五部分；不提前填未学内容，也不仅凭测试通过就标记掌握。

## 1. 核心知识点

<!-- 用自己的话解释是什么、有什么用、适用条件 -->

- **隐式 vs 显式转换**：兼容数字运算自动提升（`int + float -> float`），原变量不变；字符串与数字必须显式转换，建议用新变量保存结果，避免覆盖原输入（如 `"0456"`）。
- **`frozenset`**：去重、无序、不可增删，因此可哈希、能作字典键（普通 `set` 不行；`tuple` 需元素全部可哈希）。
- **字符数 vs 字节数**：`len(str)` 数字符，`len(bytes)` 数 UTF-8 字节（ASCII 1 字节、常用汉字 3 字节、Emoji 4 字节）。
- **`eval()` vs `ast.literal_eval()`**：`eval()` 执行表达式并可读取作用域变量，严禁用于不可信输入；`literal_eval()`
- **`type(x).__name__`（拓展）**：取出纯类型名字符串（如 `"int"`），区别于模块级 `__name__ == "__main__"`。

## 2. 最小代码示例

<!-- 一段可执行代码 + 预期输出，用来验证理解 -->

```python
from ast import literal_eval

# 1. 真假文本、截断、字符数与 UTF-8 字节数
print(bool("False"), "False".lower() == "true", int(-3.9))               # True False -3
print(len("你好"), len("你好".encode("utf-8")))                           # 2 6

# 2. frozenset 不可变且无序，按值相等命中字典键
a, b = frozenset([1, 2]), frozenset([2, 1])
print(a == b, {a: "第一组数据"}[b])                                       # True 第一组数据

# 3. list() 拆字符 vs literal_eval() 还原字面量
print(list("[1,2]")[:2], literal_eval("[1, 2]"), literal_eval("False"))  # ['[', '1'] [1, 2] False

# 4. 类型对象与纯类型名
print(type(123), type(123).__name__)                                     # <class 'int'> int
```

## 3. 与 JS/TS 的差异

<!-- 只记录真正容易混淆、值得记住的区别 -->

- **非空字符串转布尔**：`bool("False")` 与 JS `Boolean("False")` **均为真**（只有 JS `JSON.parse("false")` 才解析语义）；真假值真正的区别在空容器（Python `[]`/`{}` 为假，JS 为真）。
- **字典查键**：Python `dict` 按**值相等（`==`）+ 哈希**匹配；JS `Map` 用对象/`Set` 作键按引用匹配。
- **`frozenset` vs TS `ReadonlySet`**：前者运行期不可变，后者仅编译期约束。
- **字面量解析与编码**：`ast.literal_eval()` 类似 Python 字面量版 `JSON.parse()`；Emoji `"😀"` 长度 Python 为 `1`、JS 为 `2`（UTF-16），UTF-8 字节两边都是 `4`。
- **取类型名**：`type(x).__name__` 类似 JS `x.constructor.name`。

## 4. 易错点与验证记录

<!-- 原先怎么理解、实际结果是什么、为什么出错 -->

- **混淆 `frozenset` 的“不可变”和“无序等价”**：`mapping[frozenset([2, 1])]` 是新建查询键而非修改原集合；无序使 `[1, 2]` 与 `[2, 1]` 键相等（`tuple` 有序则不等）。

- **`list("[1, 2, 3]")` 不会还原列表**：会按字符拆开，还原字面量应使用 `ast.literal_eval()`。
- **练习复盘（`exercises_03.py`，51 项全过）**：变量复用良好；已清理：① 删去误导入 `from email.policy import default` 并把 `literal_eval` 移到顶部；② `list(d.keys())` 简写为 `list(d)`；③ 顶层 `def` 间补齐空两行；④ 去掉未要求吞异常的函数里多余的 `try/except`。

## 5. 待解决的问题

<!-- 暂时没理解的问题，下一次再验证 -->

- 后续对比实践 `json.loads()` 与 `ast.literal_eval()` 的适用边界。
- 后续学文件/二进制处理时再回看 `memoryview()`。
