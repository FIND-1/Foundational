"""容器转换：可迭代对象可以转换为列表、元组或集合。"""

# 【补充】容器转换练习。
text = "abc"
print("列表：", list(text))       # ['a', 'b', 'c']
print("元组：", tuple(text))      # ('a', 'b', 'c')
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
