try:
    number=int(input("Enter a number: "))
    print ("The number is entered", number)
except ValueError as ex:
    print("Exception:", ex)