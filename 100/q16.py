'''

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
没太看懂这道题，先按照例子输入输出给出结果
'''
result = []
list1 = [x for x in input().split(',')]

for i in list1:
    #if  int(i)%2 != 0:
    if int(i)%2:
        result.append(i)
#print(list1)
print(','.join(result))

'''
学习点：    关于 not i%j  的值判断，通过测试，当i%j == 0 ， 该表达式为True， 其余为False    
            而 一个计算表达式，如果结果为0 ，false,  不为0 True
'''