"""第 1 章 · 数字与字符串：四种数字类型，字符串的引号、拼接、索引、切片和转义。

运行：python .\\lessons\\day01-python\\01-basic-syntax\\demo_strings.py
"""

# ── 数字类型 ──────────────────────────────────────────────────────────
# JS 只有 number（再加 bigint），Python 分为 int、float、bool、complex 四种。
assert type(1) is int
assert type(1.23) is float and 3E-2 == 0.03
assert type(True) is bool
assert type(1 + 2j) is complex             # 复数：实部 + 虚部j，前端开发中很少用到

# int 没有大小上限，不像 JS 超过 2**53 就会丢失精度
assert 2 ** 64 == 18446744073709551616     # ** 是幂运算，与 JS 相同

# 除法：/ 的结果总是 float；// 是向下取整（不是向零取整）
assert 7 / 2 == 3.5
assert 7 // 2 == 3
assert -7 // 2 == -4                       # JS 中 Math.trunc(-3.5) 是 -3，这里是 -4

# 浮点数误差和 JS 完全一样（两者都使用 IEEE 754）
assert 0.1 + 0.2 != 0.3


# ── 字符串：引号 ──────────────────────────────────────────────────────
# 单引号和双引号完全等价；三引号用于多行字符串（JS 用反引号 `...`）
assert 'abc' == "abc"
paragraph = """这是一个段落，
可以由多行组成"""
assert paragraph.count("\n") == 1

# 相邻的字符串字面量会在编译时自动拼接，常用于在括号内拆分长字符串
assert "this " "is " "string" == "this is string"

# f-string 相当于 JS 的模板字符串 `${}`（原教程未讲，但它是最常用的格式化方式）
name = "runoob"
assert f"hi {name}, {1 + 1}" == "hi runoob, 2"


# ── 字符串：运算 ──────────────────────────────────────────────────────
assert "ab" + "cd" == "abcd"
assert "ab" * 3 == "ababab"                # JS：'ab'.repeat(3)

# Python 不会做隐式类型转换：JS 中 "a" + 1 得到 "a1"，Python 会直接报错
try:
    "a" + 1
except TypeError:
    pass
else:
    raise AssertionError("这里应当抛出 TypeError")
assert "a" + str(1) == "a1"                # 需要显式转换（第 3 章会详细讲）


# ── 字符串：索引与切片 ────────────────────────────────────────────────
# 不要把变量命名为 str：那样会覆盖内置的 str 类型（原教程就这样写了）
s = "123456789"

assert s[0] == "1"
assert s[-1] == "9"                        # 负数索引从右往左数；JS 中 s[-1] 是 undefined，要用 s.at(-1)

# 索引越界会抛 IndexError（JS 返回 undefined）
try:
    s[100]
except IndexError:
    pass
else:
    raise AssertionError("这里应当抛出 IndexError")

# 切片 s[start:end:step]：左闭右开，相当于 JS 的 s.slice(start, end)，但多了步长
assert s[0:-1] == "12345678"
assert s[2:5] == "345"                     # 取下标 2、3、4
assert s[2:] == "3456789"
assert s[:3] == "123"
assert s[1:5:2] == "24"                    # 取下标 1、3
assert s[::-1] == "987654321"              # 反转字符串，JS 需要 [...s].reverse().join('')
assert s[2:100] == "3456789"               # 切片越界不会报错，只取到末尾

# 没有单独的“字符”类型：一个字符就是长度为 1 的 str
assert type(s[0]) is str and len(s[0]) == 1

# 字符串不可修改（和 JS 相同），但 Python 一定会报错，JS 非严格模式下会静默忽略
try:
    s[0] = "X"
except TypeError:
    pass
else:
    raise AssertionError("这里应当抛出 TypeError")


# ── 转义与原始字符串 ──────────────────────────────────────────────────
assert len("a\nb") == 3                    # \n 是一个换行字符
assert r"a\nb" == "a\\nb"                  # r 前缀：反斜杠不转义，类似 JS 的 String.raw`a\nb`
assert len(r"a\nb") == 4                   # 常用于 Windows 路径和正则表达式

print("demo_strings: all passed")
