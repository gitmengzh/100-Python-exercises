#列表，元组，字符串，字典，集合相互转化

#列表转元组：
list1 = [1,2,3,45,'a','c']
tuple1 = tuple(list1)
print(tuple1)

#元组转列表
tuple2 = (1,2,4,'s','test','SKDF')
list2 = list(tuple2)
print(list2)


#列表转字典  列表不能转化成字典 可以通过enumerate方法将列表的元组
list3 = ['s','fd','4df']
list4 = [1,2,3]
dict1 = dict(enumerate(list3))
dict2 = dict(zip(list3,list4))
print(dict1,dict2)


#字典转化成列表  注：字典无法直接转化成列表，如果直接list(dict)会返回一个key的列表，以下的items,keys,values返回值为dict_items,dict_values,dict_keys,不是list类型
dict3 = {1:'s','d':4,'c':'sd',3:6}
list5 = list(dict3)
list6 = dict3.items()
list7 = dict3.values()
list8 = dict3.keys()
print(list5,list6,list7,list8,type(list5))

#列表转化成set集合
list9 = [1,2,3,4,'s','f']
set1= set(list9)
print(set1)
#set集合转化成列表
set2 = {1,2,34,4,'sd'}
list10 = list(set2)
print(list10)

#列表转化成字符串  注意，数字不能转化成字符串
list11 = [2,3,4,6,'3','sd','sd','d']
list12 = ['d','s','4']
print(' '.join(list12))


#字符串转化成列表
str1 = 'hello world'
str2 = '129734kle'
list13 = str1.split(' ')
list14 = list(str2)
list15 = [str(s) for s in str2]
print(list13,list14,list15)

#tuple元组转化字典 类似于列表

#字典转化成元组   类似于列表

#元组转成set集合
tuple3 = (1,'d',9)
set3 = set(tuple3)
print(set3)

#set转化成tuple
set4 = {84,2,4,'d'}
tuple4 = tuple(set4)
print(tuple4)

#set转化成字符串
set5 = ('9','d','s')
print(' '.join(set5))

#字符串转化成tuple
str3='743uf9ss'
str4='hello python'
set6 = str4.split(' ')
set7 = set(str(s) for s in str3)
print(set(str3),set6,set7)



#字符串转化成集合
str5 = 'sdfseg1'
set9 = set(str5)
print(set9)
