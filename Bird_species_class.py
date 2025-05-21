class parrot:
    def __init__(self, name, age,):
        self.name = name
        self.species = age

blu = parrot("Blu", 10)
woo = parrot("Woo", 15)
print("The species of blu is {}",format(blu.species))
print("The species of woo is {}",format(woo.species))
print("{} is {} years old",format(blu.name,blu.species))
print("{} is {} years old",format(woo.name,woo.species))