class Animal:
    eyes=2
    def move(self):
        print("moving")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    

a1=Dog('Rocky')
print(a1.name)
a1.move()
print(a1.eyes)

#multilevel inheritance
class Car:
    color='black'
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print('car stopped')

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner('petrol')
print(car1.type)

print(car1.color)
car1.start()
#multiple inheritance
class A:
    varA="welcome to class A"

class B:
    varB='welcome to class B'
class C(A,B):
    varC='welcome to class C'
obj=C()
print(obj.varA,obj.varB,obj.varC)

#super method 
class Bike:
    def __init__(self,type):
        self.type=type
class FZ(Bike):
    def __init__(self,color,type):
        super().__init__(type)
b1=FZ('black','petrol')
print(b1.type)