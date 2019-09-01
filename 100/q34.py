'''
定义一个函数，生成一个字典，key为1-20，value 为key的平方值，输出value
'''

def printDictValue1():
    d = {}
    l = []
    for i in range(1,21):
        d[i] = i**2
        l.append(d[i])

    print(l)

def printDictValue2():
    d = {}
    for i in range(1,21):
        d[i] = i**2
    for v in d.values():
        print(v)
test1 = printDictValue1()
test2 = printDictValue2()


'''
学习点：  如何遍历一个字典，这个没见过
            a = {}
            for key in a:   等价  for key in a.keys():
            for value in a.values()  遍历value   
            for kv in a.items()   遍历字典项   
            for (key,value) in a.items()  遍历字典键值
'''