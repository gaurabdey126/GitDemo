#Class inside a class

class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        self.lap=self.Laptop()

    def show(self): #this function is defined to print , if not this then we have to use the print as displayed below
        print(self.name, self.age, self.roll)
        self.lap.show() #calling the self.lap with show function

    class Laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand, self.ram, self.cpu)


s1 = Student('rahul', 14, 88)
s2 = Student('aryan', 15, 99)

# print(s1.name,s1.age,s1.roll)
# print(s2.name,s2.age, s2.roll)
s1.show()
s2.show()

Output::::
rahul 14 88
hp 8 i5
aryan 15 99
hp 8 i5