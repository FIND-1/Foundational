# #!/usr/bin/python3
# (叫做 Shebang（或者 Hashbang）,
# 告诉操作系统："请用 /usr/bin/python3 这个路径下的解释器来运行这个文件。"
# ----可以不写)
 
# str='123456789'
 
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
# print(str[2:])             # 输出从第三个开始后的所有字符
# print(str[1:8:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str * 2)             # 输出字符串两次
# print(str + '你好')         # 连接字符串
 
# print('------------------------------')
 
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


 
# input("\n\n按下 enter 键后退出。")


import sys; x = 'runoob'; sys.stdout.write(x + '\n')
