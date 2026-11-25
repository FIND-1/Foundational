"""第 3 章 · 隐式类型转换与字符串拼接限制。

用途：演示兼容数字类型运算时的隐式类型转换、原变量类型保持不变，以及字符串与数字不能直接相加。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/03-type-conversion/01_implicit_demo.py
预期结果：num_new 打印 124.23 且类型为 float；相加后 integer 仍为 int；
先转换再计算得到 124，先转换再拼接得到 1231。末尾演示整数与字符串直接相加的报错。
"""

# ── 1. 整数与浮点数相加的隐式转换 ─────────────────────────────────────
# 格式：int + float -> float（自动把整数提升为浮点数参与计算，结果是新对象）
# 注意：原变量 num_int 本身不会改变，仍然是 int（type 见第 1 章 02_strings_demo.py）
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:", type(num_int))
print("num_flo 数据类型为:", type(num_flo))

print("num_new 值为:", num_new)
print("num_new 数据类型为:", type(num_new))


# ── 2. 原变量类型不变 ─────────────────────────────────────────────────
# 注意：隐式转换只影响运算产生的新值；bool 与 int 混合运算也会自动按 1 / 0 提升（见第 2 章 01_numbers_demo.py）
integer = 123
decimal = 1.25
result = integer + decimal
print("整数：", integer, type(integer))
print("浮点数：", decimal, type(decimal))
print("相加结果：", result, type(result))  # 124.25 <class 'float'>
print("原变量仍是整数：", type(integer))
print("bool 与 int 相加：", True + 2, type(True + 2))  # 3 <class 'int'>

# 拓展：二进制浮点数无法精确表示所有十进制小数，极大整数转 float 也会丢失精度（精确小数用 Decimal，见第 1 章）
big_int = 10 ** 17
print("隐式转 float 仍有浮点精度问题：", 0 + 0.1 + 0.2)
print("超大整数隐式转 float 丢失低位精度：", big_int + 1.0 == big_int)


# ── 3. 字符串与数字不能直接相加 ───────────────────────────────────────
# 注意：Python 是强类型语言，不会像 JS 那样把 "123" + 1 隐式变成 "1231"，必须先显式转换
# 场景：做算术先用 int() 转数字，做文本拼接先用 str() 转字符串（或用 f-string）
print("先转换再计算：", int("123") + 1)    # 124
print("先转换再拼接：", "123" + str(1))    # 1231


# ── 拓展：观察整数与字符串直接相加的报错 ──────────────────────────────
# 注意：不同类型之间无法隐式转换时会抛 TypeError（try / except 见第 1 章 01_syntax_demo.py 末尾）
num_str = "456"
print("num_int、num_str 类型：", type(num_int), type(num_str))

try:
    _ = num_int + num_str
except TypeError as error:
    print("拓展 - 整数与字符串直接相加：", error)
