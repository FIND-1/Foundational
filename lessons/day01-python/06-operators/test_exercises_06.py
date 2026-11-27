"""第 6 章练习验收。完成 exercises_06.py 后运行本章 pytest。"""

import pytest

import exercises_06


@pytest.mark.basic
@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("full_slots", 3),
        ("remaining_minutes", 5),
        ("remainder_is_valid", True),
        ("updated_score", 14),
        ("combined_flags", 0b11),
        ("can_write", True),
        ("first_or_empty", []),
        ("has_setting", True),
        ("is_same_list", True),
        ("has_equal_contents", True),
        ("weighted_points", 14),
    ],
)
def test_basic_values(name, expected):
    actual = getattr(exercises_06, name)
    if actual is Ellipsis:
        pytest.skip(f"未完成：{name} 仍为 ...")

    assert type(actual) is type(expected)
    assert actual == expected


@pytest.mark.advanced
@pytest.mark.parametrize(
    ("items", "default", "expected"),
    [
        ([], "访客", "访客"),
        (["Rain", "Ada"], "访客", "Rain"),
        ([0, 1], 99, 0),
        ([""], "访客", ""),
        ([None], "访客", None),
    ],
)
def test_pick_first(items, default, expected):
    actual = exercises_06.pick_first(items, default)

    assert type(actual) is type(expected)
    assert actual == expected


@pytest.mark.advanced
@pytest.mark.parametrize(
    ("flags", "flag", "enabled", "expected"),
    [
        (0b001, 0b010, True, 0b011),
        (0b101, 0b100, False, 0b001),
        (0b101, 0b010, False, 0b101),
        (0b101, 0b100, True, 0b101),
        (0, 1 << 40, True, 1 << 40),
    ],
)
def test_update_permission(flags, flag, enabled, expected):
    actual = exercises_06.update_permission(flags, flag, enabled)

    assert type(actual) is int
    assert actual == expected
