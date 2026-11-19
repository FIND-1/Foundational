"""bytes 保存字节，文本和字节需要通过编码转换。"""

message = "你好"
data = message.encode("utf-8")
print("编码结果：", data)
print("解码结果：", data.decode("utf-8"))  # 你好
print("字符数量与字节数量：", len(message), len(data))  # 2 6
print("字节序列的首个元素：", data[0])  # 整数，取值 0 到 255

ascii_data = bytes("hello", encoding="utf-8")
print("构造 bytes：", ascii_data)
mutable = bytearray(ascii_data)
mutable[0] = ord("H")
print("修改 bytearray：", mutable.decode("utf-8"))  # Hello
print("原 bytes 不变：", ascii_data)
