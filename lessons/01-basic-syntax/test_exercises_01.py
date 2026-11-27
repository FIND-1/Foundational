"""第 1 章练习的自动测试。不要修改本文件，要让测试通过，请完善 exercises_01.py。"""

from io import StringIO
import runpy
import sys

import pytest

import exercises_01
from exercises_01 import (
    describe_number,
    every_other,
    is_palindrome,
    is_valid_name,
    print_row,
    strip_brackets,
)


# 每个变量单列一项，空着上一项也能看到下一项的错误。
@pytest.mark.basic
@pytest.mark.parametrize(("name", "expected"), [
    ("can_use_user_name", True), ("can_use_2nd", False),
    ("can_use_dollar", False), ("can_use_class", False),
    ("every_other_char", "2468"), ("inner_text", "Python"),
    ("reversed_text", "987654321"), ("floor_neg", -4),
    ("win_path", "C:\\new\\test"), ("joined_age", "age=18"),
])
def test_basic_value(name, expected):
    value = getattr(exercises_01, name)
    if value is Ellipsis:
        pytest.skip(f"未完成：{name} 仍为 ...")
    assert type(value) is type(expected)
    assert value == expected


@pytest.mark.basic
@pytest.mark.parametrize(("typed", "expected"), [
    ("Ada", "Ada\n"), ("小雨", "小雨\n"), ("", "访客\n"),
])
def test_basic_terminal(typed, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", StringIO(typed + "\n"))
    runpy.run_path(exercises_01.__file__, run_name="__main__")
    assert capsys.readouterr().out == expected


# ══════════════════════════════ 进阶练习测试（可选） ══════════════════════════════
@pytest.mark.advanced
@pytest.mark.parametrize("name", ["user_name", "_total", "姓名", "count2"])
def test_adv_valid_names(name):
    assert is_valid_name(name) is True


@pytest.mark.advanced
@pytest.mark.parametrize("name", ["2nd", "user-name", "$price", "class", "True", ""])
def test_adv_invalid_names(name):
    assert is_valid_name(name) is False


@pytest.mark.advanced
@pytest.mark.parametrize(("text", "expected"), [("123456789", "2468"), ("ab", "b"), ("a", "")])
def test_adv_every_other(text, expected):
    assert every_other(text) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("text", "expected"), [("[abc]", "abc"), ("()", "")])
def test_adv_strip_brackets(text, expected):
    assert strip_brackets(text) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(
    ("text", "expected"),
    [("level", True), ("上海自来水来自海上", True), ("python", False), ("", True)],
)
def test_adv_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.advanced
@pytest.mark.parametrize(("n", "expected"), [(5, "positive"), (-0.5, "negative"), (0, "zero")])
def test_adv_describe_number(n, expected):
    assert describe_number(n) == expected


@pytest.mark.advanced
def test_adv_print_row(capsys):
    print_row(1, 2, 3)
    assert capsys.readouterr().out == "1 | 2 | 3"
