"""按教学顺序加载第 6 章 Demo，验证关键行为和输出。"""

import importlib.util
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ("filename", "expected_lines"),
    [
        (
            "01_arith_compare_demo.py",
            ("负数整除和取模： -3 2", "负除数取模： -2", "链式比较： True"),
        ),
        (
            "02_assignment_demo.py",
            ("除法赋值： 10.0", "列表别名： ['Rain', 'Ada']", "表达式内赋值： 3"),
        ),
        (
            "03_bitwise_logic_demo.py",
            ("负数右移： -2", "空列表短路： []", "非空文本短路： Rain"),
        ),
        (
            "04_member_id_demo.py",
            (
                "字符串与字典： True True False",
                "切片身份与值： True True",
                "逻辑优先级： True False",
                "幂与负号： 512 -4 4",
            ),
        ),
    ],
)
def test_demo_outputs(filename, expected_lines, capsys):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    displayed_lines = capsys.readouterr().out.splitlines()
    for line in expected_lines:
        assert line in displayed_lines
