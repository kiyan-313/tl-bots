class India():
    def capital(self):
        print('new delhi is the capital of India')
    def language(self):
        print('hindi is the most widely spoken language of India')
    def type(self):
        print('india is a developing country')

class Usa():
    def capital(self):
        print('washington,d.c is the capital of usa')

    def language(self):
        print('english is the primary language of usa')

    def type(self):
        print('usa is a developing country')

obj_ind = India()
obj_usa = Usa()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()