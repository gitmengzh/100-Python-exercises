'''
请编写断言语句以验证列表[2,4,6,8]中的每个数字是否偶数
'''


list1 = [2,4,6,8]
try:
    for i in list1:

        assert i%2==0
except:
    print("不全为偶数")
else:
    print("全为偶数")
