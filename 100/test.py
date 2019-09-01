
def test1():
    d1 = input()
    d2 = int(d1)
    d_float = round(d2)
    type1 = type(d_float)
    int1 = int(d2)
    print(float(d1), type1, str(2),d_float)

def test2():


    x, y = map(int, input().split(','))
    lst = []

    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i * j)
        lst.append(tmp)

    print(lst,x,y)

def test3():
    y = map(int, [3])
    m,n = int([2,3])

    print(m,n)

def test4():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break;

def test5():
    list1 = ['abd','sdf','urty']
    list1.sort()
    print(list1)

def test6():
    test = input()
    print(type(test))


def test7():
    value = []
    items = [x for x in input().split(',')]
    for p in items:
        intp = int(p, 2)
        if not intp % 5:
            value.append(p)

    print(','.join(value))

def test8():
    '''操作符理解'''
    a = 0
    a+=1
    b = 10
    b -= 1
    c = 1
    c=+1
    d = 10
    d =-1
    print(a,b,c,d)
#a = test8()
# n = 2002%11
# i = not 2001%2
# k = not 2002%112
# s = type(k)
# y = type(i)
# m = -2
# a = not m
# b=10
# c=6
# if b%c:
#     print(1,"True")
# else:
#     print(2,"False")
#print(s,k,y,i,n,a)

#print( map(int, input().split(',')))

a = 10
b = 3
c = a/b
d = a//b
print(c,d)

################################
import re

def test9 ():
    '''
    string1 = "test@144423@tesdfsst@123@sdfsf"
    part1 = "(\w+)@(\w+)@(\w+)@(\w+)@(\w+)"
    res = re.match(part1,string1)
    print(res.group(1),res.groups(),res.group(2),res.group(3),res.group(4),res.group())
    '''
    str1 = input().split()
    part1 = ("\d+")
    for s in str1:
        res = re.match(part1,s)
    print(res.groups())

test = test9()