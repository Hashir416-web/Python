rowSize=int(input("Ënter the amount of rows you want to add: "))
if rowSize%2==0:
    halfdiamondrow=int(rowSize/2)
else:
    halfdiamondrow=int(rowSize/2)+1
space=halfdiamondrow-1
for i in range(1,halfdiamondrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,halfdiamondrow):
    for j in range(1,space+1):
        print(end=(" "))
    space=space+1
    num=1
    for j in range(1,2*(halfdiamondrow-i)):
        print(end=str(num))
        num=num+1
    print()