"""第 1 章 · 语法骨架：编码、标识符、关键字、注释、缩进、多行语句、代码组。

运行：python .\\lessons\\day01-python\\01-basic-syntax\\demo_syntax.py
所有 assert 通过时只打印最后一行；修改任意结论再运行，看看哪里会报错。
"""

import keyword

# ── 编码 ──────────────────────────────────────────────────────────────
# Python 3 源文件默认是 UTF-8，和写 JS 文件一样，直接写中文即可。
# `# -*- coding: xxx -*-` 只有在文件不是 UTF-8 时才需要，实际几乎用不到。


# ── 标识符 ────────────────────────────────────────────────────────────
# 规则和 JS 基本相同：字母或下划线开头，后面可以跟字母、数字、下划线，区分大小写。
# 和 JS 的区别：不允许使用 `$`。
# str.isidentifier() 用来检查名字是否符合标识符规则（原教程用 exec 判断，不安全）。
assert "user_name".isidentifier()
assert "_total".isidentifier()
assert "姓名".isidentifier()             # 支持 Unicode，但项目里建议只用英文
assert not "2nd_place".isidentifier()    # 不能以数字开头
assert not "user-name".isidentifier()    # 不能包含连字符
assert not "$price".isidentifier()       # 在 JS 中合法，在 Python 中非法

count, Count = 1, 2                      # 区分大小写：这是两个不同的变量
assert count != Count

# isidentifier() 不会检查关键字，要和 keyword.iskeyword() 一起使用
assert "class".isidentifier() and keyword.iskeyword("class")

# 命名风格（PEP 8）与 JS 不同：
#   变量和函数用 snake_case（JS 用 camelCase）  ->  user_name、calculate_area()
#   类用 PascalCase（与 JS 相同）               ->  StudentInfo
#   常量用全大写（这只是约定，语言不会阻止修改） ->  MAX_SIZE = 1024
#   _name   以下划线开头表示“内部使用”（只是约定，JS 的 #private 是强制的）
#   __name  在类中会触发名称改写（name mangling），学到类时再展开


# ── 关键字 ────────────────────────────────────────────────────────────
# Python 3.11 共有 35 个关键字。True、False、None 首字母大写，对应 JS 的 true、false、null。
assert len(keyword.kwlist) == 35
assert "True" in keyword.kwlist and "true" not in keyword.kwlist
# JS 运算符在 Python 中对应关键字：&& -> and，|| -> or，! -> not，else if -> elif
assert {"and", "or", "not", "elif"} <= set(keyword.kwlist)
# 软关键字只在特定语法中有特殊含义，平时可以当变量名使用（例如 match、case）
assert "match" in keyword.softkwlist and not keyword.iskeyword("match")


# ── 注释 ──────────────────────────────────────────────────────────────
# Python 只有 # 单行注释，没有 // 和 /* */。
# 三引号 '''...''' 或 """...""" 本质上是字符串，不是注释；
# 放在模块、函数或类的第一行时，它会成为 docstring（作用类似 JSDoc），可以在运行时读取：
assert __doc__.startswith("第 1 章")


# ── 行与缩进 ──────────────────────────────────────────────────────────
# 用 `:` + 缩进代替 JS 的 `{}`；同一代码块的缩进必须一致，PEP 8 约定使用 4 个空格。
x = 10
if x > 5:
    size = "big"
else:
    size = "small"
assert size == "big"

# 空代码块必须写 pass（JS 可以直接写 {}）
if x < 0:
    pass

# 缩进不一致会在编译阶段报错，整个文件都无法运行。
# 所以这里用 compile() 只编译一段错误代码，不影响本文件运行：
bad_code = "if True:\n    a = 1\n  b = 2\n"
try:
    compile(bad_code, "<bad>", "exec")
except IndentationError as error:
    assert "unindent does not match" in error.msg
else:
    raise AssertionError("这里应当抛出 IndentationError")


# ── 多行语句 ──────────────────────────────────────────────────────────
# Python 以换行作为语句结束，不需要分号，也不存在 JS 的自动分号插入（ASI）问题。
# 写长表达式时可以用反斜杠续行：
total = 1 + \
        2 + \
        3
assert total == 6

# 更推荐用括号续行（PEP 8 的建议）：() [] {} 内部可以直接换行
total = (1 +
         2 +
         3)
items = ["item_one", "item_two",
         "item_three"]
assert total == 6 and len(items) == 3

# 一行写多条语句可以用分号分隔，但不推荐
a = 1; b = 2
assert a + b == 3


# ── 代码组（子句） ────────────────────────────────────────────────────
# if、while、def、class 等复合语句的首行以关键字开头、以冒号结尾，
# 后面缩进的代码就是它的“代码组”；首行加上代码组合称一个子句（clause）。
# def 定义函数（相当于 JS 的 function），return 返回结果。
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:          # JS 写 else if，Python 写 elif
        return "B"
    else:
        return "C"


assert grade(95) == "A" and grade(70) == "B" and grade(30) == "C"

# ── 空行 ──────────────────────────────────────────────────────────────
# 空行不是语法，只用来增强可读性。PEP 8 约定：顶层函数和类之间空两行，
# 类中的方法之间空一行（上面 grade 前后的两个空行就是这个约定）。

print("demo_syntax: all passed")
