'''
定义一个函数,生成一个List,List内容为1-20的平方,然后打印List前五个值
'''

def printList5():
    l = []
    for i in range(1,21):
        l.append(i**2)

    print(l[:5])

test = printList5()
