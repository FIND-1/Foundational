"""集合和字典。"""

#!/usr/bin/python3

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

#!/usr/bin/python3

my_dict = {}
my_dict['one'] = "1 - 菜鸟教程"
my_dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(my_dict['one'])       # 输出键为 'one' 的值
print(my_dict[2])           # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

# 使用 print 显示创建字典的结果。
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print({x: x**2 for x in (2, 4, 6)})
print(dict(Runoob=1, Google=2, Taobao=3))



# 【补充】以下保留原有扩展示例。
"""集合和字典：观察元素、键和值。"""

first = {1, 2, 3, 3}
second = {3, 4}
print("集合去重后的数量：", len(first))  # 3
print("成员判断：", 2 in first)  # True
print("并集、交集：", sorted(first | second), sorted(first & second))  # sorted 返回排序后的列表
print("差集、对称差集：", sorted(first - second), sorted(first ^ second))
print("空集合与空字典：", type(set()), type({}))

person = {"name": "Rain", "age": 18}
person["age"] = 19
person["city"] = "上海"
print("按键读取：", person["name"])
print("读取不存在的键：", person.get("job", "未填写"))
print("所有键：", list(person.keys()))
print("所有值：", list(person.values()))
print("键值对：", list(person.items()))
