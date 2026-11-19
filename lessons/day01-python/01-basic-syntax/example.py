"""基础语法：运行本文件，观察每一段的输出。"""

import keyword
import math
from math import sqrt

# 合法的变量名；Python 区分大小写。
user_name = "Rain"
print("变量：", user_name)
print("if 是关键字：", "if" in keyword.kwlist)

# 冒号后的缩进表示同一个代码块。
if len(user_name) > 0:
    print("用户名不为空")
    print("这两行属于同一个代码块")

# 括号内部可以换行，不需要反斜杠。
total = (
    1
    + 2
    + 3
)
print("合计：", total)  # 6

text = "123456789"
print("首字符：", text[0])       # 1
print("倒数第一个：", text[-1])  # 9
print("切片：", text[1:8:2])     # 2468，结束位置 8 不包含
print("换行：", "hello\nPython")
print("原始字符串：", r"hello\nPython")

print("不换行", end=" ")
print("继续输出")
print("平方根：", math.sqrt(16), sqrt(25))  # 4.0 5.0

# 取消下面两行的注释，可以练习输入。input 的返回值是字符串。
# answer = input("请输入你的名字：")
# print("你好，", answer)
