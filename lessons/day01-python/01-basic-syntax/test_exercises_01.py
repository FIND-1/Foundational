"""第 1 章练习的自动测试。不要修改本文件，要让测试通过，请完善 exercises_01.py。

运行（项目根目录）：python -m pytest lessons/day01-python/01-basic-syntax -v
"""

import pytest

from exercises_01 import (
    describe_number,
    every_other,
    is_palindrome,
    is_valid_name,
    print_row,
    strip_brackets,
)


# ── 练习 1 ────────────────────────────────────────────────────────────
@pytest.mark.parametrize("name", ["user_name", "_total", "姓名", "count2"])
def test_valid_names(name):
    assert is_valid_name(name) is True


@pytest.mark.parametrize("name", ["2nd", "user-name", "$price", "class", "True", ""])
def test_invalid_names(name):
    assert is_valid_name(name) is False


# ── 练习 2 ────────────────────────────────────────────────────────────
@pytest.mark.parametrize(("text", "expected"), [("123456789", "2468"), ("ab", "b"), ("a", "")])
def test_every_other(text, expected):
    assert every_other(text) == expected


@pytest.mark.parametrize(("text", "expected"), [("[abc]", "abc"), ("()", "")])
def test_strip_brackets(text, expected):
    assert strip_brackets(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [("level", True), ("上海自来水来自海上", True), ("python", False), ("", True)],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


# ── 练习 3 ────────────────────────────────────────────────────────────
@pytest.mark.parametrize(("n", "expected"), [(5, "positive"), (-0.5, "negative"), (0, "zero")])
def test_describe_number(n, expected):
    assert describe_number(n) == expected


# ── 练习 4 ────────────────────────────────────────────────────────────
def test_print_row(capsys):
    print_row(1, 2, 3)
    assert capsys.readouterr().out == "1 | 2 | 3"
