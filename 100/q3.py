#给一个整数n，生成一个从1到n （均包括在内）内容为（n:n*n）的字典，例如：输入3,字典为{1：1，2：4，3：9}


num = int(input("请输入一个整数:"))
d = dict()
for i in range(1,num+1):
    d[i] = i*i

print(d)


'''
python3.x版本中，舍弃了raw_input函数，只保留了input( )函数，其接收任意输入，将所有输入默认为字符串处理，并返回字符串类型, 因此必须对于输入的数进行转换
定义空字典，如何增加字典内容。
'''