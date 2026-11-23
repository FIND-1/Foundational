"""第 1 章练习（分「基础练习」与「进阶练习」两层）。

做法：
1. 先完成「基础练习」：把题 1～3 的 `...` 改成你的表达式，再写题 4 的缩进块（只用到本章基础语法，不需要 def）。
2. 运行基础测试：./.venv/Scripts/python.exe -m pytest lessons/day01-python/01-basic-syntax -m basic -v
3. 「进阶练习」为可选挑战（需先了解 def / return / if-elif-else），把 `raise NotImplementedError` 换成实现即可。
4. 运行全部测试：./.venv/Scripts/python.exe -m pytest lessons/day01-python/01-basic-syntax -v
注意：不要修改 test_exercises_01.py；未完成的题会显示为 SKIPPED。
"""

import keyword  # 基础题 1 和进阶练习 1 用它检查保留关键字。


# ══════════════════════════════ 一、基础练习（必做） ══════════════════════════════
# `...`（三个半角点）是这里的待填标记，每填一项即可单独验证。

# 基础题 1：判断以下字符串能否作为 Python 变量名（用本章介绍的方法和关键字检查写出布尔表达式）
# 提示：回忆字母/下划线开头、不允许 $、不能是关键字。
can_use_user_name = "user_name".isidentifier() and not keyword.iskeyword("user_name")   # "user_name"  # "user_name"
can_use_2nd  = "2nd".isidentifier() and not keyword.iskeyword("2nd")           # "2nd"
can_use_dollar = "$price".isidentifier() and not keyword.iskeyword("$price")       # "$price"
can_use_class = "class".isidentifier() and not keyword.iskeyword("class")   # "class"

# 基础题 2：字符串切片（请用下方给定变量写出切片表达式，不要直接写死结果字符串）
raw_text = "123456789"
bracketed = "[Python]"

every_other_char =  raw_text[1::2]   # 从 raw_text 下标 1 开始每隔一个字符取一个，应得到 "2468"
inner_text = bracketed[1:-1]         # 去掉 bracketed 首尾各一个字符，应得到 "Python"
reversed_text = raw_text[::-1]     # 反转 raw_text，应得到 "987654321"

# 基础题 3：整除、原始字符串与显式拼接
floor_neg = -7 // 2      # 请写出计算 -7 向下整除 2 的表达式，应得到 -4
win_path = r"C:\new\test"            # 请用原始字符串 r"..." 表示路径 C:\new\test（不发生转义）
age_num = 18
joined_age = "age=" + str(age_num)          # 请用 "age=" 与 str(...) 拼接 age_num，应得到 "age=18"


# 基础题 4：从终端读一行名字，不显示提示语。输入为空时输出「访客」，
# 否则输出读到的名字。只输出一行。自己写 input、if / else 和缩进。
# 【补充】__name__ 是 Python 为当前模块设置的名字。直接运行文件时它等于 "__main__"，
# 所以会进入下面的缩进块；pytest 导入本文件时它是模块名，导入过程会跳过这段交互。
# raise 会抛出异常。模板用 NotImplementedError("练习待完成") 告诉测试这道题还没填写。
# 把入口里整行占位语句替换为你的代码，无须定义函数。
if __name__ == "__main__":
    name = input()
    if name == "":
        print("访客")
    else:
        print(name)


# ══════════════════════════════ 二、进阶练习（可选） ══════════════════════════════
# 前置知识：def 定义函数、return 返回值、if / elif / else 条件判断。
# 若尚未学习函数语法，可先跳过本节，不影响第 1 章基础验收。

def is_valid_name(name):
    """【进阶】当 name 可以作为变量名时返回 True：符合标识符规则，并且不是关键字。

    提示：参考 01_syntax_demo.py 中的 str.isidentifier() 和 keyword.iskeyword()。
    """
    return name.isidentifier() and not keyword.iskeyword(name)
    # 其他等价写法：
    # return name.isidentifier() and name not in keyword.kwlist  # 用 not in 检查关键字列表



def every_other(s):
    """【进阶】从下标 1 开始，每隔一个字符取一个。例如 '123456789' -> '2468'。只用一次切片。"""
    return s[1::2]
    # 其他等价写法：
    # return s[slice(1, None, 2)]                                # slice() 对象写法，等价于 s[1::2]
    # return "".join(s[i] for i in range(1, len(s), 2))          # 生成器表达式 + range 步长


def strip_brackets(s):
    """【进阶】去掉首尾各一个字符。例如 '[abc]' -> 'abc'。只用一次切片。"""
    return s[1:-1]
    # 其他等价写法：
    # return s[slice(1, -1)]                                     # slice() 对象写法，等价于 s[1:-1]


def is_palindrome(s):
    """【进阶】判断 s 是否是回文（正着读和反着读一样）。例如 'level' -> True。不用循环。"""
    return s == s[::-1]
    # 其他等价写法：
    # return s == "".join(reversed(s))                           # 内置 reversed() 反转后再拼接


def describe_number(n):
    """【进阶】n > 0 返回 'positive'，n < 0 返回 'negative'，n == 0 返回 'zero'。"""
    if n > 0:
        return 'positive'
    if  n < 0:
        return 'negative'
    if  n == 0:
        return 'zero'
    # 其他等价写法（无需引入模块）：
    # 1) 常规 if / elif / else：
    # if n > 0:
    #     return "positive"
    # elif n < 0:
    #     return "negative"
    # else:
    #     return "zero"
    
    # 2) Python 3.10+ match-case 模式匹配（带守卫条件 if）：
    # match n:
    #     case x if x > 0: return "positive"
    #     case x if x < 0: return "negative"
    #     case _: return "zero"


def print_row(a, b, c):
    """【进阶】调用一次 print，在终端输出 'a | b | c'，并且末尾不换行。

    例如 print_row(1, 2, 3) 输出 '1 | 2 | 3'。提示：sep 和 end 参数。
    """
    print(a, b, c, sep=" | ", end="")
    # 其他等价写法（无需引入模块）：
    # print(f"{a} | {b} | {c}", end="")                  # f-string（Python 3.6+ 常用）
    # print("{} | {} | {}".format(a, b, c), end="")       # str.format()
    # print(" | ".join(map(str, (a, b, c))), end="")      # 类似 JS 的 [a, b, c].join(" | ")
    # print(f"{a} | {b} | {c}", end="")
    # print("{} | {} | {}".format(a, b, c), end="") 

