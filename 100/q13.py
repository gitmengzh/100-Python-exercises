'''

输入一个句子，然后计算字母和数字的个数
'''

input_string = input()
dict1 = {"DIGITS":0,"LETTERS":0}

for i in input_string:
    if i.isdigit():
        dict1["DIGITS"]+=1
    if i.isalpha():
        dict1["LETTERS"]+=1
    else:
        pass

print("DIGITS:",dict1["DIGITS"],"LETTERS:",dict1["LETTERS"],type(i))


'''
学习点：  对于字符串，可以遍历
          对于字符串，可以判断其每个元素的类型  str.isdigit()  str.isalpha()
'''