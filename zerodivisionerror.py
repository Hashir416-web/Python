try:
    num1, num2=eval(input("Enter 2 numbers, sperated by a coma: "))
    result=num1/num2
    print("result is", result)
except ZeroDivisionError:
    print("Division by 0 is an error")
except SyntaxError:
    print("There is a missing coma")
except:
    print("Wrong unput")
else:
    print("No exceptions")
finally:
    print("There wil exucute no matter what.")