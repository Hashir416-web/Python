a=int(input("insert the value 1:"))
b=int(input("insert the value 2:"))
c=int(input("insert the value 3:"))
avg= a+b+c/3
print("avg=",avg)
if avg>a and avg>b and avg>c:
    print("%d is highher than %d, %d,%d", (avg, a,b,c))
elif avg > a and avg >b:
    print("%d is highher than %d, %d", (avg, a,b))
elif avg > a and avg>c:
    print("%d is highher than %d, %d", (avg, a,c))
elif avg> b and avg > c:
     print("%d is highher than %d, %d", (avg,b,c))
elif avg>a:
    print("%d is highher than %d", (avg,a))
elif avg>b:
    print("%d is highher than %d", (avg,b))
elif avg>c:
    print("%d is highher than %d", (avg,c))
else:
    print("invalid statement")