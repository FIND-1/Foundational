# Python3 基础语法

参考：[菜鸟教程：Python3 基础语法](https://www.runoob.com/python3/python3-basic-syntax.html)

在项目根目录的 PowerShell 中运行示例：

```powershell
python .\lessons\day01-python\01-basic-syntax\example.py
```

`example.py` 是综合示例，以下文件按知识点拆分，均可独立运行；将上面命令中的文件名替换即可：

- `01-identifiers-comments.py`：标识符、关键字和注释。
- `02-blocks-and-lines.py`：缩进、代码块和多行语句。
- `03-numbers-and-strings.py`：数字、字符串和切片。
- `04-input-output-imports.py`：输入、输出、导入和命令行参数。

## 编码与运行

Python 3 源文件默认使用 UTF-8，可以直接编写中文。第一行 `#!/usr/bin/env python3` 是 Shebang，用于类 Unix 系统直接执行脚本时寻找解释器；通过 `python 文件名.py` 运行时不需要它。

## 标识符和关键字

变量、函数等的名字称为标识符。名字不能以数字开头，不能包含连字符，也不能使用 `if`、`for` 等关键字；大小写不同的名字也不同。Python 支持中文标识符，实际项目中通常使用有意义的英文名，如 `user_name`。

**关键字**是 Python 语法中有特殊用途的词。例如 `if` 用于条件判断，`for` 用于循环，因此不能把它们当作普通变量名。`keyword` 则是 Python 自带的标准库模块，可以帮助我们查看和判断这些关键字，无需额外安装。

```python
import keyword  # 导入模块，之后才能通过 keyword.名称 使用它的功能

print(keyword.kwlist)  # 当前 Python 版本的关键字列表
```

例如，`user_name` 可以作为变量名；`2name` 以数字开头，不能作为变量名；`if` 是关键字，也不能作为变量名。

## 注释、缩进和代码块

`#` 后面是单行注释，解释器不会执行。三引号创建多行字符串，放在模块、函数或类的开头可作为文档字符串，并非真正的注释。

Python 通过缩进划分代码块，冒号后的同一级语句应保持相同缩进，通常使用 4 个空格。空行用于提高可读性，不代替缩进。

示例中的 `if`、`elif`、`else` 用于按条件选择代码块：例如分数至少为 90 时执行第一段，否则依次判断其他条件。`>=` 表示大于或等于；`len(user_name)` 返回字符串的字符数，`> 0` 判断字符数是否大于 0。`"if" in keyword.kwlist` 中的 `in` 判断字符串是否在关键字列表中。

## 多行语句

括号 `()`、列表 `[]`、字典 `{}` 内可以自然换行；也可以用反斜杠续行，但括号通常更易读。同一行的多条简单语句可以用分号分开，一般建议分行写。

## 字符串和切片

单引号、双引号均可表示字符串，三引号可以写多行文本。索引从 0 开始，负数索引从末尾开始。切片格式为 `文字[开始:结束:步长]`，包含开始位置，不包含结束位置；例如 `"123456789"[1:8:2]` 得到 `2468`。`\n` 表示换行，原始字符串 `r"..."` 保留反斜杠。

数字包括整数 `int`、浮点数 `float`、布尔值 `bool` 和复数 `complex`；详细的类型和操作见 `02-basic-data-types`。

## 输入、输出与导入

`input()` 等待输入并返回字符串；`print()` 默认换行，可用 `end` 指定结尾。`import math` 用模块名访问成员，`from math import sqrt` 则直接导入成员。`help(print)` 可以在交互环境查看帮助。

示例额外使用了 Python 自带的 `math` 数学模块：`math.sqrt(16)` 计算 16 的平方根，结果为 `4.0`；`from math import sqrt` 后可写成 `sqrt(16)`。`print("a", "b", sep=" | ")` 使用 `sep` 设置多个输出项之间的分隔符，结果为 `a | b`。`sys` 也是 Python 自带模块，提供与解释器相关的信息；使用前先写 `import sys`。

示例中的 `input()` 以注释形式保留，避免运行时等待；想练习时可自行取消注释。

`sys.argv` 保存脚本路径和命令行参数，`sys.path` 保存模块搜索路径。参数应跟在脚本路径后，例如 `python .\lessons\day01-python\01-basic-syntax\04-input-output-imports.py Rain`。
