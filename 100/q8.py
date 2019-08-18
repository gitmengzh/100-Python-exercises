'''
 输入N个单词，以逗号分割，然后以字母排序后，输出，并用逗号隔开

'''

orignal_string = input().split(',')
final_string = sorted(orignal_string)
print(','.join(final_string))



'''
学习点：  list.sort() 函数   list.sort(cmp = None, key = None, reverse = False
                        cmp 可选参数，如果指定该参数，那么将按照该参数排序
                        key 主要用来进行元素的比较，只有一个参数，指定可迭代对象中的一个元素来进行排序
                        reverse  True 降序， False 升序，默认值
        sorted  使用于任何可迭代的容器
        sorted(iterable, cmd= None, key = None, reverse = False)
        第一个参数，可迭代对象， 其他与sort一样
'''