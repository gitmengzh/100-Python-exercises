'''
定义一个函数,生成一个List,List内容为(1-20)的平方,打印结果
'''

def printList():
    l = []
    for i in range(1,21):
        l.append(i**2)
    print(l)

test = printList()