'''
查找1000到3000(均包括)内所有数的每一位都为偶数
'''

value2 = []
value3 = []



for i in range(1000,3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):

        value2.append(s)
    else:
        value3.append(i)

print(','.join(value2))


'''
学习点：  str.join(sequence)    参数：要连接的元素序列  返回值：返回通过指定字符链接序列中元素后生成的新字符串 用于字符串操作
            思路：对于计算每一位的，可以将数字转话成字符串，然后通过字符串下标属性去判断
            有些计算和函数适用的对象不一样，这个需要转化数据格式，注意
'''