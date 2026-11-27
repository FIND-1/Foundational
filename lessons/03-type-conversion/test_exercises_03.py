"""第 3 章练习的自动测试。不要修改本文件，要让测试通过，请完善 exercises_03.py。"""

from io import StringIO
import runpy
import sys

import pytest

import exercises_03
from exercises_03 import (
    codes_to_text,
    pairs_to_dict_keys,
    parse_based_int,
    parse_bool_text,
    parse_int_safe,
    parse_literal_safe,
)


# 每个变量单列一项，空着上一项也能看到下一项的结果；同时校验精确类型。
@pytest.mark.basic
@pytest.mark.parametrize(("name", "expected"), [
    ("implicit_sum", 124.25), ("explicit_sum", 15), ("joined_text", "123"),
    ("truncated", -3), ("as_float", 3.5), ("as_int", 3),
    ("flag_bool", True), ("flag_is_true", False),
    ("from_bin", 5), ("from_hex", 255), ("as_bin", "0b1010"), ("as_hex", "0xa"),
    ("letters_tuple", ("a", "b", "c")), ("unique_count", 3),
    ("person_dict", {"name": "Rain", "age": 18}), ("person_keys", ["name", "age"]),
    ("char_a", "A"), ("rain_code", 38632), ("as_bytes", b"AB"),
])
def test_basic_value(name, expected):
    value = getattr(exercises_03, name)
    if value is Ellipsis:
        pytest.skip(f"未完成：{name} 仍为 ...")
    assert type(value) is type(expected)
    assert value == expected


@pytest.mark.basic
def test_basic_originals_unchanged():
    if exercises_03.explicit_sum is Ellipsis and exercises_03.unique_count is Ellipsis:
        pytest.skip("未完成：待完成基础题 1 或题 4 后验证原变量未变")
    assert type(exercises_03.base_int) is int and exercises_03.base_int == 123
    assert type(exercises_03.num_text) is str and exercises_03.num_text == "12"
    assert exercises_03.raw_nums == [1, 2, 2, 3]


@pytest.mark.basic
@pytest.mark.parametrize(("typed", "expected"), [
    ("12\n3\n", "15\n<class 'int'>\n"),
    ("-5\n20\n", "15\n<class 'int'>\n"),
    ("0456\n4\n", "460\n<class 'int'>\n"),
])
def test_basic_terminal(typed, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", StringIO(typed))
    runpy.run_path(exercises_03.__file__, run_name="__main__")
    assert capsys.readouterr().out == expected


# ══════════════════════════════ 进阶练习测试（可选） ══════════════════════════════
@pytest.mark.advanced
@pytest.mark.parametrize(("value", "default", "expected"), [
    ("42", None, 42),
    (-3.9, 0, -3),
    ("3.5", 0, 0),
    ("abc", -1, -1),
    (None, "invalid", "invalid"),
])
def test_adv_parse_int_safe(value, default, expected):
    result = parse_int_safe(value, default)
    assert type(result) is type(expected)
    assert result == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("text", "expected"), [
    ("true", True),
    ("TRUE", True),
    ("False", False),
    ("FALSE", False),
    ("yes", None),
    ("", None),
])
def test_adv_parse_bool_text(text, expected):
    assert parse_bool_text(text) is expected


@pytest.mark.advanced
def test_adv_parse_based_int():
    assert parse_based_int("42") == 42
    assert parse_based_int("101", 2) == 5
    assert parse_based_int("ff", 16) == 255
    assert parse_based_int("0o17", 0) == 15


@pytest.mark.advanced
@pytest.mark.parametrize(("pairs", "expected"), [
    ([("a", 1), ("b", 2), ("a", 3)], ["a", "b"]),
    ([], []),
    ([("name", "Rain"), ("age", 18)], ["name", "age"]),
])
def test_adv_pairs_to_dict_keys(pairs, expected):
    assert pairs_to_dict_keys(pairs) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("codes", "expected"), [
    ([65, 66, 67], "ABC"),
    ([228, 189, 160], "你"),
    ([], ""),
])
def test_adv_codes_to_text(codes, expected):
    assert codes_to_text(codes) == expected


@pytest.mark.advanced
@pytest.mark.parametrize(("text", "default", "expected"), [
    ("[1, 2, 3]", None, [1, 2, 3]),
    ("{'a': 1, 'ok': True}", None, {"a": 1, "ok": True}),
    ("(1, 'x')", None, (1, "x")),
    ("1 + 2", None, None),
    ("[1,", "bad", "bad"),
])
def test_adv_parse_literal_safe(text, default, expected):
    assert parse_literal_safe(text, default) == expected
