'''
输入一个句子，计算其中大写字母和小写字母的个数，并输出
'''

input_string = input()
dict1 = {"UPPER":0,"LOWER":0}

for i in input_string:
    if i.islower():
        dict1["LOWER"]+=1
    if i.isupper():
        dict1["UPPER"]+=1
    else:
        pass

print("UPPER:{},LOWER:{}".format(dict1["UPPER"],dict1["LOWER"]))


'''
学习点，与13类似，判断字符串中元素的类型
'''