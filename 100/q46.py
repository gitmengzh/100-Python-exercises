'''
编写一个程序,用map和filter创建一个新列表,内容为[1,2,3,4,5,6,7,8,9,10]中偶数的平方
'''


l = [1,2,3,4,5,6,7,8,9,10]
l1 = filter(lambda x: x%2==0,l)
l2 = map(lambda x:x**2,l1)
l3 = map(lambda x:x**2, filter(lambda x:x%2==0,l))   #可以写成一行

print(list(l2),list(l3))