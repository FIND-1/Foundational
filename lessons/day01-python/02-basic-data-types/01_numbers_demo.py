"""第 2 章 · 变量赋值、标准数据类型与数字（Number）。

用途：演示变量赋值、多变量赋值、type() 与 isinstance() 的区别、bool 与 int 的关系、del 和数值运算。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/01_numbers_demo.py
预期结果：先打印 100、1000.0、runoob；子类实例用 isinstance 判断为 True，用 type 判断为 False；
数值运算依次得到 9、2.3、21、0.5、0、2、32；0o17 打印 15。末尾演示两种报错。
"""

# ── 1. 变量赋值 ───────────────────────────────────────────────────────
# 【必会】变量不用声明（没有 let / const），第一次用 = 赋值时才创建。
# 变量本身没有类型，类型属于它指向的对象。print 和 = 的用法见第 1 章 01_syntax_demo.py 开头。
counter = 100          # 整型变量
miles = 1000.0         # 浮点型变量
name = "runoob"        # 字符串

print(counter)
print(miles)
print(name)


# ── 2. 多个变量赋值 ───────────────────────────────────────────────────
# 【必会】a = b = c = 1 先创建整数 1，再让 a、b、c 三个名字都指向它。
a = b = c = 1
print("同一个值赋给三个变量：", a, b, c)

# 【必会】a, b, c = 1, 2, "runoob" 按位置一一对应：a 得 1，b 得 2，c 得 "runoob"。
# 【补充】类似 JS 的解构 const [a, b, c] = [1, 2, "runoob"]，但 Python 不需要方括号。
a, b, c = 1, 2, "runoob"
print("按位置分别赋值：", a, b, c)

# type(值) 返回对象的类型，首次讲解见第 1 章 02_strings_demo.py 的「数字类型」。
x = 10           # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串；name 重新赋值后指向新对象
is_active = True  # 布尔值
a, b, c = 1, 2, "three"
print("四个变量的类型：", type(x), type(y), type(name), type(is_active))

#【补充】Python 允许多变量赋值时，左右两边的元素个数必须相同，否则会报 ValueError。
# e, s = [1, 2, "three"]
# ValueError: too many values to unpack (expected 2)

# ── 3. 标准数据类型 ───────────────────────────────────────────────────
# 6 种：Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）；
# 另有 bool（布尔，是 int/Number 的子类，常单独列出，合起来共 7 项）。
# 此外还有 bytes 等类型，见 05_bytes_demo.py。
#   不可变（4 个）：Number、String、bool、Tuple —— 不能原地修改，只能让变量指向新对象
#   可变（3 个）：  List、Dictionary、Set     —— 可以原地增删改元素
# 列表、元组见 03_list_tuple_demo.py，集合、字典见 04_set_dict_demo.py。


# ── 4. Number：int、float、bool、complex ─────────────────────────────
# Python 3 只有一种整数 int，长度不受固定位数限制，没有 Python 2 的 long。
# 【了解】4 + 3j 是复数，j 表示虚数单位，日常业务与 AI 应用开发中很少用到，认得即可。
a, b, c, d = 20, 5.5, True, 4 + 3j
print("四种数字类型：", type(a), type(b), type(c), type(d))

# 【必会】isinstance(值, 类型) 判断值是否属于该类型，返回 True 或 False（第 1 章 03_io_import_demo.py 进阶段已用过）。
a = 111
print("111 是 int 吗？", isinstance(a, int))

# 【了解】class A: 定义一个类，pass 占位表示类里暂时没有内容（pass 见第 1 章 01_syntax_demo.py「行与缩进」）。
# class B(A): 定义 A 的子类 B，类似 JS 的 class B extends A {}。A() 创建 A 的实例，不需要 new。
class A:
    pass


class B(A):
    pass


parent = A()
child = B()
# 【必会】isinstance 会把子类实例也算作父类类型；type(...) == A 只认具体类型。
print("isinstance(parent, A)：", isinstance(parent, A))  # True
print("type(parent) == A：", type(parent) == A)          # True
print("isinstance(child, A)：", isinstance(child, A))    # True
print("type(child) == A：", type(child) == A)            # False
# 【补充】只接受某个具体类型时，惯用写法是 type(值) is 类型，结果与上面的 == 相同。
print("type(child) is B：", type(child) is B)            # True


