'''
请使用生成器编写程序，以逗号分隔的形式打印0到n之间的偶数，同时通过控制台输入n。
'''


def genreator1(n):
    i = 0
    while i<n:
        if i%2 == 0:
            yield i

        i +=1


values = []
n = int(input())

for i in genreator1(n):
    values.append(str(i))
print(','.join(values))

'''
如何定义一个生成器,yield关键字, 对于生成器,只能通过打印的方式获取
'''