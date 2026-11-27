"""第 3 章 · 字符、Unicode 码点、字节与内存视图转换。

用途：演示 chr() 与 ord() 互转、文本与字节编解码、bytes / bytearray 互转，以及 memoryview 零拷贝视图。
运行（仓库根目录，已激活 .venv）：python lessons/03-type-conversion/04_chars_bytes_demo.py
"""

# ── 1. Unicode 码点与单字符互转 ───────────────────────────────────────
# 格式：chr(整数码点) -> 单个字符（范围 0～0x10FFFF，对应 JS 的 String.fromCodePoint(code)）
# 注意：反向操作 ord(单个字符) 见第 2 章 05_bytes_demo.py，两者互为逆运算
print("码点转字符：", chr(65))            # A
print("字符转码点：", ord("A"))           # 65；ord 只接受长度为 1 的字符
print("中文码点往返：", chr(ord("雨")))   # 雨


# ── 2. 文本与 UTF-8 字节互转（复习） ──────────────────────────────────
# 注意：encode / decode 首次讲解见第 2 章 05_bytes_demo.py；UTF-8 中一个常用汉字占 3 字节
text = "你好"
data = text.encode("utf-8")
print("编码为字节：", data, type(data))                    # b'\xe4\xbd\xa0\xe5\xa5\xbd' <class 'bytes'>
print("解码为文本：", data.decode("utf-8"))                # 你好
print("字符数和 UTF-8 字节数：", len(text), len(data))     # 2 6


# ── 3. 整数序列与 bytes / bytearray 互转 ──────────────────────────────
# 格式：bytes(0～255 整数列表) -> 不可变字节；bytearray(0～255 整数列表) -> 可修改字节
# 注意：每个整数必须在 0～255 之间；bytes(mutable) 会把可修改的 bytearray 冻结成不可变副本
immutable = bytes([65, 66])
mutable = bytearray([65, 66])
mutable[1] = 67
frozen_bytes = bytes(mutable)
print("整数列表转 bytes：", immutable)                   # b'AB'
print("修改 bytearray 并冻结：", mutable, frozen_bytes)  # bytearray(b'AC') b'AC'


# ── 4. 拓展：内存视图 memoryview() ────────────────────────────────────
# 格式：memoryview(缓冲区对象) -> memoryview（不复制底层字节数据，直接共享内存）
# 场景：处理大块二进制数据（文件、图片、网络缓冲）时避免拷贝开销；类似 JS 的 DataView / TypedArray 视图
# 注意：对 bytearray 创建的视图可修改，且修改会直接反映到原对象；对 bytes 创建的视图只读
view = memoryview(mutable)
print("视图长度与切片：", len(view), list(view))         # 2 [65, 67]
view[0] = 68                                             # 68 对应 'D'，直接修改底层 mutable
print("通过视图修改后原对象同步变化：", mutable)          # bytearray(b'DC')


# ── 5. 拓展：观察字符与字节转换的报错 ─────────────────────────────────
# 注意：字节值超出 0～255 会抛 ValueError；memoryview 不接受 str（只接受 bytes / bytearray 等）
try:
    _ = bytes([256])
except ValueError as error:
    print("拓展 - 字节超出 0～255：", error)  # bytes must be in range(0, 256)

try:
    _ = memoryview("AB")
except TypeError as error:
    print("拓展 - 字符串不支持 memoryview：", error)  # memoryview: a bytes-like object is required, not 'str'
