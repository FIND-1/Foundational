"""第 1 章 · 数字与字符串：四种数字类型，字符串的引号、拼接、索引、切片和转义。

用途：直观打印各种数字与字符串操作结果，并与 JS 对照。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/01-basic-syntax/demo_strings.py
预期结果：除法打印 3.5、3 和 -4；s[2:5] 打印 345；原始字符串保留反斜杠，最后一行打印 `demo_strings: all passed`。
"""

# ── 1. 数字类型 ───────────────────────────────────────────────────────
# type(...) 显示一个值的类型，例如 int 表示整数。
# 【补充】JS 只有 number（加 bigint），Python 分为 int、float、bool、complex 四种。
n_int = 1
n_float = 1.23
n_sci = 3E-2                           # 科学计数法：0.03
n_bool = True
n_complex = 1 + 2j                     # 复数：实部 + 虚部j，前端开发中很少用到
print("数字类型：", type(n_int), type(n_float), type(n_bool), type(n_complex))

# 【补充】int 没有大小上限，不像 JS 超过 2**53 就会丢失精度；** 是幂运算
big_int = 2 ** 64
print("2 的 64 次方：", big_int)

# 【补充】两个整数用 / 相除得到 float；// 是向下取整（JS 中 Math.trunc(-3.5) 是 -3，Python -7 // 2 是 -4）
print("除法对比：", 7 / 2, 7 // 2, -7 // 2)

# 【补充】这个例子与 JS 的 Number 一样，二进制浮点数无法精确表示十进制的 0.1。
print("0.1 + 0.2 =", 0.1 + 0.2)


# ── 2. 字符串：引号、拼接与 f-string ──────────────────────────────────
# 单引号和双引号完全等价；三引号用于多行字符串（JS 用反引号 `...`）
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
# count(...) 统计指定文本出现的次数。
print("单引号与双引号：", word, sentence)
print("多行文本：", paragraph)
print("多行换行数：", paragraph.count("\n"))

# 相邻字符串字面量会在编译时自动拼接
auto_joined = "this " "is " "string"
# 【补充】f-string 相当于 JS 的模板字符串 `${}`
name = "runoob"
greeting = f"hi {name}, {1 + 1}"
print("自动拼接：", auto_joined)
print("f-string：", greeting)

# 运算：+ 拼接、* 重复（JS 为 'ab'.repeat(3)）
print("两个字符串相加：", "ab" + "cd")
repeated = "ab" * 3
explicit_join = "a" + str(1)           # Python 不做隐式类型转换，必须显式 str(1)
print("重复与拼接：", repeated, explicit_join)


# ── 3. 字符串：索引与切片 ─────────────────────────────────────────────
# 注意：不要把变量命名为 str，否则会覆盖内置的 str 类型。
s = "123456789"

print("第 1 个字符 s[0]：", s[0])
print("最后 1 个字符 s[-1]：", s[-1])        # 负数索引从右往左数（JS 需要 s.at(-1)）

# 切片 s[start:end:step]：左闭右开，相当于 JS 的 s.slice(start, end)，但多了步长 step
print("s[0:-1] =", s[0:-1])
print("s[2:5]  =", s[2:5])             # 下标 2、3、4
print("s[2:]   =", s[2:])
print("s[:3]   =", s[:3])              # 省略起点，从头取到下标 3 之前
print("s[1:5:2]=", s[1:5:2])           # 下标 1、3，步长为 2
print("s[::-1] =", s[::-1])            # 步长为 -1 实现反转（JS 需 [...s].reverse().join('')）
print("s[2:100]=", s[2:100])           # 切片越界不会报错，只取到末尾

# Python 没有单独的“字符”类型，单个字符就是长度为 1 的 str
first_char = s[0]
print("单字符类型与长度：", type(first_char), len(first_char))


# ── 4. 转义与原始字符串 ───────────────────────────────────────────────
normal_str = "a\nb"                    # \n 是一个换行字符
raw_str = r"a\nb"                      # r 前缀：反斜杠不被转义，类似 JS 的 String.raw`a\nb`
print("普通转义字符串：\n" + normal_str)
print("原始字符串：", raw_str, "长度：", len(raw_str))


# 【补充】【进阶】assert 自动核对终端里观察到的结果，读基础示例时可以停在这里。
assert type(n_int) is int and type(n_float) is float and n_sci == 0.03
assert 7 / 2 == 3.5 and 7 // 2 == 3 and -7 // 2 == -4
assert word == "字符串" and auto_joined == "this is string"
assert repeated == "ababab" and explicit_join == "a1"
assert s[0] == "1" and s[-1] == "9"
assert s[1:5:2] == "24" and s[::-1] == "987654321"
assert type(first_char) is str and len(first_char) == 1
assert len(normal_str) == 3 and raw_str == "a\\nb" and len(raw_str) == 4
assert type(n_bool) is bool and type(n_complex) is complex
assert big_int == 18446744073709551616 and 0.1 + 0.2 != 0.3
assert 'abc' == "abc" and paragraph.count("\n") == 1
assert greeting == "hi runoob, 2" and "ab" + "cd" == "abcd"
assert s[0:-1] == "12345678" and s[2:5] == "345" and s[:3] == "123"
assert s[2:] == "3456789" and s[2:100] == "3456789"

# ── 【进阶】用 try/except 验证报错行为 ────────────────────────────────
# 说明：这里使用后续章节才学到的 try/except 捕获预期错误，证明 Python 会严格报错而不是静默忽略：
try:
    _ = "a" + 1                        # JS 中会得到 "a1"，Python 直接报 TypeError
except TypeError:
    print("【进阶】验证通过：字符串与整数相加抛出 TypeError")
else:
    raise AssertionError("这里应当抛出 TypeError")

try:
    _ = s[100]                         # JS 中返回 undefined，Python 直接报 IndexError
except IndexError:
    print("【进阶】验证通过：索引越界抛出 IndexError")
else:
    raise AssertionError("这里应当抛出 IndexError")

try:
    s[0] = "X"                         # 字符串不可变；JS 非严格模式静默失败，Python 抛 TypeError
except TypeError:
    print("【进阶】验证通过：修改字符串字符抛出 TypeError")
else:
    raise AssertionError("这里应当抛出 TypeError")

print("demo_strings: all passed")
