"""第 1 章 · 输入输出、导入、命令行参数。

运行：python .\\lessons\\day01-python\\01-basic-syntax\\demo_io_import.py
带参数运行：python .\\lessons\\day01-python\\01-basic-syntax\\demo_io_import.py Rain 123
体验 input：python .\\lessons\\day01-python\\01-basic-syntax\\demo_io_import.py --ask
"""

import contextlib
import io
import sys


def captured(action):
    """执行 action()，并以字符串形式返回它向终端打印的内容，方便用 assert 检查 print 的结果。"""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):   # with：临时把输出重定向到 buffer，代码块结束后自动恢复
        action()
    return buffer.getvalue()


# ── print ─────────────────────────────────────────────────────────────
# print(*objects, sep=" ", end="\n")：参数之间用 sep 连接，最后补上 end。
# 和 console.log 的区别：可以修改分隔符和结尾。
# lambda 相当于 JS 的箭头函数：lambda: print("a") ≈ () => console.log("a")
assert captured(lambda: print("a", "b")) == "a b\n"
assert captured(lambda: print("a", "b", sep=" | ")) == "a | b\n"
assert captured(lambda: print("a", end=" ")) == "a "      # 不换行
assert captured(lambda: print()) == "\n"                    # 只输出一个换行

# print 的返回值是 None（相当于 JS 的 undefined / null）
assert captured(lambda: print(print("x"))) == "x\nNone\n"

# sys.stdout.write 是更底层的写法：不会自动换行，返回写入的字符数
with contextlib.redirect_stdout(io.StringIO()) as buffer:
    written = sys.stdout.write("runoob\n")
assert written == 7 and buffer.getvalue() == "runoob\n"
# 在交互式环境（REPL）中会额外看到一个 7：REPL 会自动显示表达式的值，就像浏览器控制台一样


# ── input ─────────────────────────────────────────────────────────────
# input(prompt) 会阻塞等待用户输入，返回值永远是 str（类似浏览器的 prompt()）。
# 为了不卡住常规运行，只有传入 --ask 时才执行：
if "--ask" in sys.argv:
    age = input("你的年龄：")
    print("input 返回的类型：", type(age))          # <class 'str'>
    print("明年：", int(age) + 1)                   # 需要先转成 int 才能做加法


# ── import ────────────────────────────────────────────────────────────
# 与 ES Module 的对应关系：
#   import sys                     ≈ import * as sys from "sys"
#   from sys import argv, path     ≈ import { argv, path } from "sys"
#   import keyword as kw           ≈ import * as kw from "keyword"
#   from sys import *              JS 中没有对应写法；会把名字直接灌进当前文件，不推荐使用
from sys import argv, path
import keyword as kw

assert argv is sys.argv and path is sys.path      # 导入的是同一个对象，不是副本
assert kw.iskeyword("def")
# 模块和 ES Module 一样会被缓存：同一个模块在一个进程里只执行一次


# ── 命令行参数 ────────────────────────────────────────────────────────
# sys.argv[0] 是脚本路径，之后是传入的参数，全部都是 str。
# 对比 Node：process.argv 是 [node 路径, 脚本路径, ...参数]，Python 少了第一项。
assert isinstance(sys.argv[0], str)
print("命令行参数：", sys.argv[1:])               # 带 Rain 123 运行时得到 ['Rain', '123']

# 在 PowerShell 中执行 python -h，可以查看解释器自身的选项，例如 -c、-m、-V。
# 解析复杂参数时使用标准库 argparse（相当于 Node 生态中的 commander / yargs）。

print("demo_io_import: all passed")
