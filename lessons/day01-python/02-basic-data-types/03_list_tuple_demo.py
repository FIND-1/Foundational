"""第 2 章 · 列表（List）与元组（Tuple）。

用途：演示列表的截取、拼接、修改、步长切片、单词倒序，以及元组的截取、不可变和单元素写法。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/02-basic-data-types/03_list_tuple_demo.py
预期结果：切片赋值后列表为 [9, 2, 13, 14, 15, 6]，再删除后为 [9, 2, 6]；单词倒序得到 runoob like I；
(42) 的类型是 int，(20,) 的类型是 tuple。末尾演示修改元组元素的报错。
"""

# ── 1. 列表：创建、截取与拼接 ─────────────────────────────────────────
# 【必会】[元素, 元素, ...] 创建列表，类似 JS 数组，元素类型可以不同。
# 索引和切片与字符串相同，切片返回新列表；+ 拼接两个列表，* 重复列表。
my_list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 不用 list 作变量名，避免覆盖内置类型
tinylist = [123, 'runoob']

print(my_list)             # ['abcd', 786, 2.23, 'runoob', 70.2]
print(my_list[0])          # 第一个元素：abcd
print(my_list[1:3])        # 下标 1 和 2：[786, 2.23]
print(my_list[2:])         # 从下标 2 到末尾：[2.23, 'runoob', 70.2]
print(tinylist * 2)        # [123, 'runoob', 123, 'runoob']
print(my_list + tinylist)  # 拼接两个列表

# 【必会】列表可以嵌套。nested[1] 取出内层列表 [2, 3]，再用 [0] 取出其中的 2。
nested = [1, [2, 3]]
print("嵌套列表取值：", nested[1][0])  # 2


# ── 2. 列表的元素可以修改 ─────────────────────────────────────────────
# 【必会】a[0] = 9 替换首项；a[2:5] = [13, 14, 15] 用右侧列表替换下标 2、3、4 三项。
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print("修改后：", a)  # [9, 2, 13, 14, 15, 6]
# 把一段切片赋值为空列表 []，就删除了这一段元素。
a[2:5] = []
print("删除一段后：", a)  # [9, 2, 6]

# 【补充】【必会】列表.append(元素) 在原列表末尾添加一项，返回 None（JS 的 push 返回新长度）。
# 列表还有 pop() 等方法，后续课程再讲。
items = ["苹果", "香蕉", "梨", "橙子"]
items[0] = "桃子"
items.append("葡萄")
print("修改并追加后：", items)


# ── 3. 步长与逆向截取 ─────────────────────────────────────────────────
# 【必会】列表[start:end:step] 的第三个参数是步长。下面从下标 1 取到 4 之前，每隔一个取一个。
letters = ['r', 'u', 'n', 'o', 'o', 'b']
print("letters[1:4:2]：", letters[1:4:2])  # ['u', 'o']

# 【进阶】步长为负数表示逆向读取。下面的函数把句子的单词倒序排列，单词内的字母顺序不变。
# def 和 return 见第 1 章 03_io_import_demo.py「代码组」。
# 【了解】文本.split(" ") 在每个空格处切开，返回字符串列表；连续两个空格会留下一个空字符串 ""。
# 【了解】" ".join(列表) 用一个空格把列表中的字符串连成一个新字符串。
def reverseWords(input):
    # 通过空格把字符串分隔成单词列表
    inputWords = input.split(" ")
    # [-1::-1]：从最后一个元素开始，省略终点表示一直到开头，步长 -1 每次向左移动一位
    inputWords = inputWords[-1::-1]
    # 重新用空格拼接单词
    output = ' '.join(inputWords)
    return output


# 【补充】函数名用 snake_case，参数名用 text，避免遮住内置函数 input。
# 步长为负时起点默认是末项，所以 [::-1] 与 [-1::-1] 结果相同。
def reverse_words(text):
    words = text.split(" ")
    return " ".join(words[::-1])


# 直接运行本文件时 __name__ 等于 "__main__"，进入下面的代码块（详见第 1 章 exercises_01.py 基础题 4 的注释）。
if __name__ == "__main__":
    sentence = "I like runoob"
    print("原例：", reverseWords(sentence))
    print("改写：", reverse_words(sentence))
    # 两个单词之间有两个空格时，split(" ") 会多出一个空字符串，倒序后两个空格仍保留。
    print("连续空格：", reverse_words("I  like").split(" "))


# ── 4. 元组：创建与截取 ───────────────────────────────────────────────
# 【必会】(元素, 元素, ...) 创建元组。它和列表一样有序、可索引、可切片、可用 + 和 *，但元素不能修改。
# 【补充】JS 没有元组类型，接近的是 TS 的 readonly [string, number]。
my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)  # 不用 tuple 作变量名
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
# 元组本身不能替换元素，但如果元素是列表，可以修改这个列表的内容。
pair = (1, [2, 3])
pair[1].append(4)
print("元组里的列表被修改：", pair)  # (1, [2, 3, 4])


# ── 6. 0 个或 1 个元素的元组 ──────────────────────────────────────────
# 【必会】() 是空元组；只有一个元素时必须在后面加逗号，例如 (20,)。
# 没有逗号时括号只是数学运算的括号，(42) 就是整数 42。
tup1 = ()      # 空元组
tup2 = (20,)   # 一个元素，需要在元素后添加逗号
not_a_tuple = (42)  # 这是整数 42，不是元组
print("三种写法的类型：", type(tup1), type(tup2), type(not_a_tuple))
# 空元组和空列表一样是假值（bool 的规则见 02_str_bool_demo.py）。
print("bool(())、bool(tup2)：", bool(tup1), bool(tup2))  # False True

# string、list 和 tuple 都属于序列（sequence）：有序，支持索引和切片。
point = (3, 4)
print("元组的索引、切片与拼接：", point[0], point[:1], point + (5,))


# ── 【补充】【进阶】观察修改元组元素的报错 ────────────────────────────
# 给元组的某个下标赋值会抛 TypeError；try / except 的读法见第 1 章 01_syntax_demo.py 末尾。
try:
    tup[0] = 11
except TypeError as error:
    print("【进阶】修改元组元素：", error)
