'''
编写一个程序，根据给定的公式计算并打印该值：
Q = [（2 * C * D）/ H]的平方根
以下是C和H的固定值：
C是50.H是30。
D是变量，其值应以逗号分隔的顺序输入到程序中。
将结果输出，并用逗号隔开
'''


import math
c= 50
h = 30
value = []
items = [x for x in input().split(',')]
for d in items:
    # sqrt1 = math.sqrt(2*c*float(d)/h)
    # round1 = round(sqrt1)
    # #int1 = int(round1)
    # str1 = str(round1)
    # value.append(str1)
    value.append(str(round(math.sqrt(2*c*float(d)/h))))
    #print(sqrt1,round1,str1)
a = (','.join(value))  #将列表的所有元素进行输出，并以,做为分隔符
print(a,type(a))
#print (','.join(value),value)


'''
学习点：math 的 sqrt 方法，用于开方求根

        round(x,num)方法，返回浮点数x的四舍五入值 num为保留的位数，3为小数点后3为，0，返回的也是浮点数，eg: round(2.13，0）返回2.0
        num 不写时，返回int 类型,复数表示小数点前边多少位四舍五入，如 round(1234.2,-3)  返回1000，浮点数类型
        
        数字字符串无法直接转为int类型,需要先转化成float类型 int(float(num))
        
        列表可以用表达式生成
        
        列表推导式 x for x in range（）  这里也可以用if,while 等循环或者判断语句
        对于列表推导式的理解:
                    list = [itme | for item in iterable]
                    竖线后面：一个循环表达式或者判断语句，这里式一个for循环表达式
                    数显前面：可以认为是我们想要放在列表中的元素，也可以是一个相关表达式
                    list = [x*x for x in range (10)]
                    items = [x for x in input().split(',')]
                    
        引申学习： lambda表达式，用在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
                    a = lambda x,y:x+y  后边的表达式不能出现if, while ,for 等循环语句
                    a(1，2) = 3
'''