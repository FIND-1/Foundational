"""第 6 章 · 成员、身份与运算符优先级。

用途：检查成员，对比值相等与对象身份，并观察括号如何影响表达式。
运行：./.venv/Scripts/python.exe lessons/06-operators/04_member_id_demo.py
预期结果：值相等的切片副本身份不同，默认逻辑优先级与显式括号得到不同结果。
"""

# 格式：值 in 容器、值 not in 容器 -> bool。列表按元素判断。
numbers = [1, 2, 3]
print("列表成员：", 2 in numbers, 5 not in numbers)  # True True

# 字符串按子串判断，字典默认查键。字典值对应的字符串会在该成员检查中得到 False。
contact = {"name": "Rain"}
print("字符串与字典：", "Py" in "Python", "name" in contact, "Rain" in contact)

# 格式：左值 is 右值、左值 is not 右值 -> bool。两个名字指向同一对象时 is 为 True。
# [:] 创建新列表，元素值仍相等。比较列表内容用 ==，检查是否同一对象用 is。
alias = numbers
shallow_copy = numbers[:]
print("别名身份：", numbers is alias)  # True
print("切片身份与值：", numbers is not shallow_copy, numbers == shallow_copy)

# 格式：id(对象) -> int。对象仍存活时标识稳定，别名的标识相同。
print("别名标识相等：", id(numbers) == id(alias))  # True

# 场景：用 None 表示缺省时，使用 is None 或 is not None。
selected = None
print("是否未选择：", selected is None)

# 格式：用 (表达式) 显式分组。乘法优先于加法，括号先把 1 + 2 组成一个操作数。
print("算术优先级：", 1 + 2 * 3, (1 + 2) * 3)  # 7 9

# 注意：表中的优先级决定如何分组。and 高于 or，但短路可能跳过整个右侧子表达式。
first = True
second = False
third = False
print("逻辑优先级：", first or second and third, (first or second) and third)

# 拓展：连续的 ** 向右分组。负号在幂左侧时，先算幂再取负。
print("幂与负号：", 2 ** 3 ** 2, -2 ** 2, (-2) ** 2)  # 512 -4 4
