"""变量赋值、类型判断与数字运算。"""

#!/usr/bin/python3

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1

a, b, c = 1, 2, "runoob"

# 变量定义
x = 10           # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值

# 多变量赋值
a, b, c = 1, 2, "three"

# 查看数据类型
print(type(x))         # <class 'int'>
print(type(y))         # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_active)) # <class 'bool'>

var1 = 1
var2 = 10

# 数字、浮点数、布尔值和复数的类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 使用 print 显示类型判断结果。
a = 111
print(isinstance(a, int))  # True

# B 继承 A；isinstance 会考虑继承关系，type 比较具体类型。
class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # True
print(type(A()) == A)       # True
print(isinstance(B(), A))  # True
print(type(B()) == A)      # False

print(issubclass(bool, int))  # True：bool 是 int 的子类
print(True == 1, False == 0)  # True True
print(True + 1, False + 1)    # 2 1
# 直接写 1 is True 和 0 is False 会产生 SyntaxWarning；这里用变量展示身份比较。
one, zero = 1, 0
print(one is True, zero is False)  # False False

# 删除变量的写法：del var1 或 del var1, var2。
# 执行 del 后，变量名不能再次使用，除非重新赋值。

# 使用 print 显示各表达式的结果。
print(5 + 4)   # 9
print(4.3 - 2) # 2.3
print(3 * 7)   # 21
print(2 / 4)   # 0.5
print(2 // 4)  # 0
print(17 % 3)  # 2
print(2 ** 5)  # 32



# 【补充】以下保留原有扩展示例。
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
