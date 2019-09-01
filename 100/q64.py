'''
请使用列表推导编写一个程序，以逗号分隔的形式打印斐波那契序列，并通过控制台输入给定的n。
'''

def f(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

num = int(input())
list1 = [str(f(x)) for x in range(1,num+1)]
print(','.join(list1))


'''
重点   使用列表推导编写程序
'''