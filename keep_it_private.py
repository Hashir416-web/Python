class myclass:
    __privatevar =27
    def __privmeth(self):
        print("Im in my class")
    def hello(self):
        print("private variable value is:",self.__privatevar)
foo = myclass()
foo.hello()
foo.__privmeth()
