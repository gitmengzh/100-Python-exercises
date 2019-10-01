#python 字符串操作。

#  1 字符串排序
str1 = "test123453sdfsfAAAAsdDF"
list1 = list(str1)
list1.sort()
print(''.join(list1))
str2 = "Hello world  abc  Asd"
list2 = list(str2.split(' '))
list2.sort()
print(''.join(list2))
tuple1 = tuple(list2)
# 区分大小写排序
list3 = [(x.lower(),x)for x in list(str2.split(' '))]
list3.sort()
list4 = [s[1] for s in list3]

print(''.join(s[1] for s in list3),list4)




#   2 字符串反转

list5 = reversed(list(str1))
print(''.join(list5))
str3 = str1[::-1]
print(str3)


#字符串格式化
print('this is my name: %s , my age is %d' % ('menzh',20))
str2.isdigit()
str2.isalpha()
str2.islower()