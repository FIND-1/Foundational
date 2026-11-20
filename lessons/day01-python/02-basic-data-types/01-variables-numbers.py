"""第 2 章 · 变量赋值、类型判断与数字运算。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/02-basic-data-types/01-variables-numbers.py
观察 B 的实例通过 A 的继承判断，精确类型判断为 False，最后的负数整除得到 -4。
"""

counter = 100          # 整型变量
miles = 1000.0         # 浮点型变量
name = "runoob"        # 字符串

print(counter)
print(miles)
print(name)

# 链式赋值从右向左读，三个名字都指向整数 1。
a = b = c = 1

# 一次给多个名字赋不同的值时，按位置一一对应；这里 c 会指向字符串。
a, b, c = 1, 2, "runoob"

# 变量定义
x = 10           # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True  # 布尔值

# 多变量赋值
a, b, c = 1, 2, "three"

# 查看数据类型
print(type(x))         # <class 'int'>
print(type(y))         # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_active))  # <class 'bool'>

var1 = 1
var2 = 10

# 数字、浮点数、布尔值和复数的类型。
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# 使用 print 显示类型判断结果。
a = 111
print(isinstance(a, int))  # True

# 【进阶】class A 定义一个类，A() 创建它的实例。class B(A) 定义 A 的子类，B() 创建子类实例。
class A:
    pass


class B(A):
    pass


parent = A()
child = B()
# 【补充】type(child) 取得实例的具体类型。只接受 A 本身时，用 is A 检查它是否就是类对象 A。
print(type(parent) is A)  # True
print(type(child) is A)   # False
# 也接受子类时，用 isinstance；同一个 child 在这里得到 True。
print(isinstance(parent, A))  # True
print(isinstance(child, A))   # True

# issubclass(子类, 父类) 检查类之间的继承关系。bool 继承自 int，因此输出 True。
print(issubclass(bool, int))
print(True == 1, False == 0)  # True True
print(True + 1, False + 1)    # 2 1
# 直接写 1 is True 和 0 is False 会产生 SyntaxWarning；这里用变量展示身份比较。
one, zero = 1, 0
print(one is True, zero is False)  # False False

# 删除变量的写法：del var1 或 del var1, var2。
# 执行 del 后，变量名不能再次使用，除非重新赋值。

# 使用 print 显示各表达式的结果。
print(5 + 4)   # 9
print(4.3 - 2)  # 2.3
print(3 * 7)   # 21
print(2 / 4)   # 0.5
print(2 // 4)  # 0
print(17 % 3)  # 2
print(2 ** 5)  # 32

# 【补充】变量赋值、数值类型和类型判断。

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
