# Day 01：Python 基础

课程顺序与菜鸟教程目录一致。

1. [基础语法](01-basic-syntax/README.md)（已按新规范完成：要点 + JS 对照 + `functions.md` + demo + 分层 pytest 练习 + 笔记）
2. [基本数据类型](02-basic-data-types/README.md)（已按新规范完成：要点 + JS 对照 + `functions.md` + demo + 分层 pytest 练习 + 笔记）
3. [数据类型转换](03-type-conversion/README.md)（旧结构，待按 `source` 顺序迁移）
4. [解释器](04-interpreter/README.md)（旧结构，待按 `source` 顺序迁移）

## 第 3～4 章待调整事项（迁移备忘）

按 03 → 04 逐章迁移。迁移前逐项核对 `example.py`、各主题脚本和 `practice.md`，保留题意、示例和预期结果。现阶段这两章的基础题按原练习页手动验收。

| 章节 | 保留内容 | 下次迁移的具体工作 |
| --- | --- | --- |
| 03 类型转换 | 综合示例、5 个主题脚本、字符串转整数后求和的练习 | 先验证转换结果、类型和原变量；把异常捕获、字面量解析列为进阶。逐项核对转换函数的重载与参数限制。 |
| 04 解释器 | 问候脚本、版本与参数示例、REPL 加法与退出练习 | 保留交互模式的人工验收；为脚本输出添加测试，将命令行参数扩展单列。 |

迁移时沿用第一章的函数速查、分层测试和个人笔记模板。每章 README 的清单记录学习状态。

截图中的后续课程依次为注释、运算符、数字、字符串、列表和元组；目前 `source` 中尚未提供这些课程的页面。

相关目录：[pytest 教程](../tooling/pytest/README.md)；原来的 `str.py` 已移到 [`lessons/playground/`](../playground/str.py)（自由实验区）。
