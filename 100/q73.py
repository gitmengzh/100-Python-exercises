#列表反转与排序


list0 = ['a','b','c',1,2,3]
list1 = [1,3,5,10,9,27]
list2 = ['a','abc','c','n','hello']
list3 = ['abc','acd','Hij','hac','Zab','zzc']
list4 = ['a','b','c',1,2,3]
list5 = ['a','b','1','4','z','A']

'''
反转的方法  reversed   [::-1]  枚举遍历法
'''

result1 = list(reversed(list0))
result2 = list0[::-1]

for i,j in enumerate(list4):
     list0[len(list0)-i-1] = j
print(result1,result2,list0)


'''
排序方法： sorted， sort(修改原列表)
note:同一类型才能比较排序
     默认情况下，排序为升序，既 reverse 为False, reverse True为升序
'''

result3 = sorted(list3)
list5.sort()
list1.sort(reverse=True)

print(result3,list5,list1)

list6 = ['ADB','23s','asdi','234']
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
'''
key 参数或者函数 与sort和sorted配合使用
'''
list6.sort(key=str.lower)
result6 = sorted(list6,key=str.lower)
result7 = sorted(student_tuples,key=lambda student:student[2],reverse=True)
print(list6,result6,result7)

'''
Operater 模块 itemgetter 和 attrgetter
attrgetter方法需要针对的是定义了元素含义的排序，如列表每一项分别是name,grade,age
单独给个列表无法使用
'''


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

from operator import attrgetter, itemgetter
result8 = sorted(student_tuples,key=itemgetter(2))
result9 = sorted(student_objects,key=attrgetter('age'))
print(result9,result8)




