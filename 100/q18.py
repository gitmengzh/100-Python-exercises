'''
网站要求用户输入用户名和密码进行注册。 编写程序以检查用户输入的密码的有效性。
以下是检查密码的标准：
1. [a-z]之间至少有1个字母
2. [0-9]之间至少有1个数字
1. [A-Z]之间至少有一个字母
3. [$＃@]中至少有1个字符
4.最短交易密码长度：6
5.交易密码的最大长度：12
您的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。 将打印符合条件的密码，每个密码用逗号分隔。

'''

import re

values = []
list_password = [x for x in input().split(',')]

for password in list_password:
    if len(password)<6 or len(password)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",password):
        continue
    elif not re.search("[0-9]",password):
        continue
    elif not re.search("[A-Z]",password):
        continue
    elif not re.search("[@#$]",password):
        continue
    elif re.search("\s",password):
        continue
    else:
        pass
    values.append(password)
print(','.join(values))