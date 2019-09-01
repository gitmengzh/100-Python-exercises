'''
To define a custom exception, we need to define a class inherited from Exception.
定义一个自定义异常,我们需要从Exception中继承一个类
'''

class CustomException(Exception):
    def __init__(self,errorinfo):
        self.error = errorinfo
    def __str__(self):
        return self.error


def ageExcept(age):
        if age <0 or age>130:
            raise CustomException("the age is not correct")
        elif isinstance(age, int):
            raise CustomException("the age is not int")
        else:
                print(age)



try :
    test = ageExcept(int(100))
except CustomException as e:
    print(e)

'''
    https://www.runoob.com/python3/python3-errors-execptions.html
知识点:自定义错误类 raise 后边要跟一个错误类
        python 使用raise抛出异常   唯一的一个参数就是抛出的异常,必须是一个类或者实例

        __str__:在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
        当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
        __str__方法需要返回一个字符串，当做这个对象的描写
'''









'''
学习点:raise语句,自定义错误信息
'''