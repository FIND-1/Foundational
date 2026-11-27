"""第 6 章 · 赋值运算符、列表引用与海象运算符。

用途：演示普通赋值与数值增量赋值，对比列表 += 原地修改与 = ... + ... 重新绑定的对象身份，并介绍海象运算符。
运行（仓库根目录，已激活 .venv）：python lessons/06-operators/02_assignment_demo.py
"""

# ── 1. 普通赋值与数值增量赋值 ─────────────────────────────────────────
# 格式：变量 = 值 -> 先求右侧值，再绑定到左侧变量（变量赋值见第 2 章 01_numbers_demo.py）
score = 10
step = 2

# 格式：变量 += 增量 -> 加上增量后写回变量
score += step
print("加分：", score)  # 12

# 格式：变量 -= 值、*= 值、/= 值 -> 分别做减法、乘法、除法后写回
score -= step
score *= step
print("减分后翻倍：", score)  # 20
score /= step
print("除法赋值：", score)  # 10.0

# 格式：变量 **= 指数、//= 除数、%= 除数 -> 分别做幂、整除、取模后写回
quantity = 3
quantity **= step  # 9
quantity //= step  # 4
quantity %= 3  # 1
print("整除后取模：", quantity)  # 1


# ── 2. 列表 += 原地修改与 + 重新绑定 ──────────────────────────────────
# 格式：对象1 is 对象2 -> bool（判断是否同一对象，详见 04_member_id_demo.py）；
#       id(对象) -> int（返回对象标识，仅用于观察身份，详见 functions.md）
# 注意：列表的 += 会原地扩展当前对象，alias 与 names 引用同一个列表，因此 alias 同步看到新增元素
names = ["Rain"]
alias = names
names += ["Ada"]
print("列表别名：", alias)  # ['Rain', 'Ada']
print("+= 原地修改身份不变：", names is alias, id(names) == id(alias))  # True True

# 注意：a = a + [元素] 会先拼接出新列表对象，再把左侧变量重新绑定到新列表；
#       原别名 old_alias 仍指向旧列表，不会受到影响
rebound = ["Rain"]
old_alias = rebound
rebound = rebound + ["Ada"]
print("重新绑定后的列表与原别名：", rebound, old_alias)  # ['Rain', 'Ada'] ['Rain']
print("+ 重新绑定身份改变：", rebound is old_alias, id(rebound) == id(old_alias))  # False False


# ── 3. 拓展：海象运算符（:=）──────────────────────────────────────────
# 拓展：常规写法先计算长度并赋值，再进入 if 判断
names += ["Lin"]
count = len(names)
if count > 2:
    print("先赋值：", count)  # 3

# 拓展：格式：(变量 := 表达式) -> 赋值并返回该值
# 括号用于明确分组，使赋值结果直接参与外层比较；日常逻辑简单时保持上面的两行写法即可
if (count := len(names)) > 2:
    print("表达式内赋值：", count)  # 3
