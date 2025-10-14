class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print(self.firstname,self.lastname)

p1=Person('amir','amiri')

class Student(Person):
        def __init__(self, firstname, lastname,age):
             super().__init__(firstname, lastname)
    # def __init__(self, firstname, lastname,age):
    #     Person.__init__(firstname, lastname)
             self.age=age

s1=Student('amir','amiri',23)
print(s1.age)
s1.printname()