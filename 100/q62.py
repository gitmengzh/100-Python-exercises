'''
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

'''

def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1)+100


num1 = int(input("请输入一个正整数:"))
print(f(num1))

'''
递归的使用
'''

