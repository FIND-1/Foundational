"""第 4 章 · 运行问候脚本，观察命令行参数。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/04-interpreter/example.py Rain
第一行显示 Hello, Python!，第二行向 Rain 问好，最后一行显示解释器版本。省略 Rain 可观察默认问候语。
"""

import sys

# 调用 print 时左括号紧跟函数名，行末可以省略分号。运行后，终端显示 Hello, Python!。
print("Hello, Python!")

# 【补充】先用两个分支选名字。sys.argv[0] 是脚本路径，长度大于 1 时才有 sys.argv[1]。
# if len(sys.argv) > 1:
#     name = sys.argv[1]
# else:
#     name = "Python 学习者"

# 两个分支都只选一个值时，可写成条件表达式，类似 JS 的条件运算符。
# 先读 if 后面的条件，只计算选中的一侧；无参数时跳过下标 1，使用默认名字。
name = sys.argv[1] if len(sys.argv) > 1 else "Python 学习者"
print("你好，", name, sep="")
# sys.version 是版本信息文本，用 split() 按空白拆开后，[0] 取版本号。
print("当前解释器版本：", sys.version.split()[0])
