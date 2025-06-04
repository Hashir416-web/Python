from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("I can crawl")
class dog(Animal):
    print("I can bark")
class lion(Animal):
    def move(self):
        print("I can roar")
r=human()
r.move()
k=snake()
k.move()
d=dog()
d.move()
l=lion()
l.move()
