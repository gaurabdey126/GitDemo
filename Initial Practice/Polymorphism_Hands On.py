# #Polymorphism: one thing multiple forms
#
# #DUCK TYPING
# #
# class Pycharm:
#     def execute(self):
#         print('Compile')
#         print ('Run')
#
# class Myeditor:
#     def execute(self):
#         print('Spell Check')
#         print ('Symbol')
#
# def myfunction(self):
#    self.execute()
#
# p=Pycharm()
# m=Myeditor()
#
# myfunction(p)
# myfunction(m)
#
# # OUTPUT:::
# # Compile #p
# # Run #p
# #
# # Spell Check #m
# # Symbol #m
# ####################################################################################################################################
#
# # #OPERATOR OVERLOADING:
# # CALLING AND USING BACKGROUND METHOD
# # + -> __ADD__()
# # - -> __SUB__()
# # ...
# #Q. We want to SUM up the marks of 2 students
# class Student:
#     def __init__(self, m1, m2):
#         self.m1=m1
#         self.m2=m2
#
#     def __add__(self, other): #self=s1, other=s2
#         sum1=self.m1+other.m1
#         sum2=self.m2+other.m2
#         sum3=sum1 + sum2
#         return sum3
#
# s1=Student(50,40)
# s2=Student(60,50)
#
# sum3=s1+s2
# print (sum3) #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'...Hence we have to OVERLOAD the add method
#
# # OUTPUT:::
# # 200
# #####################################################################################################
# # #OPERATOR OVERLOADING:
# #Q. We want to see which student won
# class Student:
#     def __init__(self, m1, m2):
#         self.m1=m1
#         self.m2=m2
#
#     def __add__(self, other): #self=s1, other=s2
#         sum1=self.m1+other.m1
#         sum2=self.m2+other.m2
#         sum3=sum1 + sum2
#         return sum3
#
#     def __gt__(self, other):
#         r1=self.m1+self.m2
#         r2=other.m1+other.m2
#
#         if r1>r2:
#             return True
#         else:
#             return False
# #
# # s1=Student(50,40)
# # s2=Student(60,50)
# #
# # sum3=s1+s2
# # print (sum3) #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'...Hence we have to OVERLOAD the add method
# #
# # if s1>s2:
# #     print('s1 got more marks and WON')
# # else:
# #     print('s2 got more marks and WON') #TypeError: '>' not supported between instances of 'Student' and 'Student'...Hence we have to OVERLOAD the Greater than method
# #
# #
# # # OUTPUT:::
# # # 200
# # #s2 got more marks and WON
# # ##################################################################################################################################
#
# ##METHOD OVERLOADING::When two or more methods in the same class have the same name but different parameters, it's called Overloading.
#
# class Math:
#     def sum(self,a,b):
#         s=0
#         s=a+b+1   #have added 1 here just to make different from the below method
#         return s
#
#     def sum(self,a=None, b=None, c=None): #if we pass more than 2 parameters
#         s=0
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s=a
#         return s
#
# s1=Math()
# print(s1.sum(3,2,4)) #Output 9
# print(s1.sum(3,2)) #Output 5
# print(s1.sum(3)) #Output 3
# ##################################################################################################################################
#
# class Math:
#     def sum(self,a,b):
#         s=0
#         s=a+b+1   #have added 1 here just to make different from the below method
#         return s
#
#     # def sum(self,a=None, b=None, c=None): #if we pass more than 2 parameters
#     #     s=0
#     #     if a!=None and b!=None and c!=None:
#     #         s=a+b+c
#     #     elif a!=None and b!=None:
#     #         s=a+b
#     #     else:
#     #         s=a
#     #     return s
#
# s1=Math()
# print(s1.sum(3,2)) #Output 6 as the Overloading method is commented and it is taking the first method
###################################################################################################################################

#METHOD OVERRIDING: When the method signature (name and parameters) are the same in the superclass and the child class, it's called Overriding.

# class A:
#     def show(self):
#         print ('in A')
#
# class B:
#     pass
#
# a1=B()
# a1.show() #Output::: AttributeError: 'B' object has no attribute 'show'
#################################################################################################################################

class A:
    def show(self):
        print ('in A')

class B(A):
    def show(self):
        print ('in B')

z1=B()
z1.show() #Output::: in B::::::: as the method call will call the value from class B as B itself has got a method as "show" and it doesn't require from A
###################################################################################################################