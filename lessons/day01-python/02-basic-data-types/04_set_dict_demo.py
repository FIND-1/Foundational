"""第 2 章 · 集合（Set）与字典（Dictionary）。

用途：演示集合的创建、成员测试和四种集合运算，字典的创建、读写、视图、dict() 构造与字典推导式。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/04_set_dict_demo.py
预期结果：打印「Runoob 在集合中」；排序后的交集为 ['a', 'c']；循环和推导式都得到 {2: 4, 4: 16, 6: 36}；
get 读取缺失的键得到「未填写」。末尾演示 KeyError 和不可哈希键的报错。
"""

# ── 1. 集合：创建与成员测试 ───────────────────────────────────────────
# 【必会】{元素, 元素, ...} 创建集合，重复元素自动去掉。集合不保证顺序，每次打印的顺序可能不同。
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)

# 元素 in 集合 检查是否包含该元素（in 的首次讲解见第 1 章 01_syntax_demo.py 末尾）。
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')


# ── 2. 集合运算 ───────────────────────────────────────────────────────
# set(字符串) 把每个字符放进集合，重复字符只留一个（set() 见第 1 章 functions.md）。
a = set('abracadabra')
b = set('alacazam')
print(a)           # a 中不重复的字符

# 【必会】- 差集（在 a 不在 b）、| 并集（在 a 或 b）、& 交集（同时在两者）、^ 对称差集（只在其中一个）。
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 【补充】【必会】sorted(集合) 返回排好序的新列表，原集合不变。打印前排序可以让每次的顺序一致。
print("排序后的差集、并集：", sorted(a - b), sorted(a | b))
print("排序后的交集、对称差集：", sorted(a & b), sorted(a ^ b))

# 【补充】len(集合) 是去重后的元素个数：{1, 2, 3, 3} 只有 3 个元素。
first = {1, 2, 3, 3}
print("去重后的数量：", len(first))


# 【必会】空集合必须写 set()，因为 {} 创建的是空字典。两者都是假值。
print("set() 和 {} 的类型：", type(set()), type({}))
print("空集合、空字典的真假：", bool(set()), bool({}))


# ── 3. 字典：创建与读写 ───────────────────────────────────────────────
# 【必会】{} 创建空字典；字典[键] = 值 在键不存在时新增，存在时修改。字典[键] 读取对应的值。
# 【补充】键可以是整数等不可变类型；JS 普通对象的键会被转成字符串，更接近的是 Map。
my_dict = {}
my_dict['one'] = "1 - 菜鸟教程"
my_dict[2] = "2 - 菜鸟工具"

# 【必会】{键: 值, 键: 值} 直接写出字典。Python 3.7 起字典保持插入顺序。
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(my_dict['one'])       # 键为 'one' 的值
print(my_dict[2])           # 键为 2 的值
print(tinydict)             # 完整的字典

# 【必会】字典.keys() 返回所有键的视图，字典.values() 返回所有值的视图。
print(tinydict.keys())      # dict_keys(['name', 'code', 'site'])
print(tinydict.values())    # dict_values(['runoob', 1, 'www.runoob.com'])


# ── 4. dict() 构造与字典推导式 ────────────────────────────────────────
# 【必会】dict(键值对序列) 把每一对（这里是元组，见 03_list_tuple_demo.py）的第一项作键、第二项作值，得到 {'Runoob': 1, ...}。
#  格式 {键: 值, 键: 值}
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))

# 【补充】【进阶】for 变量 in 序列: 依次取出每一项执行缩进块，类似 JS 的 for (const x of [2, 4, 6])。
squares = {}
for x in (2, 4, 6):
    squares[x] = x ** 2  
print("循环写入：", squares)  # {2: 4, 4: 16, 6: 36}

# 【进阶】循环只为每一项生成一个键值对时，可写成字典推导式 {键: 值 for 变量 in 序列}。
# 先读 for 部分，再看冒号两侧的键和值，结果与上面的循环相同。需要分步调试时，展开的循环更方便。
print("字典推导式：", {x: x ** 2 for x in (2, 4, 6)})

# 【必会】dict(名字=值, ...) 把关键字参数的名字用作字符串键，第一个键是 "Runoob"。
print(dict(Runoob=1, Google=2, Taobao=3))


# ── 5. 【补充】字典的常用读取方式 ─────────────────────────────────────
person = {"name": "Rain", "age": 18}
person["age"] = 19
person["city"] = "上海"
print("按键读取：", person["name"])
# 【必会】字典.get(键, 默认值) 在键不存在时返回默认值，且不会新增这个键。
print("读取不存在的键：", person.get("job", "未填写"))
print("get 后仍没有 job：", "job" in person)  # in 检查字典的键
# 【必会】list(视图) 把视图转成普通列表；字典.items() 返回 (键, 值) 对的视图。
print("所有键：", list(person.keys()))
print("所有值：", list(person.values()))
print("键值对：", list(person.items()))


# ── 【补充】【进阶】观察字典的两种报错 ────────────────────────────────
# try / except 的读法见第 1 章 01_syntax_demo.py 末尾。
# 用 [] 读取不存在的键会抛 KeyError；JS 对象读取不存在的属性返回 undefined。
try:
    _ = person["job"]
except KeyError as error:
    print("【进阶】缺少的键：", error)

# 字典的键必须可哈希（不可变）。列表可以修改，不能作键，会抛 TypeError。
try:
    _ = {[1, 2]: "列表作键"}
except TypeError as error:
    print("【进阶】列表作键：", error)
