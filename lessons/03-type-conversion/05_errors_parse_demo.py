"""第 3 章 · 拓展：转换失败、异常处理与安全解析。

用途：区分 ValueError 与 TypeError，演示用 try / except / else 处理失败转换，以及对比 eval() 与 ast.literal_eval()。
运行（仓库根目录，已激活 .venv）：python lessons/03-type-conversion/05_errors_parse_demo.py
预期结果：'12' 转换成功，'3.5' 和 'abc' 触发 ValueError，None 触发 TypeError；
eval("1 + 2") 得 3；literal_eval 解析 "[1, 2, 3]" 得列表，拒绝 "1 + 2"。
"""

# 拓展：from 模块 import 名称（见第 1 章 03_io_import_demo.py）；ast 是解析 Python 语法的标准库模块
from ast import literal_eval 


# ── 1. 拓展：ValueError 与 TypeError 的区别 ───────────────────────────
# 注意：for 遍历见第 2 章 04_set_dict_demo.py；try / except / else 见第 1 章 01_syntax_demo.py
# 格式：f"{变量!r}" -> 在 f-string 中用 repr(变量) 格式插入（字符串会带上引号，方便看清内容）
# 注意：类型对了但内容不合格式（如 "3.5"、"abc"）抛 ValueError；类型本身就不支持（如 None）抛 TypeError
parsed_values = []
for value in ("12", "3.5", "abc"):
    try:
        converted = int(value)
    except ValueError:
        print(f"{value!r} 不是有效的整数字符串（ValueError）")
    else:
        parsed_values.append(converted)
        print(f"{value!r} 转成整数：{converted}")

try:
    _ = int(None)
except TypeError as error:
    print("None 的类型不能直接转成整数（TypeError）：", error)


# ── 2. 拓展：eval() 与安全风险 ────────────────────────────────────────
# 格式：eval(表达式字符串) -> 执行 Python 表达式并返回结果（类似 JS 的 eval()，但只支持单个表达式，不支持赋值等语句）
# 注意：严禁对不可信输入使用 eval()；普通数字转换直接用 int() / float()，完整参数与异常见 functions.md
text = "1 + 2"
eval_result = eval(text)
print("原始文本：", text, type(text))                     # 1 + 2 <class 'str'>
print("eval 求值：", eval_result, type(eval_result))      # 3 <class 'int'>
print("比较与拼接：", eval("10 > 5"), eval("'a' + 'b'"))  # True ab

# 注意：eval() 默认可读取当前作用域的变量（也是安全风险来源之一）
price = 100
quantity = 3
print("读取变量计算：", eval("price * quantity"))         # 300


# ── 3. 拓展：用 ast.literal_eval() 解析 Python 字面量 ──────────────────
# 格式：literal_eval(字面量字符串) -> 解析后的 Python 对象（支持数字、字符串、容器、布尔、None 等字面量）
# 场景：把 Python 字面量文本还原为数据对象（类似 JS 的 JSON.parse()；标准 JSON 仍用 json.loads()）
# 注意：literal_eval() 不执行任意代码，但不代表完全没有安全风险；过大或嵌套过深的输入可能导致资源耗尽
list_text = "[1, 2, 3]"
values = literal_eval(list_text)
print("list() 会逐字符拆分：", list(list_text))         # ['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
print("literal_eval 还原列表：", values, type(values))  # [1, 2, 3] <class 'list'>
print("还原元组与字典：", literal_eval("(1, 2)"), literal_eval("{'name': 'Rain'}"))  # (1, 2) {'name': 'Rain'}
print("还原集合与空值：", literal_eval("{1, 2, 2}"), literal_eval("None"))           # {1, 2} None

# 注意：bool("False") 按非空判真得 True，literal_eval("False") 按字面量解析得 False
print("bool vs literal_eval：", bool("False"), literal_eval("False"))  # True False

# 注意：普通算术表达式（如 "1 + 2"）和函数调用不是字面量，会抛出 ValueError
try:
    _ = literal_eval("1 + 2")
except ValueError as error:
    print("不支持算术表达式（ValueError）：", error)
