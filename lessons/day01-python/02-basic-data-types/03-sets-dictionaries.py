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
