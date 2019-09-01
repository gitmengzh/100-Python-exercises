'''
请使用生成器编写一个程序，以逗号分隔的形式打印可以在0和n之间以5和7整除的数字，同时通过控制台输入n。
'''

def generator1(n):
    i = 0
    while i<n:
        if i%5==0 or i%7==0:
            yield i
        i+=1

num = int(input())
values = []
for i in generator1(num):
    values.append(str(i))  #这个转化为字符串是因为要以逗号分隔的形式打印结果,这个需要List转变为str,
                            #那么,List中的整数类型需要转化成字符串类型,不然无法转换


print(','.join(values))

'''
  List 包含数字不能直接转化成字符串
'''