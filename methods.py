# method ==>    1.instance  2.class 3.static

import datetime

class person :
    def __init__(self , name , height , age):
        self.name = name
        self.height = height
        self.age = age
    def show(self): #define a instance method
        print(f'{self.name} is {self.height} and {self.age} years old')
    @classmethod #define a class method
    def from_birth(cls , name , height , age):
        return cls(name , height , datetime.datetime.now().year - age)
    @staticmethod  #define a static method
    def is_adult(age):
        if age > 18:
            print("yes")
        else :
            print("no")

p1 = person.from_birth('kian' , 175 , 2008)
p1.is_adult(p1.age)
p1.show()  # call instance method

