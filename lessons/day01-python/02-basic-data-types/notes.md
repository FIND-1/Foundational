# 第 2 章笔记

> 定位：只记录**我理解了什么、验证了什么、踩了什么坑**（不摘抄教材）。
> 阶段性记录：学到哪一小节就记哪一小节，按需选填，不必每节写满五部分；不提前填未学内容，也不仅凭测试通过就标记掌握。

## 1. 核心知识点

<!-- 用自己的话解释是什么、有什么用、适用条件 -->
Python 的 6 个标准数据大类：Number、String、Tuple、List、Dictionary、Set。
其中 Number 是大类统称（不是内置类型名），包含 int、float、complex、bool 四种具体类型；在继承关系上 bool 是 int 的子类，但日常当作逻辑值使用，因此常被单独列出。

不可变数据（4 个）：Number、String、bool、Tuple
可变数据（3 个）：List、Dictionary 、Set

## 2. 最小代码示例

<!-- 一段可执行代码 + 预期输出，用来验证理解 -->

```python
# 1. type vs isinstance（bool 是 int 的子类）
print(isinstance(True, int), type(True) is int)  # True False

# 2. 元组包含可变对象（外层不可换槽位，内层列表可原地改）
t = ([1, 2], 3)
t[0].append(9)
print(t)                                         # ([1, 2, 9], 3)

# 3. 字典安全读取 & 集合自动去重
d = {"name": "Rain"}
print(d.get("job", "未填写"), len({1, 2, 3, 3}))  # 未填写 3

# 4. bytes 单下标 vs 切片 vs 拼接 & 拼 emoji
b = b"hello"
print(b[1], b[1:3], b + b"world")                # 101 b'el' b'helloworld'
print(("😀".encode("utf-8") + b).decode("utf-8"))  # 😀hello
```

## 3. 与 JS/TS 的差异

<!-- 只记录真正容易混淆、值得记住的区别 -->

- **字典 vs JS 对象**：Python 字典不能点号取值（`d.name` 报错）；读缺失键 `d["job"]` 抛 `KeyError`（安全读用 `d.get("job", 默认值)`）；字符串键必须加引号，数字键不会转字符串。
- **空容器真假值**：Python 中 `[]`、`{}`、`()`、`set()` 全是 `False`（JS 中 `[]`、`{}` 为真）。
- **字符串拆分与拼接**：Python `split("")` 报 `ValueError`；`join` 写法相反（`"--".join(words)`）。
- **`bool(x)` 的使用时机**：只在保存/返回布尔结果时调用（类似 JS `Boolean(x)` / `!!x`），`if` 条件里直接写 `if x:`。
- **元组与字节的可变性**：`tuple` 不可变、`list` 可变；`bytes` 不可变、`bytearray` 可变（类似 `tuple` vs `list`）。

## 4. 易错点与验证记录

<!-- 原先怎么理解、实际结果是什么、为什么出错 -->

- **6 种还是 7 种**：`Number` 是大类统称而非内置类名；`bool` 是 `int` 子类归进 `Number` 为 6 大类，按日常逻辑值单列为 7 项（不可变 4 + 可变 3）。
- **`complex` 的实部与虚部**：`z = complex(3, 4)` 等价于 `3 + 4j`；`z.real` / `z.imag` 返回的都是 `float`，且 `.imag` 不带 `j`（日常业务/AI 应用层极少用，认得即可）。
- **`t = ([1, 2], 3)` 的类型**：外层仍是 `tuple`，不是列表；不能换槽位 `t[0] = ...`，但可改内层列表（类似 JS `Object.freeze` 浅冻结）。
- **`bytes` 拼接与多字节字符**：`b` 只是类型外壳，不会拼进内容里；`bytearray[0]` 只能赋 `0～255` 整数，塞汉字或 emoji 要先 `.encode("utf-8")` 再拼接或切片赋值（改文本优先先 `decode` 回 `str`）。
- **原地修改方法返回 `None`（测验踩坑）**：`result = items.append('香蕉')` 执行后，`items` 会原地变成 `['苹果', '香蕉']`，但 `result` 是 **`None`** 而不是列表。Python 的惯例是“原地修改类方法（`append`、`sort`、`reverse`）统一返回 `None`，不改原对象的方法/函数（`sorted`、`replace`）才返回新对象”，切忌写成 `items = items.append(...)` 把原列表覆盖成 `None`。
- **第 2 章练习复盘（写法规范）**：
  - 优先复用已有变量（如 `total_seconds // 60`）而不是硬编码 `125`，修改输入时计算结果自动联动；
  - 避免多余类型转换：`sorted(set(first) & set(second))` 直接接收集合并返回列表，无需外包 `list()`；
  - 遵循 PEP 8：顶层 `def` 函数之间空两行；字典推导式 `{n: n ** 2 for n in numbers}` 简洁地道，值得保持。

## 5. 待解决的问题

<!-- 暂时没理解的问题，下一次再验证 -->

- **教程“6 种标准数据类型”与官方层级分类的衔接**：教程按具体类型拆开讲（Number/String/Tuple/List/Dictionary/Set + bool），官方按能力分为数字/序列/映射/集合四大层级（`str`/`list`/`tuple` 同属序列，类似 JS 里 `Array`/`Map`/`Set` 拆开教但规范上都归 `Object`）。后续学完类型转换、序列操作和面向对象后再回看巩固这套层级关系。
