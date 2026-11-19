"""学习标识符、关键字和注释。"""

import keyword  # 导入 Python 自带的关键字查询模块，无需安装

user_name = "Rain"  # 下划线可以连接多个单词
User_name = "雨"  # 大小写不同，是另一个名字
print("不同变量：", user_name, User_name)
print("当前版本关键字：", keyword.kwlist)  # 查看关键字列表

# 以 # 开头的是注释，不会执行。
# 三引号用于多行字符串；文件或函数开头的字符串可作为文档字符串。
description = """第一行
第二行"""
print("多行字符串：", description)
