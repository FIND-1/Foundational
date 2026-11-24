"""第 2 章 · 变量赋值、标准数据类型与数字（Number）。

用途：演示变量赋值、多变量赋值、type() 与 isinstance() 的区别、bool 与 int 的关系、del 和数值运算。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/01_numbers_demo.py
预期结果：先打印 100、1000.0、runoob；子类实例用 isinstance 判断为 True，用 type 判断为 False；
数值运算依次得到 9、2.3、21、0.5、0、2、32；0o17 打印 15。末尾演示两种报错。
"""

# ── 1. 变量赋值 ───────────────────────────────────────────────────────
# 格式：变量名 = 值（首次赋值即创建，无需 let / const）
# 注意：变量本身没有类型，类型属于它指向的对象（print 与 = 见第 1 章 01_syntax_demo.py）
counter = 100          # 整型变量
miles = 1000.0         # 浮点型变量
name = "runoob"        # 字符串

print(counter)
print(miles)
print(name)


# ── 2. 多个变量赋值 ───────────────────────────────────────────────────
# 格式：变量1 = 变量2 = 变量3 = 值 -> 三个名字指向同一个对象
a = b = c = 1
print("同一个值赋给三个变量：", a, b, c)

# 格式：变量1, 变量2, 变量3 = 值1, 值2, 值3 -> 按位置一一对应赋值
# 注意：类似 JS 解构 const [a, b, c] = [1, 2, "runoob"]，但不需方括号；左右数量不同会报 ValueError
a, b, c = 1, 2, "runoob"
print("按位置分别赋值：", a, b, c)

# 格式：type(值) -> 对象的精确类型（首次讲解见第 1 章 02_strings_demo.py「数字类型」）
x = 10           # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串；重新赋值后指向新对象
is_active = True  # 布尔值
a, b, c = 1, 2, "three"
print("四个变量的类型：", type(x), type(y), type(name), type(is_active))

# 拓展：左右数量不一致会抛 ValueError，例如：
# e, s = [1, 2, "three"]  -> ValueError: too many values to unpack (expected 2)

# ── 3. 标准数据类型 ───────────────────────────────────────────────────
# 6 种标准类型 + bool（int 的子类，常单列）：
#   不可变：Number、String、bool、Tuple —— 不能原地修改，只能重新赋值
#   可变：  List、Dictionary、Set     —— 可以原地增删改元素
# 其余类型见后续文件：str/bool(02)、list/tuple(03)、set/dict(04)、bytes(05)。


# ── 4. Number：int、float、bool、complex ─────────────────────────────
# 注意：Python 3 只有一种整数 int（长度不限，没有 Python 2 的 long）
# 拓展：4 + 3j 是复数（j 为虚数单位），日常业务与 AI 应用开发极少用到，认得即可
a, b, c, d = 20, 5.5, True, 4 + 3j
print("四种数字类型：", type(a), type(b), type(c), type(d))

# 格式：isinstance(值, 类型) -> bool（判断值是否属于该类型或其子类）
a = 111
print("111 是 int 吗？", isinstance(a, int))

# 拓展：class A: 定义类；class B(A): 定义子类（类似 JS 的 class B extends A {}）；A() 创建实例无需 new
class A:
    pass


class B(A):
    pass


parent = A()
child = B()
# 场景：允许子类通过用 isinstance(值, 父类)；只认精确类型用 type(值) is 类型
# 注意：对子类实例 child，isinstance(child, A) 为 True，而 type(child) == A 为 False
print("isinstance(parent, A)：", isinstance(parent, A))  # True
print("type(parent) == A：", type(parent) == A)          # True
print("isinstance(child, A)：", isinstance(child, A))    # True
print("type(child) == A：", type(child) == A)            # False
print("type(child) is B：", type(child) is B)            # True


