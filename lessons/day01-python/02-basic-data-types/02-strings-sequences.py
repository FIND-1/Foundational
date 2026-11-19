"""字符串、列表和元组的基本操作。"""

text = "Python"
print("字符串索引和切片：", text[0], text[-1], text[1:5:2])  # P n yh
print("拼接与重复：", text + "3", text * 2)
print("字符串是不可变的：", text.replace("P", "J"), text)  # 原值不变

items = ["苹果", "香蕉", "梨", "橙子"]
print("列表切片：", items[1:3])  # 香蕉、梨
items[0] = "桃子"  # 列表可修改
items.append("葡萄")
print("修改后：", items)
print("列表拼接和重复：", [1, 2] + [3], [1, 2] * 2)

point = (3, 4)
print("元组：", point[0], point[:1], point + (5,))
print("空元组和单元素元组：", (), (3,))
print("有无逗号的区别：", type((3,)), type((3)))
