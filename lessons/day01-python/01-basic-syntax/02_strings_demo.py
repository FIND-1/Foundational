"""第 1 章 · 数字与字符串：四种数字类型，字符串的引号、拼接、索引、切片和转义。

用途：直观打印各种数字与字符串操作结果，并与 JS 对照。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/01-basic-syntax/02_strings_demo.py
预期结果：除法打印 3.5、3 和 -4；s[2:5] 打印 345；原始字符串保留反斜杠。末尾演示三种字符串操作的报错。
"""

# ── 1. 数字类型 ───────────────────────────────────────────────────────
# type(值) 返回它的类型。例如打印 type(1) 会看到 <class 'int'>。
# 【补充】JS 只有 number（加 bigint），Python 分为 int、float、bool、complex 四种。
n_int = 1
n_float = 1.23
n_sci = 3E-2                           # 科学计数法：0.03
n_bool = True
n_complex = 1 + 2j                     # 复数：实部 + 虚部j，前端开发中很少用到
print("数字类型：", type(n_int), type(n_float), type(n_bool), type(n_complex))

# 【补充】** 表示乘方。Python 整数可按内存扩展，JS Number 超出安全整数范围后无法精确表示每个整数。
big_int = 2 ** 64
print("2 的 64 次方：", big_int)

# 【补充】【必会】两个整数用 / 相除得到 float；// 向下取整，所以 -7 // 2 得到 -4。
print("除法对比：", 7 / 2, 7 // 2, -7 // 2)

# 【补充】这个例子与 JS 的 Number 一样，二进制浮点数无法精确表示十进制的 0.1。
print("0.1 + 0.2 =", 0.1 + 0.2)

# 【补充】【了解】from decimal import Decimal 从标准库取出 Decimal，后面可以直接写这个名字。
# 把十进制文本传给 Decimal，再相加；这里能精确得到 0.3。若先传入浮点数，就会带入其二进制近似值。
from decimal import Decimal

print('Decimal("0.1") + Decimal("0.2") =', Decimal("0.1") + Decimal("0.2"))


# ── 2. 字符串：引号、拼接与 f-string ──────────────────────────────────
# 单引号和双引号完全等价；三引号用于多行字符串（JS 用反引号 `...`）
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，

可以由多行组成"""
print("单引号与双引号：", word, sentence)
print("多行文本：", paragraph)
# text.count(part) 返回 part 在 text 中出现的次数。这里统计换行符，试着增减空行再观察结果。
print("多行换行数：", paragraph.count("\n"))

# 相邻字符串字面量会在编译时自动拼接
auto_joined = "this " "is " "string"
name = "runoob"
print("自动拼接：", auto_joined)

# 运算：+ 拼接、* 重复（JS 为 'ab'.repeat(3)）
print("两个字符串相加：", "ab" + "cd")
repeated = "ab" * 3
# 【必会】str(值) 返回文本。先把整数 1 转为 "1"，再和 "a" 拼接，得到 "a1"。
explicit_join = "a" + str(1)
print("重复与拼接：", repeated, explicit_join)

# 【补充】把变量或计算结果嵌入一句话时，f-string 可以保留整句的阅读顺序。
# 先看显式拼接，再读 f"文字{表达式}"：花括号里的表达式会求值并格式化，类似 JS 的模板字符串。
print("拼接问候语：", "hi " + name + ", " + str(1 + 1))
greeting = f"hi {name}, {1 + 1}"
print("f-string：", greeting)


# ── 3. 字符串：索引与切片 ─────────────────────────────────────────────
# 注意：不要把变量命名为 str，否则会覆盖内置的 str 类型。
s = "123456789"

# s[i] 取下标为 i 的字符。0 是第一位，-1 是最后一位（JS 可写 s.at(-1)）。
print("第 1 个字符 s[0]：", s[0])
print("最后 1 个字符 s[-1]：", s[-1])

# 【必会】s[start:end:step] 从 start 开始，每次移动 step 个位置，在 end 之前停下。
# 【补充】省略 step 时步长为 1，类似 JS 的 s.slice(start, end)；负步长表示从右往左取。
print("s[0:-1] =", s[0:-1])
print("s[2:5]  =", s[2:5])             # 下标 2、3、4
print("s[2:]   =", s[2:])
print("s[:3]   =", s[:3])              # 省略起点，从头取到下标 3 之前
print("s[1:5:2]=", s[1:5:2])           # 下标 1、3，步长为 2
print("s[::-1] =", s[::-1])            # 步长为 -1 实现反转（JS 需 [...s].reverse().join('')）
print("s[2:100]=", s[2:100])           # 切片越界不会报错，只取到末尾

# 取出一个字符仍然得到 str，长度为 1。len 的首次示例见 01_syntax_demo.py 的「关键字」。
first_char = s[0]
print("单字符类型与长度：", type(first_char), len(first_char))


# ── 4. 转义与原始字符串 ───────────────────────────────────────────────
# 【必会】r"..." 保留反斜杠，因此下面的原始字符串有四个字符；普通字符串只有三个。
# 【补充】JS 可用 String.raw`a\nb` 保留这段文字中的反斜杠。
normal_str = "a\nb"
raw_str = r"a\nb"
print("普通转义字符串：\n" + normal_str)
print("原始字符串：", raw_str, "长度：", len(raw_str))


# ── 【补充】【进阶】观察字符串操作的报错 ──────────────────────────
# 这里预期两类错误：TypeError 表示操作与类型不符，IndexError 表示下标越界。
# _ 是普通变量名，惯例上表示用不到结果。异常分支的读法见 01_syntax_demo.py 的缩进报错示例。
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
