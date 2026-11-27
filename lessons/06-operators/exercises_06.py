"""第 6 章练习（分「基础练习」与「进阶练习」两层）。"""


# ══════════════════════════════ 一、基础练习（必做） ══════════════════════════════
# `...`（三个半角点）是这里的待填标记，每填一项即可单独验证。
# 请复用题目给定的变量写表达式，不要直接写死结果。

# 基础题 1：算术、负数运算边界与链式比较（01_arith_compare_demo.py）
# 1) 把总分钟数拆成完整时段数量和剩余分钟，并用链式比较检查剩余分钟是否在 [0, 时段长度)。
# 2) 对 neg_dividend (-7) 和 divisor (3)，分别求 int() 向零截断的商、// 向下取整的商和 % 余数。
total_minutes = 95
slot_minutes = 30
full_slots = ...
remaining_minutes = ...
remainder_is_valid = ...

neg_dividend = -7
divisor = 3
trunc_quotient = ...
floor_quotient = ...
neg_remainder = ...

# 基础题 2：增量赋值、列表原地修改与重新绑定（02_assignment_demo.py）
# 1) 先把 starting_score 保存到 updated_score，再用一条增量赋值加上 bonus（保留 starting_score 不变）。
# 2) 对 primary_tags 用 += 原地追加 extra_tag，再用 is 判断它与 alias_tags 是否仍为同一对象。
# 3) 对 copied_tags 用 = ... + ... 拼接 extra_tag 重新绑定，再用 is not 判断它与 snapshot_tags 是否已不同。
starting_score = 10
bonus = 4
updated_score = ...

extra_tag = ["python"]
primary_tags = ["js"]
alias_tags = primary_tags
# 在下面写一条对 primary_tags 使用 += 的语句，再填写身份判断表达式：
tags_mutated_in_place = ...

copied_tags = ["js"]
snapshot_tags = copied_tags
# 在下面写一条对 copied_tags 使用 = ... + ... 重新绑定的语句，再填写身份判断表达式：
tags_rebound = ...

# 基础题 3：逻辑返回值、短路与缺省值处理（03_bitwise_logic_demo.py）
# 1) 用 and 安全读取空列表与非空列表的第一项（空列表短路返回 []，非空列表返回首项本身）。
# 2) 用 or 给空字符串回退默认名称 "访客"。
# 3) 对合法假值 0、空字符串 "" 与缺省值 None，用条件表达式仅在值为 None 时回退默认值。
empty_items = []
filled_items = ["Rain", "Ada"]
first_or_empty = ...
first_or_filled = ...

empty_name = ""
fallback_name = ...

retry_limit = 0
custom_label = ""
unset_option = None
kept_zero = ...           # 仅当 retry_limit is None 时回退为 3，否则保留原值
kept_empty_label = ...    # 仅当 custom_label is None 时回退为 "默认"，否则保留原值
default_for_none = ...    # 仅当 unset_option is None 时回退为 "默认"，否则保留原值

# 基础题 4：成员、身份与优先级分组（04_member_id_demo.py）
# 检查字典键与字典值是否存在；用身份判断别名，用值相等比较切片副本；
# 用括号让加法先分组，再乘上倍数，得到加权总分。
settings = {"name": "Rain"}
setting_key = "name"
setting_value = "Rain"
has_setting = ...
has_setting_value = ...
original_items = ["Python"]
alias_items = original_items
copied_items = original_items[:]
is_same_list = ...
has_equal_contents = ...
base_points = 3
extra_points = 4
multiplier = 2
weighted_points = ...


# ══════════════════════════════ 二、进阶练习（可选） ══════════════════════════════
# 前置知识：def 定义函数、return 返回值、if 判断（见第 1 章进阶练习及前面示例）。
# 若尚未学习函数语法，可先跳过本节，不影响第 6 章基础验收。


def pick_first(items, default):
    """【进阶】非空列表返回第一个元素，空列表返回 default。

    非空列表的首项可能是 0、空字符串或 None，仍然应原样返回。
    """
    raise NotImplementedError("练习待完成")


def update_permission(flags, flag, enabled):
    """【进阶】打开或关闭指定二进制权限位，并返回更新后的整数掩码。

    flags 是非负整数，flag 是只含一个置位的正整数，enabled 是布尔值。
    没有被指定的其他权限位应保持原样。参考 03_bitwise_logic_demo.py 拓展段。
    """
    raise NotImplementedError("练习待完成")
