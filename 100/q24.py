'''
python 有很多内置函数，通过编写一个程序，打印一些python内置函数的文档，并自己写一个函数，为自己的功能添加文档
'''


print (abs.__doc__,int.__doc__,input.__doc__)

def square(num):
    '''
    return the square value of the input number.
    the input number must be integer
    :param num:
    :return:
    '''
    return num**2
print (square(2))
print(square.__doc__)



'''
学习点    __doc__:  (暂时不过多学习)
'''
