class person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(person):
    def __init__(self, name, idnumber, salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnumber)
a=Employee("Sebastion", 886012, 20000000, "Intern")
a.display()