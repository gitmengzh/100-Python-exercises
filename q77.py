#set（集合） 常用方法操作
#1 去重
list1 = [1,2,2,3,4,5,3,7]
list1 = list(set(list1))
print(list1)



set1 = {1, 2, 3, 's', 5, 6, 7}
print(set1)

'''
.add(x)

向 set “s”中增加元素 x

s.remove(x)

从 set “s”中删除元素 x, 如果不存在则引发 KeyError

s.discard(x)

如果在 set “s”中存在元素 x, 则删除

s.pop()

删除并且返回 set “s”中的一个不确定的元素, 如果为空则引发 KeyError

s.clear()

删除 set “s”中的所有元素

difference(self, *args, **kwargs):比较两个集合，找出对方没有的元素，并返回一个新的集合

intersection_update(self, *args, **kwargs):　　找出两个集合的相同元素并更新自己
'''

# tuple  元组  不可变
# 1 排序
import operator
tuple1 = (1,2,4,5,63,5,6)
result1 = sorted(tuple1)
result2 = sorted(tuple1,reverse=True)
print(result1,result2)

#对一个包含元组的列表进行排序
list1 = [(1,'a'),(10,'C'),(12,'b'),(3,'g')]
list2 = [(1,'a'),(10,'C'),(12,'b'),(3,'g')]
list1.sort(key=operator.itemgetter(1))
list2.sort(key=lambda x:x[0])


print(list1,list2)
# 2 反转
tuple2 = tuple(reversed(tuple1))
print(tuple2,tuple1[::-1])
