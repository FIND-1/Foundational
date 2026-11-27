# 第 4 章 · Python3 解释器

学习模式：Quick Review（速览学习）

阅读材料：[菜鸟教程原文 HTML](../../source/04-interpreter.html)（在浏览器中打开）

## 学习步骤

1. 按「环境配置与版本查看 → 交互式编程 → 脚本式编程」阅读原文，对照下方要点。
2. 用仓库的 Python 3.11 启动 REPL，完成一次表达式求值和一次多行输入，再回到 PowerShell 运行脚本。
3. 自答「理解检查」。命令行参数和版本信息可查阅[函数速查](functions.md)。

## 要点（按原文顺序）

1. **配置与版本**。解释器读取并执行 Python 代码。系统通过 `PATH` 中的目录寻找命令。本仓库用 `.venv` 隔离依赖，直接运行虚拟环境里的解释器即可确认版本。
2. **交互式编程**。直接启动解释器进入 REPL。`>>>` 等待新输入，`...` 等待当前代码块的后续行。多行块输入完成后再按一次空回车。`exit()` 退出交互环境，Windows 还可用 `Ctrl+Z` 再按回车，Linux/macOS 可用 `Ctrl+D`。
3. **脚本式编程**。先把代码保存为 `.py`，再按「解释器、脚本路径」的顺序运行。Linux/macOS 可用首行 `#!/usr/bin/env python3` 和 `chmod +x hello.py`，然后执行 `./hello.py`。直接运行时 `__name__` 为 `"__main__"`，导入时为模块名。

## 【补充】Node.js 对照与原文勘误

- 在 Node.js 中，用 `node` 进入 `>` 提示符，用 `.exit` 或连续两次 `Ctrl+C` 退出。`node app.js` 与 `python app.py` 的脚本入口类似。`.venv` 和 `node_modules` 都支持项目级依赖隔离，`.venv` 还指定项目的解释器。
- 原文的 Linux `PATH` 示例应添加 `/usr/local/python3/bin` 目录。需要传给子进程时使用 `export`，需要跨终端保留时写入 shell 配置。Windows 的 `set path=...` 属于当前 CMD 会话，PowerShell 对应 `$env:Path += ";C:\Python311"`。原文使用早期 Python 版本演示，本仓库以 Python 3.11 为准。
- 示例按 `print("Hello, Python!")` 和 `if flag:` 格式书写。Shebang 惯用 `#!/usr/bin/env python3`。Windows 可直接调用解释器，也可以通过支持 Shebang 的 `py` 启动器运行脚本。

## 运行

在仓库根目录打开 PowerShell。环境准备见[第 1 章「运行」](../01-basic-syntax/README.md#运行)。

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe
```

版本命令应显示 `Python 3.11.x`。进入 REPL 后，只输入提示符右侧的代码。在 `print` 后的 `...` 提示符处直接按回车提交多行代码块。

```python
>>> 1 + 2
3
>>> flag = True
>>> if flag:
...     print("flag 条件为 True!")
...
flag 条件为 True!
>>> exit()
```

回到 PowerShell 后，把下面的代码保存为 `lessons/playground/interpreter_hello.py`。第一行输出问候语，第二行输出解释器给当前脚本设置的 `__name__`。

```python
print("Hello, Python!")
print(__name__)
```

```powershell
.\.venv\Scripts\python.exe .\lessons\playground\interpreter_hello.py
```

预期依次输出 `Hello, Python!` 和 `__main__`。

### 理解检查

1. `>>>` 和 `...` 分别表示什么？多行 `if` 什么时候开始执行？
2. 在 Windows 如何从 REPL 返回 PowerShell？只输入 `exit` 会看到什么？
3. 为什么脚本命令要在 PowerShell 输入？直接执行和被导入时，`__name__` 各是什么？

## 学习验收标准

- [ ] 本章完成：能独立在 REPL 中求值并退出，再从 PowerShell 运行一个 `.py` 文件，说明两种运行方式的区别。
