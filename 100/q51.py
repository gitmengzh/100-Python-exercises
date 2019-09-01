'''
定义一个名为Rectangle的类，它可以通过长度和宽度构造。 Rectangle类有一个可以计算区域的方法。
'''


class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calcArea(self):
        area = self.length*self.width
        print(area)




rect = Rectangle(5,4)
rect.calcArea()