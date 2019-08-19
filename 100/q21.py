'''
一个机器人从（0，0）出发，跟据输入的操作进行，UP,DOWN 控制第一个坐标，LEFT，RIGHT控制第二个坐标，最后输出距离原点的距离，结果是浮点数四舍五入
input: RIGHT 4
       LEFT  3
       输出5
'''

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "DOWN":
        pos[0]-=steps
    if direction == "UP":
        pos[0]+=steps
    if direction == "LEFT":
        pos[1] -= steps

    if direction == "RIGHT":
        pos[1] += steps
    else:
        print("没有该操作，请重新输入")
print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))


'''
学习点：  sqrt:  求平方跟
        思路:还是将操作和坐标分开，判断操作，然后计算坐标
'''