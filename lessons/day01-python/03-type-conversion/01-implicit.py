"""第 3 章 · 观察整数与浮点数相加的结果。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/03-type-conversion/01-implicit.py
第一组计算得到浮点数 124.23；观察第二组相加后 integer 的类型仍为 int。
"""

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:", type(num_int))
print("num_flo 数据类型为:", type(num_flo))

print("num_new 值为:", num_new)
print("num_new 数据类型为:", type(num_new))

# 字符串与整数直接相加会抛 TypeError；取消注释可观察。
# num_int = 123
# num_str = "456"
#
# print("num_int 数据类型为:", type(num_int))
# print("num_str 数据类型为:", type(num_str))
#
# print(num_int + num_str)

# 【补充】隐式转换：兼容的数字类型参与运算时，Python 会处理结果类型。

integer = 123
decimal = 1.25
result = integer + decimal
print("整数：", integer, type(integer))
print("浮点数：", decimal, type(decimal))
print("相加结果：", result, type(result))  # 124.25，float
print("原变量仍是整数：", type(integer))

# 不同于兼容的数字，字符串和整数不能直接相加，否则会抛出 TypeError。
# 错误示例：print("123" + 1)

print("先转换再计算：", int("123") + 1)  # 124
print("先转换再拼接：", "123" + str(1))  # 1231
