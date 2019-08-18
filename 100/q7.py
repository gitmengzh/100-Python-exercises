'''
编写一个程序，输入两个数x，y，输出一个x行，Y列的二维数组
元素内容为二维数组的横坐标和纵坐标乘积( 列表的坐标从0开始，这个需要注意)
eg: 输入 3，5
    输出[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]
'''

#x,y =map(input("请输入两个整数：".split()))


list1 = []
x,y = map(int,input("请输入两个数:").split(','))


for m  in range(x):
    list2 = []
    for n in range(y):

        list2.append(m*n)

    list1.append(list2)

print (list1, x,y,type(x))

'''
学习点：  map()函数，根据提供的函数对指定序列做映射
          map(function, iterable,...)   函数，一个或者多个序列
          返回一个迭代器
          迭代器：
          其实主要不明白上边那个赋值怎么做的
'''