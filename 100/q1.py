#2000到3200之间，可以被7整除，不是5的倍数

l = []
for i in range(2000,3201):
    if (i%7 == 0) and (i%5!=0):
        l.append(str(i))

print(l)


'''
学习点： 学习到如何将循环元素加到一个列表中 l.append(str(i))
'''