# 第 5 章 · Python3 注释

学习模式：Quick Review（速览学习）

阅读材料：[菜鸟教程原文 HTML](../../source/05-comments.html)（在浏览器中打开）

## 学习步骤

1. 按「单行注释 → 多行注释 → Docstring」通读原文，回顾[第 1 章的注释要点](../01-basic-syntax/README.md#要点按原文顺序)。
2. 带着「`#` 写在哪才是注释？」「字符串放在哪才是文档字符串？」两个问题阅读下方要点，查阅 [`inspect.getdoc()` 速查](functions.md)。
3. 先预测输出，再运行下方的短例子，最后独立完成「理解检查」。

## 要点（按原文顺序）

1. **单行注释**。字符串以外的 `#` 从当前位置注释到行尾，可单独占一行，也可跟在语句后。字符串里的 `#` 是普通字符，比如 `"C#"` 会保留 `#`。
2. **多行说明**。每行加 `#` 写成一段注释。原文的 `'''` 和 `"""` 都是字符串定界符，同一组未转义的引号会结束当前字符串，另一种引号可以保留在内容里。三引号内开头的 `#` 也会保留在字符串内容中。
3. **Docstring（文档字符串）**。模块、函数、类或方法体的第一条语句如果是字符串字面量，就会成为它的文档字符串。前面的空行和 `#` 注释不占用语句位置。可以用 `对象.__doc__` 直接读取，用 [`help(对象)`](../04-interpreter/functions.md#了解help) 在终端查看帮助，也可以用 `inspect.getdoc(对象)` 获取清理过缩进的文档文本。
4. **多行和类的 Docstring**。简单说明写一行即可。复杂说明先写一句摘要，空一行后再写参数、返回值或异常。原文的 `Person` 示例把类、初始化方法和普通方法的说明分别写在各自定义的开头。Google、Sphinx/reST、NumPy 是常见的文档书写风格，同一项目沿用已有格式。

## 【补充】JS/TS 对照与原文勘误

- JS/TS 用 `//` 和 `/* ... */` 写注释。Python 的代码说明用 `#`，文档字符串的用途类似 JSDoc，可以通过 `__doc__` 在运行时读取。
- 原文把三引号称为多行注释。三引号内再次出现一组未转义的同类三引号，会提前闭合字符串，让后面的文本暴露给解释器，原文的嵌套例子因此出现语法错误。原文「正确示例」里的 `#` 仍属于字符串内容。多行说明逐行加 `#`。[Python 3.11 词法参考](https://docs.python.org/3.11/reference/lexical_analysis.html#comments)
- 按 PEP 8，`#` 后留一个空格，行尾注释与前方语句至少隔两个空格。按 PEP 257，文档字符串统一使用三双引号。[PEP 8](https://peps.python.org/pep-0008/#comments) · [PEP 257](https://peps.python.org/pep-0257/)

## 运行

在仓库根目录打开 PowerShell，将下方代码保存为 `lessons/playground/comments.py`，再执行这条命令。环境准备见[第 1 章「运行」](../01-basic-syntax/README.md#运行)。

```powershell
.\.venv\Scripts\python.exe .\lessons\playground\comments.py
```

【补充】`def add(a, b):` 定义接收两个参数的函数，缩进后的第一条语句用于记录文档。调用 `add(2, 3)` 时，`return a + b` 把 `5` 交给调用方。`import inspect` 导入标准库模块，`inspect.getdoc(add)` 传入函数对象并返回整理后的两行文档。

```python
import inspect


def add(a, b):
    """返回两个数的和。

    a 和 b 都是待相加的数。
    """
    return a + b


# 技能标签里的 # 是文本的一部分。
tag = "C#"  # 保留标签的原始拼写
print(tag, add(2, 3))
print(inspect.getdoc(add))
```

预期输出

```text
C# 5
返回两个数的和。

a 和 b 都是待相加的数。
```

### 理解检查

1. 自己写一段两行注释，再给包含 `#` 的字符串加一条行尾注释。运行后解释输出为什么仍有 `#`。
2. 把示例中的三引号字符串移到 `import inspect` 下方并去掉整段的缩进，保留函数体里的 `return`。先预测结果，再运行验证 `inspect.getdoc(add)` 的输出变化，并解释模块和函数各自从哪里识别 Docstring。
3. 选做：先恢复示例，分别用 `print(add.__doc__)` 和 `help(add)` 查看文档。对比原始缩进、帮助文本中的函数签名，以及 `inspect.getdoc(add)` 的输出。

## 学习验收标准

- [ ] 本章完成：能用示例区分 `#` 注释和三引号字符串，并解释什么位置的字符串会成为 Docstring。
