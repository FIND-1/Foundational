"""第 2 章 · 集合（Set）与字典（Dictionary）。

用途：演示集合的创建、成员测试和四种集合运算，字典的创建、读写、视图、dict() 构造与字典推导式。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/04_set_dict_demo.py
预期结果：打印「Runoob 在集合中」；排序后的交集为 ['a', 'c']；循环和推导式都得到 {2: 4, 4: 16, 6: 36}；
get 读取缺失的键得到「未填写」。末尾演示 KeyError 和不可哈希键的报错。
"""

# ── 1. 集合：创建与成员测试 ───────────────────────────────────────────
# 格式：{元素, 元素, ...} -> set（自动去重）；元素 in 集合 -> bool（检查是否存在）
# 注意：集合无序，每次打印的顺序可能不同（in 见第 1 章 01_syntax_demo.py 末尾）
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)

if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')


# ── 2. 集合运算 ───────────────────────────────────────────────────────
# 格式：set(字符串或序列) -> set（把每个字符放进集合并去重；详见第 1 章 functions.md）
a = set('abracadabra')
b = set('alacazam')
print(a)           # a 中不重复的字符

# 格式：a - b 差集（在 a 不在 b）；a | b 并集；a & b 交集；a ^ b 对称差集（只在其中一个）
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 格式：sorted(集合) -> 排好序的新列表（原集合不变）
# 场景：打印或比较集合结果时，先排序可让输出顺序固定
print("排序后的差集、并集：", sorted(a - b), sorted(a | b))
print("排序后的交集、对称差集：", sorted(a & b), sorted(a ^ b))

# 注意：len(集合) 是去重后的数量，{1, 2, 3, 3} 只有 3 个元素（保留重复需用 list 或 tuple）
first = {1, 2, 3, 3}
print("去重后的数量：", len(first))

# 格式：set() -> 空集合；{} -> 空字典
# 注意：不能用 {} 建空集合；两者在 bool() 中都为 False
print("set() 和 {} 的类型：", type(set()), type({}))
print("空集合、空字典的真假：", bool(set()), bool({}))


# ── 3. 字典：创建与读写 ───────────────────────────────────────────────
# 格式：{} 空字典；{键: 值, 键: 值} 直接创建；字典[键] = 值 写入/覆盖；字典[键] 读取
# 注意：字符串键必须加引号；键可以是整数/元组等不可变类型且保持原类型（更接近 JS 的 Map）；不能用点号 d.key
# 注意：Python 3.7 起字典保持插入顺序
my_dict = {}
my_dict['one'] = "1 - 菜鸟教程"
my_dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(my_dict['one'])       # 键为 'one' 的值
print(my_dict[2])           # 键为 2 的值
print(tinydict)             # 完整的字典

# 格式：字典.keys() -> 所有键的视图；字典.values() -> 所有值的视图
print(tinydict.keys())      # dict_keys(['name', 'code', 'site'])
print(tinydict.values())    # dict_values(['runoob', 1, 'www.runoob.com'])


# ── 4. dict() 构造与字典推导式 ────────────────────────────────────────
# 格式：dict([(键1, 值1), (键2, 值2)]) -> dict（把每对元组的第一项作键、第二项作值）
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))

# 拓展：for 变量 in 序列: 依次取出每项执行缩进块（类似 JS 的 for (const x of [2, 4, 6])）
# 注意：下面每轮以 x 作键、x ** 2 作值写入 squares（如 x=2 时 squares[2] = 4），最终得到 {2: 4, 4: 16, 6: 36}
squares = {}
for x in (2, 4, 6):
    squares[x] = x ** 2
print("循环写入：", squares)  # {2: 4, 4: 16, 6: 36}

# 拓展：字典推导式 {键: 值 for 变量 in 序列} -> dict（结果与上面循环相同；需分步调试时展开循环更方便）
print("字典推导式：", {x: x ** 2 for x in (2, 4, 6)})

# 格式：dict(键名=值, ...) -> dict（关键字参数名自动变成字符串键，如 "Runoob"）
print(dict(Runoob=1, Google=2, Taobao=3))


# ── 5. 字典的常用读取方式 ─────────────────────────────────────────────
person = {"name": "Rain", "age": 18}
person["age"] = 19
person["city"] = "上海"
print("按键读取：", person["name"])

# 格式：字典.get(键, 默认值) -> 对应的值或默认值（不传默认值时返回 None）
# 场景：不确定键在不在时用 get()，不会报错也不会新增键（类似 JS 的 obj.job ?? "未填写"）
print("读取不存在的键：", person.get("job", "未填写"))
print("get 后仍没有 job：", "job" in person)  # in 检查字典的键

# 格式：字典.items() -> (键, 值) 元组视图；list(视图) -> 普通列表
print("所有键：", list(person.keys()))
print("所有值：", list(person.values()))
print("键值对：", list(person.items()))


# ── 拓展：观察字典的两种报错 ──────────────────────────────────────────
# 注意：用 [] 读不存在的键直接抛 KeyError（JS 对象返回 undefined）；try / except 见第 1 章 01_syntax_demo.py
try:
    _ = person["job"]
except KeyError as error:
    print("【进阶】缺少的键：", error)

# 注意：字典的键必须可哈希（不可变）；列表可变，作键会抛 TypeError
try:
    _ = {[1, 2]: "列表作键"}
except TypeError as error:
    print("【进阶】列表作键：", error)
