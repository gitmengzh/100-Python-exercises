'''
定义一个方法，打印一个字典，key为1-n, value为key的平方
'''


def printDict(n):
    try:
        num_dict = {}
        for i in range(1,n+1):

            num_dict[i] = i**2
        print(num_dict)

    except:
        print("数值不正确，请输入一个整数")

test = printDict(20)
