"""第 1 章练习。

做法：把每道题中的 `raise NotImplementedError` 换成你自己的实现，然后在项目根目录运行：
    python -m pytest lessons/day01-python/01-basic-syntax
测试代码在 test_exercises_01.py 中，不要修改它。仍未完成的题会显示为 SKIPPED（未完成）。
"""

import keyword  # 练习 1 会用到


# ── 练习 1：合法变量名 ────────────────────────────────────────────────
def is_valid_name(name):
    """当 name 可以作为变量名时返回 True：符合标识符规则，并且不是关键字。

    提示：参考 demo_syntax.py 中的 str.isidentifier() 和 keyword.iskeyword()。
    """
    raise NotImplementedError


# ── 练习 2：切片 ──────────────────────────────────────────────────────
def every_other(s):
    """从下标 1 开始，每隔一个字符取一个。例如 '123456789' -> '2468'。只用一次切片。"""
    raise NotImplementedError


def strip_brackets(s):
    """去掉首尾各一个字符。例如 '[abc]' -> 'abc'。只用一次切片。"""
    raise NotImplementedError


def is_palindrome(s):
    """判断 s 是否是回文（正着读和反着读一样）。例如 'level' -> True。不用循环。"""
    raise NotImplementedError


# ── 练习 3：if / elif / else ──────────────────────────────────────────
def describe_number(n):
    """n > 0 返回 'positive'，n < 0 返回 'negative'，n == 0 返回 'zero'。"""
    raise NotImplementedError


# ── 练习 4：print 的 sep 和 end ───────────────────────────────────────
def print_row(a, b, c):
    """调用一次 print，在终端输出 'a | b | c'，并且末尾不换行。

    例如 print_row(1, 2, 3) 输出 '1 | 2 | 3'。提示：sep 和 end 参数。
    """
    raise NotImplementedError
