'''
编写一个接受字符串的程序,如果输入的结果为'yes'或者'YES'或者'Yes',输出yes, 否则输出'No'
'''
def printYesOrNo():
    l1 = ['yes','YES','Yes']
    s = input()
    if s in l1:
        print('Yes')
    else:
        print('No')



test = printYesOrNo()