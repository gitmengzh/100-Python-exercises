#计算一个数的阶乘



def test(l):
    if l == 1:
        return 1
    else:
        return l*test(l-1)

print('请输入一个数字：', end='')
l = int(input())

print (test(l))



'''
学习点：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
'''
