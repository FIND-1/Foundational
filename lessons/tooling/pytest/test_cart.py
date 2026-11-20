"""pytest 教程示例，配合同目录的 README.md 阅读。

运行：python -m pytest lessons/tooling/pytest -v
"""

import sys

import pytest

from cart import add_item, apply_discount, load_cart, save_cart, total


# ── 1. 最基本的测试：test_ 开头的函数 + 普通 assert ─────────────────────
def test_add_item_to_empty_cart():
    cart = add_item({}, "apple", 3.5)
    assert cart == {"apple": {"price": 3.5, "quantity": 1}}


def test_same_item_accumulates():
    cart = {}
    add_item(cart, "apple", 3.5)
    add_item(cart, "apple", 3.5, quantity=2)
    assert cart["apple"]["quantity"] == 3


# ── 2. 断言会抛出异常：pytest.raises ────────────────────────────────────
def test_negative_price_raises():
    with pytest.raises(ValueError, match="价格不能为负数"):   # match 是正则表达式，匹配异常信息
        add_item({}, "apple", -1)


def test_exception_details():
    with pytest.raises(ValueError) as exc_info:             # 需要检查异常对象时使用 as
        add_item({}, "apple", 1, quantity=0)
    assert "数量至少为 1" in str(exc_info.value)


# ── 3. 浮点数比较：pytest.approx ────────────────────────────────────────
def test_total_with_float():
    cart = {}
    add_item(cart, "a", 0.1)
    add_item(cart, "b", 0.2)
    assert total(cart) == pytest.approx(0.3)                # 直接写 == 0.3 会失败


# ── 4. 参数化：同一段逻辑，多组数据 ─────────────────────────────────────
@pytest.mark.parametrize(
    ("amount", "percent", "expected"),
    [
        (100, 0, 100),
        (100, 20, 80),
        (100, 100, 0),
        (59.9, 10, 53.91),
    ],
    ids=["不打折", "八折", "免费", "小数"],                  # 可选：为每组数据命名，显示在 -v 输出中
)
def test_apply_discount(amount, percent, expected):
    assert apply_discount(amount, percent) == pytest.approx(expected)


@pytest.mark.parametrize("percent", [-1, 101])
def test_invalid_discount(percent):
    with pytest.raises(ValueError):
        apply_discount(100, percent)


# ── 5. fixture：准备测试数据（相当于 Jest 的 beforeEach） ────────────────
@pytest.fixture
def fruit_cart():
    cart = {}
    add_item(cart, "apple", 3.5, quantity=2)
    add_item(cart, "pear", 2.0)
    return cart


def test_total_with_fixture(fruit_cart):                    # 参数名与 fixture 同名，pytest 会自动注入
    assert total(fruit_cart) == 9.0


def test_fixture_is_fresh_each_time(fruit_cart):
    add_item(fruit_cart, "melon", 10)                       # 修改不会影响其他测试：每个测试拿到的都是新的 fixture
    assert len(fruit_cart) == 3


@pytest.fixture
def cart_file(tmp_path):                                    # fixture 可以依赖其他 fixture；tmp_path 是内置的临时目录
    path = tmp_path / "cart.json"
    yield path                                              # yield 之前是准备，之后是清理（相当于 afterEach）
    if path.exists():
        path.unlink()                                       # tmp_path 本身会被自动清理，这里仅演示 yield 的写法


def test_save_and_load(fruit_cart, cart_file):
    save_cart(fruit_cart, cart_file)
    assert load_cart(cart_file) == fruit_cart


# ── 6. 常用内置 fixture：capsys、monkeypatch ────────────────────────────
def test_capture_print(capsys):
    print("hello", end="")
    assert capsys.readouterr().out == "hello"


def test_fake_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "42")   # 测试结束后自动恢复原来的 input
    assert int(input("年龄：")) + 1 == 43


# ── 7. 标记：skip、skipif、xfail ────────────────────────────────────────
@pytest.mark.skip(reason="演示：无条件跳过")
def test_skipped():
    assert False


@pytest.mark.skipif(sys.platform != "win32", reason="只在 Windows 上运行")
def test_windows_only():
    assert sys.platform == "win32"


@pytest.mark.xfail(reason="演示：已知问题，0.1 + 0.2 不精确等于 0.3", strict=True)
def test_known_float_issue():
    assert 0.1 + 0.2 == 0.3
