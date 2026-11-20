# 【补充】第四章 Python 3.11 函数与方法速查

【必会】运行问候脚本用到的 `print` 和 `len` 见[第 1 章函数速查](../01-basic-syntax/functions.md)。

## 【了解】str.split

`sys.version.split()[0]` 先按空白拆分版本信息，再取首项。例如 `"3.11.9 extra"` 的首项是 `"3.11.9"`。两种分隔方式、参数与异常见[第 2 章的单词反转实例](../02-basic-data-types/functions.md)。

## 【必会】交互模式下的 exit

在 `>>>` 后输入 `exit()` 可退出交互环境，类似在 Node.js REPL 中输入 `.exit`。`exit(code=None)` 由标准库 `site` 通常在启动时提供。可选的 `code` 可按位置或关键字传入，默认为 `None`（正常退出），也可给整数退出状态。调用引发 `SystemExit`，无正常返回值；传入多余参数会抛 `TypeError`，禁用 `site` 时名字可能不存在。Windows 下也可按 `Ctrl+Z` 后回车。
