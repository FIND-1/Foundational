"""第 3 章示例的自检。学习者的练习由 test_exercises_03.py 单独验收。"""

from ast import literal_eval
import importlib.util
from pathlib import Path

import pytest

_DIR = Path(__file__).parent


def _load_demo(filename):
    path = _DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


implicit = _load_demo("01_implicit_demo.py")
numbers_str = _load_demo("02_numbers_str_demo.py")
containers = _load_demo("03_containers_demo.py")
chars_bytes = _load_demo("04_chars_bytes_demo.py")
errors_parse = _load_demo("05_errors_parse_demo.py")


def test_implicit_conversion():
    assert implicit.num_new == 124.23 and type(implicit.num_new) is float
    assert type(implicit.num_int) is int and type(implicit.integer) is int
    assert implicit.result == 124.25 and type(implicit.result) is float
    with pytest.raises(TypeError):
        _ = implicit.num_int + implicit.num_str


def test_explicit_numbers_and_strings():
    assert (numbers_str.x_int, numbers_str.y_int, numbers_str.z_int) == (1, 2, 3)
    assert (numbers_str.x_flt, numbers_str.y_flt, numbers_str.z_flt, numbers_str.w_flt) == (1.0, 2.8, 3.0, 4.2)
    assert (numbers_str.x_str, numbers_str.y_str, numbers_str.z_str) == ("s1", "2", "3.0")
    assert numbers_str.num_sum == 579 and type(numbers_str.num_sum) is int
    assert numbers_str.quantity_text == "0456" and numbers_str.quantity == 456
    assert (int(3.9), int(-3.9), int(float("3.5"))) == (3, -3, 3)
    assert repr("hello") == "'hello'" and ascii("雨") == r"'\u96e8'"
    assert bool("False") is True and (numbers_str.flag_text.lower() == "true") is False
    assert (int("101", 2), int("ff", 16), int("0xff", 0)) == (5, 255, 255)
    assert (bin(10), oct(10), hex(10)) == ("0b1010", "0o12", "0xa")


def test_containers_conversion():
    assert containers.chars_list == ["a", "b", "c"]
    assert containers.chars_tuple == ("a", "b", "c")
    assert containers.chars_set == {"a", "b"}
    assert len(containers.unique) == 3 and containers.numbers == [1, 2, 2, 3]
    assert containers.frozen_numbers == frozenset({1, 2, 3})
    assert containers.a == containers.b == frozenset({1, 2})
    assert containers.mapping[containers.a] == "第一组数据"
    assert containers.mapping[containers.b] == "第一组数据"
    assert containers.person == {"name": "Rain", "age": 18}
    assert containers.overwritten == {"a": 9, "b": 2}
    assert list(containers.person) == ["name", "age"]
    assert list(containers.person.items()) == [("name", "Rain"), ("age", 18)]
    with pytest.raises(TypeError):
        _ = set([[1, 2]])
    with pytest.raises(ValueError):
        _ = dict([("a", 1, 2)])


def test_chars_bytes_and_memoryview():
    assert chr(65) == "A" and ord("A") == 65 and chr(ord("雨")) == "雨"
    assert (len(chars_bytes.text), len(chars_bytes.data)) == (2, 6)
    assert chars_bytes.data.decode("utf-8") == "你好"
    assert chars_bytes.immutable == b"AB"
    assert chars_bytes.frozen_bytes == b"AC"
    assert chars_bytes.mutable == bytearray(b"DC")
    with pytest.raises(ValueError):
        _ = bytes([256])
    with pytest.raises(TypeError):
        _ = memoryview("AB")


def test_errors_and_literal_eval():
    assert errors_parse.parsed_values == [12]
    assert errors_parse.eval_result == 3
    assert errors_parse.values == [1, 2, 3]
    with pytest.raises(ValueError):
        _ = int("3.5")
    with pytest.raises(TypeError):
        _ = int(None)
    with pytest.raises(ValueError):
        _ = literal_eval("1 + 2")
