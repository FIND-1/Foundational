"""第 6 章 · 普通赋值、增量赋值与海象运算符。

用途：用计分演示数值更新，观察列表别名和表达式内赋值。
运行：./.venv/Scripts/python.exe lessons/day01-python/06-operators/02_assignment_demo.py
预期结果：加分后为 12，除法赋值后为 10.0，列表别名看到原地追加，长度为 3。
"""

# 格式：变量 = 值。先求右侧的值，再把它绑定到左侧的变量。
score = 10
step = 2

# 格式：变量 += 增量。这里在 10 的基础上加 2，再把 12 写回 score。
score += step
print("加分：", score)

# 格式：变量 -= 值、*= 值、/= 值，分别做减法、乘法和除法，然后写回。
score -= step
score *= step
print("减分后翻倍：", score)  # 20
score /= step
print("除法赋值：", score)  # 10.0

# 格式：变量 **= 指数、//= 除数、%= 除数，分别做幂、整除、取模后写回。
# 用整数 3 起步，依次得到 9、4、1。
quantity = 3
quantity **= step
quantity //= step
quantity %= 3
print("整除后取模：", quantity)

# 注意：列表的 += 会原地扩展，alias 引用同一个列表，因此也能看到新增元素。
names = ["Rain"]
alias = names
names += ["Ada"]
print("列表别名：", alias)  # ['Rain', 'Ada']

# 拓展：先用常规写法，len(names) 计算一次长度，再判断是否达到门槛。
names += ["Lin"]
count = len(names)
if count > 2:
    print("先赋值：", count)

# 拓展：格式：(变量 := 表达式) -> 表达式的值。先把长度存进 count，再与 2 比较。
# 括号把赋值部分圈起来，使 count 记录长度 3。
if (count := len(names)) > 2:
    print("表达式内赋值：", count)
