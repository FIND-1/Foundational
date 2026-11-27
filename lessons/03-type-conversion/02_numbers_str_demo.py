"""第 3 章 · 显式类型转换：数字、字符串、布尔与进制。

用途：演示 int()、float()、str()、repr()、ascii()、bool()、str.lower()、complex()，以及进制解析与格式化。
运行（仓库根目录，已激活 .venv）：python lessons/03-type-conversion/02_numbers_str_demo.py
"""

# ── 1. int()、float()、str() 基础转换 ─────────────────────────────────
# 格式：int(值) -> int（浮点数向零截断，整数文本按十进制解析）
# 格式：float(值) -> float（整数、浮点数或数字文本转为浮点数）
# 格式：str(值) -> str（返回适合展示的文本；首次讲解见第 1 章 02_strings_demo.py）
x_int = int(1)      # 1
y_int = int(2.8)    # 2
z_int = int("3")    # 3
print("int() 结果：", x_int, y_int, z_int)  # 1 2 3

x_flt = float(1)      # 1.0
y_flt = float(2.8)    # 2.8
z_flt = float("3")    # 3.0
w_flt = float("4.2")  # 4.2
print("float() 结果：", x_flt, y_flt, z_flt, w_flt)  # 1.0 2.8 3.0 4.2

x_str = str("s1")  # 's1'
y_str = str(2)     # '2'
z_str = str(3.0)   # '3.0'
print("str() 结果：", x_str, y_str, z_str)  # s1 2 3.0


# ── 2. 显式转换后相加，以及保留原始输入 ───────────────────────────────
# 注意：先求右边 int(num_str) 得到新整数，再赋回 num_str；此后 num_str 指向整数，原文本丢失
num_int = 123
num_str = "456"

print("num_int 数据类型为:", type(num_int))           # <class 'int'>
print("类型转换前，num_str 数据类型为:", type(num_str))  # <class 'str'>

num_str = int(num_str)
print("类型转换后，num_str 数据类型为:", type(num_str))  # <class 'int'>

num_sum = num_int + num_str
print("num_int 与 num_str 相加结果为:", num_sum)       # 579
print("num_sum 数据类型为:", type(num_sum))           # <class 'int'>

# 场景：实际开发中通常用新变量名保存转换结果，避免覆盖原文本（例如 "0456" 的前导零还需用于展示）
quantity_text = "0456"
quantity = int(quantity_text)
print("保留原始输入：", quantity_text, type(quantity_text), "->", quantity, type(quantity))  # 0456 <class 'str'> -> 456 <class 'int'>


# ── 3. 截断、小数文本与复数 ───────────────────────────────────────────
# 注意：int() 转换浮点数时直接舍去小数部分（向零截断），类似 JS 的 Math.trunc()；
# 注意：这与整除 // 不同，-7 // 2 向下取整得 -4，而 int(-3.9) 向零截断得 -3
text = "42"
number = int(text)
print("整数与原文本：", number, type(number), "|", text, type(text))  # 42 <class 'int'> | 42 <class 'str'>
print("向零截断：", int(3.9), int(-3.9))                              # 3 -3

# 注意：int("3.5") 会抛 ValueError（不是整数格式）；需先用 float() 转浮点数，再用 int() 截断
print("浮点数与二次转换：", float("3.5"), int(float("3.5")))          # 3.5 3
print("数字转字符串拼接：", "年龄：" + str(18))                       # 年龄：18

# 拓展：complex(实部, 虚部) 构造复数（虚部默认 0；详见第 2 章 01_numbers_demo.py）
print("复数转换：", complex(2), complex(2, 3))                        # (2+0j) (2+3j)


# ── 4. str()、repr() 与 ascii() ───────────────────────────────────────
# 格式：repr(对象) -> str（返回偏调试/代码风格的表示字符串，如字符串会保留引号）
# 场景：给用户展示用 str()；调试时区分 "42" 和 42 用 repr()
print("str vs repr（字符串）：", str("hello"), "|", repr("hello"))    # hello | 'hello'
print("str vs repr（数字）：", str(42), "|", repr(42))                # 42 | 42

# 拓展：ascii(对象) -> str（类似 repr()，但把非 ASCII 字符转成 \uXXXX 等转义序列）
print("repr vs ascii（中文）：", repr("雨"), "|", ascii("雨"))        # '雨' | '\u96e8'


# ── 5. 布尔值转换与真假文本解析 ───────────────────────────────────────
# 注意：bool() 真假规则见第 2 章 02_str_bool_demo.py；非空字符串（包括 "False"）都为 True
print("假值：", bool(0), bool(""), bool(None))  # False False False
print("非空字符串为真：", bool("False"))         # True，不会解析英文单词含义

# 格式：字符串.lower() -> 转为小写的新字符串（原字符串不变，类似 JS 的 s.toLowerCase()）
# 场景：把配置或用户输入中的 "true" / "false" 文本解析成布尔值时，应先统一大小写再显式比较
flag_text = "False"
print("解析真假文本：", flag_text.lower() == "true")  # False


# ── 6. 进制解析与进制格式化 ───────────────────────────────────────────
# 格式：int(字符串, 进制) -> int（进制范围 2～36，按指定进制把文本解析为十进制整数）
# 注意：类似 JS 的 parseInt(text, radix)，但 Python 遇非法字符直接抛 ValueError，不会只读前面合法部分
print("进制解析：", int("101", 2), int("ff", 16))                      # 5 255
# 拓展：base=0 时根据 0b / 0o / 0x 前缀自动识别进制
print("自动识别进制：", int("0b101", 0), int("0o17", 0), int("0xff", 0))  # 5 15 255

# 格式：bin(整数) / oct(整数) / hex(整数) -> 带 0b / 0o / 0x 前缀的字符串
# 注意：JS 对应 n.toString(2 / 8 / 16) 且不带前缀；Python 负数会在前缀前保留负号（如 -0b101）
print("进制格式化：", bin(10), oct(10), hex(10))  # 0b1010 0o12 0xa
print("负数进制：", bin(-5), hex(-15))             # -0b101 -0xf
