"""第 6 章 · 位运算与逻辑运算。

用途：用二进制位展示掩码与移位，再看短路求值怎样保护下标和除法。
运行：./.venv/Scripts/python.exe lessons/06-operators/03_bitwise_logic_demo.py
预期结果：按位得到 12、61、49、-61、240、15。短路表达式保留操作数。
"""

# 格式：整数 & 整数，只有两边对应位都为 1 时才保留该位。
# 60 的低八位是 00111100，13 是 00001101，共有位是 00001100。
left = 60
right = 13
print("按位与：", left & right)  # 12

# 格式：整数 | 整数，至少一边为 1 即置 1；整数 ^ 整数，两边不同才置 1。
print("按位或和异或：", left | right, left ^ right)  # 61 49

# 格式：~整数 -> 按位取反。Python 的 ~x 等于 -x - 1。
print("按位取反：", ~left)  # -61

# 格式：整数 << 位数、整数 >> 位数。左移 2 位相当于乘 4，右移 2 位相当于整除 4。
# 右移负数也按向下取整处理。位数必须是非负整数，负位数会抛出 ValueError。
print("左移和右移：", left << 2, left >> 2)  # 240 15
print("负数右移：", -3 >> 1)  # -2

# 格式：0b 后写二进制位。0b01 和 0b10 分别是整数 1 和 2，各占一个权限位。
# 场景：用 | 合并权限，用 & 取出目标位，再与 0 比较判断该位是否开启。
read_flag = 0b01
write_flag = 0b10
flags = read_flag | write_flag
print("可写：", (flags & write_flag) != 0)  # True
# 拓展：先对写权限取反，再用 & 清除该位并保留其他位。
print("去掉写权限：", flags & ~write_flag)  # 1

# 格式：左值 and 右值。左值为假值时直接返回左值，否则求值并返回右值。
# 空列表是假值，names[0] 因短路没有求值。非空列表则取到第一个名字。
names = []
print("空列表短路：", names and names[0])  # []
names = ["Rain"]
print("非空列表取首项：", names and names[0])  # Rain

# 格式：左值 or 右值。左值为真值时直接返回左值，否则求值并返回右值。
# 空字符串会选默认文本，非空文本会跳过右侧的除零表达式。
user_input = ""
print("空输入回退：", user_input or "访客")  # 访客
print("非空文本短路：", names[0] or (1 / 0))  # Rain

# 格式：not 值 -> bool。反转真值，当前 names 非空，因此得到 False。
print("列表是否为空：", not names)
