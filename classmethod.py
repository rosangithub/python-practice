class Person:
    name="ram"
    # def changeName(self,name):
    #     #Person.name=name
    #     self.__class__.name=name
#i want to change the name  of the class 
#we can use the class method to change the name of the class\

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName('himal')
print(p1.name)
print(Person.name)