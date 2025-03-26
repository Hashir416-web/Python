print("half pyramid pattern of stars(*)")
n=int(input("amount of rows you want: "))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()