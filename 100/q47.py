'''
写一个程序,用filter生成一个列表,内容为1-20之间偶数的平方
'''


newList = filter(lambda x:x%2==0,range(1,21))
print(list(newList))