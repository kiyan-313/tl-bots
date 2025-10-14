cs=[
    {
        'title':'python',
        'teacher':'amiri'
    },
    {
        'title':'html',
        'teacher':'dehyami'
    },
    {
        'title':'php',
        'teacher':'enayati'
    }
]

class user:
    def __init__(self,firstname,lastname):
        self.fname=firstname
        self.lname=lastname

    def fullname(self):
        print(f' my full name is{self.fname} {self.lname}')

class Student(user):
        def __init__(self, firstname, lastname,email):
             super().__init__(firstname, lastname)
             self.email=email
             self.courses=[]


        def fullname(self):
             print('i am an student')
             super().fullname()
        

        def printcourses(self):
            if self.courses:
                  for course in self.courses:
                       print(course['title'])
            else:
                print('this user has no course')

class teacher(user):
     def __init__(self, firstname, lastname,code):
          super().__init__(firstname, lastname)
          self.code=code

     def fullname(self):
          print('i am a teacher')
          super().fullname()


s1=Student('amir','amiri','amir@gmail.com')

s1.courses.append(cs[1])
s1.courses.append(cs[0])
s2=Student('ahmad','ahmadi','ahmad@gmail.com')
s2.printcourses()

