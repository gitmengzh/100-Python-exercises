'''
定义一个名为Shape的类及其子类Square。 Square类有一个init函数，它以length为参数。
这两个类都有一个区域函数，可以打印默认情况下Shape的区域为0的形状区域。

'''

class Shape():
    def __init__(self,s):
        self.s = s
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length,s):
        self.lenth = length
        Shape.__init__(self,s)   #Square是Shape的子类,需要在Square初始化函数中对父类的初始化
                                #函数进行初始化
    def area(self):
        return self.lenth*self.lenth


'''
需要提供注意的是，在子类中，如果要继承父类，必须用显明的方式将所继承的父类方法写出来，
例如上面的Person.init(self,name,lang,email)，必须这样写，才能算是在子类中进行了继承。
如果不写上，是没有继承的。用编程江湖的黑话（比较文雅地称为“行话”）说就是“显式调用父类方法”。
对于为什么要用继承：
从技术上说，OOP里，继承最主要的用途是实现多态。对于多态而言，重要的是接口继承性，
属性和行为是否存在继承性，这是不一定的。事实上，大量工程实践表明，
重度的行为继承会导致系统过度复杂和臃肿， 反而会降低灵活性。因此现在比较提倡的是基于接口的轻度继承理念。
这种模型里因为父类（接口类）完全没有代码，因此根本谈不上什么代码复用了。

在Python里，因为存在Duck Type，接口定义的重要性大大的降低，继承的作用也进一步的被削弱了。

另外，从逻辑上说，继承的目的也不是为了复用代码，而是为了理顺关系


'''
