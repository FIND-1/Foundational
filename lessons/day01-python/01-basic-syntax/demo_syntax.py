"""第 1 章 · 语法骨架：编码、标识符、关键字、注释、缩进与多行语句。

用途：直观演示第 1 章的语法规则与 Python / JS 差异。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/01-basic-syntax/demo_syntax.py
预期结果：变量 count 和 Count 分别打印 1 和 2，缩进代码块打印 big，两种续行都得到 6。末尾演示缩进错误的提示。
"""

# print(...) 把括号里的值写到终端；字符串用引号包住，变量用 = 绑定到值。
# import 把模块载入当前文件，随后可用“模块名.名称”读取它提供的内容。
import keyword

# ── 1. 编码 ───────────────────────────────────────────────────────────
# Python 3 源文件默认是 UTF-8，和写 JS 文件一样，直接写中文即可。
# `# -*- coding: cp-1252 -*-` 只有在文件不是 UTF-8 时才需要，实际几乎用不到。


# ── 2. 标识符 ─────────────────────────────────────────────────────────
# 规则和 JS 基本相同：字母或下划线开头，后面可以跟字母、数字、下划线，区分大小写。
# 【补充】和 JS 的区别：不允许使用 `$`。
# text.isidentifier()：点号前的 text 是要检查的字符串，空括号表示不用额外传参数。
# 拼写符合标识符规则返回 True，否则返回 False。例如 "2nd_place" 以数字开头，结果为 False。
valid_name = "user_name"
invalid_digit = "2nd_place"
invalid_dollar = "$price"
chinese_name = "姓名"

print("标识符检查：", valid_name.isidentifier(), invalid_digit.isidentifier(), invalid_dollar.isidentifier())
print("中文标识符：", chinese_name.isidentifier())

count = 1
Count = 2                              # 区分大小写：这是两个不同的变量
print("区分大小写：", count, Count)

# keyword.iskeyword(word)：把单词传给 keyword 模块，属于保留关键字时返回 True。
# 下面的 "class" 拼写合规，同时也是关键字，所以两次检查都会打印 True。
word = "class"
print("class 符合标识符拼写规则吗？", word.isidentifier(), "是关键字吗？", keyword.iskeyword(word))

# 【补充】命名风格（PEP 8: 是 Python 的官方代码风格规范）与 JS 不同：
#   变量和函数用 snake_case（JS 用 camelCase）  ->  user_name、calculate_area()
#   类用 PascalCase（与 JS 相同）               ->  StudentInfo
#   常量用全大写（只是约定，语言不会阻止修改）   ->  MAX_SIZE = 1024
#   _name   以下划线开头表示“内部使用”（只是约定，JS 的 #private 是强制的）
#   __name  在类中会触发名称改写，学到类时再展开。


# ── 3. 关键字 ─────────────────────────────────────────────────────────
# Python 3.11 共有 35 个关键字。True、False、None 首字母大写，对应 JS 的 true、false、null。
# kwlist 是关键字列表；len(...) 统计项数，[:6] 取最前面的六项。
kw_count = len(keyword.kwlist)
print("关键字总数：", kw_count)
print("前 6 个关键字：", keyword.kwlist[:6])

# JS 运算符在 Python 中的关键字对应：&& -> and，|| -> or，! -> not，else if -> elif
# keyword.softkwlist 保存软关键字列表（如 match、case）。它们只在特定语法中生效。
print("软关键字：", keyword.softkwlist)


# ── 4. 注释 ───────────────────────────────────────────────────────────
# Python 只有 # 单行注释，没有 // 和 /* */。
# 三引号 '''...''' 或 """...""" 本质上是字符串；放在模块、函数或类第一行时会成为 docstring（类似 JSDoc）。
# __doc__ 是文件开头的说明文字。先用 text.splitlines() 把文字按行拆成列表，
# 再用 [0] 取列表第一项，所以这里仅打印说明的第一行。
print("本文件 docstring 开头：", __doc__.splitlines()[0])


# ── 5. 行与缩进 ───────────────────────────────────────────────────────
# if 在条件为 True 时执行缩进块，其他情况执行 else 的缩进块。
# 用 `:` + 缩进代替 JS 的 `{}`；同一代码块的缩进必须一致，PEP 8 约定使用 4 个空格。
x = 10
if x > 5:
    size = "big"
else:
    size = "small"
print("缩进代码块结果：", size)

# pass 是一条什么都不做的语句，写在缩进块里可以给空分支占位。JS 可以直接写 {}。
if x < 0:
    pass


# ── 6. 多行语句 ───────────────────────────────────────────────────────
# Python 以换行作为语句结束，不需要分号，也不存在 JS 的自动分号插入（ASI）问题。
# 方式 A：反斜杠续行
total_slash = 1 + \
              2 + \
              3

# 方式 B：括号内自然换行（推荐，PEP 8 建议）
total_paren = (1 +
               2 +
               3)
# [元素, 元素, ...] 创建有序列表，类似 JS 数组；下面这个列表有三个字符串。
items = ["item_one", "item_two",
         "item_three"]
print("多行求和：", total_slash, total_paren, "列表长度：", len(items))

# 【补充】【进阶】in 和 not in 检查列表里有没有某一项，and 要求两边都成立。
print("只有首字母大写的 True 是关键字：", "True" in keyword.kwlist and "true" not in keyword.kwlist)
# text.startswith(prefix) 返回文本是否以指定前缀开头，类似 JS 的 startsWith。
print("文档说明以「第 1 章」开头：", __doc__.startswith("第 1 章"))
# {值, 值, ...} 写出集合，set(列表) 把列表转成集合。<= 检查左边每一项都在右边。
print("这四个关键字都在列表中：", {"and", "or", "not", "elif"} <= set(keyword.kwlist))

# ── 【进阶】用 compile() 与 try/except 验证缩进报错 ───────────────────
# 缩进错误会在编译阶段直接卡住整个文件，所以用字符串 + compile() 单独编译演示。
bad_code = "if True:\n    a = 1\n  b = 2\n"  # 第 3 行只有 2 个空格，既不对齐 a=1 也没退回顶格
bad_code = "if True:\n    a = 1\n  b = 2\n"
bad_code = "if True:\n    a = 1\n  b = 2\n" 
# python 变量不用 let / const 声明，每次写 bad_code = ... 都是用新值覆盖旧值（相当于 JS 里对 let 变量反复重新赋值），写再多遍也不会报错，最终只保留最后一次的值
# try/except 类似 JS 的 try/catch；只编译不运行，没报错才会走 else
try:
    compile(bad_code, "<bad>", "exec")
except IndentationError as error:
    print("【进阶】成功捕获缩进错误：", error.msg)
else:
    print("【进阶】这段代码缩进正确，可以编译。")
