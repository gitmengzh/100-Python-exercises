'''
定义一个函数,生成一个元组(tuple),内容为1-20的平方,打印所有数值
'''

def printTuple():
    l = []
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))

test = printTuple()


'''
对于生成tuple的,可以先生成List,然后转换成tuple
'''