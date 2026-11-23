# Python3 解释器

[打开本章教程原文](../../../source/04-interpreter.html)（在 VS Code 中右键该文件，选择 Open with Live Server，或在浏览器中打开）。原教程的问候脚本已放进 `example.py`；原先的版本和参数演示保留为【补充】。

对应资料：`source/04-interpreter.html`，即[菜鸟教程：Python3 解释器](https://www.runoob.com/python3/python3-interpreter.html)。

原文顺序为交互式编程 → 脚本式编程；阅读后完成 [本章练习](practice.md)。【补充】示例函数的完整调用方式见 [函数速查](functions.md)。

Python 解释器负责读取并执行 Python 代码。可以在交互模式下逐句执行，也可以运行保存在 `.py` 文件里的代码。

## 查看 Python 版本

在仓库根目录的 PowerShell 中输入：

```powershell
.\.venv\Scripts\python.exe --version
```

【补充】在已激活 `.venv` 的终端中，`python` 指向这个虚拟环境的解释器。要查看系统安装的版本，Windows 通常可用 `py --version`，Linux 或 macOS 常用 `python3 --version`。

## 交互式运行

在同一个 PowerShell 输入 `.\.venv\Scripts\python.exe`。看到 `>>>` 后输入下列 Python 语句，按回车观察结果。

```python
>>> 1 + 2
3
>>> print("你好，Python")
你好，Python
```

`>>>` 是解释器提示符，不需要自己输入。输入 `exit()` 退出；Windows 下也可以按 `Ctrl+Z` 后回车，返回 PowerShell。

## 脚本式运行

在项目根目录执行：

```powershell
.\.venv\Scripts\python.exe .\lessons\day01-python\04-interpreter\example.py
.\.venv\Scripts\python.exe .\lessons\day01-python\04-interpreter\example.py Rain
```

两个命令都会先运行教程中的 `Hello, Python!`；第二个还向【补充】示例传入 `Rain`。脚本可以通过 `sys.argv` 获取参数，第一项是脚本路径，其后的项是传入的参数。

【补充】原文把问候语写成 `print ("Hello, Python!");`，脚本采用 `print("Hello, Python!")`。运行这两种写法，终端都会显示同一句问候语。

【补充】读参数示例时，分别预测传入 `Rain` 和省略参数时会执行哪个分支，再看条件表达式如何选出同一个名字。`sys.argv` 的首次示例见[第 1 章的命令行参数](../01-basic-syntax/03_io_import_demo.py)。

Linux 和 macOS 上直接执行脚本（例如 `./example.py`）时，需要文件具备执行权限，并设置合适的 Shebang；通过 `python example.py` 或 `python3 example.py` 运行则由命令直接指定解释器。

## 学习验收

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能分清 PowerShell 与 Python 的 `>>>` 提示符。
- [ ] 基础练习通过：独立完成 [本章练习](practice.md)，按其中的验收条件核对结果。
- [ ] 进阶练习通过（可选，分层题待迁移）
- [ ] 本章完成：能回答理解检查中的问题，并独立得到基础练习要求的结果。
