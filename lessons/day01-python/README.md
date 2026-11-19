# Day 01：Python 基础

课程顺序与菜鸟教程目录一致。每个课程目录中有讲解、运行命令和独立示例。

1. [基础语法](01-basic-syntax/README.md)
2. [基本数据类型](02-basic-data-types/README.md)
3. [数据类型转换](03-type-conversion/README.md)
4. [解释器](04-interpreter/README.md)

截图中的后续课程依次为注释、运算符、数字、字符串、列表和元组；目前 `source` 中尚未提供这些课程的页面。根目录的 `str.py` 是已有的字符串切片练习。

`str.py` 当前大部分练习已被注释，实际执行的最后一行通过 `import sys` 导入标准库模块，用 `sys.stdout.write(x + '\n')` 向终端写入文本；`\n` 表示换行。分号将同一行的简单语句分开。`sys.stdout.write()` 返回写入的字符数，脚本没有打印这个返回值。
