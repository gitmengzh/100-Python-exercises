'''
使用生成器定义一个类，该生成器可以再给定范围0和n之间迭代可被7整除的数字u


'''

def putNumebers(n):
    i = 0
    while i <n:
        j = i
        i = i+1
        if j%7 == 0:
            yield j

for a in putNumebers(100):
    print(a)


'''
学习点：   yield   在python中带有yield的函数称之为生成器（generator),
                    变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
          生成器   一类特殊的迭代器，带有yield的函数为一个生成器，可以返回多次
                   受内存限制，列表容量有限，而且列表占内存。如果列表元素可以按照某种算法推算出来，就可以一边循环，一边计算，这种
                   一边循环一边计算的机制就叫做生成器
                   generator保存的是算法，每次调用要用next()，但是一般用for循环，不会用next（）
                   生成器的两种创建方法
                   g = (x*x for x in range(10)   列表的生成 l = 【x*x for x in ranget(10)】 将圆括号改成方括号
                   
                   
          迭代器   ：直接作用于for循环的对象统称为可迭代对象：Iterable， list, tuple,dict,set,str,generator
                    可以使用isinstance()判断一个对象是否是Iterable对象：
'''