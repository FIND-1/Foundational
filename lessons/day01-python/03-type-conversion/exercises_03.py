"""第 3 章练习（分「基础练习」与「进阶练习」两层）。

做法：
1. 先完成「基础练习」：把题 1～5 的 `...` 改成你的表达式，再写题 6 的入口代码（只用本章基础语法，不需要 def）。
2. 运行基础测试：./.venv/Scripts/python.exe -m pytest lessons/day01-python/03-type-conversion -m basic -v
3. 「进阶练习」为可选挑战（需先了解 def / return / try...except），把 `raise NotImplementedError("练习待完成")` 换成实现即可。
4. 运行全部测试：./.venv/Scripts/python.exe -m pytest lessons/day01-python/03-type-conversion -v
注意：不要修改 test_exercises_03.py；未完成的题会显示为 SKIPPED。
"""


# ══════════════════════════════ 一、基础练习（必做） ══════════════════════════════
# `...`（三个半角点）是这里的待填标记，每填一项即可单独验证。
# 请复用题目给定的变量写表达式，不要修改原变量，也不要直接写死结果。

# 基础题 1：隐式转换与字符串转整数求和（01_implicit_demo.py、02_numbers_str_demo.py）
base_int = 123
base_float = 1.25
implicit_sum = ...          # 把 base_int 和 base_float 相加，观察隐式转换结果与类型

num_text = "12"
addend = 3
explicit_sum = ...          # 把 num_text 转成整数后与 addend 相加，应得到 15（不要改写 num_text）
joined_text = ...           # 把 addend 转成字符串后拼到 num_text 后面，应得到 "123"

# 基础题 2：截断、小数文本与真假文本（02_numbers_str_demo.py）
neg_price = -3.9
truncated = ...             # 用 int() 把 neg_price 转为整数，观察向零截断的结果
decimal_text = "3.5"
as_float = ...              # 把 decimal_text 转为浮点数
as_int = ...                # 把 decimal_text 先转浮点数再转整数（直接 int("3.5") 会报错）
flag_text = "False"
flag_bool = ...             # 用 bool() 转 flag_text，先预测再运行
flag_is_true = ...          # 先把 flag_text 转小写，再判断是否等于 "true"

# 基础题 3：进制解析与格式化（02_numbers_str_demo.py）
bin_text = "101"
hex_text = "ff"
from_bin = ...              # 按二进制解析 bin_text，应得到 5
from_hex = ...              # 按十六进制解析 hex_text，应得到 255
decimal_num = 10
as_bin = ...                # 把 decimal_num 转为二进制字符串（带 0b 前缀）
as_hex = ...                # 把 decimal_num 转为十六进制字符串（带 0x 前缀）

# 基础题 4：容器转换（03_containers_demo.py）
letters = "abc"
letters_tuple = ...         # 把 letters 转为元组，应得到 ('a', 'b', 'c')
raw_nums = [1, 2, 2, 3]
unique_count = ...          # 用 set() 去重并用 len() 求不重复元素个数（不要修改 raw_nums）
pairs = [("name", "Rain"), ("age", 18)]
person_dict = ...           # 用 dict() 把 pairs 转为字典
sample_person = {"name": "Rain", "age": 18}
person_keys = ...           # 用 list() 取出 sample_person 的全部键

# 基础题 5：字符码点与字节转换（04_chars_bytes_demo.py）
code_a = 65
char_a = ...                # 用 chr() 把码点 code_a 转为字符
rain_char = "雨"
rain_code = ...             # 用 ord() 求 rain_char 的 Unicode 码点
byte_values = [65, 66]
as_bytes = ...              # 用 bytes() 把 byte_values 转为不可变字节序列


# 基础题 6：从终端读两行整数文本，不显示提示语。
# 把两行文本分别转成整数后相加；第一行输出求和结果，第二行输出该结果的类型（type(...)）。
# 例如依次输入 12 和 3 时，输出两行：15 和 <class 'int'>。
# 自己写 input、int、type 和 print；转换结果请用新变量保存，保留原输入字符串。
# __name__ 与 NotImplementedError 占位的含义见第 1 章 exercises_01.py 基础题 4 的注释。
# 把入口里整行占位语句替换为你的代码，无须定义函数。
if __name__ == "__main__":
    raise NotImplementedError("练习待完成")


# ══════════════════════════════ 二、进阶练习（可选） ══════════════════════════════
# 前置知识：def 定义函数、return 返回值、if / elif / else、try / except（见第 1 章与 05_errors_parse_demo.py）。
# 若尚未学习函数或异常处理语法，可先跳过本节，不影响第 3 章基础验收。


def parse_int_safe(value, default=None):
    """【进阶】把 value 转为整数；若引发 ValueError 或 TypeError，返回 default。

    例如 ("42", None) -> 42，("3.5", 0) -> 0，(None, -1) -> -1。
    提示：参考 05_errors_parse_demo.py，只捕获 ValueError 和 TypeError。
    """
    raise NotImplementedError("练习待完成")


def parse_bool_text(text):
    """【进阶】不区分大小写解析布尔文本：'true' 返回 True，'false' 返回 False，其余返回 None。

    例如 'TRUE' -> True，'False' -> False，'yes' -> None。提示：str.lower()。
    """
    raise NotImplementedError("练习待完成")


def parse_based_int(text, base=10):
    """【进阶】按指定进制 base 把整数文本 text 转为 int。

    例如 ('101', 2) -> 5，('ff', 16) -> 255，('42',) -> 42。
    """
    raise NotImplementedError("练习待完成")


def pairs_to_dict_keys(pairs):
    """【进阶】先把 (键, 值) 对序列转为字典，再返回去重后的键列表（保持首次出现的顺序）。

    例如 [('a', 1), ('b', 2), ('a', 3)] -> ['a', 'b']。不用循环。
    """
    raise NotImplementedError("练习待完成")


def codes_to_text(codes):
    """【进阶】把 0～255 整数列表先转为 bytes，再按 UTF-8 解码为字符串。

    例如 [65, 66, 67] -> 'ABC'，[228, 189, 160] -> '你'。
    """
    raise NotImplementedError("练习待完成")


def parse_literal_safe(text, default=None):
    """【进阶】用 ast.literal_eval 解析 Python 字面量文本；遇到 ValueError 或 SyntaxError 返回 default。

    例如 '[1, 2]' -> [1, 2]，'1 + 2' -> default，'[1,' -> default。
    提示：可在本文件顶部或函数内写 from ast import literal_eval；不要使用 eval()。
    """
    raise NotImplementedError("练习待完成")
