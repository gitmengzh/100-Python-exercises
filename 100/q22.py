'''
输入内容，统计一下每个词的个数
'''

freq = {}
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1  #这个操作。。。。

words = list(freq.keys())
words.sort()

for w in words:
    print("%s:%d"%(w,freq[w]))
'''
学习点： 字典的get方法  
        思路：  分割句子，将单词作为字典的key  将单词的个数作为value,  将key作为一个list存储，然后循环list，输出
                自己想不到的地方（怎么操作字典）
'''