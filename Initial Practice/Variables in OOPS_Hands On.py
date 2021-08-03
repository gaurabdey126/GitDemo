# There are 2 type of variables in OOPS:
# Instance variable: which is created under __init__
# Class(static) variable : which is created outside __init__....It is common to all the objects present in that class.

# class Car:
#     wheels = 4 #Class variable
#
#     def __init__(self):
#         self.mil = 10       #instance variable
#         self.brand = 'BMW'  #instance variable
#
# c1=Car()
# c2=Car()
#
# print (c1.mil, c1.brand, c1.wheels)
# print (c2.mil, c2.brand, c2.wheels)
#
# Output::::
# 10 BMW 4
# 10 BMW 4
#################################################################################################################################

class Car:
    wheels = 4 #Class variable

    def __init__(self):
        self.mil = 10       #instance variable
        self.brand = 'BMW'  #instance variable

c1=Car()
c2=Car()

Car.wheels=8    #changing the Class variable value

print (c1.mil, c1.brand, c1.wheels)
print (c2.mil, c2.brand, c2.wheels)

Output::::
10 BMW 8
10 BMW 8