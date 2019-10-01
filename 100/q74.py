'''
字典的常用操作
'''
#get() 需要传一个key值
dict1 = {1:'abc','b':'weie','3':'abcid'}
dict2 = {1:'sdf',3:'cdf',2:'iend'}


result1 = dict1.get(1)
print(result1)

#dict.items() 输出字典内容以列表中的元组
#python3之后没有 iteritems

result2 = dict2.items()

print(result2)
#dict_items([(1, 'abc'), ('b', 'weie'), ('3', 'abcid')])

#排序
dict3={}
list1 = sorted(dict2.keys())
for i in list1:
    dict3[i]=dict2[i]
print(dict3, dict2)
dict2.clear()
for j in list1:
    dict2[j] = dict3[j]


print(dict3,dict2)





#反转  基本思路：遍历key values, 然后在新的字典中新的key等于value
dict4 = {'a':1,'b':2,'c':3}
new_dict = {}
for i,j in dict4.items():
    new_dict[j]=i
print(new_dict)


#拷贝字典
dict5 = dict4.copy()
print(dict5)

