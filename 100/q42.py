'''
写一个函数,给定一个tuple(1,2,3,4,5,67,8,9,10),生成一个新的元组,内容为给定元组中的偶数.
'''

def printNewTuple():
    t1 = (1,2,3,4,5,6,7,8,9,10)

    l2 = []
    for i in t1:
        if i%2 == 0:
            l2.append(i)

    print(tuple(l2))


test = printNewTuple()


'''
知识点:元组也可以遍历
'''

