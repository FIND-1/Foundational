"""第一章示例的自检。学习者的练习由 test_exercises_01.py 单独验收。"""

import keyword

import pytest

import demo_strings as strings
import demo_syntax as syntax


def test_names_and_keywords():
    assert syntax.valid_name.isidentifier() and "_total".isidentifier()
    assert syntax.chinese_name.isidentifier()
    assert not syntax.invalid_digit.isidentifier() and not syntax.invalid_dollar.isidentifier()
    assert not "user-name".isidentifier()
    assert syntax.count != syntax.Count
    assert syntax.word.isidentifier() and keyword.iskeyword(syntax.word)
    assert syntax.kw_count == 35
    assert "True" in keyword.kwlist and "true" not in keyword.kwlist
    assert {"and", "or", "not", "elif"} <= set(keyword.kwlist)
    assert "match" in keyword.softkwlist and not keyword.iskeyword("match")


def test_blocks_and_continuations():
    assert syntax.__doc__.startswith("第 1 章")
    assert syntax.size == "big"
    assert syntax.total_slash == syntax.total_paren == 6
    assert len(syntax.items) == 3
    with pytest.raises(IndentationError, match="unindent does not match"):
        compile(syntax.bad_code, "<bad>", "exec")


def test_numbers():
    assert type(strings.n_int) is int and type(strings.n_float) is float
    assert type(strings.n_bool) is bool and type(strings.n_complex) is complex
    assert strings.n_sci == 0.03
    assert strings.big_int == 18446744073709551616
    assert 7 / 2 == 3.5 and 7 // 2 == 3 and -7 // 2 == -4
    assert 0.1 + 0.2 != 0.3


def test_string_construction():
    assert 'abc' == "abc" and strings.word == "字符串"
    assert strings.auto_joined == "this is string"
    assert strings.greeting == "hi runoob, 2"
    assert "ab" + "cd" == "abcd" and strings.repeated == "ababab"
    assert strings.explicit_join == "a1"
    assert len(strings.normal_str) == 3
    assert strings.raw_str == "a\\nb" and len(strings.raw_str) == 4


def test_line_breaks():
    assert "第一行\n第二行".count("\n") == 1
    assert strings.paragraph.count("\n") == 2


def test_indexing_and_slicing():
    s = strings.s
    assert s[0] == "1" and s[-1] == "9"
    assert s[0:-1] == "12345678" and s[2:5] == "345" and s[:3] == "123"
    assert s[2:] == "3456789" and s[2:100] == "3456789"
    assert s[1:5:2] == "24" and s[::-1] == "987654321"
    assert type(strings.first_char) is str and len(strings.first_char) == 1


def test_string_errors():
    with pytest.raises(TypeError):
        _ = "a" + 1
    with pytest.raises(IndexError):
        _ = strings.s[100]
    with pytest.raises(TypeError):
        strings.s[0] = "X"
