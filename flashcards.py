class flashcards:
    def __init__(self,word, meaning):
        self.word = word
        self.meaning = meaning
        def __str__(self):
            return self.word+'('+self.meaning+')'
flash = []
print("Welcome to the flashcard application")
while True:
    word = input("Enter the name you want to add to your flashcard.: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcards(word, meaning))
    option = int(input(" Enter 0 if you want to add more flashcards? (0 for Yes, 1 for No): "))
    if option:
        break
print("\nYour flashcards are:")
for i in flash:
    print(">",i)