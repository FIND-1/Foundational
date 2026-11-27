"""第 6 章 · 位运算与逻辑运算。

用途：演示六种整数位运算与拓展权限掩码，展示 and / or / not 的返回值与短路求值，以及 or 与仅在 None 时回退的区别。
运行（仓库根目录，已激活 .venv）：python lessons/06-operators/03_bitwise_logic_demo.py
"""

# ── 1. 整数位运算 ─────────────────────────────────────────────────────
# 格式：整数 & 整数 -> 按位与（对应位都为 1 才保留 1）
# 60 的低八位是 00111100，13 是 00001101，共有位是 00001100
left = 60
right = 13
print("按位与：", left & right)  # 12

# 格式：整数 | 整数 -> 按位或（任一为 1 即置 1）；整数 ^ 整数 -> 按位异或（不同才置 1）
print("按位或和异或：", left | right, left ^ right)  # 61 49

# 格式：~整数 -> 按位取反（对 Python 整数，~x 等于 -x - 1）
print("按位取反：", ~left)  # -61

# 格式：整数 << 位数、整数 >> 位数 -> 左移等价于乘 2**位数，右移等价于向下整除 2**位数
# 注意：Python 整数左移不会丢弃高位；位数必须为非负整数，否则抛 ValueError
print("左移和右移：", left << 2, left >> 2)  # 240 15
print("负数右移：", -3 >> 1)  # -2


# ── 2. 拓展：二进制权限掩码与清除 ─────────────────────────────────────
# 拓展：格式：0b 后写二进制位（0b01 为 1，0b10 为 2，各占一个权限位）
# 拓展：用 | 合并权限，用 & 取出目标位再与 0 比较判断是否开启；用 flags & ~位 清除指定位并保留其他位
read_flag = 0b01
write_flag = 0b10
flags = read_flag | write_flag
print("拓展 - 可写：", (flags & write_flag) != 0)  # True
print("拓展 - 去掉写权限：", flags & ~write_flag)  # 1


# ── 3. 逻辑运算符：返回值与短路求值 ───────────────────────────────────
# 注意：真假值规则见第 2 章 02_str_bool_demo.py（None、False、0、""、空容器为假，其余为真）
# 格式：左值 and 右值 -> 左值为假时直接返回左值（短路），否则求值并返回右值
# 空列表是假值，names[0] 因短路未求值，避免 IndexError；非空列表则返回首项本身
names = []
print("空列表短路：", names and names[0])  # []
names = ["Rain"]
print("非空列表取首项：", names and names[0])  # Rain

# 格式：左值 or 右值 -> 左值为真时直接返回左值（短路），否则求值并返回右值
user_input = ""
print("空输入回退：", user_input or "访客")  # 访客
print("非空文本短路：", names[0] or (1 / 0))  # Rain

# 格式：not 值 -> bool（始终返回布尔值）
print("列表是否为空：", not names)  # False


# ── 4. 默认值：or 与仅在 None 时回退 ──────────────────────────────────
# 注意：0、""、False 都是假值，用 `值 or 默认值`（类似 JS 的 ||）会把这些合法假值也替换掉
# 格式：默认值 if 值 is None else 值 -> 条件表达式，先算中间的 if 条件，只求值命中的一侧（类似 JS 的 ??）
# 注意：is None 判断变量是否为 None（is 身份判断详见 04_member_id_demo.py）；repr() 见第 3 章 02_numbers_str_demo.py
retries = 0
nickname = ""
enabled = False
missing = None

print("or 会误盖合法假值：", retries or 3, nickname or "访客", enabled or True)  # 3 访客 True
safe_retries = 3 if retries is None else retries
safe_nickname = "访客" if nickname is None else nickname
safe_enabled = True if enabled is None else enabled
safe_missing = "访客" if missing is None else missing
print("仅 None 时回退：", safe_retries, repr(safe_nickname), safe_enabled, safe_missing)  # 0 '' False 访客
