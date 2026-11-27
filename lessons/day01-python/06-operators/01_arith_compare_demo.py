"""第 6 章 · 算术与比较运算符。

用途：观察基本运算、负数整除和取模，以及比较结果和链式比较。
运行：./.venv/Scripts/python.exe lessons/day01-python/06-operators/01_arith_compare_demo.py
预期结果：7 / 3 得到小数，-7 // 3 得到 -3，-7 % 3 得到 2，链式比较得到 True。
"""

left = 7
right = 3

# 格式：左值 + 右值求和，左值 - 右值求差，左值 * 右值求积。
print("加、减、乘：", left + right, left - right, left * right)  # 10 4 21

# 格式：左值 / 右值 -> 商。两个整数相除也得到 float；7 / 3 约为 2.333。
print("除法：", left / right)

# 格式：底数 ** 指数 -> 幂。7 的三次方是 343。
print("乘方：", left ** right)

# 格式：被除数 // 除数 -> 向下取整的商；被除数 % 除数 -> 与该商配对的余数。
# 注意：一元 - 把 7 变成 -7。-7 / 3 约为 -2.333，向下取整得到 -3；
# -7 = (-3) * 3 + 2。对整数，非零余数的符号与除数一致，除数为 0 时会抛出 ZeroDivisionError。
negative = -left
print("整除和取模：", left // right, left % right)  # 2 1
print("负数整除和取模：", negative // right, negative % right)  # -3 2
print("负除数取模：", left % -right)  # -2

# 格式：== 判断相等，!= 判断不等。这里 7 与 3 不相等，依次得到 False 和 True。
print("相等、不等：", left == right, left != right)

# 格式：<、<=、>、>= 依次判断小于、小于等于、大于、大于等于。
# 先用不同的数区分大小，再用同一个数检查 <= 和 >= 是否包含相等。
print("大小比较：", right < left, left <= left, left > right, right >= right)

# 格式：下界 <= 值 < 上界 -> 左闭右开的区间判断。本例 3 <= 7 且 7 < 10。
# 注意：链式比较中的中间表达式只求值一次。
upper = left + right
print("链式比较：", right <= left < upper)  # True
