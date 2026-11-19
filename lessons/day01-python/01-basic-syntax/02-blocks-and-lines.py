"""学习缩进、代码块以及跨行书写。"""

score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")  # 相同代码块保持一致缩进
else:
    print("继续练习")

total = (
    1
    + 2
    + 3
)
items = [
    "苹果",
    "香蕉",
]
print("多行表达式：", total, items)

first = 1; second = 2  # 分号可分隔简单语句，通常建议分行写
print("同一行的两次赋值：", first, second)
