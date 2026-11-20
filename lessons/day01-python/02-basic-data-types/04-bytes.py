"""bytes 字节类型。"""

x = b"hello"           # 使用 b 前缀创建 bytes 对象
print(x)               # b'hello'
print(type(x))         # <class 'bytes'>
print(x[0])            # 104（'h' 的 ASCII 值，bytes 元素是整数）

x = bytes("hello", encoding="utf-8")

x = b"hello"
y = x[1:3]          # 切片操作，得到 b'el'
z = x + b"world"    # 拼接操作，得到 b'helloworld'
print(y)            # b'el'
print(z)            # b'helloworld'

x = b"hello"
if x[0] == ord("h"):    # ord("h") 返回 104
    print("第一个元素是 'h'")



# 【补充】以下保留原有扩展示例。
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
