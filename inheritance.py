class Student:
    def __init__(self,name):
        self.name=name
s1=Student('Rosan')
print(s1.name)
del s1.name#to deletet the attribute name 
#print(s1.name)

class Account:
    def __init__(self,acc_no,acc_password):
        self.account_no=acc_no
        self.__acc_password=acc_password
        def reset_password(self):
            print("reset password")
            print(self.__acc_password)
a1=Account(5421,123)
print(a1.account_no)

class Person:
    __name="anonymous"
    def __hello(self):
        print("hello gyes my name is Rosan Shrestha")  
    def welcome(self):
        self.__hello()

p1=Person()
#print(p1.__name)
#print(p1.__hello())
p1.welcome()
#inheritance in python 
class Car:
    color='black'
    @staticmethod
    def startCar():
        print("Start car")
    @staticmethod
    def stopCar():
        print("car stopped")
    

    
class ToyotaCar(Car):#method to inherit the parent classw
    def __init__(self,name):
        self.name=name
car1=ToyotaCar('Fortuner')
print(car1.name)
car1.startCar()
car1.stopCar()
print(car1.color)
#types of inheritance 
#single inheritance 
#multilevel inheritance 
#and 
