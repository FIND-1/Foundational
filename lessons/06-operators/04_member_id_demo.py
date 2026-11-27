"""第 6 章 · 成员、身份与运算符优先级。

用途：演示多种容器的成员判断、值相等与对象身份的区别，并区分运算符优先级分组与实际求值顺序。
运行（仓库根目录，已激活 .venv）：python lessons/06-operators/04_member_id_demo.py
"""

# ── 1. 成员运算符（in / not in）───────────────────────────────────────
# 格式：值 in 容器、值 not in 容器 -> bool（列表和元组按元素判断，集合按元素判断且查找更快）
# 注意：tuple、set 与 dict.values() 详见第 2 章 03_list_tuple_demo.py 和 04_set_dict_demo.py
numbers = [1, 2, 3]
print("列表成员：", 2 in numbers, 5 not in numbers)  # True True

coords = (10, 20)
tags = {"python", "web"}
print("元组与集合成员：", 10 in coords, "python" in tags)  # True True

# 字符串按子串判断，字典默认只查键；如需查字典的值，对 字典.values() 使用 in
contact = {"name": "Rain"}
print("字符串与字典：", "Py" in "Python", "name" in contact, "Rain" in contact)  # True True False
print("字典查值：", "Rain" in contact.values())  # True


# ── 2. 身份运算符（is / is not）与值相等（==）─────────────────────────
# 格式：左值 is 右值、左值 is not 右值 -> bool（两个名字指向同一对象时 is 为 True）
# 场景：比较容器内容用 ==，检查是否同一对象用 is；[:] 创建的是新列表副本
alias = numbers
shallow_copy = numbers[:]
print("别名身份：", numbers is alias)  # True
print("切片身份与值：", numbers is not shallow_copy, numbers == shallow_copy)  # True True

# 格式：id(对象) -> int（对象存活时标识稳定，别名的标识相同；详见 functions.md）
print("别名标识相等：", id(numbers) == id(alias))  # True

# 场景：用 None 表示缺省时，固定使用 is None 或 is not None（03_bitwise_logic_demo.py 已用于缺省值回退）
selected = None
print("是否未选择：", selected is None)  # True


# ── 3. 运算符优先级、分组与求值顺序 ───────────────────────────────────
# 格式：用 (表达式) 显式分组；乘法优先于加法
print("算术优先级：", 1 + 2 * 3, (1 + 2) * 3)  # 7 9

# 注意：优先级决定的是“语法如何加括号分组”，不等于“高优先级子表达式一定会先执行”
#       and 优先级高于 or，因此 `first or second and third` 分组为 `first or (second and third)`
first = True
second = False
third = False
print("逻辑优先级：", first or second and third, (first or second) and third)  # True False

# 注意：实际求值默认从左到右并受短路控制；
#       下面右侧分组 `right_flag and (1 / 0)` 若先执行会触发除零错误，
#       但因左侧 first 已为 True，or 直接短路返回 True，整个右侧分组从未求值
right_flag = True
print("分组与求值顺序：", first or (right_flag and (1 / 0)), first or right_flag and (1 / 0))  # True True


# ── 4. 拓展：幂右结合与负号优先级 ─────────────────────────────────────
# 拓展：连续的 ** 向右分组，2 ** 3 ** 2 等价于 2 ** (3 ** 2)；负号在幂左侧时先算幂再取负
print("幂与负号：", 2 ** 3 ** 2, -2 ** 2, (-2) ** 2)  # 512 -4 4
