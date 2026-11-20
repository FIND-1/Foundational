# Python3 解释器

[打开本章教程原文](../../../source/04-interpreter.html)（在 VS Code 中右键该文件，选择 Open with Live Server，或在浏览器中打开）。原教程的问候脚本已放进 `example.py`；原先的版本和参数演示保留为【补充】。

对应资料：`source/04-interpreter.html`，即[菜鸟教程：Python3 解释器](https://www.runoob.com/python3/python3-interpreter.html)。

原文顺序为交互式编程 → 脚本式编程；阅读后完成 [本章练习](practice.md)。【补充】示例函数的完整调用方式见 [函数速查](functions.md)。

Python 解释器负责读取并执行 Python 代码。可以在交互模式下逐句执行，也可以运行保存在 `.py` 文件里的代码。

## 查看 Python 版本

在 Windows PowerShell 中输入：

```powershell
python --version
```

如果 `python` 不可用，可以尝试 `py --version`。Linux 或 macOS 环境中也常使用 `python3 --version`。

## 交互式运行

在 PowerShell 输入 `python`，出现 `>>>` 后进入 Python 交互环境。输入表达式后回车即可看到结果：

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
python .\lessons\day01-python\04-interpreter\example.py
python .\lessons\day01-python\04-interpreter\example.py Rain
```

两个命令都会先运行教程中的 `Hello, Python!`；第二个还向【补充】示例传入 `Rain`。脚本可以通过 `sys.argv` 获取参数，第一项是脚本路径，其后的项是传入的参数。

【补充】示例使用 `import sys` 导入 Python 自带的 `sys` 模块。`len(sys.argv)` 统计参数列表的长度：当长度大于 1 时，`sys.argv[1]` 是传入的名字，否则使用默认名字。`a if 条件 else b` 是条件表达式：条件成立时取 `a`，否则取 `b`；这属于补充用法，本章练习不要求使用。`print(..., sep="")` 让多个输出项之间不插入默认空格。

【补充】`sys.version` 是描述当前解释器版本的字符串，`.split()` 默认按空白字符拆成列表，`[0]` 取第一项，即示例中打印的版本号。

Linux 和 macOS 上直接执行脚本（例如 `./example.py`）时，需要文件具备执行权限，并设置合适的 Shebang；通过 `python example.py` 或 `python3 example.py` 运行则由命令直接指定解释器。

## 学习验收

- [ ] 未开始
- [ ] 阅读完成
- [ ] 示例理解完成：能分清 PowerShell 与 Python 的 `>>>` 提示符。
- [ ] 基础练习通过：独立完成 [本章练习](practice.md)，按其中的验收条件核对结果。
- [ ] 进阶练习通过（可选，分层题待迁移）
- [ ] 本章完成：能回答理解检查中的问题，并独立得到基础练习要求的结果。
