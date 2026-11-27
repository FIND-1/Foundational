"""第 1 章 · 语法骨架：编码、标识符、关键字、注释、缩进与多行语句。

用途：直观演示第 1 章的语法规则与 Python / JS 差异。
运行（仓库根目录，已激活 .venv）：python lessons/01-basic-syntax/01_syntax_demo.py
预期结果：变量 count 和 Count 分别打印 1 和 2，缩进代码块打印 big，两种续行都得到 6。末尾演示缩进错误的提示。
"""

# 格式：print(值1, 值2) -> 默认空格分隔并换行；变量 = 值 绑定对象；import 模块名 载入模块
# 注意：载入模块后用“模块名.名称”读取内容；字符串用引号包住
import keyword

# ── 1. 编码 ───────────────────────────────────────────────────────────
# 注意：Python 3 源文件默认 UTF-8，直接写中文即可（与 JS 一样）
# 拓展：# -*- coding: cp-1252 -*- 仅在非 UTF-8 文件中需要，实际几乎不用


# ── 2. 标识符 ─────────────────────────────────────────────────────────
# 格式：字符串.isidentifier() -> bool（拼写合规返回 True，否则 False）
# 注意：字母或下划线开头，可含字母/数字/下划线，区分大小写；与 JS 不同，不允许使用 $
valid_name = "user_name"
invalid_digit = "2nd_place"
invalid_dollar = "$price"
chinese_name = "姓名"

print("标识符检查：", valid_name.isidentifier(), invalid_digit.isidentifier(), invalid_dollar.isidentifier())
print("中文标识符：", chinese_name.isidentifier())

count = 1
Count = 2                              # 区分大小写：这是两个不同的变量
print("区分大小写：", count, Count)

# 格式：keyword.iskeyword(字符串) -> bool（检查是否为保留关键字）
# 注意："class" 拼写合规，但同时是关键字，不能作变量名，所以两次检查都为 True
word = "class"
print("class 符合标识符拼写规则吗？", word.isidentifier(), "是关键字吗？", keyword.iskeyword(word))

# 拓展：PEP 8（官方代码风格）命名约定与 JS 的差异：
#   变量/函数：snake_case（JS 用 camelCase）  -> user_name、calculate_area()
#   类：      PascalCase（与 JS 相同）        -> StudentInfo
#   常量：    全大写（仅约定，语言不禁止修改） -> MAX_SIZE = 1024
#   _name     单下划线开头表示“内部使用”（仅约定，JS 的 #private 是强制的）
#   __name    类中会触发名称改写，学到类时再展开


# ── 3. 关键字 ─────────────────────────────────────────────────────────
# 格式：len(列表) -> 项数；列表[:6] -> 前 6 项
# 注意：Python 3.11 共 35 个关键字；True、False、None 首字母大写（对应 JS 的 true、false、null）
kw_count = len(keyword.kwlist)
print("关键字总数：", kw_count)
print("前 6 个关键字：", keyword.kwlist[:6])

# 注意：逻辑运算用 and、or、not、elif（对应 JS 的 &&、||、!、else if）
# 拓展：keyword.softkwlist 是软关键字（如 match、case），只在特定语法中生效
print("软关键字：", keyword.softkwlist)


# ── 4. 注释 ───────────────────────────────────────────────────────────
# 格式：# 单行注释；三引号 '''...''' 或 """...""" 放文件/函数/类首行作文档说明（docstring，类似 JSDoc）
# 注意：Python 没有 // 和 /* */
# 拓展：__doc__ 保存文件开头 docstring；字符串.splitlines()[0] 按行拆分后取第一行
print("本文件 docstring 开头：", __doc__.splitlines()[0])


# ── 5. 行与缩进 ───────────────────────────────────────────────────────
# 格式：if 条件: 缩进块 / else: 缩进块
# 注意：用“冒号 + 缩进”代替 JS 的 {}；同一代码块缩进必须一致（PEP 8 约定 4 空格）
x = 10
if x > 5:
    size = "big"
else:
    size = "small"
print("缩进代码块结果：", size)

# 格式：pass -> 空语句占位（JS 可直接写 {}）
if x < 0:
    pass


# ── 6. 多行语句 ───────────────────────────────────────────────────────
# 格式：行尾用 \ 续行，或把长表达式放进 () / [] / {} 内自动换行
# 注意：Python 以换行结束语句，不写分号，无 JS 的自动分号插入（ASI）问题
# 方式 A：反斜杠续行
total_slash = 1 + \
              2 + \
              3

# 场景：长表达式优先用括号换行，每行可写注释，也不怕 \ 后误加空格（两种写法都得 6）
total_paren = (
    1
    + 2
    + 3
)
# 格式：[元素, 元素, ...] -> 有序列表（类似 JS 数组）
items = ["item_one", "item_two",
         "item_three"]
print("多行求和：", total_slash, total_paren, "列表长度：", len(items))

# 拓展：in / not in 检查成员；字符串.startswith(前缀) 类似 JS 的 startsWith；set <= set 检查子集
print("只有首字母大写的 True 是关键字：", "True" in keyword.kwlist and "true" not in keyword.kwlist)
print("文档说明以「第 1 章」开头：", __doc__.startswith("第 1 章"))
print("这四个关键字都在列表中：", {"and", "or", "not", "elif"} <= set(keyword.kwlist))

# ── 拓展：用 compile() 与 try/except 验证缩进报错 ──────────────────────
# 注意：\n 表示换行；变量可重新赋值，编译时取最后一次赋的值（第三行 2 空格与前两行不对齐）
bad_code = "if True:\n    a = 1\n    b = 2\n"
bad_code = "if True:\n    a = 1\n  b = 2\n"
# 格式：compile(源码, 显示文件名, "exec") -> 编译多行源码；try / except 异常类型 as error / else
# 拓展：发生 IndentationError 进入 except（error.msg 存原因），无错才进入 else
try:
    compile(bad_code, "<bad>", "exec")
except IndentationError as error:
    print("【进阶】成功捕获缩进错误：", error.msg)
else:
    print("【进阶】这段代码缩进正确，可以编译。")
