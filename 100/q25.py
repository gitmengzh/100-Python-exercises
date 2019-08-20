'''
定义一个类，它具有类参数并具有相同的实例参数
'''

class Person:
    name = "Person"

    def __init__(self,name=None):
        self.name = name

        