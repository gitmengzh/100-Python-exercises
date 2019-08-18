#输入一些字符，以，作为分割，转化为list 和tuple
value = input()
l1= value.split(',')
l2 = value.split(',',3)
t = tuple(l1)

print(l1,l2,t)


'''
Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
str.split(str="", num=string.count(str)).
eg:  上边的输入输出
1,2,4,5,6.w,d
['1', '2', '4', '5', '6.w', 'd'] ['1', '2', '4', '5,6.w,d'] ('1', '2', '4', '5', '6.w', 'd')
'''