def add(p,q):
    return p + q
def subtract(p,q):
    return p - q
def multiply(p,q):
    return p * q
def divide(p,q):
    return p/q
print ("please select operation")
print ("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice=input("Please choose a option a/b/c/d: ")
num_1=int(input("Please enter the first numeral: "))
num_2=int(input("Please choose your second numeral: "))
if (choice=='a'):
    print ( num_1,"+", num_2 , "=",add(num_1,num_2))
elif(choice=='b'):
    print ( num_1,"-", num_2 , "=", subtract(num_1,num_2))
elif (choice=='ç'):
    print ( num_1,"*", num_2 , "=",multiply(num_1,num_2))
elif (choice=='d'):
    print ( num_1,"/", num_2 , "=",divide(num_1,num_2))
else:
    print("This is a invalid term")