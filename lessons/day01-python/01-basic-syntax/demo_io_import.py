"""第 1 章 · 输入输出、导入、命令行参数。

用途：演示 print 参数、input() 输入、import 导入方式以及 sys.argv 命令行参数。
在仓库根目录运行（PowerShell 提示符已显示 (.venv)）：
  基础运行：python lessons/day01-python/01-basic-syntax/demo_io_import.py
  带参数运行：python lessons/day01-python/01-basic-syntax/demo_io_import.py Rain 123
  体验 input：python lessons/day01-python/01-basic-syntax/demo_io_import.py --ask
预期结果：输入模式下键入 18 会看到明年为 19；常规输出含 A B C、a | b、写入字符数 7 和命令行参数列表，以及最后一行 `demo_io_import: all passed`。
"""

# import 载入模块；sys.argv 保存启动脚本时传入的参数。
import sys

# 空行帮助分清代码段。顶层的函数或类定义之间通常空两行，类内方法之间空一行。

# ── input 输入 ─────────────────────────────────────────────────────
# input(prompt) 会阻塞等待用户输入，返回值永远是 str（类似浏览器的 prompt()）。
# 为了不卡住常规运行，只有传入 --ask 参数时才执行：
# in 检查列表里是否有这个参数；int(...) 把十进制整数字符串转成整数，请输入如 18。
if "--ask" in sys.argv:
    age_text = input("你的年龄：")
    print("input 返回的类型：", type(age_text))     # <class 'str'>
    next_year = int(age_text) + 1                 # 需要先用 int() 转成数字才能做加法
    print("明年：", next_year)


# 一行写多条语句可以用分号分隔，但不推荐
a = 1; b = 2
print("同行分号：", a + b)


# ── 代码组（子句） ───────────────────────────────────────────
# if、while、def、class 等复合语句首行以冒号结尾，后面缩进的代码就是它的“代码组”。
# 【补充】下面用 def 定义一个简单函数（相当于 JS 的 function），用 return 返回结果：
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:                  # JS 写 else if，Python 写 elif
        return "B"
    else:
        return "C"


print("代码组函数结果：", grade(95), grade(70), grade(30))
# 首行和缩进块合称子句。


# ── print 输出 ─────────────────────────────────────────────────────
# print(*objects, sep=" ", end="\n")：参数之间用 sep 连接，最后补上 end。
# 和 JS console.log 的区别：Python 可以直接指定分隔符 sep 和结尾字符 end。
first = "a"
second = "b"

print(first, second)                 # 默认用空格分隔，末尾换行 -> 输出: a b
print(first, second, sep=" | ")      # 修改分隔符 -> 输出: a | b

# 不换行输出：把默认的 end="\n" 改成空格或空字符串
print(first, end=" ")
print(second, end=" ")
print()                              # 空 print() 只输出一个换行

# print() 的返回值是 None（相当于 JS 的 undefined）
return_value = print("测试返回值")
print("print() 的返回值是：", return_value)

# 【补充】交互式解释器还会回显表达式的返回值，所以直接调用 write 会多看到一个数字。
# sys.stdout.write 是更底层的写入方法：不会自动换行，返回写入的字符数
text = "runoob\n"
written_count = sys.stdout.write(text)
print("写入字符数：", written_count)


# ── import 与 from...import ────────────────────────────────────────
# 【补充】与 ES Module 的对应关系：
#   import sys                     ≈ import * as sys from "sys"
#   from sys import argv, path     ≈ import { argv, path } from "sys"
#   import keyword as kw           ≈ import * as kw from "keyword"
#   from sys import *              会把模块内所有公开名称灌进当前文件，不推荐使用
from sys import argv, path
import keyword as kw

print("keyword.iskeyword('def') =", kw.iskeyword("def"))
# 模块和 ES Module 一样会被缓存：同一个模块在一个进程里只执行一次


# ── 命令行参数 ─────────────────────────────────────────────────────
# sys.argv[0] 是当前脚本的路径，后面依次是命令行传入的参数，全部都是 str。
# 对比 Node：process.argv 是 [node 路径, 脚本路径, ...参数]，Python 少了第一项。
script_path = sys.argv[0]
user_args = sys.argv[1:]             # 切片取出第 1 项之后的所有参数

print("当前脚本：", script_path)
print("命令行参数：", user_args)     # 带 Rain 123 运行时得到 ['Rain', '123']

# 在 PowerShell 中执行 python -h，可以查看 Python 解释器自身的命令行选项。
# 【补充】解析复杂命令行参数时，项目里通常使用标准库 argparse（相当于 Node 的 commander / yargs）。

# 【补充】【进阶】精确核对空格、换行和返回值，基础阅读到此即可。
assert grade(95) == "A" and grade(70) == "B" and grade(30) == "C"
assert return_value is None
assert written_count == 7            # "runoob" 6 个字符 + "\n" 1 个字符 = 7
assert argv is sys.argv              # 导入的是同一个列表对象，不是副本
assert path is sys.path
assert kw.iskeyword("def") is True
# isinstance(...) 检查对象是否属于给定的类型。
assert isinstance(script_path, str)
assert a + b == 3

# StringIO 是内存中的文本流。with 临时把标准输出指向它，退出缩进块时恢复；
# getvalue() 取回完整文本。lambda: 表达式 创建一个稍后调用的无参数函数。
import contextlib
import io


def captured(action):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        action()
    return buffer.getvalue()


assert captured(lambda: print("a", "b")) == "a b\n"
assert captured(lambda: print("a", "b", sep=" | ")) == "a | b\n"
assert captured(lambda: print("a", end=" ")) == "a "
assert captured(lambda: print()) == "\n"
assert captured(lambda: print(print("x"))) == "x\nNone\n"

with contextlib.redirect_stdout(io.StringIO()) as buffer:
    written = sys.stdout.write("runoob\n")
assert written == 7 and buffer.getvalue() == "runoob\n"

print("demo_io_import: all passed")
