"""第 1 章 · 输入输出、导入、命令行参数。

用途：演示 print 参数、input() 输入、import 导入方式以及 sys.argv 命令行参数。
在仓库根目录运行（PowerShell 提示符已显示 (.venv)）：
  基础运行：python lessons/day01-python/01-basic-syntax/demo_io_import.py
  带参数运行：python lessons/day01-python/01-basic-syntax/demo_io_import.py Rain 123
  体验 input：python lessons/day01-python/01-basic-syntax/demo_io_import.py --ask
预期结果：输入模式下键入 18 会看到明年为 19；常规输出含 A B C、a | b、写入字符数 7 和命令行参数列表，以及最后一行 `demo_io_import: all passed`。
"""

# sys.argv 是一个字符串列表，依次保存脚本路径和你在命令行追加的参数。
import sys

# 空行帮助分清代码段。顶层的函数或类定义之间通常空两行，类内方法之间空一行。

# ── input 输入 ─────────────────────────────────────────────────────
# input(prompt) 会阻塞等待用户输入，返回值永远是 str（类似浏览器的 prompt()）。
# 带 --ask 时才会询问年龄，请输入整数，如 18。【补充】这里的成员检查类似 JS 的 args.includes("--ask")。
if "--ask" in sys.argv:
    age_text = input("你的年龄：")
    # 即使输入 18，这里看到的也是 <class 'str'>。
    print("input 返回的类型：", type(age_text))
    # int(文本) 把整数字符串转成整数，所以接下来的 + 1 会算出 19。
    next_year = int(age_text) + 1
    print("明年：", next_year)


# 一行写多条语句可以用分号分隔，但不推荐
a = 1; b = 2
print("同行分号：", a + b)


# ── 代码组（子句） ───────────────────────────────────────────
# if、while、def、class 等复合语句首行以冒号结尾，后面缩进的代码就是它的“代码组”。
# 【补充】def grade(score): 定义一个接收分数的函数，类似 JS 的 function grade(score)。
# 调用 grade(70) 时，score 取值 70。if 和 elif 依次检查条件，else 处理剩余情况；
# 遇到 return 就结束本次调用，把等级交给调用处，这次得到 "B"。
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
# *objects 表示可以传零个或多个值；调用时直接写这些值。sep= 和 end= 按名字指定选项。
# 【补充】和 JS console.log 的区别：Python 可以直接指定分隔符 sep 和结尾字符 end。
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

# sys.stdout 是标准输出流，默认通向终端。sys.stdout.write(text) 原样写出字符串，
# 返回写入的字符数。这里六个字母加上一个换行符，返回 7。
# 【补充】在交互式解释器中直接调用 write，解释器还会回显这个返回值。
text = "runoob\n"
written_count = sys.stdout.write(text)
print("写入字符数：", written_count)


# ── import 与 from...import ────────────────────────────────────────
# from 模块 import 名称：导入后可以直接写 argv 和 path。sys.path 是查找模块时使用的路径列表。
# import 模块 as 别名：给模块取个短名，下面用 kw 访问 keyword 模块。
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
# 【补充】与 Node.js 的对应关系（Python 少了最前面的 node 路径）：
#   Node.js: process.argv  -> [node 路径, 脚本路径, ...参数]
#   Python:  sys.argv      -> [脚本路径, ...参数]
# sys.argv[1:] 是切片，从下标 1 取到末尾。传入 Rain 123 时得到 ['Rain', '123']。
script_path = sys.argv[0]
user_args = sys.argv[1:]

print("当前脚本：", script_path)
print("命令行参数：", user_args)
# 在 PowerShell 中执行 python -h，可以查看 Python 解释器自身的命令行选项。
# 【补充】解析复杂命令行参数时，项目里通常使用标准库 argparse（相当于 Node 的 commander / yargs）。


# ── 【补充】【进阶】断言与输出捕获验证 ─────────────────────────────
# assert 是 Python 的断言语句，读作“这里的条件应该成立”：
#   条件成立 -> 没有额外输出，继续执行
#   条件失败 -> 抛出 AssertionError，脚本停在失败的那一行 ,
#   *( 目的让python 进行自我检查,日常可以不写)
assert a + b == 3
assert grade(95) == "A" and grade(70) == "B" and grade(30) == "C"
# 这里用 is None 检查前面那次 print 的返回值。
assert return_value is None
assert written_count == 7
assert argv is sys.argv              # 导入的是同一个列表对象，不是副本
assert path is sys.path
assert kw.iskeyword("def") is True
# isinstance(值, 类型) 返回 True 或 False；这里检查脚本路径是否为字符串。
assert isinstance(script_path, str)

# 【补充】【进阶】检查空格和换行时，先把输出收进内存，再比较完整文本。
import contextlib
import io


# captured(action) 接收一个函数。action() 在指定位置调用它，类似 JS 的回调。
def captured(action):
    # io.StringIO() 创建一个空的内存文本流，用来收集本来要打印到终端的文字。
    buffer = io.StringIO()
    # with contextlib.redirect_stdout(buffer): 让缩进块里的输出写入 buffer，离开块时恢复。
    with contextlib.redirect_stdout(buffer):
        action()
    # buffer.getvalue() 取出至今写入的全部文字，空格和换行也会保留。
    return buffer.getvalue()


# lambda: 表达式 创建无参数函数，类似 JS 的 () => 表达式。传给 captured 时先不执行；
# 等 action() 调用它才打印。第一条断言因此能检查到两个字母中间的空格和末尾的换行。
assert captured(lambda: print("a", "b")) == "a b\n"
assert captured(lambda: print("a", "b", sep=" | ")) == "a | b\n"
assert captured(lambda: print("a", end=" ")) == "a "
assert captured(lambda: print()) == "\n"
assert captured(lambda: print(print("x"))) == "x\nNone\n"

# with ... as buffer 把这里用于接收输出的文本流命名为 buffer，方便稍后取回写入的内容。
with contextlib.redirect_stdout(io.StringIO()) as buffer:
    written = sys.stdout.write("runoob\n")
assert written == 7 and buffer.getvalue() == "runoob\n"

print("demo_io_import: all passed")
