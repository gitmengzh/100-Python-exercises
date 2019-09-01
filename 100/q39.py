'''
定义一个函数,生成一个List,List内容为1-20的平方,打印除了前五个的所有数值
'''

def printListExceptFirst5():
    l = []
    for i in range(1,21):
        l.append(i**2)
    print(l[5:])

test = printListExceptFirst5()