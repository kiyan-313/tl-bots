class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print(self.firstname,self.lastname)


p1=Person('amir','amiri')
print(p1.firstname)
p1.printname()