"""第 2 章 · 集合运算、字典的创建与读取。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/02-basic-data-types/03-sets-dictionaries.py
观察两个集合的共同元素，以及循环和字典推导式得到的同一组平方值。
"""

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合（无序，重复元素会被自动去掉）

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set 可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)           # a 中的唯一字符

print(a - b)       # a 和 b 的差集（在 a 中但不在 b 中）
print(a | b)       # a 和 b 的并集（在 a 或 b 中）
print(a & b)       # a 和 b 的交集（同时在 a 和 b 中）
print(a ^ b)       # a 和 b 的对称差集（在 a 或 b 中，但不同时存在）

# {} 创建空字典；给 my_dict[键] 赋值会新增或更新该键对应的值。
my_dict = {}
my_dict['one'] = "1 - 菜鸟教程"
my_dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(my_dict['one'])       # 输出键为 'one' 的值
print(my_dict[2])           # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
# keys() 和 values() 分别返回键和值的视图。打印时能看到 name 等键及其对应的值。
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

# dict(键值对列表) 用每一对中的第一项作键、第二项作值。
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
# 【补充】【进阶】先读循环：for 每次取出一个数，缩进块写入这个数和它的平方。
squares = {}
for x in (2, 4, 6):
    squares[x] = x ** 2
print(squares)
# 当循环只为每个元素生成一个键值对时，可用字典推导式。从 for 开始读，再看冒号两侧的键和值。
# 两种写法都得到 {2: 4, 4: 16, 6: 36}；需要分步调试时，展开的循环更容易观察中间值。
print({x: x ** 2 for x in (2, 4, 6)})
# dict(名称=值) 把关键字的名字用作字符串键，例如第一个键是 "Runoob"。
print(dict(Runoob=1, Google=2, Taobao=3))

# 【补充】集合和字典：观察元素、键和值。

first = {1, 2, 3, 3}
second = {3, 4}
print("集合去重后的数量：", len(first))  # 3
print("成员判断：", 2 in first)  # True
# sorted(集合) 返回排序后的新列表，让每次打印的顺序一致。
print("并集、交集：", sorted(first | second), sorted(first & second))
print("差集、对称差集：", sorted(first - second), sorted(first ^ second))
print("空集合与空字典：", type(set()), type({}))

person = {"name": "Rain", "age": 18}
person["age"] = 19
person["city"] = "上海"
print("按键读取：", person["name"])
# 需要默认值时用 get(键, 默认值)。这里缺少 job，返回“未填写”，字典中不会新增 job。
print("读取不存在的键：", person.get("job", "未填写"))
print("所有键：", list(person.keys()))
print("所有值：", list(person.values()))
# items() 返回键值对视图，list(...) 把这些键值对收进列表。
print("键值对：", list(person.items()))