# ── 5. bool 是 int 的子类 ─────────────────────────────────────────────
# 【必会】issubclass(子类, 父类) 检查类之间的继承关系。bool 继承自 int，因此得到 True。
print("bool 是 int 的子类吗？", issubclass(bool, int))
print("True 是 int 实例吗？", isinstance(True, int), "具体类型是 int 吗？", type(True) is int)
# == 比较值：True 的值是 1，False 的值是 0，所以还能参与加法。
print("True == 1，False == 0：", True == 1, False == 0)  # True True
print("True + 1，False + 1：", True + 1, False + 1)      # 2 1
# is 检查是否同一个对象（第 1 章 03_io_import_demo.py 的进阶段）。1 和 True 值相等，但不是同一个对象。
# 直接写 1 is True 会触发 SyntaxWarning，所以先把数字放进变量再比较。
one, zero = 1, 0
print("1 is True，0 is False：", one is True, zero is False)  # False False


# ── 6. 创建与删除 ─────────────────────────────────────────────────────
# 指定一个值时，就会创建一个 Number 对象。
var1 = 1
var2 = 10
# 【必会】del 名字 删除变量与对象的绑定；del 名字1, 名字2 一次删除多个。删除后再访问会报错，除非重新赋值。
# 【补充】JS 的 delete 只删除对象属性，不能删除用 let / const 声明的变量。
del var1, var2


# ── 7. 数值运算 ───────────────────────────────────────────────────────
# / 和 // 的区别见第 1 章 02_strings_demo.py。【必会】% 求余数，17 % 3 得到 2。
print("加法 5 + 4：", 5 + 4)       # 9
print("减法 4.3 - 2：", 4.3 - 2)   # 2.3
print("乘法 3 * 7：", 3 * 7)       # 21
print("除法 2 / 4：", 2 / 4)       # 0.5，结果总是 float
print("整除 2 // 4：", 2 // 4)     # 0，向下取整
print("取余 17 % 3：", 17 % 3)     # 2
print("乘方 2 ** 5：", 2 ** 5)     # 32
print("负数整除 -7 // 2：", -7 // 2)  # -4
# 【补充】Python 的 % 结果与除数同号，-7 % 3 得到 2；JS 的 -7 % 3 得到 -1。
print("负数取余 -7 % 3：", -7 % 3)

# 【必会】int 和 float 混合计算时，int 会自动转成 float，所以 1 + 2.0 得到 3.0。
print("混合计算 1 + 2.0：", 1 + 2.0)
# 同一个变量可以先后指向不同类型的对象。
value = 1
value = "one"
print("变量重新指向字符串：", type(value))


# ── 8. 数值类型实例 ───────────────────────────────────────────────────
# 【必会】整数可以写成十进制，也可以用 0o（八进制）、0x（十六进制）、0b（二进制）前缀。打印时都显示十进制。
print("八进制 0o17、十六进制 0x69、二进制 0b101：", 0o17, 0x69, 0b101)  # 15 105 5
print("负数与前缀：", -786, -0x260)                                   # -786 -608
# float 可以省略整数或小数部分，也可以用 e 表示 10 的幂：32.3e+18 是 32.3 乘以 10 的 18 次方。
print("浮点数写法：", -90., 32.3e+18, 70.2E-12)

# 【了解】复数把两个数字绑在一起：不带 j 的是“实部”，j/J 前面的系数是“虚部”（可类比 JS 对象 { real: 3.0, imag: 4.0 }）。
# complex(实部, 虚部) 与直接写 3 + 4j 等价；打印同时有实部和虚部的复数时会自动加括号，显示为 (3+4j)。
# 复数.real 取实部，复数.imag 取虚部（只返回数字，不带 j），即使传入整数，底层也统一存为 float。
z = complex(3, 4)
print("complex(3, 4)：", z, z == 3 + 4j, z.real, z.imag)  # (3+4j) True 3.0 4.0
# 简写形式：3.14j 省略实部（默认 0.0）；45.j 等价于 45.0j；-.6545 + 0J 中 j/J 大小写均可，虚部为 0.0。
print("复数写法：", 3.14j, 45.j, -.6545 + 0J)            # 3.14j 45j (-0.6545+0j)


# ── 【补充】【进阶】观察两种报错 ──────────────────────────────────────
# try / except 的读法见第 1 章 01_syntax_demo.py 的缩进报错示例。
# 访问已被 del 删除的名字会抛 NameError（JS 访问未声明的变量抛 ReferenceError）。
try:
    print(var1)
except NameError as error:
    print("【进阶】删除后再访问：", error)

# 整数字面量不允许前导零：080 在编译阶段就是 SyntaxError，八进制要写成 0o 前缀。
try:
    compile("n = 080", "<number>", "exec")
except SyntaxError as error:
    print("【进阶】前导零报错：", error.msg)
