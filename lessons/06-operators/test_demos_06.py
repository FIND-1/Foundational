"""按教学顺序加载第 6 章 Demo，验证关键行为和输出。"""

import importlib.util
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ("filename", "expected_lines"),
    [
        (
            "01_arith_compare_demo.py",
            (
                "负数整除和取模： -3 2",
                "向零截断 vs 向下取整与取模： -2 -3 2",
                "负除数取模： -2",
                "跨类型相等比较： False True",
                "链式比较： True",
            ),
        ),
        (
            "02_assignment_demo.py",
            (
                "除法赋值： 10.0",
                "列表别名： ['Rain', 'Ada']",
                "+= 原地修改身份不变： True True",
                "重新绑定后的列表与原别名： ['Rain', 'Ada'] ['Rain']",
                "+ 重新绑定身份改变： False False",
                "表达式内赋值： 3",
            ),
        ),
        (
            "03_bitwise_logic_demo.py",
            (
                "负数右移： -2",
                "拓展 - 可写： True",
                "拓展 - 去掉写权限： 1",
                "空列表短路： []",
                "非空文本短路： Rain",
                "or 会误盖合法假值： 3 访客 True",
                "仅 None 时回退： 0 '' False 访客",
            ),
        ),
        (
            "04_member_id_demo.py",
            (
                "元组与集合成员： True True",
                "字符串与字典： True True False",
                "字典查值： True",
                "切片身份与值： True True",
                "逻辑优先级： True False",
                "分组与求值顺序： True True",
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
