"""第 2 章练习的自动测试。不要修改本文件，要让测试通过，请完善 exercises_02.py。

运行基础练习：./.venv/Scripts/python.exe -m pytest lessons/day01-python/02-basic-data-types -m basic -v
运行全部练习：./.venv/Scripts/python.exe -m pytest lessons/day01-python/02-basic-data-types -v
"""

from io import StringIO
import runpy
import sys

import pytest

import exercises_02
from exercises_02 import (
    common_sorted,
    count_unique,
    is_strict_int,
    last_word,
    squares_dict,
    utf8_size,
)


# 每个变量单列一项，空着上一项也能看到下一项的结果。
@pytest.mark.basic
@pytest.mark.parametrize(("name", "expected"), [
    ("minutes", 2), ("seconds", 5), ("half", 62.5),
    ("bool_is_int", True), ("bool_exact_int", False),
    ("first_last", "Rb"), ("repeated_word", "RunoobRunoob"),
    ("empty_list_truth", False), ("false_text_truth", True),
    ("fruit_count", 3), ("odd_numbers", [1, 3, 5]), ("single", (20,)),
    ("common", {2, 3}), ("only_in_a", {1}), ("empty_set", set()),
    ("person_name", "Rain"), ("person_job", "未填写"),
    ("encoded", b"\xe4\xbd\xa0\xe5\xa5\xbd"), ("byte_count", 6), ("first_byte", 104),
])
def test_basic_value(name, expected):
    value = getattr(exercises_02, name)
    if value is Ellipsis:
        pytest.skip(f"未完成：{name} 仍为 ...")
    assert type(value) is type(expected)
    assert value == expected


@pytest.mark.basic
def test_basic_fruits_modified():
    fruits = exercises_02.fruits
    if fruits[0] is Ellipsis:
        pytest.skip("未完成：fruits[0] 仍为 ...")
    assert fruits == ["桃子", "香蕉", "梨"]


@pytest.mark.basic
@pytest.mark.parametrize(("typed", "expected"), [
    ("hello", "5\n5\n"), ("你好", "2\n6\n"), ("", "0\n0\n"),
])
def test_basic_terminal(typed, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", StringIO(typed + "\n"))
    runpy.run_path(exercises_02.__file__, run_name="__main__")
    assert capsys.readouterr().out == expected


# ══════════════════════════════ 进阶练习测试（可选） ══════════════════════════════
@pytest.mark.advanced
@pytest.mark.parametrize(("value", "expected"), [
    (5, True), (-3, True), (True, False), (3.0, False), ("5", False),
])
def test_adv_is_strict_int(value, expected):
    assert is_strict_int(value) is expected


@pytest.mark.advanced
@pytest.mark.parametrize(("items", "expected"), [([1, 1, 2], 2), ([], 0), (["a", "b", "a"], 2)])
def test_adv_count_unique(items, expected):
    assert count_unique(items) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("first", "second", "expected"), [
    ([3, 1, 2, 2], [2, 3, 4], [2, 3]), ([1], [2], []), (["b", "a"], ["a", "b"], ["a", "b"]),
])
def test_adv_common_sorted(first, second, expected):
    assert common_sorted(first, second) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("text", "expected"), [
    ("I like runoob", "runoob"), ("Python", "Python"), ("a  b  ", "b"),
])
def test_adv_last_word(text, expected):
    assert last_word(text) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("text", "expected"), [("A你", 4), ("", 0), ("hello", 5)])
def test_adv_utf8_size(text, expected):
    assert utf8_size(text) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("numbers", "expected"), [
    ((2, 4), {2: 4, 4: 16}), ([3], {3: 9}), ((), {}),
])
def test_adv_squares_dict(numbers, expected):
    assert squares_dict(numbers) == expected
