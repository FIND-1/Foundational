"""字符、Unicode 码点，以及文本与字节之间的转换。"""

# 【补充】字符与字节转换练习。
print("码点转字符：", chr(65))  # A
print("字符转码点：", ord("A"))  # 65；ord 需要单个字符
print("中文码点往返：", chr(ord("雨")))  # 雨

text = "你好"
data = text.encode("utf-8")
print("编码为字节：", data, type(data))
print("解码为文本：", data.decode("utf-8"))  # 你好
print("字符数和 UTF-8 字节数：", len(text), len(data))  # 2 6

# bytes 不可变，bytearray 可修改；输入的整数必须在 0 到 255 之间。
mutable = bytearray([65, 66])
mutable[1] = 67
print("可修改字节：", mutable, bytes(mutable))  # bytearray(b'AC') b'AC'
