'''
编写一个程序,接受以空格为分隔的单词,打印以数字组成的单词
'''

import re
def printNumWords():
    part1 = ("\d+")
    l1 = input()
    res1 = re.findall(part1,l1)

    print(res1)

test = printNumWords()



'''
知识点:   re.findall()
         在字符串中查找正则表达式匹配的所有子串,返回一个列表,如果没有,返回空列表
'''