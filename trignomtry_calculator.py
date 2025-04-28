import math
def trigmetry_calculator():
    print("what would you like to calculate?")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Log")
    print("5. hyp")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        anglev= float(input("Enter the angle in degrees: "))