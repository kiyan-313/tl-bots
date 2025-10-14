class Person():
    def __init__(self,name,lastname):
        self.myname=name
        self.mylastname=lastname
    
    def fullname(self):
        print(self.myname)
        print(self.mylastname)

p1=Person('milad','dehyami')
p1.fullname()
         