"""第 6 章 · 算术与比较运算符。

用途：演示基本算术、int() 向零截断与 // 向下取整及 % 取模的对照、六种比较、跨类型比较限制与链式比较。
运行（仓库根目录，已激活 .venv）：python lessons/06-operators/01_arith_compare_demo.py
"""

left = 7
right = 3

# ── 1. 基本算术运算 ───────────────────────────────────────────────────
# 格式：左值 + 右值、左值 - 右值、左值 * 右值（基本运算初识见第 1 章 02_strings_demo.py、第 2 章 01_numbers_demo.py）
print("加、减、乘：", left + right, left - right, left * right)  # 10 4 21

# 格式：左值 / 右值 -> 商（两个整数相除也得到 float）
print("除法：", left / right)  # 2.3333333333333335

# 格式：底数 ** 指数 -> 幂
print("乘方：", left ** right)  # 343


# ── 2. 整除、取模与 int() 向零截断 ────────────────────────────────────
# 格式：被除数 // 除数 -> 向下取整的商；被除数 % 除数 -> 与该商配对的余数
# 注意：一元 - 把 7 变成 -7；-7 / 3 约为 -2.333：
#   int(-7 / 3) 向零截断得 -2（见第 3 章 02_numbers_str_demo.py）；
#   -7 // 3 向下取整得 -3，配对余数 -7 % 3 得 2，满足 (-3) * 3 + 2 == -7
# 注意：对整数，非零余数与除数同号（与 JS % 相反）；除数为 0 时抛 ZeroDivisionError
negative = -left
print("整除和取模：", left // right, left % right)  # 2 1
print("负数整除和取模：", negative // right, negative % right)  # -3 2
print("向零截断 vs 向下取整与取模：", int(negative / right), negative // right, negative % right)  # -2 -3 2
print("负除数取模：", left % -right)  # -2


# ── 3. 比较运算与链式比较 ─────────────────────────────────────────────
# 格式：== 判断相等，!= 判断不等（布尔与比较初识见第 2 章 02_str_bool_demo.py）
print("相等、不等：", left == right, left != right)  # False True

# 格式：<、<=、>、>= 依次判断小于、小于等于、大于、大于等于
print("大小比较：", right < left, left <= left, left > right, right >= right)  # True True True True

# 注意：== / != 允许跨类型比较且不做隐式转换；
#       <、<=、>、>= 要求操作数可排序，跨类型大小比较直接报错（不引入 try/except）：
#       3 < "4"  -> TypeError: '<' not supported between instances of 'int' and 'str'
print("跨类型相等比较：", 3 == "3", 3 != "3")  # False True

# 格式：下界 <= 值 < 上界 -> 左闭右开的区间判断
# 注意：链式比较中的中间表达式只求值一次（JS 写 3 <= 7 < 10 会先得 true 再算 1 < 10）
upper = left + right
print("链式比较：", right <= left < upper)  # True
