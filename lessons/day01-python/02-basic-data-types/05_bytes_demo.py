"""第 2 章 · bytes 类型与文本编码。

用途：演示 bytes 的创建、按下标读取整数、切片与拼接，以及 encode / decode 和可修改的 bytearray。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/05_bytes_demo.py
预期结果：b"hello" 的首个元素打印 104；x[1:3] 打印 b'el'；"你好" 有 2 个字符、6 个 UTF-8 字节；
bytearray 修改后解码为 Hello。末尾演示修改 bytes 元素的报错。
"""

# ── 1. 用 b 前缀创建 bytes ────────────────────────────────────────────
# 【必会】b"..." 写出 bytes 对象，它是不可变的字节序列，每个元素是 0～255 的整数，不是字符。
# 【补充】JS 中接近的是 Uint8Array，但 Uint8Array 可以修改元素。
x = b"hello"
print(x)               # b'hello'
print(type(x))         # <class 'bytes'>
print(x[0])            # 104：'h' 的 ASCII 值，取单个元素得到 int


# ── 2. 用 bytes() 转换 ────────────────────────────────────────────────
# 【必会】bytes(文本, encoding="utf-8") 用指定编码把字符串转成 bytes，这里得到 b'hello'。
x = bytes("hello", encoding="utf-8")
print("bytes() 转换：", x)


# ── 3. 切片与拼接 ─────────────────────────────────────────────────────
# 与字符串类似，bytes 支持切片和 +，结果都是新的 bytes 对象，原对象不变。
x = b"hello"
y = x[1:3]          # 切片，得到 b'el'
z = x + b"world"    # 拼接，得到 b'helloworld'
print(y)            # b'el'
print(z)            # b'helloworld'


# ── 4. 用 ord() 比较元素 ──────────────────────────────────────────────
# 【必会】ord(字符) 返回字符的 Unicode 码点，ord("h") 得到 104。
# bytes 的元素是整数，所以要和整数比较；ASCII 字符在 UTF-8 中正好是同值的单字节。
x = b"hello"
if x[0] == ord("h"):
    print("第一个元素是 'h'")
# 【补充】直接拿整数和单字符字符串比较不会报错，但结果总是 False。
print("x[0] == 'h'：", x[0] == "h")


# ── 5. 【补充】文本与字节的互相转换 ───────────────────────────────────
# 【必会】文本.encode("utf-8") 把字符串编码为 bytes；字节.decode("utf-8") 用相同编码还原文本。
# 【补充】对应 JS 的 new TextEncoder().encode(text) 和 new TextDecoder("utf-8").decode(bytes)。
message = "你好"
data = message.encode("utf-8")
print("编码结果：", data)
print("解码结果：", data.decode("utf-8"))  # 你好
# 一个汉字在 UTF-8 中占 3 个字节，所以字符数和字节数不同。
print("字符数量与字节数量：", len(message), len(data))  # 2 6
print("字节序列的首个元素：", data[0])  # 228，取值 0～255


# ── 6. 【补充】可修改的 bytearray ─────────────────────────────────────
# 【必会】bytearray(字节) 复制出一个可修改的字节序列；修改副本不会影响原来的 bytes。
ascii_data = bytes("hello", encoding="utf-8")
mutable = bytearray(ascii_data)
mutable[0] = ord("H")                          # 赋值时右侧必须是 0～255 的整数
print("修改 bytearray：", mutable.decode("utf-8"))  # Hello
print("原 bytes 不变：", ascii_data)            # b'hello'

# 数据类型转换（int()、float()、list() 等）在第 3 章具体介绍。


# ── 【补充】【进阶】观察修改 bytes 元素的报错 ─────────────────────────
# bytes 不可变，给下标赋值会抛 TypeError；try / except 的读法见第 1 章 01_syntax_demo.py 末尾。
try:
    ascii_data[0] = 72
except TypeError as error:
    print("【进阶】修改 bytes 元素：", error)
