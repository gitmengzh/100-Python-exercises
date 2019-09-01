'''
请编写一个程序，使用随机模块和列表理解输出0到10之间的随机偶数。
'''

import random


v = random.choice([i for i in range(0,11) if i%2==0])
print(v)



'''
random choice  接收一个元组,列表,字符串,返回一个随机数
'''