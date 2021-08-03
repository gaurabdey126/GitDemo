#ABSTRACT Method and CLASS::An abstract class is a class that is declared abstract —it may or may not include abstract methods. Abstract classes cannot be instantiated, but they can be subclassed. ...
# However, if it does not, then the subclass must also be declared abstract .

# What is the purpose of abstract class?
# The short answer: An abstract class allows you to create functionality that subclasses can implement or override. An interface only allows you to define functionality, not implement it.
# And whereas a class can extend only one abstract class, it can take advantage of multiple interfaces

# from abc import ABC, abstractmethod
#
# class Computer(ABC):
#     @abstractmethod #This is must to make a method as an ABSTRACT method
#     def process(self):
#         pass # Not declaring any statement
#
# class Laptop(Computer):
#     def process(self):
#         print ('Executing')
#
# class Whiteboard(Computer):
#     def write(self):
#         print('White')
#
# class Programmer:
#     def work(self,com):
#         print('solving bugs')
#         com.process()
#
# com1=Laptop()
# com2=Whiteboard() #TypeError: Can't instantiate abstract class Whiteboard with abstract method process
# prog1=Programmer()
# prog1.work(com2)

################################################################################################################################

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod #This is must to make a method as an ABSTRACT method
    def process(self):
        pass # Not declaring any statement

class Laptop(Computer):
    def process(self):
        print ('Executing')

class Whiteboard:
    def write(self):
        print('White')

class Programmer:
    def work(self,com):
        print('solving bugs')
        com.process()

com1=Laptop()
com2=Whiteboard() #TypeError: Can't instantiate abstract class Whiteboard with abstract method process
prog1=Programmer()
prog1.work(com1)

OUTPUT::::
solving bugs
Executing