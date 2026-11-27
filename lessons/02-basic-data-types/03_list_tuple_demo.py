"""第 2 章 · 列表（List）与元组（Tuple）。

用途：演示列表的截取、拼接、修改、步长切片、单词倒序，以及元组的截取、不可变和单元素写法。
运行（仓库根目录，已激活 .venv）：python lessons/02-basic-data-types/03_list_tuple_demo.py
预期结果：切片赋值后列表为 [9, 2, 13, 14, 15, 6]，再删除后为 [9, 2, 6]；单词倒序得到 runoob like I；
(42) 的类型是 int，(20,) 的类型是 tuple。末尾演示修改元组元素的报错。
"""

# ── 1. 列表：创建、截取与拼接 ─────────────────────────────────────────
# 格式：[元素, 元素, ...] -> list（类似 JS 数组，元素可不同类型）；支持下标、切片、+ 拼接、* 重复
# 注意：不要用 list 作变量名，避免覆盖内置类型；切片返回新列表
my_list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(my_list)             # ['abcd', 786, 2.23, 'runoob', 70.2]
print(my_list[0])          # 第一个元素：abcd
print(my_list[1:3])        # 下标 1 和 2：[786, 2.23]
print(my_list[2:])         # 从下标 2 到末尾：[2.23, 'runoob', 70.2]
print(tinylist * 2)        # [123, 'runoob', 123, 'runoob']
print(my_list + tinylist)  # 拼接两个列表

# 格式：嵌套列表[外层下标][内层下标] -> 逐层取值（nested[1] 得 [2, 3]，再 [0] 得 2）
nested = [1, [2, 3]]
print("嵌套列表取值：", nested[1][0])  # 2


# ── 2. 列表的元素可以修改 ─────────────────────────────────────────────
# 格式：列表[下标] = 新值；列表[头下标:尾下标] = 新列表（替换该段，赋 [] 即删除该段）
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print("修改后：", a)  # [9, 2, 13, 14, 15, 6]
a[2:5] = []
print("删除一段后：", a)  # [9, 2, 6]

# 格式：列表.append(元素) -> None（在原列表末尾追加一项）
# 注意：与 JS 的 push 返回新长度不同，Python 的 append 原地修改并返回 None
items = ["苹果", "香蕉", "梨", "橙子"]
items[0] = "桃子"
items.append("葡萄")
print("修改并追加后：", items)


# ── 3. 步长与逆向截取 ─────────────────────────────────────────────────
# 格式：列表[头下标:尾下标:步长] -> 新列表（下面从下标 1 到末尾，每隔一个取一个）
letters = ['r', 'u', 'n', 'a', 'n', 'b']
print("letters[1::2]：", letters[1::2])  # ['u', 'a', 'b']

# 拓展：步长为负数表示逆向截取；以下演示单词倒序（def / return 见第 1 章 03_io_import_demo.py）
# 格式：字符串.split("分隔符") -> 字符串列表；"分隔符".join(列表) -> 拼接后的新字符串
# 注意：split(" ") 遇连续空格会保留空串 ""；split("") 在 Python 会报 ValueError（与 JS 不同）
def reverseWords(input):
    # 通过空格把字符串分隔成单词列表
    inputWords = input.split(" ")
    # [-1::-1]：从最后一项开始，省略终点一直到开头，步长 -1 每次左移一位
    inputWords = inputWords[-1::-1]
    # 重新拼接单词
    output = " ".join(inputWords)
    return output


# 拓展：按 PEP 8 改写为 snake_case，参数名用 text 避免遮住内置函数 input；[::-1] 与 [-1::-1] 等价
def reverse_words(text):
    words = text.split(" ")
    return " ".join(words[::-1])


# 拓展：直接运行本文件时 __name__ == "__main__" 成立（详见第 1 章 exercises_01.py 注释）
if __name__ == "__main__":
    sentence = "I like runoob"
    print("原例：", reverseWords(sentence))
    print("改写：", reverse_words(sentence))
    print("连续空格：", reverse_words("I  like").split(" "))


# ── 4. 元组：创建与截取 ───────────────────────────────────────────────
# 格式：(元素, 元素, ...) -> tuple（有序、可索引切片、支持 + 和 *，但不可修改元素）
# 场景：结构固定、不想被改的数据（如坐标、多返回值）；类似 TS 的 readonly [string, number]
# 注意：不要用 tuple 作变量名
my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(my_tuple)               # 完整元组
print(my_tuple[0])            # 第一个元素：abcd
print(my_tuple[1:3])          # 下标 1 和 2：(786, 2.23)
print(my_tuple[2:])           # 从下标 2 开始的所有元素
print(tinytuple * 2)          # 重复两次
print(my_tuple + tinytuple)   # 连接两个元组

tup = (1, 2, 3, 4, 5, 6)
print(tup[0])    # 1
print(tup[1:5])  # (2, 3, 4, 5)


# ── 5. 元组可以包含可变对象 ───────────────────────────────────────────
# 注意：pair 本身是元组（不能替换槽位，pair[1] = [9] 报错），但槽位里的列表可原地修改
# 拓展：类似 JS 浅冻结 const pair = Object.freeze([1, [2, 3]])，pair[1].push(4) 合法
pair = (1, [2, 3])
pair[1].append(4)
print("元组里的列表被修改：", pair)  # (1, [2, 3, 4])


# ── 6. 0 个或 1 个元素的元组 ──────────────────────────────────────────
# 格式：() 空元组；(元素,) 单元素元组（末尾必须加逗号）
# 注意：不加逗号时 (42) 只是普通数学括号，结果是整数 42；空元组为假值（bool 见 02_str_bool_demo.py）
tup1 = ()      # 空元组
tup2 = (20,)   # 一个元素，需要在元素后添加逗号
not_a_tuple = (42)  # 这是整数 42，不是元组
print("三种写法的类型：", type(tup1), type(tup2), type(not_a_tuple))
print("bool(())、bool(tup2)：", bool(tup1), bool(tup2))  # False True

# 注意：str、list、tuple 都属于序列（sequence）：有序，支持索引和切片
point = (3, 4)
print("元组的索引、切片与拼接：", point[0], point[:1], point + (5,))


# ── 拓展：观察修改元组元素的报错 ──────────────────────────────────────
# 注意：给元组下标赋值会抛 TypeError（try / except 见第 1 章 01_syntax_demo.py 末尾）
try:
    tup[0] = 11
except TypeError as error:
    print("【进阶】修改元组元素：", error)
