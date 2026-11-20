"""第 2 章 · 复习基本数据类型。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/02-basic-data-types/example.py
依次观察变量类型、集合去重后的数量 2，以及 UTF-8 字节解码得到的“你好”。各项用法见本章四个主题脚本。
"""


counter = 100          # 整型变量
miles = 1000.0         # 浮点型变量
name = "runoob"        # 字符串

print(counter)
print(miles)
print(name)

# 【补充】基本数据类型和常用操作。

# 变量指向对象，类型属于对象。
age, height, name = 18, 1.75, "Rain"
print("类型：", type(age), type(height), type(name))
print("整数判断：", isinstance(age, int))
a = b = 10
print("多变量赋值：", a, b)

print("数字：", 7 / 2, 7 // 2, 7 % 2, 2 ** 3)  # 3.5 3 1 8
print("布尔与复数：", True, 2 + 3j)

word = "Python"
print("字符串：", word[0], word[1:4], word * 2)  # P yth PythonPython

fruits = ["苹果", "香蕉", "苹果"]
fruits[1] = "橙子"
fruits.append("梨")
print("列表：", fruits)

point = (3, 4)
single = (3,)  # 逗号不能省略
print("元组：", point, single, point[0])

colors = {"红", "蓝", "红"}  # 重复值自动去重；展示顺序不固定
print("集合数量：", len(colors))
print("交集：", {1, 2} & {2, 3})  # {2}

person = {"name": "Rain", "age": 18}
person["age"] = 19
print("字典：", person["name"], person["age"])

# 文本与字节之间需要指定编码；bytes 本身不可变。
message = "你好"
encoded = message.encode("utf-8")
print("UTF-8 字节：", encoded)
print("解码为文本：", encoded.decode("utf-8"))  # 你好
