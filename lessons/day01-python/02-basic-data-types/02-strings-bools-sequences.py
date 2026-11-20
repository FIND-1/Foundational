"""第 2 章 · 字符串、布尔值、列表和元组。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/02-basic-data-types/02-strings-bools-sequences.py
观察空列表的真假值、列表切片赋值前后的元素，以及单词倒序后的 runoob like I。
"""

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

# bool(x) 返回 x 的真假值。数值零、空串和空列表为假；其余几个输入为真。
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

# 【补充】需要得到布尔值供后续使用时可以调 bool(x)；在 if 中直接写 x 就会做同样的真假判断。
x = 10
if x:
    print("x 是非零值，在布尔上下文中为 True")

my_list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 避免使用 list 作为变量名，会覆盖内置类型
tinylist = [123, 'runoob']

print(my_list)             # 打印整个列表：['abcd', 786, 2.23, 'runoob', 70.2]
print(my_list[0])          # 打印第一个元素（索引 0）：abcd
print(my_list[1:3])        # 打印索引 1 和 2 的元素（不含索引 3）：[786, 2.23]
print(my_list[2:])         # 打印从索引 2 开始到末尾的所有元素：[2.23, 'runoob', 70.2]
print(tinylist * 2)        # 重复打印 tinylist 两次：[123, 'runoob', 123, 'runoob']
print(my_list + tinylist)  # 拼接两个列表

# 【必会】给 a[0] 赋值会替换首项。给 a[2:5] 赋值会用右侧列表替换下标 2 到 4 的元素。
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)  # [9, 2, 13, 14, 15, 6]
a[2:5] = []  # 删除切片中对应的元素
print(a)  # [9, 2, 6]


# 【进阶】这个函数把单词按倒序排列，保留每个单词内的字母顺序。def 和 return 见第 1 章 demo_io_import.py 的「代码组」。
def reverseWords(input):
    # split(" ") 在每个普通空格处分割；连续两个空格会在列表中留下一个空字符串。
    inputWords = input.split(" ")
    # 从最后一项开始，以 -1 为步长一直取到开头。
    inputWords = inputWords[-1::-1]
    # " ".join(...) 在相邻两项之间放一个空格，返回拼好的字符串。
    return " ".join(inputWords)


# 【补充】函数名用 snake_case，参数名 text 明确了输入类型，也保留了内置 input 的含义。
def reverse_words(text):
    words = text.split(" ")
    # 负步长时默认从末项开始，所以 [::-1] 和上例取到相同的逆序副本。
    return " ".join(words[::-1])


# 直接运行文件时 __name__ 为 "__main__"，下面会打印 runoob like I。
if __name__ == "__main__":
    sentence = "I like runoob"
    print(reverse_words(sentence))

my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)  # 避免使用 tuple 作为变量名
tinytuple = (123, 'runoob')

print(my_tuple)               # 输出完整元组
print(my_tuple[0])            # 输出第一个元素：abcd
print(my_tuple[1:3])          # 输出索引 1 和 2 的元素：(786, 2.23)
print(my_tuple[2:])           # 输出从索引 2 开始的所有元素
print(tinytuple * 2)          # 输出两次 tinytuple
print(my_tuple + tinytuple)   # 连接两个元组

tup1 = ()    # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

not_a_tuple = (42)  # 这是整数 42，不是元组

# 运行到下面的注释行时，可取消注释观察给元组元素赋值的报错。
tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])
# tup[0] = 11  # 元组元素不能直接修改

# 【补充】字符串、列表和元组的基本操作。

text = "Python"
print("字符串索引和切片：", text[0], text[-1], text[1:5:2])  # P n yh
print("拼接与重复：", text + "3", text * 2)
# text.replace("P", "J") 返回换好字母的新字符串，原来的 text 仍指向 "Python"。
print("字符串是不可变的：", text.replace("P", "J"), text)

items = ["苹果", "香蕉", "梨", "橙子"]
print("列表切片：", items[1:3])  # 香蕉、梨
items[0] = "桃子"  # 列表可修改
# items.append("葡萄") 在原列表末尾添加一个元素，下行能看到新增的水果。
items.append("葡萄")
print("修改后：", items)
print("列表拼接和重复：", [1, 2] + [3], [1, 2] * 2)

point = (3, 4)
print("元组：", point[0], point[:1], point + (5,))
print("空元组和单元素元组：", (), (3,))
print("有无逗号的区别：", type((3,)), type((3)))
