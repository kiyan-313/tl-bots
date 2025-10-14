class Teacher:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'amir str'
    def __repr__(self):
        return 'amir repr'
t=Teacher('amir')
# print(t)
# print(t.name)
print(str(t))
print(repr(t))