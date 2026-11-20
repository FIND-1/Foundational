"""第 3 章 · 观察容器转换与去重。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/03-type-conversion/03-containers.py
列表转为集合后含三个不同的数，原列表仍有四项。
"""

# 【补充】容器转换练习。
text = "abc"
print("列表：", list(text))       # ['a', 'b', 'c']
# tuple(text) 按原顺序把每个字符作为元组的一项，得到三个字符。
print("元组：", tuple(text))
print("集合：", set("aab"))      # 去重，显示顺序不固定

numbers = [1, 2, 2, 3]
unique = set(numbers)
print("去重后的元素数量：", len(unique))  # 3
print("原列表没有改变：", numbers)
print("元组转列表：", list((1, 2)))

# dict() 接收键值对，重复的键以后一个值为准。
pairs = [("name", "Rain"), ("age", 18)]
person = dict(pairs)
print("键值对转字典：", person)
print("字典转列表只得到键：", list(person))
print("字典键值对列表：", list(person.items()))

# 集合元素和字典的键必须可哈希，不能直接使用列表作为元素或键。
