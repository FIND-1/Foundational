"""在终端运行脚本，可在文件路径后传入一个名字。"""

import sys  # 标准库模块，提供命令行参数和解释器版本信息

# sys.argv[0] 是脚本路径；存在第一个参数时，它位于 sys.argv[1]。
name = sys.argv[1] if len(sys.argv) > 1 else "Python 学习者"  # 有参数时取参数，否则用默认值
print("你好，", name, sep="")
print("当前解释器版本：", sys.version.split()[0])  # 按空白拆分版本信息并取第一项
