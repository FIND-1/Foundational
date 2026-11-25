"""第 3 章 · 拓展：转换失败、异常处理与安全解析。

用途：区分 ValueError 与 TypeError，演示用 try / except / else 处理失败转换，以及对比 eval() 与 ast.literal_eval()。
运行（仓库根目录，已激活 .venv）：python lessons/day01-python/03-type-conversion/05_errors_parse_demo.py
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
# 格式：eval(表达式字符串) -> 执行 Python 表达式并返回结果（类似 JS 的 eval()）
# 注意：切勿对不可信的外部输入使用 eval()，它能执行任意代码；解析数字用 int() / float()
eval_result = eval("1 + 2")
print("eval 计算表达式：", eval_result, type(eval_result))  # 3 <class 'int'>


# ── 3. 拓展：用 ast.literal_eval() 安全解析字面量 ─────────────────────
# 格式：literal_eval(字面量字符串) -> 解析后的 Python 对象（只支持数字、字符串、列表、元组、字典、集合、布尔、None）
# 场景：把形如 "[1, 2, 3]" 的 Python 字面量文本还原为容器对象（JSON 数据仍优先用标准库 json.loads()）
# 注意：不执行函数调用或算术表达式，遇到 "1 + 2" 会抛 ValueError；对不可信输入仍需限制大小和深度
values = literal_eval("[1, 2, 3]")
print("解析列表字面量：", values, type(values))  # [1, 2, 3] <class 'list'>

try:
    _ = literal_eval("1 + 2")
except ValueError:
    print("literal_eval 拒绝算术表达式（ValueError）")
