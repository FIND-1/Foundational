"""第 3 章 · 容器类型转换：list、tuple、set、frozenset 与 dict。

用途：演示序列、集合、不可变集合和字典之间的互相转换，以及去重、原对象不变和常见错误。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/03-type-conversion/03_containers_demo.py
预期结果：字符串拆为 ['a', 'b', 'c'] 和 ('a', 'b', 'c')；去重后元素数量为 3 且原列表不变；
字典转列表只得到键；重复键以后者覆盖前者。末尾演示两种容器转换报错。
"""

# ── 1. 字符串与序列转 list / tuple / set ──────────────────────────────
# 格式：tuple(可迭代对象) -> tuple（按顺序取出每项构造不可变元组；list / set 见第 2 章）
# 注意：字符串也是可迭代对象，转换时会按单个字符拆开
text = "abc"
chars_list = list(text)
chars_tuple = tuple(text)
chars_set = set("aab")
print("列表：", chars_list)                      # ['a', 'b', 'c']
print("元组：", chars_tuple)                     # ('a', 'b', 'c')
print("集合（排序展示）：", sorted(chars_set))   # ['a', 'b']；集合本身无序


# ── 2. 列表去重与元组互转 ─────────────────────────────────────────────
# 注意：类型转换返回转换结果，不会自动修改原变量（此处原列表 numbers 不变）
#      是否创建新对象，取决于具体类型和转换方式
numbers = [1, 2, 2, 3]
unique = set(numbers)
print("去重后的元素数量：", len(unique))         # 3
print("原列表没有改变：", numbers)               # [1, 2, 2, 3]
print("元组转列表：", list((1, 2)))              # [1, 2]
print("列表转元组：", tuple([1, 2]))             # (1, 2)


# ── 3. 拓展：不可变集合 frozenset() ───────────────────────────────────
# 格式：frozenset(可迭代对象) -> frozenset（去重且不可增删元素）
# 注意：集合无序。调用 .add() 或 .remove() 会抛出 AttributeError
#      JS 没有原生等价类型，TS 的 ReadonlySet 只在类型层面限制修改
frozen_numbers = frozenset(numbers)
print("不可变集合：", frozen_numbers)                # frozenset({1, 2, 3})
print("数据类型：", type(frozen_numbers))            # <class 'frozenset'>

# 注意：集合包含相同的元素时，比较结果为 True，与传入顺序无关
a = frozenset([1, 2])
b = frozenset([2, 1])
print("集合是否相等：", a == b)                      # True

# 场景：frozenset 可哈希，可用作字典的键。普通 set 不可哈希
# 注意：a 和 b 相等且哈希值相同，因此两个键查到的是同一项
mapping = {a: "第一组数据"}
print("按原键查询：", mapping[a])                    # 第一组数据
print("按等价键查询：", mapping[b])                  # 第一组数据


# ── 4. 字典与键值对序列互转 ───────────────────────────────────────────
# 格式：dict(键值对序列) -> dict（每项依次提供键和值，见第 2 章 04_set_dict_demo.py）
# 注意：重复键以后出现的值为准，类似 JS 的 Object.fromEntries(pairs)
pairs = [("name", "Rain"), ("age", 18)]
person = dict(pairs)
overwritten = dict([("a", 1), ("b", 2), ("a", 9)])
print("键值对转字典：", person)                      # {'name': 'Rain', 'age': 18}
print("重复键以后者为准：", overwritten)             # {'a': 9, 'b': 2}

# 注意：list(字典) 只取键。要取出键值对，先调用 .items()（见第 2 章 04_set_dict_demo.py）
print("字典转列表只得到键：", list(person))          # ['name', 'age']
print("字典键值对列表：", list(person.items()))      # [('name', 'Rain'), ('age', 18)]


# ── 5. 拓展：容器类型转换的常见异常 ──────────────────────────────────
# 注意：set / frozenset 的元素和 dict 的键都必须可哈希
#      int、float、str、frozenset 可哈希。list、dict、set 不可哈希
print("整数列表转集合：", set([1, 2, 2]))            # {1, 2}

# 拓展：try 中的 set([[1, 2]]) 遇到不可哈希的列表，抛出 TypeError
# except TypeError as error 捕获异常并将它保存为 error，供后续打印
try:
    _ = set([[1, 2]])
except TypeError as error:
    print("列表不能作为集合元素：", error)

# 注意：tuple 的每个元素都可哈希时，整个 tuple 才可哈希
print("元组作为集合元素：", set([(1, 2)]))           # {(1, 2)}

# 注意：dict() 接收的每个键值对必须恰好有两项。长度为 3 时抛出 ValueError
print("合法键值对转字典：", dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}
try:
    _ = dict([("a", 1, 2)])
except ValueError as error:
    print("键值对长度错误：", error)
