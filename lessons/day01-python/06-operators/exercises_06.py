"""第 6 章 · 运算符练习。

把基础题的 ... 改成自己的表达式或语句，优先复用给定变量。
基础验证：./.venv/Scripts/python.exe -m pytest lessons/day01-python/06-operators -m basic -v
选做函数题时，把 NotImplementedError 占位替换为实现，再运行 -m advanced。
"""

# 基础题 1：算术与比较（Demo 01）
# 把总分钟数拆成完整时段数量和剩余分钟。再检查剩余时间是否在 [0, 时段长度)。
total_minutes = 95
slot_minutes = 30
full_slots = ...
remaining_minutes = ...
remainder_is_valid = ...

# 基础题 2：赋值（Demo 02）
# 先把起始分数保存到 updated_score，再用一条增量赋值加上 bonus。
# 用自己的两行代码替换下面的占位，保留 starting_score。
starting_score = 10
bonus = 4
updated_score = ...

# 基础题 3：位运算与逻辑（Demo 03）
# 用按位或合并权限。检查组合后的权限是否包含写权限。
# 用一个短路表达式安全读取空列表第一项，约定空列表时结果就是空列表。
read_flag = 0b01
write_flag = 0b10
combined_flags = ...
can_write = ...
empty_items = []
first_or_empty = ...

# 基础题 4：成员、身份与优先级（Demo 04）
# 检查键名是否存在。用身份判断别名是否为同一个列表，用值相等比较切片副本。
# 让加法先分组，再乘上倍数，得到两部分分数的加权总分。
settings = {"name": "Rain"}
setting_key = "name"
has_setting = ...
original_items = ["Python"]
alias_items = original_items
copied_items = original_items[:]
is_same_list = ...
has_equal_contents = ...
base_points = 3
extra_points = 4
multiplier = 2
weighted_points = ...


# 进阶题前置知识：def、return、if 和参数（见第 1 章进阶练习及前面示例）。
def pick_first(items, default):
    """非空列表返回第一个元素，空列表返回 default。

    非空列表的首项可能是 0、空字符串或 None，仍然应原样返回。
    """
    raise NotImplementedError("练习待完成")


def update_permission(flags, flag, enabled):
    """打开或关闭指定权限位，并返回更新后的整数掩码。

    flags 是非负整数，flag 是只含一个置位的正整数，enabled 是布尔值。
    没有被指定的其他权限位应保持原样。参考 Demo 03 的权限例子。
    """
    raise NotImplementedError("练习待完成")
