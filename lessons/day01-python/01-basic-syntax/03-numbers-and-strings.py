"""数字与字符串基础。"""

print("数字类型：", 10, 3.14, True, 2 + 3j)
text = "123456789"
print("索引：", text[0], text[-1])  # 1 9
print("切片：", text[0:-1], text[2:5])  # 12345678 345
print("步长为 2：", text[1:8:2])  # 2468；结束下标 8 不包含
print("重复与拼接：", text * 2, text + "你好")
print("转义字符：", "hello\nPython")
print("原始字符串：", r"hello\nPython")
print("多行字符串：", """第一行
第二行""")
