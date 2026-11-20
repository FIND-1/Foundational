# 第 1 章笔记

> 这里只写你自己的话：疑问、踩过的坑、和 JS 不一样的地方、“原来如此”的时刻。

## 疑问

- 练习时候,缩进很重要!

## 踩坑记录

<!-- 记下报错信息、原因和解决方法 -->

-修改 demo_syntax.py 实验代码影响了 demo 自检（demo_syntax.py）

把 bad_code 第 3 行原本故意写错的 2 个空格改成了 4 个空格后，代码变成了合法缩进，导致 test_demos_01.py 预期捕获 IndentationError 时失败。
跑目录级 pytest 时会连带跑 test_demos_*.py

## 和 JS 不一样的地方

- 方法使用不同,变量命名定义不一样,Python 有函数局部作用域，但 if 不创建块级作用域。

- `#!/usr/bin/python3` 叫做 Shebang（或者 Hashbang），作用是告诉操作系统：“请用 /usr/bin/python3 这个路径下的解释器来运行这个文件。”可以不写。
