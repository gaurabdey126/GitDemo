#Constructor - allocate size to object
# Self ---> suppose we have multiple objects(say c1, c2, c3, etc.). When we are calling c1, then self takes the place of c1...basically Self replace the object that is called

#class Employee:
#    def __init__(self):
#        self.name ='john'
#        self.age = 28
#        self.gender ='M'

#c1 = Employee() #object creation in class Employee
#c2 = Employee() #object creation in class Employee

#print(c1.name, c1.age, c1.gender) #we are calling c1, but self is taking place of c1
#print(c2.name, c2.age, c2.gender) #we are calling c2, but self is taking place of c2

#Output:::
#john 28 M
#john 28 M
##############################################################################################################

# class Employee:
#     def __init__(self):
#         self.name ='john'
#         self.age = 28
#         self.gender ='M'
#
# c1 = Employee() #object creation in class Employee
# c2 = Employee() #object creation in class Employee
#
# c1.name='bond' #we are changing values of the self
# c2.gender = 'F'
#
# print(c1.name, c1.age, c1.gender) #we are calling c1, but self is taking place of c1
# print(c2.name, c2.age, c2.gender) #we are calling c2, but self is taking place of c2

# Output:::
# bond 28 M
# john 28 F
#############################################################################################################

# class Employee:
#     def __init__(self):
#         self.name ='john'
#         self.age = 28
#         self.gender ='M'
#
#     def update(self):
#         self.age=30
#
# c1 = Employee()  # object creation in class Employee
# c2 = Employee()  # object creation in class Employee
#
# c1.name='bond' #we are changing values of the self
# c2.gender = 'F'
#
# c1.update() #updating the age for c1
# c2.update() #updating the age for c1
#
# print(c1.name, c1.age, c1.gender) #we are calling c1, but self is taking place of c1
# print(c2.name, c2.age, c2.gender) #we are calling c2, but self is taking place of c2
#
# Output::::
# bond 30 M
# john 30 F

###############################################################################################################################

# class Employee:
#     def __init__(self):
#         self.name ='john'
#         self.age = 28
#         self.gender ='M'
#
#     # def update(self):
#     #     self.age=30
#
#     def compare(self,c2):
#         if self.age == c2.age:
#             print('They are same')
#         else:
#             print ('They are DIFFERENT')
#
# c1 = Employee()  # object creation in class Employee
# c2 = Employee()  # object creation in class Employee
#
# # c1.name='bond' #we are changing values of the self
# # c2.gender = 'F'
#
# # c1.update() #updating the age for c1
# # c2.update() #updating the age for c1
# #
# # print(c1.name, c1.age, c1.gender) #we are calling c1, but self is taking place of c1
# # print(c2.name, c2.age, c2.gender) #we are calling c2, but self is taking place of c2
#
# c1.compare(c2)
#
#
# # Output::::
# # They are same
#####################################################################################################################################

# class Employee:
#     def __init__(self):
#         self.name ='john'
#         self.age = 28
#         self.gender ='M'
#
#     # def update(self):
#     #     self.age=30
#
#     def compare(self,c2):
#         if self.age == c2.age:
#             print('They are same')
#         else:
#             print ('They are DIFFERENT')
#
# c1 = Employee()  # object creation in class Employee
# c2 = Employee()  # object creation in class Employee
#
# # c1.name='bond' #we are changing values of the self
# # c2.gender = 'F'
#
# # c1.update() #updating the age for c1
# # c2.update() #updating the age for c1
# #
# # print(c1.name, c1.age, c1.gender) #we are calling c1, but self is taking place of c1
# # print(c2.name, c2.age, c2.gender) #we are calling c2, but self is taking place of c2
#
# c1.compare(c2)
# print ('c1:',c1.age, 'c2:',c2.age)
#
#
# # Output::::
# # They are same
# #c1: 28 c2: 28
####################################################################################################################################

class Employee:
    def __init__(self):
        self.name ='john'
        self.age = 28
        self.gender ='M'

    def update(self):
        self.age=30

    def compare(self,c2):
        if self.age == c2.age:
            print('They are same')
        else:
            print ('They are DIFFERENT')

c1 = Employee()  # object creation in class Employee
c2 = Employee()  # object creation in class Employee

# c1.name='bond' #we are changing values of the self
# c2.gender = 'F'

c1.update() #updating the age for c1
# c2.update() #updating the age for c1
#
# print(c1.name, c1.age, c1.gender) #we are calling c1, but self is taking place of c1
# print(c2.name, c2.age, c2.gender) #we are calling c2, but self is taking place of c2

c1.compare(c2)
print ('c1:',c1.age, 'c2:',c2.age)


# Output::::
# They are DIFFERENT
# c1: 30 c2: 28


