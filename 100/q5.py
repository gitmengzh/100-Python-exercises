#定义一个类，有两个方法，getString:从控制台获取字符串，printString：以大写的形式打印字符串


class InputOutputString():
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input()


    def printString(self):
        print(self.s.upper())

teststring = InputOutputString()
teststring.getString()
teststring.printString()


'''
学习知识点： upper() 方法将字符串中的小写字母转为大写字母。  str.upper()

'''
