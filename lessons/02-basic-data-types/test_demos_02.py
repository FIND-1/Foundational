"""第 2 章示例的自检。学习者的练习由 test_exercises_02.py 单独验收。"""

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


numbers = _load_demo("01_numbers_demo.py")
str_bool = _load_demo("02_str_bool_demo.py")
seq = _load_demo("03_list_tuple_demo.py")
mapping = _load_demo("04_set_dict_demo.py")
bytes_demo = _load_demo("05_bytes_demo.py")


def test_assignment():
    assert (numbers.counter, numbers.miles) == (100, 1000.0)
    assert (numbers.a, numbers.b, numbers.c) == (111, 5.5, True)
    assert numbers.name == "Alice" and numbers.is_active is True
    assert type(numbers.value) is str


def test_type_and_isinstance():
    assert type(numbers.d) is complex
    assert isinstance(numbers.child, numbers.A) and type(numbers.child) != numbers.A
    assert type(numbers.parent) is numbers.A
    assert issubclass(bool, int) and True + 1 == 2
    assert numbers.one == True and numbers.one is not True  # noqa: E712
    assert not hasattr(numbers, "var1") and not hasattr(numbers, "var2")


def test_number_literals_and_operators():
    assert (0o17, 0x69, 0b101, -0x260) == (15, 105, 5, -608)
    assert 2 / 4 == 0.5 and 2 // 4 == 0 and 17 % 3 == 2 and 2 ** 5 == 32
    assert -7 // 2 == -4 and -7 % 3 == 2
    assert type(1 + 2.0) is float
    assert numbers.z == 3 + 4j and numbers.z.real == 3.0
    with pytest.raises(SyntaxError):
        compile("n = 080", "<number>", "exec")


def test_strings_and_bools():
    s = str_bool.my_str
    assert (s[0:-1], s[2:5], s[2:]) == ("Runoo", "noo", "noob")
    assert str_bool.word[-6] == "P" and str_bool.replaced == "Jython"
    assert (float(True), str(True)) == (1.0, "True")
    assert [bool(v) for v in (0, 42, "", "Python", [], [1], None, "False")] == [
        False, True, False, True, False, True, False, True,
    ]
    assert str_bool.x_is_truthy is True
    with pytest.raises(TypeError):
        str_bool.word[0] = "m"


def test_lists():
    assert seq.a == [9, 2, 6]
    assert seq.items == ["桃子", "香蕉", "梨", "橙子", "葡萄"]
    assert seq.letters[1:4:2] == ["u", "a"] and seq.nested[1][0] == 2
    assert seq.reverseWords("I like runoob") == seq.reverse_words("I like runoob") == "runoob like I"
    assert seq.reverse_words("I  like") == "like  I"


def test_tuples():
    assert seq.my_tuple[1:3] == (786, 2.23) and seq.tup[1:5] == (2, 3, 4, 5)
    assert seq.pair == (1, [2, 3, 4])
    assert type(seq.tup2) is tuple and type(seq.not_a_tuple) is int and seq.tup1 == ()
    with pytest.raises(TypeError):
        seq.tup[0] = 11


def test_sets():
    assert "Runoob" in mapping.sites and len(mapping.first) == 3
    assert sorted(mapping.a & mapping.b) == ["a", "c"]
    assert sorted(mapping.a - mapping.b) == ["b", "d", "r"]
    assert type({}) is dict and type(set()) is set


def test_dicts():
    assert mapping.my_dict == {"one": "1 - 菜鸟教程", 2: "2 - 菜鸟工具"}
    assert list(mapping.tinydict.keys()) == ["name", "code", "site"]
    assert mapping.squares == {x: x ** 2 for x in (2, 4, 6)} == {2: 4, 4: 16, 6: 36}
    assert dict(Runoob=1) == dict([("Runoob", 1)])
    assert mapping.person.get("job", "未填写") == "未填写" and "job" not in mapping.person
    assert list(mapping.person.items())[-1] == ("city", "上海")


def test_bytes():
    assert bytes_demo.y == b"el" and bytes_demo.z == b"helloworld"
    assert bytes_demo.x[0] == ord("h") == 104
    assert (len(bytes_demo.message), len(bytes_demo.data)) == (2, 6)
    assert bytes_demo.mutable == bytearray(b"Hello") and bytes_demo.ascii_data == b"hello"
    with pytest.raises(TypeError):
        bytes_demo.ascii_data[0] = 72
