'''

'''

l1 = [1,2,3,4,5,6,7,8,9,10]

l2 = map(lambda x:x**2,l1)

for i in l2:
    print(i)



'''
知识点:  map(函数表达式,迭代器1,迭代器2....)   根据函数或者函数表达式,对迭代器中的元素做映射
                                            迭代器中的元素依次作用函数或者函数表达式,输出新的迭代器
                                            返回值:python2 返回一个列表,
                                            python3   返回一个迭代器
'''