"""第 1 章 · 数字与字符串：四种数字类型，字符串的引号、拼接、索引、切片和转义。

用途：直观打印各种数字与字符串操作结果，并与 JS 对照。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/01-basic-syntax/02_strings_demo.py
预期结果：除法打印 3.5、3 和 -4；s[2:5] 打印 345；原始字符串保留反斜杠。末尾演示三种字符串操作的报错。
"""

# ── 1. 数字类型 ───────────────────────────────────────────────────────
# 格式：type(值) -> 对象的类型（如 <class 'int'>）
# 注意：JS 只有 number（加 bigint）；Python 分为 int、float、bool、complex 四种
n_int = 1
n_float = 1.23
n_sci = 3E-2                           # 科学计数法：0.03
n_bool = True
n_complex = 1 + 2j                     # 拓展：复数（实部 + 虚部j），日常业务开发很少用到
print("数字类型：", type(n_int), type(n_float), type(n_bool), type(n_complex))

# 格式：底数 ** 指数 -> 乘方
# 注意：Python 的 int 长度不限；JS Number 超出安全整数范围会丢精度
big_int = 2 ** 64
print("2 的 64 次方：", big_int)

# 格式：/ 普通除法（总得 float）；// 整除（向下取整）
# 注意：负数向下取整往更小的数靠，所以 -7 // 2 得到 -4（不是 -3）
print("除法对比：", 7 / 2, 7 // 2, -7 // 2)

# 注意：与 JS 一样，二进制浮点数无法精确表示十进制的 0.1
print("0.1 + 0.2 =", 0.1 + 0.2)

# 拓展：需要精确小数运算（如金额）时，从 decimal 导入 Decimal 并传入字符串
# 注意：若传入浮点数会带入二进制误差，必须传字符串如 Decimal("0.1")
from decimal import Decimal

print('Decimal("0.1") + Decimal("0.2") =', Decimal("0.1") + Decimal("0.2"))


# ── 2. 字符串：引号、拼接与 f-string ──────────────────────────────────
# 格式：'...' 与 "..." 完全等价；三引号 """...""" 写多行字符串（类似 JS 反引号 `...`）
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，

可以由多行组成"""
print("单引号与双引号：", word, sentence)
print("多行文本：", paragraph)
# 格式：字符串.count(子串) -> 出现次数（这里统计换行符 \n 的个数）
print("多行换行数：", paragraph.count("\n"))

# 拓展：相邻的字符串字面量在编译时会自动拼接
auto_joined = "this " "is " "string"
name = "runoob"
print("自动拼接：", auto_joined)

# 格式：字符串1 + 字符串2 -> 拼接；字符串 * 次数 -> 重复（JS 为 'ab'.repeat(3)）
# 格式：str(值) -> 转为字符串（不能直接 "a" + 1，需先 str(1)）
print("两个字符串相加：", "ab" + "cd")
repeated = "ab" * 3
explicit_join = "a" + str(1)
print("重复与拼接：", repeated, explicit_join)

# 格式：f"文字{表达式}" -> 格式化字符串（类似 JS 模板字符串 `hi ${name}, ${1 + 1}`）
# 场景：把变量或表达式嵌入句子时，比 + 拼接更易读
print("拼接问候语：", "hi " + name + ", " + str(1 + 1))
greeting = f"hi {name}, {1 + 1}"
print("f-string：", greeting)


# ── 3. 字符串：索引与切片 ─────────────────────────────────────────────
# 注意：不要把变量命名为 str，否则会覆盖内置的 str 类型
s = "123456789"

# 格式：变量[下标] -> 单个字符（长度仍为 1 的 str）
# 注意：0 是第一位，-1 是最后一位（JS 可写 s.at(-1)）
print("第 1 个字符 s[0]：", s[0])
print("最后 1 个字符 s[-1]：", s[-1])

# 格式：变量[头下标:尾下标:步长] -> 新字符串（不含尾下标）
# 注意：省略步长默认 1，即 变量[头下标:尾下标]（类似 JS 的 s.slice(start, end)）；负步长表示从右往左
# 拓展：切片越界不报错，只取到末尾；s[::-1] 可直接反转（JS 需 [...s].reverse().join('')）
print("s[0:-1] =", s[0:-1])
print("s[2:5]  =", s[2:5])             # 下标 2、3、4
print("s[2:]   =", s[2:])
print("s[:3]   =", s[:3])              # 省略起点，从头取到下标 3 之前
print("s[1:5:2]=", s[1:5:2])           # 下标 1、3，步长为 2
print("s[::-1] =", s[::-1])            # 步长为 -1 实现反转
print("s[2:100]=", s[2:100])           # 切片越界不报错，只取到末尾

# 注意：Python 没有单独的字符类型，单字符仍是 str（len 见 01_syntax_demo.py「关键字」）
first_char = s[0]
print("单字符类型与长度：", type(first_char), len(first_char))


# ── 4. 转义与原始字符串 ───────────────────────────────────────────────
# 格式：r"..." -> 原始字符串，反斜杠按原样保留（JS 类似 String.raw`a\nb`）
# 注意："a\nb" 中 \n 是换行，共 3 个字符；r"a\nb" 不转义，共 4 个字符
normal_str = "a\nb"
raw_str = r"a\nb"
print("普通转义字符串：\n" + normal_str)
print("原始字符串：", raw_str, "长度：", len(raw_str))


# ── 拓展：观察字符串操作的三种报错 ────────────────────────────────────
# 注意：TypeError 表示类型不符，IndexError 表示下标越界；_ 惯例表示忽略返回值
# 拓展：try / except 读法见 01_syntax_demo.py 末尾
try:
    _ = "a" + 1                        # JS 中会得到 "a1"，Python 直接报 TypeError
except TypeError:
    print("【进阶】字符串与整数相加抛出 TypeError")

try:
    _ = s[100]                         # JS 中返回 undefined，Python 直接报 IndexError
except IndexError:
    print("【进阶】索引越界抛出 IndexError")

try:
    s[0] = "X"                         # 字符串不可变；JS 非严格模式静默失败，Python 抛 TypeError
except TypeError:
    print("【进阶】修改字符串字符抛出 TypeError")
