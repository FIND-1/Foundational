"""pytest 教程用的被测代码：一个极简的购物车。

购物车是一个字典：{商品名: {"price": 单价, "quantity": 数量}}。
"""

import json


def add_item(cart, name, price, quantity=1):
    """向 cart 添加商品，同名商品累加数量。返回 cart 本身。"""
    if price < 0:
        raise ValueError(f"价格不能为负数：{price}")
    if quantity < 1:
        raise ValueError(f"数量至少为 1：{quantity}")
    old_quantity = cart.get(name, {"quantity": 0})["quantity"]
    cart[name] = {"price": price, "quantity": old_quantity + quantity}
    return cart


def total(cart):
    """计算总价。sum(... for ...) 是生成器表达式，类似 JS 中先 map 再 reduce。"""
    return sum(item["price"] * item["quantity"] for item in cart.values())


def apply_discount(amount, percent):
    """按百分比打折，percent 必须在 0～100 之间。"""
    if not 0 <= percent <= 100:          # Python 支持连续比较，相当于 0 <= percent and percent <= 100
        raise ValueError(f"折扣必须在 0～100 之间：{percent}")
    return amount * (100 - percent) / 100


def save_cart(cart, path):
    """把购物车以 JSON 格式保存到 path（pathlib.Path 对象）。"""
    path.write_text(json.dumps(cart, ensure_ascii=False), encoding="utf-8")


def load_cart(path):
    """从 path 读取购物车。"""
    return json.loads(path.read_text(encoding="utf-8"))
