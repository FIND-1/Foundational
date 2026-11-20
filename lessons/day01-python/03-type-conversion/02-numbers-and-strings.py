"""第 3 章 · 数字、字符串和进制的显式转换。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/03-type-conversion/02-numbers-and-strings.py
观察 42 转为整数后的类型、负数 -3.9 转为整数得到 -3，以及十六进制 ff 解析得到 255。
"""

# 【必会】int(文本) 解析十进制整数，给浮点数时则向零截断。前三次赋值依次得到 1、2、3。
x = int(1)   # x 为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3

# float(x) 接受数值或数字文本，结果总是浮点数；"4.2" 会变成数值 4.2。
x = float(1)     # x 为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2")  # w 输出结果为 4.2

x = str("s1")  # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

# 【补充】显式转换：数字、字符串、布尔值和进制。

text = "42"
number = int(text)
print("整数：", number, type(number))  # 42 int
print("原值：", text, type(text))      # 42 str
print("浮点数：", float("3.5"))       # 3.5
# complex(实部, 虚部) 用两个数构造复数，这里得到 (2+3j)。
print("复数：", complex(2, 3))
print("截去小数：", int(3.9), int(-3.9))  # 3 -3，向零截断
print("浮点数字符串：", int(float("3.5")))  # 3

print("转字符串：", str(42))
# repr(值) 返回便于区分类型的表示文本；这里打印的 hello 两旁能看到引号。
print("对象表示：", repr("hello"))
print("假值：", bool(0), bool(""), bool(None))  # 均为 False
print("非空字符串：", bool("False"))  # True，不会解析文字含义
# 文本.lower() 返回小写副本。这里比较 "false" 与 "true"，得到 False。
print("解析真假文本：", "False".lower() == "true")

# int(文本, 进制) 按第二个参数指定的进制读取，"101" 按二进制读作 5。
print("进制解析：", int("101", 2), int("ff", 16))  # 5 255
# bin、oct、hex 分别把整数格式化为带前缀的二、八、十六进制字符串。
print("进制格式：", bin(10), oct(10), hex(10))  # 0b1010 0o12 0xa
