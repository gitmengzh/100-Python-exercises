'''
给定一些电子邮箱地址,打印电子邮箱的名字,假设电子邮箱的名字和公司名字以数字字母下划线组成
'''
import re
def printMileName():
    try:
        emailName = input()
        part1 = "(\w+)@((\w+\.)+(com))"
        r1 = re.match(part1,emailName)
        print(r1.group(1))
    except:
        print("输入的邮箱格式不正确")





test = printMileName()


'''
学习点: re  关于re太长,用点学点,不然看完也忘了
            \w  匹配数字字母下划线
            re.match :re.match(pattern,string,flags=0)
            pattern 要匹配的正则表达式,String 要匹配的字符串  flags 正则表达式匹配的方式,例如:是否区分大小写, 多行匹配
            group: 通过re.match匹配的内容,可以用group(num=0) 或者groups获取匹配的内容
                    group(num=n) 可以输入一个或者多个小组号,返回的内容为一个小组内容或者包含多个小组内容的元组.
                    groups()  返回一个包含所有小组的元组
                    小组划分应该跟分割符有关系,这一点待确认
'''