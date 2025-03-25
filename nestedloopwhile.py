num=int(input("Enter yout number: "))
t=num
numLen=0
while t>0:
    numLen=numLen+1
    t=(t/10)
if numLen>=4:
    numLen=int(numLen/2)
    chk=0
    while num>0:
        rem=num%10
    if chk==numLen:
        minOne=rem 