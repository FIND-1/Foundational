"""隐式转换：兼容的数字类型参与运算时，Python 会处理结果类型。"""

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
