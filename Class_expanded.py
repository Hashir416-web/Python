class object:
    def __init__(self,year,age,name):
        self.year = year
        self.age = age
        self.name = name
josh = object(2000,23,"josh")
sebastian = object(2001,22,"sebastian")
print("Hello, i am in",josh.year)
print("my age is ",josh.age)
print("my name is ",josh.name)