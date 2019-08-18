from operator import itemgetter


list1 = []
while  True:
		s = input()
		if not s:
			break
		list1.append(tuple(s.split(",")))
print (sorted(list1,key=itemgetter(0,1,2)))


'''
学习点：python sorted函数和 oprator.itemgetter函数

'''