"""第 2 章 · 字符串（String）与布尔类型（bool）。

用途：复习字符串的截取、拼接、转义，演示 bool() 的真假规则、逻辑运算、比较运算和条件判断。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/02_str_bool_demo.py
预期结果：my_str[2:5] 打印 noo；word[-6] 打印 P；bool([]) 为 False、bool("False") 为 True；
两句 This will ... print 都会出现。末尾演示修改字符串字符的报错。
"""

# ── 1. 字符串：截取、拼接与重复 ───────────────────────────────────────
# 索引、切片、+、* 的首次讲解见第 1 章 02_strings_demo.py「索引与切片」。
# 变量写成 my_str 而不是 str，避免覆盖内置的 str 类型。
my_str = 'Runoob'

print(my_str)           # 整个字符串：Runoob
print(my_str[0:-1])     # 下标 0 到倒数第二个字符：Runoo
print(my_str[0])        # 第一个字符：R
print(my_str[2:5])      # 下标 2、3、4：noo
print(my_str[2:])       # 从下标 2 到末尾：noob
print(my_str * 2)       # 重复两次：RunoobRunoob
print(my_str + "TEST")  # 拼接：RunoobTEST


# ── 2. 转义与原始字符串 ───────────────────────────────────────────────
# \n 是换行；加 r 前缀后反斜杠按原样保留（第 1 章 02_strings_demo.py「转义与原始字符串」）。
print('Ru\noob')
print(r'Ru\noob')
# 反斜杠续行和三引号多行字符串见第 1 章 01_syntax_demo.py「多行语句」与 02_strings_demo.py。


# ── 3. 一个字符就是长度为 1 的字符串 ──────────────────────────────────
# Python 没有单独的字符类型（JS 也没有）。从左数下标从 0 开始，从右数从 -1 开始。
word = 'Python'
print(word[0], word[5])    # P n
print(word[-1], word[-6])  # n P
print("单个字符的类型：", type(word[0]))

# 【补充】【必会】字符串不可变。text.replace(旧, 新) 返回替换后的新字符串，原来的 word 不变。
# 【补充】JS 的 "Python".replace("P", "J") 用字符串匹配时只替换第一处；Python 默认替换全部。
replaced = word.replace("P", "J")
print("replace 返回新字符串：", replaced, "原字符串：", word)  # Jython Python


# ── 4. 布尔类型的值和类型 ─────────────────────────────────────────────
# True 和 False 都是关键字，首字母大写。
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# int(值) 把值转成整数（第 1 章 functions.md 的 int()）。True 转成 1，False 转成 0。
print(int(True))   # 1
print(int(False))  # 0
# 【补充】【必会】float(值) 转成浮点数，str(值) 转成文本。True 分别得到 1.0 和 "True"，不是 "1"。
print("float(True)、str(True)：", float(True), str(True))


# ── 5. bool()：其他类型转成布尔值 ─────────────────────────────────────
# 【必会】bool(值) 返回值的真假。None、False、数值零、空字符串、空列表等为 False，其余为 True。
# [] 是空列表，[1, 2, 3] 是有三个元素的列表（列表见 03_list_tuple_demo.py）。
print(bool(0))          # False
print(bool(42))         # True
print(bool(''))         # False
print(bool('Python'))   # True
print(bool([]))         # False
print(bool([1, 2, 3]))  # True
# 【补充】None 和 0.0 也为假。非空字符串一律为真，所以 "False" 和 "0" 都为真。
print("None、0.0、\"False\"、\"0\"：", bool(None), bool(0.0), bool("False"), bool("0"))
# 【补充】JS 中 [] 和 {} 都是真值，Python 中空列表、空元组、空字典、空集合都是假值。


# ── 6. 逻辑运算与比较运算 ─────────────────────────────────────────────
# 【必会】and：两边都为真才为真；or：有一边为真就为真；not：取反。对应 JS 的 &&、||、!。
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 【必会】> 大于，< 小于，== 等于，比较结果是布尔值。Python 没有 ===，== 不会像 JS 那样先做隐式类型转换。
print(5 > 3)   # True
print(2 == 2)  # True
print(7 < 4)   # False
# 【补充】布尔值与数字比较时按 1 和 0 计算；与字符串用 == 比较时直接得到 False。
print("True > 0，True == \"1\"：", True > 0, True == "1")  # True False


# ── 7. 布尔值在控制流中的应用 ─────────────────────────────────────────
# if 条件为真时执行缩进块（第 1 章 01_syntax_demo.py「行与缩进」）。下面两个条件恒为真。
if True:
    print("This will always print")

if not False:
    print("This will also always print")

# 【必会】if 后面可以直接写任意值，Python 会按 bool() 的规则判断真假。10 不是零，所以为真。
x = 10
if x:
    print("x 是非零值，在布尔上下文中为 True")

# 【补充】需要保存或返回布尔结果时调用 bool(x)；只在 if 中判断时直接写 if x:。
# 【补充】表达真假时用 True / False，不要用 1 / 0 代替，虽然 bool 是 int 的子类。
x_is_truthy = bool(x)
print("bool(x) 保存的结果：", x_is_truthy)


# ── 【补充】【进阶】观察字符串不可变的报错 ────────────────────────────
# 给字符串的某个下标赋值会抛 TypeError；try / except 的读法见第 1 章 01_syntax_demo.py 末尾。
try:
    word[0] = 'm'
except TypeError as error:
    print("【进阶】修改字符串字符：", error)
