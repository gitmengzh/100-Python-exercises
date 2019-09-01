'''
假设给一些电子邮箱地址,打印公司名称.假设公司名称和用户名仅由数字,字母,下划线组成.
'''
import re
def matchCPname():
    try:
        companyName = input()
        part1 = "(\w+)@(\w+)+(\.com)"
        res = re.match(part1,companyName)
        print(res.group(2))
    except:
        print("请输入正确格式的电子邮件")

test = matchCPname()