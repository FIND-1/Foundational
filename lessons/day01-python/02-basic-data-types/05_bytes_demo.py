"""第 2 章 · bytes 类型与文本编码。

用途：演示 bytes 的创建、按下标读取整数、切片与拼接，以及 encode / decode 和可修改的 bytearray。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/05_bytes_demo.py
预期结果：b"hello" 的首个元素打印 104；x[1:3] 打印 b'el'；"你好" 有 2 个字符、6 个 UTF-8 字节；
bytearray 修改后解码为 Hello。末尾演示修改 bytes 元素的报错。
"""

# ── 1. 用 b 前缀创建 bytes ────────────────────────────────────────────
# 格式：b"ASCII文本" -> bytes（不可变的字节序列，每个元素是 0～255 的整数）
# 注意：取单个元素 x[0] 得到 int（不是单字符）；类似 JS 的 Uint8Array，但 bytes 不可修改
x = b"hello"
print(x)               # b'hello'
print(type(x))         # <class 'bytes'>
print(x[0])            # 104：'h' 的 ASCII 值，取单个元素得到 int


# ── 2. 用 bytes() 转换 ────────────────────────────────────────────────
# 格式：bytes(字符串, encoding="utf-8") -> bytes（按指定编码转为字节序列）
x = bytes("hello", encoding="utf-8")
print("bytes() 转换：", x)


# ── 3. 切片与拼接 ─────────────────────────────────────────────────────
# 格式：字节[头下标:尾下标] -> 新 bytes；字节1 + 字节2 -> 拼接后的新 bytes（原对象不变）
# 注意：b 只是类型标记（不占下标也不拼进内容）；单下标 x[1] 得 int，切片 x[1:3] 仍得 bytes；不能与 str 直接相加
x = b"hello"
y = x[1:3]          # 切片，得到 b'el'
z = x + b"world"    # 拼接，得到 b'helloworld'
print(y)            # b'el'
print(z)            # b'helloworld'


# ── 4. 用 ord() 比较元素 ──────────────────────────────────────────────
# 格式：ord(单个字符) -> int（返回字符的 Unicode 码点，如 ord("h") 得 104）
# 注意：bytes 元素是整数，与单字符字符串直接 == 不会报错，但恒为 False；比较前需用 ord()
x = b"hello"
if x[0] == ord("h"):
    print("第一个元素是 'h'")
print("x[0] == 'h'：", x[0] == "h")


# ── 5. 文本与字节的互相转换 ───────────────────────────────────────────
# 格式：字符串.encode("utf-8") -> bytes；字节.decode("utf-8") -> str
# 注意：对应 JS 的 TextEncoder / TextDecoder；一个汉字在 UTF-8 占 3 字节，所以字符数(2) != 字节数(6)
message = "你好"
data = message.encode("utf-8")
print("编码结果：", data)
print("解码结果：", data.decode("utf-8"))  # 你好
print("字符数量与字节数量：", len(message), len(data))  # 2 6
print("字节序列的首个元素：", data[0])  # 228，取值 0～255


# ── 6. 可修改的 bytearray ─────────────────────────────────────────────
# 格式：bytearray(字节) -> 可修改的字节序列副本
# 注意：修改 bytearray[下标] 时右侧必须是 0～255 的整数；原 bytes 不受影响
ascii_data = bytes("hello", encoding="utf-8")
mutable = bytearray(ascii_data)
mutable[0] = ord("H")                          # 赋值时右侧必须是 0～255 的整数
print("修改 bytearray：", mutable.decode("utf-8"))  # Hello
print("原 bytes 不变：", ascii_data)            # b'hello'

# 拓展：数据类型转换（int()、float()、list() 等）在第 3 章具体介绍


# ── 拓展：观察修改 bytes 元素的报错 ───────────────────────────────────
# 注意：bytes 不可变，给下标赋值会抛 TypeError（try / except 见第 1 章 01_syntax_demo.py 末尾）
try:
    ascii_data[0] = 72
except TypeError as error:
    print("【进阶】修改 bytes 元素：", error)
