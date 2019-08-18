'''
写以个程序，接收以空格为间隔的单词输入，然后去掉重复单词，排序，输出这些单词
'''


input_string = list(input().split(' '))
list1 = list(set(input_string))
list1.sort()

print(' '.join(list1))


'''
学习点：  list  去重， 可以利用set的唯一性，先转换成set，再转换成list，或者遍历，将不在其中的，加到另一个list当中
        这道题我自己有一个误区的地方是，output_string = list.sort(),这个错误的，不可以将list直接赋值给一个变量
'''