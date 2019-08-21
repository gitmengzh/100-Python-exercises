'''
定义一个方法，接受一个整数，判断这个数为基数或者偶数，打印输出结果
'''

def checkNum(n):
    try:
        if n%2 ==0:
            print("it is an odd number!")
        else:
            print("it is an even number!")
    except:
        print("{}不是一个整数！".format(n))

test = checkNum('s')

'''
利用偶数%2结果为0进行判断
'''