class a:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a < other.a):
            return "Ob1 is less than Ob2"
        else:
            return "Ob1 is not less than Ob2"
    def __eq__(self,other):
        if (self.a == other.a):
            return "Ob1 is equal to Ob2"
        else:
            return "Ob1 is not equal to Ob2"
ob1 = a(2)
ob2 = a(3)
print ("Passed Value is",ob1.a, "and", ob2.a)
print(ob1 < ob2)
ob3 = a(4)
ob4 = a(4)
print ("Passed Value is",ob3.a, "and", ob4.a)
print(ob3 == ob4)