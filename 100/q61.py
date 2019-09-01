'''
编写一个程序，用控制台（n> 0）给定n输入计算1/2 + 2/3 + 3/4 + ... + n / n + 1。
'''

num1 = int(input("请输入一个正整数:"))
sum1 = 0.0

for i in range(1,num1+1):
    sum1 += float(float(i)/(i+1))


print(sum1)


'''
对于数值的计算,一定要注意数值类型,尤其是涉及到除法
'''