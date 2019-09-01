'''

'''




li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
for i in evenNumbers:
    print(i)


'''
学习点:   lambda使用复习
         filter() 用于列表过滤,过滤掉不符合要求的元素
         参数: 函数或函数表达式, 迭代器
         返回值:  python2  返回一个新的列表,python3 返回一个迭代器
'''
