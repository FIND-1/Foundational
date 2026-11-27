# 第 2 章 · 基本数据类型

阅读材料：[source/02-basic-data-types.html](../../source/02-basic-data-types.html)（菜鸟教程原文，在浏览器中打开）

## 学习步骤

1. **读原文**（约 20 分钟）：快速通读，不必记细节。最后一节「数据类型转换」只需浏览，第 3 章再细讲。
2. **读本页与函数速查**：看「要点」「和 JS 的差异」「原教程勘误」，首次遇到的函数与方法查 [functions.md](functions.md)；`print`、`type`、`len`、`isinstance` 等第 1 章已讲的函数查[第 1 章速查](../01-basic-syntax/functions.md)。
3. **跑 demo**：按下方顺序运行 5 个 `*_demo.py`，先预测再观察 `print()` 输出；标为 `# 拓展：` 的类定义、字典推导式和 `try...except` 只作观察，暂不要求手写。
4. **做基础练习**：完成 `exercises_02.py` 的「基础练习」（先写五组表达式，再独立写一段终端输入输出代码），用 pytest 验证（用法见 [pytest 教程](../tooling/pytest/README.md)）。
5. **选做进阶练习**：若已了解 `def` / `return`，可继续挑战「进阶练习」。
6. **阶段复盘**：学到哪一小节就顺手把自己的理解、验证、JS 差异和易错点记进 `notes.md`（按需选填，不提前填未学内容，也不仅凭测试通过就标记掌握）。

## 学习验收标准

请按实际掌握情况勾选（不能仅凭跑通 demo 就勾选“本章完成”）：

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能预测 `type(child) == A` 与 `isinstance(child, A)` 的不同结果，能说明列表和元组的可变性差异，并解释 `(42)` 与 `(20,)`、`{}` 与 `set()` 为什么类型不同、`"你好"` 为什么编码后有 6 个字节。
- [ ] 基础练习通过：独立完成六组题，`-m basic` 全部显示 `PASSED`，并能用自己的话说明每题用了什么语法、为什么这样写。例如，做完题 1 后，能解释 `bool_is_int` 与 `bool_exact_int` 为什么结果相反。
- [ ] 进阶练习通过（可选）
- [ ] 本章完成：读完原文、能解释示例、基础测试全过，并在 `notes.md` 记录易错点或自己的验证过程。

## 文件

| 文件 | 内容 |
| --- | --- |
| `01_numbers_demo.py` | 变量赋值、多变量赋值、标准数据类型、`type` 与 `isinstance`、`bool` 与 `int`、`del`、数值运算、数值字面量与复数 |
| `02_str_bool_demo.py` | 字符串截取、拼接、转义与不可变；布尔值、`bool()` 真假规则、逻辑与比较运算、条件判断 |
| `03_list_tuple_demo.py` | 列表截取、拼接、修改、步长切片、单词倒序；元组截取、不可变、单元素元组 |
| `04_set_dict_demo.py` | 集合创建、成员测试、四种集合运算；字典读写、视图、`dict()`、字典推导式、`get` |
| `05_bytes_demo.py` | `b` 前缀、`bytes()`、切片与拼接、`ord()`、`encode` / `decode`、`bytearray` |
| [functions.md](functions.md) | 本章首次引入的函数与方法完整速查（含签名、参数限制、异常与 JS 对照） |
| `exercises_02.py` | 基础练习（必做，写表达式和输入输出）+ 进阶练习（可选，写函数） |
| `test_exercises_02.py` | 练习的自动测试，不要修改 |
| `test_demos_02.py` | 5 个 Demo 的自检；运行全章 pytest 时执行 |
| `notes.md` | 个人学习笔记与错题复盘（记录理解、验证、差异、易错点与待解问题） |

## 运行

