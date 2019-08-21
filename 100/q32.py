'''
定义一个可以打印字典的函数，其中键是1到3之间的数字（包括两者），值是键的平方。
'''

def printDict():
    num_dict = {}
    for i in range(1,4):
        num_dict[i] = i**2
    print(num_dict)

test = printDict()


'''
知识点：对于字典的操作，需要注意以下
'''
