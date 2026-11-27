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
        ("trunc_quotient", -2),
        ("floor_quotient", -3),
        ("neg_remainder", 2),
        ("updated_score", 14),
        ("first_or_empty", []),
        ("first_or_filled", "Rain"),
        ("fallback_name", "访客"),
        ("kept_zero", 0),
        ("kept_empty_label", ""),
        ("default_for_none", "默认"),
        ("has_setting", True),
        ("has_setting_value", True),
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


@pytest.mark.basic
def test_basic_starting_score_preserved():
    if exercises_06.updated_score is Ellipsis:
        pytest.skip("未完成：updated_score 仍为 ...")

    assert exercises_06.starting_score == 10


@pytest.mark.basic
def test_basic_list_in_place_update():
    if exercises_06.tags_mutated_in_place is Ellipsis:
        pytest.skip("未完成：tags_mutated_in_place 仍为 ...")

    assert exercises_06.primary_tags == ["js", "python"]
    assert exercises_06.alias_tags == ["js", "python"]
    assert exercises_06.primary_tags is exercises_06.alias_tags
    assert exercises_06.tags_mutated_in_place is True
    assert exercises_06.extra_tag == ["python"]


@pytest.mark.basic
def test_basic_list_rebinding():
    if exercises_06.tags_rebound is Ellipsis:
        pytest.skip("未完成：tags_rebound 仍为 ...")

    assert exercises_06.copied_tags == ["js", "python"]
    assert exercises_06.snapshot_tags == ["js"]
    assert exercises_06.copied_tags is not exercises_06.snapshot_tags
    assert exercises_06.tags_rebound is True


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
