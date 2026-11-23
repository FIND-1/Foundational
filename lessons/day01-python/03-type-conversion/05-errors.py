"""第 3 章 · 观察转换失败后的异常处理。

在仓库根目录执行：./.venv/Scripts/python.exe lessons/day01-python/03-type-conversion/05-errors.py
观察字符串 12 解析成功、3.5 和 abc 进入错误分支，以及列表字面量解析后的类型。
"""

# 【补充】【进阶】try / except / else 的读法见第 1 章 01_syntax_demo.py 的缩进报错示例。
from ast import literal_eval  # 从标准库 ast 导入字面量解析函数

# for 依次取三个字符串，在缩进块中分别尝试转换。只有 int(value) 引发的 ValueError 进入 except。
for value in ("12", "3.5", "abc"):
    try:
        converted = int(value)
    except ValueError:
        # f-string 中的 !r 采用 repr(value) 的表示形式，输出会带上原字符串的引号。
        print(f"{value!r} 不是有效的整数字符串")
    else:
        print(f"{value!r} 转成整数：{converted}")

try:
    int(None)
except TypeError:
    print("None 的类型不能直接转换成整数")

# literal_eval(文本) 解析 Python 字面量。这里得到整数列表；对下面的加法表达式会抛出 ValueError。
values = literal_eval("[1, 2, 3]")
print("解析列表字面量：", values, type(values))

try:
    literal_eval("1 + 2")
except ValueError:
    print("算术表达式不是可接受的字面量")
