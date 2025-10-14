class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print(self.firstname,self.lastname)


class student(Person):
    pass


s1=student('milad','dehyami')

print(s1.firstname)

s1.printname