print("Please insert numerator: ")
numn= int(input())
print("Please insert denomintor:")
numd= int(input())
if numn%numd==0:
    print("\n" +str(numn)+ "is divisible by" +str(numd))
else:
    print("\n"+str(numn)+ "is not divisibe by"+str(numd))