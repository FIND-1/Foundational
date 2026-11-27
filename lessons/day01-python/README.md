# Day 01：Python 基础（主线课程索引）

课程顺序和编号与菜鸟教程目录一致，与 `source/` 中的原始教程一一对应。`day01-python` 作为本阶段固定主线目录沿用，不按实际学习天数创建新 `day` 目录。

## 差异化学习模式

学习模式不写入目录名，而标明在各章 `README.md` 顶部（规范全文见根目录 [AGENTS.md](../../AGENTS.md)）：

| 模式 | 中文名 | 适用说明 | 产出文件约定 |
| --- | --- | --- | --- |
| `Quick Review` | 速览学习 | 已有经验或重复度高的章节 | 目录只放 `README.md` 和 `functions.md`，验收只设一项 |
| `Delta Learning` | 差异学习 | 仅补新增点、理解盲区与边界行为 | 必需 `README.md`（含四类知识比对表，已掌握项用相对路径回引原章）；按需编写增量 Demo、速查与练习 |
| `Core Learning` | 重点学习 | 核心机制、差异大或后续高频依赖章节 | 完整结构（`README.md`、`functions.md`、Demo、分层练习与测试、`notes.md`） |

所有模式下，**首次出现的 API** 均保留完整签名、参数限制、默认值、返回值、异常、JS/TS 对照与 Pythonic 建议。

## 已导入原文的章节（01～06）

| 编号 | 章节目录 | 学习模式 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| 01 | [01-basic-syntax](01-basic-syntax/README.md) | Core Learning（重点学习） | 已完成 | 保留已完成学习代码、个人笔记与测试结果 |
| 02 | [02-basic-data-types](02-basic-data-types/README.md) | Core Learning（重点学习） | 已完成 | 保留已完成学习代码、个人笔记与测试结果 |
| 03 | [03-type-conversion](03-type-conversion/README.md) | Core Learning（重点学习） | 已完成 | 保留已完成学习代码、个人笔记与测试结果 |
| 04 | [04-interpreter](04-interpreter/README.md) | Quick Review（速览学习） | 已整理 | 速览验收为 REPL 与脚本实操 |
| 05 | [05-comments](05-comments/README.md) | Quick Review（速览学习） | 已整理 | 回顾注释，辨别三引号字符串与 Docstring，实操读取文档 |
| 06 | [06-operators](06-operators/README.md) | Core Learning（重点学习） | 已整理 | 算术、比较、赋值、位与逻辑、成员、身份和优先级 |

## 后续课程初始规划（07～15）

> 以下为初始模式规划；**仅为已导入 `source/` 原文的章节编课**，不提前批量生成空目录。正式编课时将根据原文内容与前章已掌握覆盖度灵活调整模式。

| 编号 | 规划目录名 | 章节主题 | 初始学习模式 | 备注 |
| --- | --- | --- | --- | --- |
| 07 | `07-numbers` | 数字 | Delta Learning（差异学习） | 复用第 1～3 章基础，补 `math` / `random` 与数值边界 |
| 08 | `08-strings` | 字符串 | Delta Learning（差异学习） | 复用第 1～3 章基础，补格式化与常用方法增量 |
| 09 | `09-lists` | 列表 | Delta Learning（差异学习） | 复用第 2～3 章基础，补原地方法、拷贝与推导式边界 |
| 10 | `10-tuples` | 元组 | Delta Learning（差异学习） | 复用第 2～3 章基础，补解包、单元素与不可变语义边界 |
| 11 | `11-dictionaries` | 字典 | Delta Learning（差异学习） | 复用第 2～3 章基础，补增删改合并、视图与常用方法 |
| 12 | `12-sets` | 集合 | Delta Learning（差异学习） | 复用第 2～3 章基础，补集合运算与增删方法差异 |
| 13 | `13-conditionals` | 条件控制 | Quick Review（速览学习） | 复用 `if/elif/else` 与条件表达式，速览 `match-case` |
| 14 | `14-loops` | 循环语句 | Core Learning（重点学习） | `for`/`while`、`range`、`enumerate`、`break`/`continue`/`else` |
| 15 | `15-first-program` | 编程第一步 | 综合实践 | 串联前 14 章基础能力，完成首个结构清晰的 Python 小程序 |

## 阶段复习与相关目录

- **阶段复习机制**：[reviews/README.md](reviews/README.md)（与正式课程目录分离；每完成 3～5 章安排一次跨章节综合实践，以知识回忆、代码应用和错题复盘为主）
- **工具教程**：[pytest 教程](../tooling/pytest/README.md)
- **自由实验区**：[`lessons/playground/`](../playground/str.py)
