string=input("Please enter your own word: ")
char=input("please enter your own charater: ")
i=0
count=0
while(i<len(string)):
    if (string[i] == char):
        count=count+1
    i=i+1
print ("The total amount of time", char,"has occured=", count )