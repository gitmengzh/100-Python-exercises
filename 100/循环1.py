#  100块钱买100只鸡，母鸡3块，公鸡1块，小鸡0.5块， 问一共有多少种买法
#  2  写一个99乘法表

counter =0
for i in range(0,34):
    for j in range(0,101):
        for k in range(0,201):
            if i+j+k == 100 and (i*3+j+k*0.5) == 100:
                counter+=1
                print(i,j,k)
print(counter)


for x in range(1,10):
    for y in range(1,x+1):
        print('{}*{}={} \t'.format(x,y,x*y),  end='')
    print("")


'''
学习点：end=''  作用使print不会默认换行
'''
