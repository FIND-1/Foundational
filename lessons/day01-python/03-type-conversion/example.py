"""显式转换后进行相加。"""

num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))



# 【补充】以下保留原有扩展示例。
"""类型转换：观察值与类型；原变量不会自动改变。"""

number = 2
result = number + 0.5  # 数字运算中的隐式转换
print("隐式转换：", result, type(result))

text = "123"
print("显式转换：", int(text) + 1, type(text))  # 124，text 仍是 str
print("小数转整数：", int(-3.8))  # -3，向 0 截断
print("小数字符串：", int(float("3.5")))  # 3
print("二进制字符串：", int("101", 2))  # 5
print("数字转字符串：", "年龄：" + str(18))
print("浮点与复数：", float("2.5"), complex(2))

print("真假转换：", bool(0), bool(""), bool("False"))  # False False True
print("容器转换：", list("ab"), tuple([1, 2]), set([1, 1, 2]))
print("键值对转字典：", dict([("name", "Rain")]))
print("字符和码点：", chr(65), ord("A"))
print("进制表示：", bin(10), oct(10), hex(10))
print("显示与表示：", str("hi"), repr("hi"))

try:
    int("3.5")
except ValueError:
    print("无法把 '3.5' 直接转成整数")
