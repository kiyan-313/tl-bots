class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def fullname(self):
        print(f' my full name is{self.firstname} {self.lastname}')

p1=Person('amir','amiri')

class Student(Person):
        def __init__(self, firstname, lastname,email):
             super().__init__(firstname, lastname)
             self.email=email


        def fullname(self):
             print('i am an student')
             super().fullname()

s1=Student('hosen','enayati','hosen@gmail.com')

s1.fullname()
