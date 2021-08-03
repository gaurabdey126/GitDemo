#Create a function that can accept two arguments name and age and print its value

# def personal(name, age):
#     print(name)
#     print(age)
#
# personal('Gaurab', 32)
######################################################################################################
#Exercise 4: Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 to salary

# def showEmployee(name, salary=9000): ###setting 9000 as default
#     print ('Employee',name, 'salary is', salary)
#
# showEmployee('John')
# showEmployee('John', 12000)
#
# OUTPUT::::
# Employee John salary is 9000
# Employee John salary is 12000
###########################################################################################################################
# Exercise 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them.
# # And also it must return both addition and subtraction in a single return call
#
# def calculation(a,b):
#     sum=a+b
#     if a>b:
#         subtract=a-b
#     else:
#         subtract=b-a
#     return sum,subtract
#
# print(calculation(100,1000))
#
# OUTPUT::::
# (1100, 900)
#################################################################################################################
# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
#
# def outer(a,b):
#     def inner(a,b):
#         add1= a+b
#         return add1
#     add2=inner(a,b)+5
#     print (add2)
#
# outer(100, 1000)
#
# OUTPUT:::
# 1105
#####################################################################################################################
# Exercise 6: Write a recursive function to calculate the sum of numbers from 0 to 10

# def calSum(num):
#     if num:
#         return num+calSum(num-1)
#     else:
#         return 0
#
# print (calSum(10))
#
# OUTPUT::::
# 55
########################################################################################################################
# Exercise 7: Assign a different name to function and call it through the new name

# def oldFunc(name, age):
#     print ('Name of student is {} and age is {}'.format(name,age))
#
# newFunc= oldFunc
#
# newFunc('John',32)
#
# OUTPUT:::::
# Name of student is John and age is 32
######################################################################################################################
# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

# def even(a,b):
#     x=[]
#     for i in range (a,b):
#         if i%2==0:
#             x.append(i)
#             i+=1
#     print (x)
#
# even(4,30)

# OUTPUT::::
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
#                 [OR]
# print(list( range(4, 30, 2))) ### [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
#################################################################################################################
# Exercise 9: Return the largest item from the given list

# aList = [4, 6, 8, 24, 12, 2]
# print(max(aList)) ### 24

##################################################################################################################

