'''
输入多个字符串，打印输出最长的那个

'''


def maxString():
    str_input = input("请输入两个字符串：")
    str_list = str_input.split(' ')

    for s in str_list:
        len1 = len(s)
        len2 = 0
        if len1>len2:
            len2 = len1



        print(str_list[len2])



'''
原题：  定义一个函数，接收两个字符串，打印输出最长的那个，如果相同长，那么全都输出打印出来
'''

def maxStr(str1,str2):
    if len(str1) == len(str2):
        print(str1,str2)
    elif len(str1)>len(str2):
        print(str1)
    else:
        print(str2)


#test = maxStr('123234','sdfjsjdflsdfjs')
test = maxString()


