"""第 2 章 · 字符串（String）与布尔类型（bool）。

用途：复习字符串的截取、拼接、转义，演示 bool() 的真假规则、逻辑运算、比较运算和条件判断。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/02_str_bool_demo.py
预期结果：my_str[2:5] 打印 noo；word[-6] 打印 P；bool([]) 为 False、bool("False") 为 True；
两句 This will ... print 都会出现。末尾演示修改字符串字符的报错。
"""

# ── 1. 字符串：截取、拼接与重复 ───────────────────────────────────────
# 格式：变量[头下标:尾下标] 截取；+ 拼接；* 重复（首次讲解见第 1 章 02_strings_demo.py）
# 注意：不要用 str 作变量名，避免覆盖内置的 str 类型
my_str = 'Runoob'

print(my_str)           # 整个字符串：Runoob
print(my_str[0:-1])     # 下标 0 到倒数第二个字符：Runoo
print(my_str[0])        # 第一个字符：R
print(my_str[2:5])      # 下标 2、3、4：noo
print(my_str[2:])       # 从下标 2 到末尾：noob
print(my_str * 2)       # 重复两次：RunoobRunoob
print(my_str + "TEST")  # 拼接：RunoobTEST


# ── 2. 转义与原始字符串 ───────────────────────────────────────────────
# 格式：r"..." -> 原始字符串，保留反斜杠（见第 1 章 02_strings_demo.py「转义与原始字符串」）
print('Ru\noob')
print(r'Ru\noob')


# ── 3. 一个字符就是长度为 1 的字符串 ──────────────────────────────────
# 注意：Python 与 JS 都没有单独的字符类型；从左数下标从 0 开始，从右数从 -1 开始
word = 'Python'
print(word[0], word[5])    # P n
print(word[-1], word[-6])  # n P
print("单个字符的类型：", type(word[0]))

# 格式：字符串.replace(旧内容, 新内容) -> 替换后的新字符串
# 注意：字符串不可变，原字符串 word 不受影响；Python 默认替换全部，JS 默认只替第一处
replaced = word.replace("P", "J")
print("replace 返回新字符串：", replaced, "原字符串：", word)  # Jython Python


# ── 4. 布尔类型的值和类型 ─────────────────────────────────────────────
# 注意：True 和 False 是关键字，首字母必须大写
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 格式：int(值) / float(值) / str(值) -> 分别转为整数、浮点数、字符串
# 注意：True 转整数为 1、转浮点为 1.0，但 str(True) 是 "True"（不是 "1"）
print(int(True))   # 1
print(int(False))  # 0
print("float(True)、str(True)：", float(True), str(True))


# ── 5. bool()：其他类型转成布尔值 ─────────────────────────────────────
# 格式：bool(值) -> True 或 False
# 注意：None、False、数值零、空串、空列表/元组/字典/集合为 False，其余为 True
# 注意：与 JS 不同，JS 中 [] 和 {} 为真，Python 中空容器为假；非空串 "False"、"0" 在两边都为真
print(bool(0))          # False
print(bool(42))         # True
print(bool(''))         # False
print(bool('Python'))   # True
print(bool([]))         # False
print(bool([1, 2, 3]))  # True
print("None、0.0、\"False\"、\"0\"：", bool(None), bool(0.0), bool("False"), bool("0"))


# ── 6. 逻辑运算与比较运算 ─────────────────────────────────────────────
# 格式：and（全真为真）、or（任一为真）、not（取反） -> 对应 JS 的 &&、||、!
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 格式：>、<、== -> bool
# 注意：Python 没有 ===，== 不会像 JS 那样隐式把字符串转成数字（True == "1" 为 False）
print(5 > 3)   # True
print(2 == 2)  # True
print(7 < 4)   # False
# 拓展：布尔值与数字比较时按 1 和 0 计算（True > 0 为 True）
print("True > 0，True == \"1\"：", True > 0, True == "1")  # True False


# ── 7. 布尔值在控制流中的应用 ─────────────────────────────────────────
# 格式：if 条件: 缩进块（首次讲解见第 1 章 01_syntax_demo.py「行与缩进」）
if True:
    print("This will always print")

if not False:
    print("This will also always print")

# 注意：if 后可直接放任意值，Python 自动按 bool() 规则判真假（10 非零 -> True）
x = 10
if x:
    print("x 是非零值，在布尔上下文中为 True")

# 场景：只在 if 里判断直接写 if x:；需要保存/返回真正的布尔值时才调 bool(x)（类似 JS 的 Boolean(x) / !!x）
# 注意：表达真假用 True / False，不要用 1 / 0 代替
x_is_truthy = bool(x)
print("bool(x) 保存的结果：", x_is_truthy)


# ── 拓展：观察字符串不可变的报错 ──────────────────────────────────────
# 注意：给字符串下标赋值会抛 TypeError（try / except 见第 1 章 01_syntax_demo.py 末尾）
try:
    word[0] = 'm'
except TypeError as error:
    print("【进阶】修改字符串字符：", error)
