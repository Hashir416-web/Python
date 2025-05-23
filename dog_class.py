class dog:
	def __init__(self, breed, age):
		self.breed = breed
		self.age = age
Billy = dog("Golden retrievr", 5)
bob = dog("German shepard", 3)
print("The name of the dog is",Billy.breed)
print("The age of the dog is",(Billy.age))
print("The name of the dog is",bob.breed)
print("The age of the dog is",(bob.age))