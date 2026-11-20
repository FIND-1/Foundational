"""第 2 章 · 文本编码与字节。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/02-basic-data-types/04-bytes.py
观察 hello 的首字节 104，以及“你好”的两个字符编码为六个 UTF-8 字节。
"""

# b 前缀写出字节串，按下标读取时得到 0 到 255 的整数。
x = b"hello"
print(x)               # b'hello'
print(type(x))         # <class 'bytes'>
print(x[0])            # 104（'h' 的 ASCII 值，bytes 元素是整数）

# bytes(文本, encoding=编码名) 用指定编码生成字节串，这里得到 b"hello"。
x = bytes("hello", encoding="utf-8")

x = b"hello"
y = x[1:3]          # 切片操作，得到 b'el'
z = x + b"world"    # 拼接操作，得到 b'helloworld'
print(y)            # b'el'
print(z)            # b'helloworld'

x = b"hello"
# ord("h") 返回字符的 Unicode 码点 104；ASCII 字符在 UTF-8 中恰好占一个同值的字节。
if x[0] == ord("h"):
    print("第一个元素是 'h'")

# 【补充】bytes 保存字节，文本和字节需要通过编码转换。

message = "你好"
# 文本.encode("utf-8") 用 UTF-8 把字符转为字节。字节串.decode("utf-8") 按相同编码还原文本。
data = message.encode("utf-8")
print("编码结果：", data)
print("解码结果：", data.decode("utf-8"))  # 你好
print("字符数量与字节数量：", len(message), len(data))  # 2 6
print("字节序列的首个元素：", data[0])  # 整数，取值 0 到 255

ascii_data = bytes("hello", encoding="utf-8")
print("构造 bytes：", ascii_data)
# bytearray(ascii_data) 从现有字节复制出可修改的序列，修改副本不会影响 ascii_data。
mutable = bytearray(ascii_data)
mutable[0] = ord("H")
print("修改 bytearray：", mutable.decode("utf-8"))  # Hello
print("原 bytes 不变：", ascii_data)
