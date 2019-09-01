'''
定义一个函数,生成一个List,内容为1-20的平方,打印最后五个值
'''

def printListLast5():
    l = []
    for i in range(1,21):
        l.append(i**2)
    print(l[-5:])


test = printListLast5()


'''
知识点:需要熟悉List的倒序查询的方式
'''