print("Do you wanna invest")
print("Yes")
print("No")
invest=str(input("Which one?: "))
if (invest=="Yes"):
    print("Ok, what do you want to buy")
    print("select yoour ride")
    print("1.bike")
    print("2.car")
    print("3. boat")
    choice=int(input("Enter yor choice: "))
    if (choice==1):
        print ("what type of bike")
        print("1.Ninja h2r")
        print("2.Yamaha")
        print("3.suziki")
        type=int(input("Enter type of bike: "))
        if choice==1:
            print("You have chosen Ninja H2R")
        elif (type==2):
            print("You have chosen Yamaha")
        else:
            print("you have chosen Suziki")
    elif (choice==2) :
        print("What type of car")
        print("1.American muscle")
        print("2.German")
        print("3.Jdm")
        hashir=int(input("what type of car: "))
        if (hashir==1):
            print("You have chosen American muscle")
        elif (hashir==2):
            print("You have chosen German")
        else:
            print("JDMを選択しました")
    else:
        print("what type of boat")
        print("1.ship")
        print("2.cruise")
        print("3.boat")
        asif=int(input("What type of boat: "))
        if (asif==1):
            print("You have chosen ship")
        elif (asif==2):
            print("You have chosen cruise ship")
        else:
            print("You have chosen a boat")
else:
    print("Ok")