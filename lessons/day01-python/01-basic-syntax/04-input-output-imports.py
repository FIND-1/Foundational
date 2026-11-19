"""输入、输出、模块导入和命令行参数。"""

import math  # 标准库数学模块，sqrt 用于计算平方根
import sys  # 标准库模块，提供命令行参数和模块搜索路径等信息
from math import sqrt  # 也可以直接导入模块中的 sqrt

print("默认换行")
print("同一行", end=" ")
print("继续输出")
print("指定分隔符：", "a", "b", sep=" | ")
print("模块导入：", math.sqrt(16), sqrt(25))  # 4.0 5.0
print("命令行参数：", sys.argv)  # 第一项是脚本路径
print("模块搜索路径数量：", len(sys.path))

# 想练习交互输入时，取消下面两行注释；input() 返回字符串。
# name = input("请输入你的名字：")
# print("你好，", name, sep="")
