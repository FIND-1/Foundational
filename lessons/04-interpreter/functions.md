# 第 4 章 · 函数与属性完整速查（Python 3.11）

前几章已讲的 API 不再重复，仅列出本章衔接点：

- 见[第 1 章函数速查](../01-basic-syntax/functions.md)：`print()`、`len()`、`str.startswith()`。
- 见[第 2 章函数速查](../02-basic-data-types/functions.md)：`str.split()`、`list()`。本章用 `sys.version.split()[0]` 按空白拆分版本信息字符串并取首项纯版本号。

---

## 【必会】交互模式下的 `exit()` 与 `quit()`

- **函数用途**：在 Python 交互式模式（REPL）中退出解释器，返回终端命令行。`exit` 与 `quit` 作用等价。
- **Python 3.11 完整签名**：`exit(code=None)`、`quit(code=None)`（实际类型均为 `_sitebuiltins.Quitter` 可调用对象）
- **全部参数与默认值**：
  - `code`（可选，默认 `None`）：退出状态码。`None` 或 `0` 表示正常退出；也可传非零整数退出码或提示字符串（传字符串时会输出到标准错误并以状态码 `1` 退出）。
- **参数限制**：`code` 可按位置或关键字（`exit(code=0)`）传入；最多传 1 个参数。
- **返回值及类型**：无正常返回值，调用后会先关闭标准输入并引发 `SystemExit` 异常以退出解释器。
- **常见错误与异常**：
  - `TypeError`：传入多于 1 个参数（如 `exit(0, 1)`）。
  - `NameError`：启动解释器时带 `-S`（禁用 `site` 模块）时，`exit` 与 `quit` 不会自动注入内置命名空间。
  - 易错点：在 `>>>` 中只输入 `exit` 不加括号，不会退出，只会打印提示文字 `Use exit() or Ctrl-Z plus Return to exit`。
- **基础示例**：
  ```python
  >>> exit()          # 退出交互模式（Windows 也可按 Ctrl+Z 再回车，Linux/macOS 按 Ctrl+D）
  ```
- **JS/TS 对照**：类似在 Node.js REPL 中输入 `.exit`（或连按两次 `Ctrl+C`）。
- **实际项目 / 惯用建议**：`exit()` / `quit()` 仅供交互式命令行使用；在 `.py` 脚本或生产代码中需要主动终止程序时，请改用 `sys.exit()`，不依赖 `site` 模块注入。

---

## 【必会】`sys.argv`

- **属性用途**：保存传递给 Python 脚本的命令行参数列表（第 1 章已在 `03_io_import_demo.py` 中初见，本章正式用于脚本参数读取）。
- **类型与访问方式**：模块属性 `list[str]`（需先 `import sys`），无函数调用参数。
- **元素约定**：
  - `sys.argv[0]`：脚本路径或名称；在交互模式或 `python -c` 模式下为 `""` / `"-c"`。
  - `sys.argv[1:]`：脚本名之后的所有命令行参数，每一项都是字符串 `str`（即便输入的是数字 `18`）。
- **常见错误与异常**：
  - `IndexError`：未传入参数时直接访问 `sys.argv[1]`。读取前应先检查 `len(sys.argv) > 1`（或用条件表达式保护）。
- **基础示例**：
  ```python
  import sys

  name = sys.argv[1] if len(sys.argv) > 1 else "Python 学习者"
  print("你好，", name, sep="")
  ```
- **JS/TS 对照**：对应 Node.js 的 `process.argv`，但 Node.js 的前两项是 `[node路径, 脚本路径]`（用户参数从 `process.argv.slice(2)` 开始），而 Python 的 `sys.argv` 不含解释器路径（用户参数从 `sys.argv[1:]` 开始）。
- **实际项目 / 惯用建议**：只有 1～2 个简单位置参数的小脚本可直接读 `sys.argv`；带 `--flag`、子命令、类型校验和自动 `--help` 的正式命令行工具，应使用标准库 `argparse`（或第三方 `typer` / `click`）。

---

## 【必会】`sys.version` 与 `sys.version_info`

- **属性用途**：查看当前运行脚本的 Python 解释器版本号与构建信息。
- **类型与访问方式**（需先 `import sys`，均为模块属性）：
  - `sys.version`：`str`，人类可读的完整版本与编译器信息，例如 `'3.11.9 (tags/v3.11.9:..., ...) [MSC v.1938 64 bit (AMD64)]'`。
  - `sys.version_info`：命名元组 `sys.version_info(major, minor, micro, releaselevel, serial)`（继承自 `tuple`），前三个字段为整数（如 `3`、`11`、`9`）。
- **常见错误与异常**：
  - `AttributeError`：拼错字段名（如写成 `sys.version_info.main`）。
  - 易错点：不要直接按字符串大小比较版本（`"3.9" >= "3.11"` 按字典序会误判为 `True`）；做版本判断必须用 `sys.version_info`。
- **基础示例**：
  ```python
  import sys

  print(sys.version.split()[0])               # '3.11.9'
  print(sys.version_info.major)               # 3
  print(sys.version_info >= (3, 11))          # True
  ```
