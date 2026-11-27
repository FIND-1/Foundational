"""第 1 章 · 输入输出、导入、命令行参数。

用途：演示 print 参数、input() 输入、import 导入方式以及 sys.argv 命令行参数。
在仓库根目录运行（PowerShell 提示符已显示 (.venv)）：
  基础运行：python lessons/01-basic-syntax/03_io_import_demo.py
  带参数运行：python lessons/01-basic-syntax/03_io_import_demo.py Rain 123
  体验 input：python lessons/01-basic-syntax/03_io_import_demo.py --ask
预期结果：输入模式下键入 18 会看到明年为 19；常规输出含 A B C、a | b、写入字符数 7 和命令行参数列表，以及最后一行 `03_io_import_demo: all passed`。
"""

# 注意：sys.argv 是字符串列表，依次保存脚本路径和命令行追加的参数
import sys

# 拓展：空行用于分隔代码段；顶层函数/类之间空两行，类内方法之间空一行

# ── input 输入 ─────────────────────────────────────────────────────
# 格式：input(提示语) -> str（等待回车，返回去掉行尾换行的字符串）
# 注意：即使输入数字 18，返回的仍是 str，参与加法前需用 int(文本) 转换
# 拓展：in 检查成员类似 JS 的 args.includes("--ask")；带 --ask 参数运行才会触发询问
if "--ask" in sys.argv:
    age_text = input("你的年龄：")
    print("input 返回的类型：", type(age_text))
    next_year = int(age_text) + 1
    print("明年：", next_year)


# 格式：语句1; 语句2 -> 分号可把两条语句写在同一行
# 场景：普通脚本推荐每行一条语句，方便阅读和逐行打断点
a = 1; b = 2
print("同行分号：", a + b)
a = 1
b = 2


# ── 代码组（子句） ───────────────────────────────────────────
# 格式：def 函数名(参数): 缩进块 -> 定义函数（类似 JS 的 function grade(score)）
# 注意：if / elif / else 首行以冒号结尾，缩进块称为代码组；遇到 return 立即返回结果
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:                  # JS 写 else if，Python 写 elif
        return "B"
    else:
        return "C"


print("代码组函数结果：", grade(95), grade(70), grade(30))


# ── print 输出 ─────────────────────────────────────────────────────
# 格式：print(值1, 值2, sep="分隔符", end="结尾符") -> None
# 注意：默认 sep=" "（空格分隔）、end="\n"（末尾换行）；返回值固定是 None（类似 JS 的 undefined）
first = "a"
second = "b"

print(first, second)                 # 默认空格分隔，末尾换行 -> a b
print(first, second, sep=" | ")      # 修改分隔符 -> a | b

# 场景：把 end 改成空格或空串可实现不换行输出
print(first, end=" ")
print(second, end=" ")
print()                              # 空 print() 只输出一个换行

return_value = print("测试返回值")
print("print() 的返回值是：", return_value)

# 拓展：sys.stdout.write(文本) -> int（原样写入终端并返回字符数；"runoob\n" 共 7 个字符）
text = "runoob\n"
written_count = sys.stdout.write(text)
print("写入字符数：", written_count)


# ── import 与 from...import ────────────────────────────────────────
# 格式：from 模块 import 名称1, 名称2；import 模块 as 别名（与 ES Module 对照见下）
#   import sys                 ≈ import * as sys from "sys"
#   from sys import argv, path ≈ import { argv, path } from "sys"
#   import keyword as kw       ≈ import * as kw from "keyword"
# 注意：不推荐 from sys import *（会把所有公开名称灌进当前文件）；模块和 ESM 一样会缓存，只执行一次
from sys import argv, path
import keyword as kw

print("keyword.iskeyword('def') =", kw.iskeyword("def"))


# ── 命令行参数 ─────────────────────────────────────────────────────
# 格式：sys.argv[0] 是脚本路径，sys.argv[1:] 是用户传入的参数列表
# 注意：比 Node.js 的 process.argv 少了最前面的 node 路径
# 拓展：复杂命令行参数通常用标准库 argparse（类似 Node 的 commander / yargs）；python -h 可查解释器选项
script_path = sys.argv[0]
user_args = sys.argv[1:]

print("当前脚本：", script_path)
print("命令行参数：", user_args)


# ── 拓展：断言与输出捕获验证 ─────────────────────────────────────────
# 格式：assert 条件 -> 条件为 True 继续执行，为 False 抛出 AssertionError
# 注意：== 比较值；is 比较是否同一对象（判断 None 用 is None）；isinstance(值, 类型) 检查类型
assert a + b == 3
assert grade(95) == "A" and grade(70) == "B" and grade(30) == "C"
assert return_value is None
assert written_count == 7
assert argv is sys.argv              # 导入的是同一个列表对象，不是副本
assert path is sys.path
assert kw.iskeyword("def") is True
assert isinstance(script_path, str)

# 拓展：用 io.StringIO 和 redirect_stdout 把终端输出暂存到内存，便于精确校验空格与换行
import contextlib
import io


# 格式：def captured(回调函数): -> 把 action() 期间的 print 输出作为字符串返回
def captured(action):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        action()
    return buffer.getvalue()


# 格式：lambda: 表达式 -> 无参匿名函数（类似 JS 的 () => 表达式），传给 captured 时先不执行
assert captured(lambda: print("a", "b")) == "a b\n"
assert captured(lambda: print("a", "b", sep=" | ")) == "a | b\n"
assert captured(lambda: print("a", end=" ")) == "a "
assert captured(lambda: print()) == "\n"
# 注意：嵌套调用从内向外执行——先打印 x，再把内层返回的 None 交给外层打印
assert captured(lambda: print(print("x"))) == "x\nNone\n"

with contextlib.redirect_stdout(io.StringIO()) as buffer:
    written = sys.stdout.write("runoob\n")
assert written == 7 and buffer.getvalue() == "runoob\n"

print("03_io_import_demo: all passed")
