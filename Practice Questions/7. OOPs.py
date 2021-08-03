# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# car1 = Vehicle('100 km/hr', '11 ltr')
# car2 = Vehicle('150 km/hr', '9 ltr')
#
# print ('car1 -> max speed is:',car1.max_speed, '   mileage is:',car1.mileage,)
# print ('car2 -> max speed is:',car2.max_speed, '   mileage is:',car2.mileage)
#
# OUTPUT::::
# car1 -> max speed is: 100 km/hr    mileage is: 11 ltr
# car2 -> max speed is: 150 km/hr    mileage is: 9 ltr
#############################################################################################################################
# OOP Exercise 2: Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass

#########################################################################################################################
# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.
#
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# bus1=Bus('Volvo','180 km/hr','8 km/ltr')
#
# print (bus1.name, bus1.max_speed, bus1.mileage, sep=', ')
#
# OUTPUT::::
# Volvo, 180 km/hr, 8 km/ltr
###########################################################################################################################
# OOP Exercise 4: Class Inheritance
# Given:
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class. You need to use method overriding.
#
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity=80):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# bus1=Bus('Volvo','180 km/hr','8 km/ltr')
# print (bus1.seating_capacity())
#
# OUTPUT:::::
# The seating capacity of a Volvo is 50 passengers
########################################################################################################################
# OOP Exercise 5: Define property that should have the same value for every class instance
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.
#
# class Vehicle:
#     color = 'White'
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# bus1=Bus('Volvo','180 km/hr','8 km/ltr')
# car1=Car('BMW','250 km/hr','10 km/ltr')
#
# print ('Bus -> name:',bus1.name, 'max speed:',bus1.max_speed, 'mileage:',bus1.mileage, 'color:',bus1.color)
# print ('Car -> name:',car1.name, 'max speed:',car1.max_speed, 'mileage:',car1.mileage, 'color:',car1.color)
#
# OUTPUT:::
# Bus -> name: Volvo max speed: 180 km/hr mileage: 8 km/ltr color: White
# Car -> name: BMW max speed: 250 km/hr mileage: 10 km/ltr color: White
#############################################################################################################################
# OOP Exercise 6: Class Inheritance
# # Given:
# # Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
# # If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# # So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# # Note: The bus seating capacity is 50. so the final fare amount should be 5500.
# # You need to override the fare() method of a Vehicle class in Bus class.
# # Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.
#
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return float(self.capacity * 100)
#
# class Bus(Vehicle):
#     def fare(self):
#         total_fare= self.capacity * 100
#         final_fare = total_fare + 0.1*(total_fare)
#         return float(final_fare)
#
# veh1 = Vehicle ("BMW", 14, 5)
# print("Total Vehicle fare is:", veh1.fare())
#
# bus1 = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", bus1.fare())
#
# # OUTPUT:::::
# # Total Vehicle fare is: 500.0
# # Total Bus fare is: 5500.0
##################################################################################################################################################################
# OOP Exercise 7: Determine which class a given Bus object belongs to (Check type of an object)
#
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
# print(type(School_bus)) # <class '__main__.Bus'>
####################################################################################################################
# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
# #
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
# # # use Python's built-in isinstance() function
# print(isinstance(School_bus, Vehicle)) #True
######################################################################################################################