- **JS/TS 对照**：`sys.version.split()[0]` 类似 Node.js 的 `process.versions.node`（`process.version` 带前缀 `v`）。
- **实际项目 / 惯用建议**：打印日志给人类看时用 `sys.version.split()[0]`；代码里做最低版本检查或兼容分支时，始终用 `sys.version_info >= (3, 11)`。

---

## 【了解】`sys.executable` 与 `sys.platform`

- **属性用途**：
  - `sys.executable`：当前正在运行的 Python 解释器可执行文件的绝对路径（无法获取时为空串 `""`）。
  - `sys.platform`：当前操作系统平台的标识符字符串。
- **类型与常见值**（需先 `import sys`，均为 `str`）：
  - `sys.executable`：例如 Windows 虚拟环境中为 `'E:\\...\\.venv\\Scripts\\python.exe'`。
  - `sys.platform`：Windows 上为 `'win32'`（64 位 Windows 同样返回 `'win32'`），Linux 上为 `'linux'`，macOS 上为 `'darwin'`。
- **基础示例**：
  ```python
  import sys

  print(sys.executable)                       # 确认是否在使用 .venv 里的解释器
  print(sys.platform == "win32")              # Windows 下为 True
  ```
- **JS/TS 对照**：分别对应 Node.js 的 `process.execPath` 与 `process.platform`（Node.js 在 Windows 下也返回 `'win32'`，macOS 也返回 `'darwin'`）。
- **实际项目 / 惯用建议**：遇到“明明装了依赖却报 `ModuleNotFoundError`”时，第一时间打印 `sys.executable` 核对当前到底用的是虚拟环境还是全局 Python；在脚本中启动同环境 Python 子进程时，也常用 `sys.executable` 代替写死 `"python"`。

---

## 【了解】`sys.exit()`

- **函数用途**：在脚本或程序中主动终止进程并向操作系统返回退出状态码。
- **Python 3.11 完整签名**：`sys.exit(status=None, /)`（需先 `import sys`）
- **全部参数与默认值**：
  - `status`（可选位置参数，默认 `None`）：退出状态。`None` 或 `0` 表示成功退出；非零整数（常用 `1`～`127`）表示异常退出；传入非整数非 `None` 对象（如错误提示字符串 `"缺少配置"`）时，解释器会将其打印到 `sys.stderr` 并以退出码 `1` 退出。
- **参数限制**：`status` 位于 `/` 之前，**只能按位置传入**，`sys.exit(status=0)` 或 `sys.exit(code=0)` 均会抛 `TypeError`；最多传 1 个参数。
- **返回值及类型**：无正常返回值，而是抛出 `SystemExit` 异常（`SystemExit` 继承自 `BaseException` 而非 `Exception`，因此普通的 `except Exception:` 不会误拦截退出，同时 `finally` 清理块仍能正常执行）。
- **常见错误与异常**：
  - `TypeError`：按关键字传参或传入多于 1 个参数。
- **基础示例**：
  ```python
  import sys

  try:
      sys.exit(0)
  except SystemExit as exc:
      print("退出码：", exc.code)  # 退出码： 0
  ```
- **JS/TS 对照**：对应 Node.js 的 `process.exit(code)`，但 `sys.exit()` 基于异常机制，允许外层 `finally` / `with` 完成资源清理后再真正结束进程。
- **实际项目 / 惯用建议**：只在命令行程序入口处调用 `sys.exit()`；库函数或底层业务函数出错时应抛具体异常（如 `ValueError`），把退出决策留给调用方。

---

## 【了解】`help()`

- **函数用途**：在交互模式中查询内置函数、模块、类型或语法关键字的在线文档（解释器启动欢迎语中的 `Type "help", ...` 即指此工具）。
- **Python 3.11 完整签名**：`help(request=...)`（内置 `help` 是 `_sitebuiltins._Helper` 实例，其 `__call__(*args, **kwds)` 转发至 `pydoc.help(request=...)`）
- **全部参数与默认值**：
  - `request`（可选，省略时进入交互式帮助系统）：任意对象（如 `print`、`str.split`、`sys`），或表示模块名/关键字的字符串（如 `"if"`、`"sys"`）。
- **参数限制**：最多传入 1 个参数，支持按位置或关键字 `request=` 传入。
- **返回值及类型**：`None`，文档内容直接输出到终端（内容较长时可能进入分页器，按 `q` 退出分页；进入交互式帮助系统后输入 `quit` 返回 `>>>`）。
- **常见错误与异常**：
  - `TypeError`：传入多于 1 个参数（如 `help(1, 2)`）。
  - `NameError`：以 `python -S` 禁用 `site` 启动解释器时不存在。
- **基础示例**：
  ```python
  >>> help(print)       # 查看 print() 的文档与参数说明
  >>> help("if")        # 查看 if 语法文档
  ```
- **JS/TS 对照**：Node.js REPL 没有内置对象文档查询函数，通常需查 MDN / TypeScript 类型定义。
- **实际项目 / 惯用建议**：仅用于交互式探索与快速查参数；不要在正式脚本里调用 `help()`。

---

更多示例见 Python 3.11 官方文档的[使用 Python 解释器](https://docs.python.org/zh-cn/3.11/tutorial/interpreter.html)、[sys 模块](https://docs.python.org/zh-cn/3.11/library/sys.html)和 [site 模块内置常量](https://docs.python.org/zh-cn/3.11/library/constants.html#constants-added-by-the-site-module)。
