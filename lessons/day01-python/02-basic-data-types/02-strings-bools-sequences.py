"""字符串、布尔值、列表和元组。"""

#!/usr/bin/python3

my_str = 'Runoob'       # 定义一个字符串变量（避免使用 str 作为变量名，会覆盖内置类型）

print(my_str)           # 打印整个字符串：Runoob
print(my_str[0:-1])     # 打印索引 0 到倒数第二个字符（不含最后一个）：Runoo
print(my_str[0])        # 打印第一个字符：R
print(my_str[2:5])      # 打印索引 2、3、4 的字符（不含索引 5）：noo
print(my_str[2:])       # 打印从索引 2 开始到末尾：noob
print(my_str * 2)       # 重复打印两次：RunoobRunoob
print(my_str + "TEST")  # 字符串拼接：RunoobTEST

# 转义字符和原始字符串。
print('Ru\noob')
print(r'Ru\noob')

# 使用正数和负数下标读取字符。
word = 'Python'
print(word[0], word[5])  # P n
print(word[-1], word[-6])  # n P

# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))   # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))          # False
print(bool(42))         # True
print(bool(''))         # False
print(bool('Python'))   # True
print(bool([]))         # False
print(bool([1, 2, 3]))  # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 布尔比较运算
print(5 > 3)   # True
print(2 == 2)  # True
print(7 < 4)   # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x 是非零值，在布尔上下文中为 True")

#!/usr/bin/python3

my_list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 避免使用 list 作为变量名，会覆盖内置类型
tinylist = [123, 'runoob']

print(my_list)             # 打印整个列表：['abcd', 786, 2.23, 'runoob', 70.2]
print(my_list[0])          # 打印第一个元素（索引 0）：abcd
print(my_list[1:3])        # 打印索引 1 和 2 的元素（不含索引 3）：[786, 2.23]
print(my_list[2:])         # 打印从索引 2 开始到末尾的所有元素：[2.23, 'runoob', 70.2]
print(tinylist * 2)        # 重复打印 tinylist 两次：[123, 'runoob', 123, 'runoob']
print(my_list + tinylist)  # 拼接两个列表

# 修改列表并显示结果。
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)  # [9, 2, 13, 14, 15, 6]
a[2:5] = []  # 删除切片中对应的元素
print(a)  # [9, 2, 6]

def reverseWords(input):

    # 通过空格将字符串分隔，把各个单词分隔为列表
    inputWords = input.split(" ")

    # inputWords[-1::-1] 三个参数说明：
    # 第一个参数 -1 表示从最后一个元素开始
    # 第二个参数为空，表示移动到列表开头
    # 第三个参数 -1 表示逆向步进（每次向左移动一个位置）
    inputWords = inputWords[-1::-1]

    # 重新用空格拼接单词
    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

#!/usr/bin/python3

my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)  # 避免使用 tuple 作为变量名
tinytuple = (123, 'runoob')

print(my_tuple)               # 输出完整元组
print(my_tuple[0])            # 输出第一个元素：abcd
print(my_tuple[1:3])          # 输出索引 1 和 2 的元素：(786, 2.23)
print(my_tuple[2:])           # 输出从索引 2 开始的所有元素
print(tinytuple * 2)          # 输出两次 tinytuple
print(my_tuple + tinytuple)   # 连接两个元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

not_a_tuple = (42)  # 这是整数 42，不是元组

# 元组不可修改：最后一行取消注释会按示例抛出 TypeError。
# 修改元组中的元素会抛出 TypeError。
tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])
# tup[0] = 11  # 元组元素不能直接修改


# 【补充】以下保留原有扩展示例。
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
