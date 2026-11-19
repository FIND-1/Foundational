"""变量赋值、数值类型和类型判断。"""

count, price, active, number = 10, 3.5, True, 2 + 3j
print("值：", count, price, active, number)
print("类型：", type(count), type(price), type(active), type(number))
first = second = 1
left, right = 2, 3
print("多变量赋值：", first, second, left, right)

print("数值运算：", 7 + 2, 7 - 2, 7 * 2, 7 / 2)
print("整除、求余、幂：", 7 // 2, 7 % 2, 2 ** 3)
print("负数向下取整：", -7 // 2)  # -4
print("布尔值是 int 子类：", isinstance(True, int))  # True
print("具体类型是 int：", type(True) is int)  # False

temporary = 10
del temporary  # 删除这个名字的绑定；再次访问前需要重新赋值
