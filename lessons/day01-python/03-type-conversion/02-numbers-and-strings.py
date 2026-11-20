"""int、float 与 str 的显式类型转换。"""

x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3

x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2

x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'



# 【补充】以下保留原有扩展示例。
"""显式转换：数字、字符串、布尔值和进制。"""

text = "42"
number = int(text)
print("整数：", number, type(number))  # 42 int
print("原值：", text, type(text))      # 42 str
print("浮点数：", float("3.5"))       # 3.5
print("复数：", complex(2, 3))         # (2+3j)
print("截去小数：", int(3.9), int(-3.9))  # 3 -3，向零截断
print("浮点数字符串：", int(float("3.5")))  # 3

print("转字符串：", str(42))
print("对象表示：", repr("hello"))  # 包含引号，便于看出是字符串
print("假值：", bool(0), bool(""), bool(None))  # 均为 False
print("非空字符串：", bool("False"))  # True，不会解析文字含义
print("解析真假文本：", "False".lower() == "true")  # False

print("进制解析：", int("101", 2), int("ff", 16))  # 5 255
print("进制格式：", bin(10), oct(10), hex(10))  # 0b1010 0o12 0xa
