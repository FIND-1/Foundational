"""第 2 章练习（分「基础练习」与「进阶练习」两层）。"""


# ══════════════════════════════ 一、基础练习（必做） ══════════════════════════════
# `...`（三个半角点）是这里的待填标记，每填一项即可单独验证。
# 请用题目给定的变量写表达式，不要直接写死结果。

# 基础题 1：数字运算与类型判断（01_numbers_demo.py）
total_seconds = 125
minutes = total_seconds // 60  # 用 // 求 total_seconds 包含几个整分钟，应得到 2
seconds = total_seconds % 60   # 用 % 求剩下的秒数，应得到 5
half = total_seconds / 2       # 用 / 求 total_seconds 的一半，应得到 62.5
bool_is_int = isinstance(True, int)      # 用 isinstance 判断 True 是否算作 int 类型
bool_exact_int = type(True) is int   # 用 type(...) is int 判断 True 的具体类型是否恰为 int

# 基础题 2：字符串与布尔值（02_str_bool_demo.py）
word = "Runoob"
first_last = word[0] + word[-1]        # 用 + 把 word 的第一个和最后一个字符拼起来，应得到 "Rb"
repeated_word = word * 2     # 用 * 把 word 重复两次
empty_list_truth = bool([])  # 用 bool() 求空列表的真假值
false_text_truth = bool("False")  # 用 bool() 求字符串 "False" 的真假值，先预测再运行

# 基础题 3：列表与元组（03_list_tuple_demo.py）
fruits = ["苹果", "香蕉", "梨"]
fruits[0] = "桃子"         # 把第一个水果改成 "桃子"：只替换右边的 ...，保留左边的 fruits[0] =
fruit_count = len(fruits)       # 用 len 求 fruits 的长度，应得到 3
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = numbers[::2]       # 用带步长的切片从 numbers 取出 [1, 3, 5]
single = (20,)            # 写出只包含整数 20 的元组

# 基础题 4：集合与字典（04_set_dict_demo.py）
a = {1, 2, 3}
b = {2, 3, 4}
common = a & b            # a 和 b 的交集
only_in_a = a - b         # 在 a 中但不在 b 中的元素
empty_set = set()         # 创建一个空集合（想一想 {} 是什么类型）
person = {"name": "Rain", "age": 18}
person_name = person["name"]       # 按键读取 person 的 "name"
person_job = person.get("job", "未填写")        # 用 get 读取 "job"，缺少时得到 "未填写"

# 基础题 5：bytes 与编码（05_bytes_demo.py）
message = "你好"
encoded = message.encode("utf-8")           # 用 UTF-8 把 message 编码为 bytes
byte_count = len(encoded)        # 直接用 message、encode 和 len 求 UTF-8 字节数，应得到 6
first_byte = b"hello"[0]        # 取 b"hello" 的第一个元素，先预测它的类型


# 基础题 6：从终端读一行文本，不显示提示语。第一行输出它的字符数，第二行输出它的 UTF-8 字节数。
# 例如输入「你好」时输出两行：2 和 6。自己写 input、len、encode 和 print。
# __name__ 与 NotImplementedError 占位的含义见第 1 章 exercises_01.py 基础题 4 的注释。
# 把入口里整行占位语句替换为你的代码，无须定义函数。
if __name__ == "__main__":
    text = input()
    print(len(text))
    print(len(text.encode("utf-8")))
    

# ══════════════════════════════ 二、进阶练习（可选） ══════════════════════════════
# 前置知识：def 定义函数、return 返回值（第 1 章 03_io_import_demo.py「代码组」）。
# 若尚未学习函数语法，可先跳过本节，不影响第 2 章基础验收。

def is_strict_int(value):
    """【进阶】value 的具体类型恰为 int 时返回 True；True、3.0 等其他类型返回 False。"""
    return type(value) is int


def count_unique(items):
    """【进阶】返回列表 items 中不重复元素的个数。例如 [1, 1, 2] -> 2。不用循环。"""
    return len(set(items))


def common_sorted(first, second):
    """【进阶】返回两个列表共同元素组成的升序列表，不含重复。

    例如 ([3, 1, 2, 2], [2, 3, 4]) -> [2, 3]。不用循环。
    """
    return sorted(set(first) & set(second))


def last_word(text):
    """【进阶】按空白拆分 text，返回最后一个单词。例如 'I like runoob' -> 'runoob'。

    假设 text 至少有一个单词；多个连续空格也不影响结果。提示：查 functions.md 中 split 的默认分隔方式。
    """
    return text.split()[-1]


def utf8_size(text):
    """【进阶】返回 text 用 UTF-8 编码后的字节数。例如 'A你' -> 4。"""
    return len(text.encode("utf-8"))


def squares_dict(numbers):
    """【进阶】返回 {数字: 数字的平方}。例如 (2, 4) -> {2: 4, 4: 16}。

    前置知识：04_set_dict_demo.py 的 for 循环或字典推导式。
    """
    return {n: n ** 2 for n in numbers}
