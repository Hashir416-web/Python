medical_cause= input("did you have medical cause of y or n")
atten=int(input("Enter the attendace percentage of the student: "))
if medical_cause == 'y':
    print("your allowed to take exam")
else:
    if atten>=75:
        print("allowed")
    else:
        print("Not allowed to take exams")