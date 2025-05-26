class IOSstring():
    def __init__(self, string):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a string: ")
    
    def print_string(self):
        print("Result is:", self.str1.upper())
str = IOSstring()
str1 = str.get_string()
str.print_string()