"""处理无效输入，避免程序因转换失败而直接中断。"""

from ast import literal_eval  # 从标准库 ast 导入字面量解析函数

for value in ("12", "3.5", "abc"):
    try:
        converted = int(value)
    except ValueError:
        print(f"{value!r} 不是有效的整数字符串")  # !r 显示值的表示形式
    else:
        print(f"{value!r} 转成整数：{converted}")

try:
    int(None)
except TypeError:
    print("None 的类型不能直接转换成整数")

# literal_eval 只接受 Python 字面量，不用于执行任意 Python 表达式。
values = literal_eval("[1, 2, 3]")
print("解析列表字面量：", values, type(values))

try:
    literal_eval("1 + 2")
except ValueError:
    print("算术表达式不是可接受的字面量")