在仓库根目录打开 PowerShell。环境准备见[第 1 章 README 的「运行」](../01-basic-syntax/README.md#运行)。

```powershell
.\.venv\Scripts\python.exe .\lessons\02-basic-data-types\01_numbers_demo.py
.\.venv\Scripts\python.exe .\lessons\02-basic-data-types\02_str_bool_demo.py
.\.venv\Scripts\python.exe .\lessons\02-basic-data-types\03_list_tuple_demo.py
.\.venv\Scripts\python.exe .\lessons\02-basic-data-types\04_set_dict_demo.py
.\.venv\Scripts\python.exe .\lessons\02-basic-data-types\05_bytes_demo.py

.\.venv\Scripts\python.exe .\lessons\02-basic-data-types\exercises_02.py   # 手动体验基础题 6，输入一行文本后回车

.\.venv\Scripts\python.exe -m pytest lessons/02-basic-data-types -m basic -v   # 只测基础练习
.\.venv\Scripts\python.exe -m pytest lessons/02-basic-data-types -v            # 测全部练习和 Demo 自检
```

集合的打印顺序每次运行可能不同，Demo 中用 `sorted()` 给出固定顺序的对照。`PASSED`、`FAILED`、`SKIPPED` 和 `deselected` 的含义与处理方法见[第 1 章 README 的「运行」](../01-basic-syntax/README.md#运行)。

## 要点（按原文顺序）

1. **变量赋值**：变量不需要声明，第一次赋值时创建；变量没有类型，类型属于它指向的对象。
2. **多个变量赋值**：`a = b = c = 1` 让三个名字指向同一个对象；`a, b, c = 1, 2, "runoob"` 按位置分别赋值。
3. **标准数据类型**：6 种标准类型 + `bool`（`int` 的子类，常单列）。不可变：`Number`（`int`、`float`、`bool`、`complex`）、`String`、`Tuple`（以及 `bytes`）；可变：`List`、`Set`、`Dictionary`。
4. **数字**：`int`（只有一种，长度不受固定位数限制）、`float`、`bool`、`complex`。`type()` 只认具体类型，`isinstance()` 把子类也算作父类。
5. **bool 与 int**：`bool` 是 `int` 的子类，`True == 1`、`True + 1 == 2`；`is` 比较对象身份，不比较值。
6. **del**：`del a, b` 删除名字的绑定，之后再访问会抛 `NameError`。
7. **数值运算**：`+ - * / // % **`；`/` 总得到 `float`，`//` 向下取整；`int` 与 `float` 混合计算时结果为 `float`。
8. **数值字面量**：`0o` 八进制、`0x` 十六进制、`0b` 二进制，十进制整数不允许前导零；`e` 表示 10 的幂；复数写作 `a + bj` 或 `complex(a, b)`。
9. **字符串**：截取 `变量[头:尾]`，`+` 拼接、`*` 重复，`r` 前缀不转义；没有单独的字符类型；不可修改单个字符。
10. **布尔类型**：只有 `True`、`False`；`and`、`or`、`not` 组合条件；`None`、`False`、数值零、空序列、空映射为假，其余为真；`if x:` 按同样规则判断。
11. **列表**：`[]` 写成，元素可不同类型、可嵌套；可索引、切片、拼接、重复；元素和切片都可以赋值修改；切片第三个参数是步长，负数表示逆向。
12. **元组**：`()` 写成，与列表类似但元素不能修改；可以包含可变对象；空元组 `()`，单元素元组必须加逗号 `(20,)`。字符串、列表、元组都是序列。
13. **集合**：`{a, b}` 或 `set()` 创建，元素不重复、不保证顺序；空集合只能用 `set()`；`-`、`|`、`&`、`^` 分别是差集、并集、交集、对称差集。
14. **字典**：`{键: 值}` 映射类型，键必须不可变（可哈希）且唯一；Python 3.7 起保持插入顺序；`keys()`、`values()` 返回视图；`dict()` 可从键值对序列或关键字参数构建；`{x: x**2 for x in ...}` 是字典推导式。
15. **bytes**：不可变的字节序列，元素是 0～255 的整数；`b"..."` 或 `bytes(文本, encoding=...)` 创建；支持切片、拼接；与字符比较时先用 `ord()` 转成整数。
16. **数据类型转换**：`int()`、`float()`、`str()`、`list()` 等用类型名转换，返回新对象。详见[第 3 章](../03-type-conversion/README.md)。

## 【补充】和 JS 的差异

| 主题 | JS | Python | 注意 |
| --- | --- | --- | --- |
| 声明变量 | `let` / `const` / `var` | 直接赋值 | 没有常量关键字，全大写只是约定 |
| 解构赋值 | `const [a, b] = [1, 2]` | `a, b = 1, 2` | 两边数量必须一致，否则 `ValueError` |
| 查看类型 | `typeof x` | `type(x)` | `typeof []`、`typeof null` 都是 `"object"`；Python 返回精确类型 |
| 继承判断 | `x instanceof A` | `isinstance(x, A)` | `isinstance` 也能判断 `int`、`str` 等内置类型 |
| 数字类型 | `number` + `bigint` | `int`、`float`、`complex`、`bool` | `int` 任意精度 |
| 取余 | `-7 % 3 === -1` | `-7 % 3 == 2` | Python 结果与除数同号 |
| 相等 | `===`（`==` 会隐式转换） | `==` 比较值，`is` 比较身份 | Python 的 `1 == "1"` 为 `False` |
| 删除 | `delete obj.key` 删属性 | `del name` 删变量绑定 | 删字典的键用 `del d[key]` |
| 字符串替换 | `replace` 默认替换第一处 | `replace` 默认替换全部 | 可用第三个参数限制次数 |
| 真值 | `[]`、`{}` 为真 | 空列表、空字典、空集合、空元组为假 | `"0"`、`"False"` 在两边都为真 |
| 逻辑运算 | `&&` `\|\|` `!` | `and` `or` `not` | |
| 列表 | `Array` | `list` | `push` 返回新长度，`append` 返回 `None` |
| 元组 | 无（TS 有 `readonly [A, B]`） | `tuple` | 单元素必须写逗号 `(20,)` |
| 集合 | `new Set([1, 2])` | `{1, 2}` / `set()` | 运算符 `\| & - ^` 直接求并、交、差、对称差 |
| 字典 | 对象 `{}` / `Map` | `dict` | 键可以是整数、元组；缺键用 `[]` 读取会抛 `KeyError` |
| 读取默认值 | `obj.key ?? "默认"` | `d.get("key", "默认")` | |
| 字节 | `Uint8Array` | `bytes`（不可变）/ `bytearray`（可变） | |
| 编码解码 | `TextEncoder` / `TextDecoder` | `str.encode()` / `bytes.decode()` | 默认都是 UTF-8 |

## 【补充】原教程勘误与不推荐写法

- **类型数量**：原文说“6 种标准数据类型，以及 bool”，随后列出 7 项，又把 bool 计入“不可变数据（4 个）”。按列表记 7 种即可。
- **`type(A()) == A`**：可以运行，但只想判断“是不是某类或其子类”时应使用 `isinstance()`；确实要求精确类型时，惯用写法是 `type(x) is A`。
- **`1 is True`**：原文用它说明身份比较，Python 3.8 起对字面量用 `is` 会产生 `SyntaxWarning`。比较值用 `==`，`is` 只用于 `None`、`True` 等单例或身份判断；Demo 先把数字放进变量再演示。
- **`del var1[, var2[, var3[...., varN]]]`**：方括号是语法说明里的“可选”记号，不是能运行的代码，实际写 `del var1, var2`。
- **“布尔值转换成字符串时 True 转成 1”**：错误。`str(True)` 得到 `"True"`；转成整数、浮点数才分别得到 `1`、`1.0`。
- **“布尔类型可以和字符串比较，True 视为 1”**：`True == "1"` 得到 `False`，`True < "a"` 会抛 `TypeError`。Python 不会在比较时把字符串转成数字。
- **列表步长例子缺代码**：原文提到“索引 1 到索引 4、步长为 2”的实例，但正文没有给出代码，`03_list_tuple_demo.py` 补了 `letters[1:4:2]`。
- **`reverseWords(input)`**：参数 `input` 遮住了内置函数 `input`，函数名和局部变量用的是 `camelCase`。按 PEP 8 应写成 `reverse_words(text)`。`split(" ")` 遇到连续空格会产生空字符串，按任意空白拆分应写 `split()`。
- **“可以把字符串看作一种特殊的元组”**：只是说二者都是不可变序列。字符串的元素只能是字符，还有大量专用方法；元组可以放任意对象。
- **“集合输出”**：原文给出的集合打印顺序只是一次运行的结果，每次运行可能不同，不要依赖它。
- **“键必须使用不可变类型”**：更准确地说是**可哈希**。包含列表的元组虽然是元组，也不能作字典的键。
- **`#!/usr/bin/python3`**：Shebang 只在类 Unix 系统直接执行脚本时有用，Windows 上用 `python 文件名` 运行时可以不写。
