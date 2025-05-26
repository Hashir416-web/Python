class employee:
    def __init__(self, name, age, salary):
        print ("Employee created")
    def __del__(self):
        print ("destructor called")
def create_obj():
    print("Creating an object...")
    obj = employee()
    print("Function is returning...")
    return obj
print('Calling create_obj()funtion')
obj = create_obj() 
print ("Program has ended...")