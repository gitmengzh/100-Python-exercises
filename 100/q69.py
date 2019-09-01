'''
请编写二进制搜索功能，搜索排序列表中的项目。 该函数应返回列表中要搜索的元素的索引。
'''
import math
def bin_search(li,element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index == -1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

li = [1,2,3,4,6,8,33,3232,3452]
print (bin_search(li,33))


'''
这个涉及到排序算法
'''