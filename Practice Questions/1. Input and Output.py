# #Exercise 1: Accept two numbers from the user and calculate multiplication
# a=int(input("Enter 1st Number: "))
# b=int(input("Enter 2nd Number: "))
# mul=a*b
# print('Multiplication of the given 2 numbers are', mul)
#
# OUTPUT::::
# Enter 1st Number: 2
# Enter 2nd Number: 18
# Multiplication of the given 2 numbers are 36
#########################################################################################################################
# #Exercise Question 2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function
#
# print ('My', 'Name','Is','James', sep="**")
#
# Output::::
# My**Name**Is**James
#########################################################################################################################
# #Exercise 3: Convert decimal number to octal using print() output formatting
# #8
# print (oct(8))
# print(bin(8))
# print(hex(8))
#
# OUTPUT:::
# 0o10
# 0b1000
# 0x8
##########################################################################################################
#Exercise 4: Display float number with 2 decimal places using print()

# n=45358.541315234345345456456
# print('%0.2f' %n)
# print('%0.5f' %n)
# # OUTPUT::::
# 45358.54
# 45358.54132
########################################################################################################
# #Misc: Square for a list of numbers
#
# def square(a,b,c):
#     for i in range(a,b,c):
#         sq=i*i
#         print (sq, end='\t')
#         i+=1
#
# square(2,10,2) #calling function with arguments
#
# # Output:::
# # 4	16	36	64
####################################################################################################################
#Exercise 5: Accept a list of 5 float numbers as an input from the user

# float_num=[]
# n=int(input('Enter the List size: '))
#
# for i in range (0,n):
#     print ('Enter number at Location, ',i,':')
#     item = float(input())
#     float_num.append(item)
#
# print ('User List is ',float_num)
#
# OUTPUT::::::::
# Enter the List size: 5
# Enter number at Location,  0 :
# 3.4
# Enter number at Location,  1 :
# 34.
# Enter number at Location,  2 :
# 23.89765
# Enter number at Location,  3 :
# 5.765
# Enter number at Location,  4 :
# 4.8909
# User List is  [3.4, 34.0, 23.89765, 5.765, 4.8909]
#####################################################################################################################################
#Exercise 7: Accept any three string from one input() call

# str1, str2, str3 = input('Enter 3 string values:').split() #split take the input values wit space in between by default
# print (str1, str2, str3)
#
# OUTPUT::::::::
# Enter 3 string values:How Are You?
# How Are You?
#####################################################################################################
# str1, str2, str3 = input('Enter 3 string values:').split(',') #split will take the values with ',' in between them
# print (str1, str2, str3)
#
# OUTPUT:::::::::
# Enter 3 string values:How,Are,You?
# How Are You?
############################################################################################################################
#Exercise 8: Format the following data using a string.format() method.
# Given:
# totalMoney = 1000
# quantity = 3
# price = 450
# Expected Output: I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = 1000 #{0} indexed at 0 position
quantity = 3 #{1}
price = 450 #{2}

print('I have %d dollars so I can buy %d football for %0.2f dollars.'%(totalMoney,quantity,price))#formatted String

print('I have {0} dollars so I can buy {1} football for {2:0.2f} dollars.'.format(totalMoney, quantity, price))

# OUTPUT:::::::
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.
##############################################################################################################################

