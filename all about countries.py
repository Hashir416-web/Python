class india:
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi") 
    def type(self):
        print("Democratic")
class Australia:
    def capital(self):
        print("Canberra")
    def language(self):
        print("English")
    def type(self):
        print("Democratic")
obj_india = india()
obj_aus = Australia()
for country in (obj_india, obj_aus):
    country.capital()
    country.language()
    country.type()