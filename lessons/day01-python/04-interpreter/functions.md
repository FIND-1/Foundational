# 【补充】第四章 Python 3.11 函数与方法速查

`print(*objects, sep=' ', end='\n', file=None, flush=False)` 与 `len(obj, /)` 的完整参数、默认值、限制、返回值、错误和示例见[官方文档](https://docs.python.org/zh-cn/3.11/library/functions.html)。【必会】先理解最常用的输出和长度判断。

## 【了解】str.split

`str.split(sep=None, maxsplit=-1)`：`sep` 默认为 `None`，表示按连续空白拆分并忽略两端空白；也可指定非空分隔字符串。`maxsplit` 默认 `-1` 表示不限制，否则限定最多分割次数。返回字符串列表；空字符串分隔符抛 `ValueError`，参数类型不对抛 `TypeError`。例 `"3.11.9 extra".split()[0]` 得 `"3.11.9"`。本章示例先用 `sys.version.split()` 拆分，再用 `[0]` 取第一项。

## 【必会】交互模式下的 exit

`exit(code=None)` 是通常由 Python 的 `site` 模块为交互环境提供的退出辅助对象：`code` 可省略，默认为 `None`；也可给退出状态。调用会引发 `SystemExit` 退出解释器，正常情况下不会继续返回。此辅助对象在禁用 `site` 的环境中可能不存在；在 Windows 交互环境也可按 `Ctrl+Z` 后回车。例：在 `>>>` 后输入 `exit()`。
