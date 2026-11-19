# Python3 解释器

对应资料：`source/04-interpreter.html`，即[菜鸟教程：Python3 解释器](https://www.runoob.com/python3/python3-interpreter.html)。

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

第一个命令运行示例；第二个还向脚本传入 `Rain`。脚本可以通过 `sys.argv` 获取参数，第一项是脚本路径，其后的项是传入的参数。

示例使用 `import sys` 导入 Python 自带的 `sys` 模块。`len(sys.argv)` 统计参数列表的长度：当长度大于 1 时，`sys.argv[1]` 是传入的名字，否则使用默认名字。`a if 条件 else b` 表示条件成立时取 `a`，否则取 `b`。`print(..., sep="")` 让多个输出项之间不插入默认空格。

`sys.version` 是描述当前解释器版本的字符串，`.split()` 默认按空白字符拆成列表，`[0]` 取第一项，即示例中打印的版本号。

Linux 和 macOS 上直接执行脚本（例如 `./example.py`）时，需要文件具备执行权限，并设置合适的 Shebang；通过 `python example.py` 或 `python3 example.py` 运行则由命令直接指定解释器。
