# 第 1 章笔记

> 定位：只记录**我理解了什么、验证了什么、踩了什么坑**（不摘抄教材）。
> 阶段性记录：学到哪一小节就记哪一小节，按需选填，不必每节写满五部分；不提前填未学内容，也不仅凭测试通过就标记掌握。

## 1. 核心知识点

<!-- 用自己的话解释是什么、有什么用、适用条件 -->

- **语法骨架**：Python 3 源文件默认 UTF-8；用 `:` + 缩进（PEP 8 为 4 空格）划分代码块，以换行结束语句；注释只有 `#`，三引号放在文件/函数首行作 docstring；空代码块用 `pass` 占位。
- **标识符与关键字**：字母或下划线开头、区分大小写、不允许 `$`；判断字符串能否作变量名，需同时满足 `s.isidentifier()` 且 `not keyword.iskeyword(s)`。
- **数字与字符串**：`/` 结果总是 `float`，`//` 向下取整（`-7 // 2 == -4`）；字符串不可变，不能直接与整数相加（需 `str()` 或 f-string）；切片 `变量[头下标:尾下标:步长]` 不含尾下标且越界不报错；`r"..."` 保留反斜杠不转义。
- **输入输出与导入**：`input()` 总是返回 `str`；`print()` 返回 `None`，支持 `sep` 和 `end`；导入用 `import` / `from...import` / `as`；命令行参数在 `sys.argv[1:]`。

## 2. 最小代码示例

<!-- 一段可执行代码 + 预期输出，用来验证理解 -->

```python
import keyword

# 1. 合法变量名检查（拼写合规 + 非关键字）
print("class".isidentifier(), keyword.iskeyword("class"))  # True True

# 2. 切片：步长、去首尾、反转
s = "123456789"
print(s[1::2], "[Python]"[1:-1], s[::-1])                  # 2468 Python 987654321

# 3. 负数整除、原始字符串与 f-string
age = 18
print(-7 // 2, r"C:\new\test", f"age={age}")               # -4 C:\new\test age=18

# 4. print 定制分隔符与不换行
print(1, 2, 3, sep=" | ", end="")                         # 1 | 2 | 3
```

## 3. 与 JS/TS 的差异

<!-- 只记录真正容易混淆、值得记住的区别 -->

- 方法使用不同,变量命名定义不一样,Python 有函数局部作用域，但 if 不创建块级作用域。

- `#!/usr/bin/python3` 叫做 Shebang（或者 Hashbang），作用是告诉操作系统：“请用 /usr/bin/python3 这个路径下的解释器来运行这个文件。”可以不写。

- **代码块与关键字**：用 `:` + 缩进代替 `{}`；`True`、`False`、`None` 首字母大写；逻辑运算用 `and` / `or` / `not` / `elif`（对应 JS 的 `&&` / `||` / `!` / `else if`）。
- **字符串拼接与索引**：`"a" + 1` 直接抛 `TypeError`（JS 会隐式转成 `"a1"`）；索引越界抛 `IndexError`（JS 返回 `undefined`），但切片越界不报错。
- **命名与私有约定**：变量与函数用 `snake_case`（JS 用 `camelCase`）；全大写常量和 `_name` 内部约定均不强制限制（JS 的 `const` 和 `#private` 是强制的）。
- **命令行参数**：`sys.argv` 为 `[脚本路径, ...参数]`，比 Node.js 的 `process.argv` 少了最前面的解释器路径。

## 4. 易错点与验证记录

<!-- 原先怎么理解、实际结果是什么、为什么出错 -->

-修改 demo_syntax.py 实验代码影响了 demo 自检（demo_syntax.py）

把 bad_code 第 3 行原本故意写错的 2 个空格改成了 4 个空格后，代码变成了合法缩进，导致 test_demos_01.py 预期捕获 IndentationError 时失败。
跑目录级 pytest 时会连带跑 test_demos_*.py

- **`test_*.py` 文件来源**：`test_demos_01.py` 和 `test_exercises_01.py` 不是 pytest 自动生成的，而是提前写好给 pytest 自动扫描执行的测试脚本（类似前端手写的 `*.test.ts`）；前者校验 Demo，后者验收练习。

## 5. 待解决的问题

<!-- 暂时没理解的问题，下一次再验证 -->

- 练习时候,缩进很重要!
