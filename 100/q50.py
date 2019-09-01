'''
Use def methodName(self) to define a method
'''

class Animal():
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print(self.name+" eat "+food)



Cat = Animal("cat")
Cat.eat('meat')