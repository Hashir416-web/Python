from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def print(self,x):
        print("Pass value is",x)
    @abstractmethod
    def task(self):
        print("We are in abstract class")
class test_class(AbstractClass):
    def task(self):
        print("We are in test class")
        def task2(self):
            print("We are in task_class")
test_obj = test_class()
test_obj.task()
test_obj.print(100)