# ── 5. bool 是 int 的子类 ─────────────────────────────────────────────
# 格式：issubclass(子类, 父类) -> bool（检查类的继承关系；bool 继承自 int）
print("bool 是 int 的子类吗？", issubclass(bool, int))
print("True 是 int 实例吗？", isinstance(True, int), "具体类型是 int 吗？", type(True) is int)
# 注意：== 比较值，True 等价于 1、False 等价于 0，因此可参与加法
print("True == 1，False == 0：", True == 1, False == 0)  # True True
print("True + 1，False + 1：", True + 1, False + 1)      # 2 1
# 注意：is 比较是否同一对象（1 和 True 值相等但不是同一对象）；直接写 1 is True 会触发 SyntaxWarning
one, zero = 1, 0
print("1 is True，0 is False：", one is True, zero is False)  # False False


# ── 6. 创建与删除 ─────────────────────────────────────────────────────
# 格式：del 变量1, 变量2 -> 删除变量名与对象的绑定
# 注意：删除后再访问会报 NameError；JS 的 delete 只删对象属性，不能删 let / const 变量
var1 = 1
var2 = 10
del var1, var2


# ── 7. 数值运算 ───────────────────────────────────────────────────────
# 格式：+ - * / // % **（/ 和 // 见第 1 章 02_strings_demo.py；% 求余数）
# 注意：Python 的 % 结果与除数同号，-7 % 3 得到 2（JS 中 -7 % 3 得到 -1）
print("加法 5 + 4：", 5 + 4)          # 9
print("减法 4.3 - 2：", 4.3 - 2)      # 2.3
print("乘法 3 * 7：", 3 * 7)          # 21
print("除法 2 / 4：", 2 / 4)          # 0.5，结果总是 float
print("整除 2 // 4：", 2 // 4)        # 0，向下取整
print("取余 17 % 3：", 17 % 3)        # 2
print("乘方 2 ** 5：", 2 ** 5)        # 32
print("负数整除 -7 // 2：", -7 // 2)  # -4
print("负数取余 -7 % 3：", -7 % 3)    # 2

# 注意：int 与 float 混合计算时自动转为 float（1 + 2.0 -> 3.0）；同一变量可随时指向新类型
print("混合计算 1 + 2.0：", 1 + 2.0)
value = 1
value = "one"
print("变量重新指向字符串：", type(value))


# ── 8. 数值类型实例 ───────────────────────────────────────────────────
# 格式：整数支持 0o(八进制)、0x(十六进制)、0b(二进制) 前缀，打印时统一显示十进制
print("八进制 0o17、十六进制 0x69、二进制 0b101：", 0o17, 0x69, 0b101)  # 15 105 5
print("负数与前缀：", -786, -0x260)                                   # -786 -608
# 格式：浮点数可省略整数或小数位，也可用 e/E 表示 10 的幂（32.3e+18 即 32.3 * 10**18）
print("浮点数写法：", -90., 32.3e+18, 70.2E-12)
# 拓展：复数由实部和虚部组成（可类比 JS 对象 { real: 3.0, imag: 4.0 }），日常业务开发极少用到
# 格式：complex(实部, 虚部) 或 实部 + 虚部j -> complex；复数.real / 复数.imag -> 均为 float（不含 j）
z = complex(3, 4)
print("complex(3, 4)：", z, z == 3 + 4j, z.real, z.imag)  # (3+4j) True 3.0 4.0
# 拓展：3.14j 省略实部（默认 0.0）；45.j 等价 45.0j；-.6545 + 0J 中 j/J 均可，虚部为 0.0
print("复数写法：", 3.14j, 45.j, -.6545 + 0J)            # 3.14j 45j (-0.6545+0j)


# ── 拓展：观察两种报错 ────────────────────────────────────────────────
# 注意：访问被 del 删除的变量抛 NameError（JS 抛 ReferenceError）；try / except 见第 1 章 01_syntax_demo.py
try:
    print(var1)
except NameError as error:
    print("【进阶】删除后再访问：", error)

# 注意：十进制整数不允许前导零（如 080 报 SyntaxError），八进制需写 0o 前缀
try:
    compile("n = 080", "<number>", "exec")
except SyntaxError as error:
    print("【进阶】前导零报错：", error.msg)
