import random
playing=True
number=str(random.randint(10,20))
print("I will generate a random number and you will have to guess it, and take1 guess at a time.")
print("The game ends with your hero")
while playing :
    guess=input("Give me your best guess \n")
    if number == guess:
        print("You got the digit, The number was. ", number)
        break
    else:
        print("Yikes that guess wasn't acurate \n")