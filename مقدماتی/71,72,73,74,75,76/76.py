class Person:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
    def fullname(self):
        print(f' my name is {self.name} {self.lastname} and my age is{self.age}')
p1=Person('amir','amiri',30)
p1.fullname()
p1.name='jamal'
p1.lastname='samoraii'
p1.fullname()
