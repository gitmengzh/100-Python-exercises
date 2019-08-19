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

for i in putNumebers(100):
    print(i)


'''
学习点：   yield   在python中带有yield的函数称之为生成器（generator),
'''