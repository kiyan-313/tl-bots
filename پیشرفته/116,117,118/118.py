
class Person:
    def __init__(self):
         self.a = 7  #public
         self._b = 8   #protrctrd
         self.__age=19  #private

    @property
    def age(self):
         return self.__age

    @age.setter
    def age(self,value):
        if value > 50:
          raise ValueError('sorry')
        self.__age=value

    @age.deleter
    def age(self):
        del self.__age

p1=Person()
print(p1.age)
p1.age=45
print(p1.age)
