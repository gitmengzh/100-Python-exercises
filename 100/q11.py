'''
 输入四位二进制数，并用逗号分隔，然后判断他们可以被5整除，用逗号分隔，打印出来
'''

value = []
items = [x for x in input().split(',')]
for i in items:
    j = int(i,2)
    if not j%5:
        value.append(i)

print(','.join(value))





'''
学习点： int()方法， int(object,base)   
                    object，一个数字或字符串参数
                    base  进制数，默认为10，这个表示object的进制数是多少
'''