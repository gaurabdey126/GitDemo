# Exercise 1: Reverse the following tuple
# # aTuple = (10, 20, 30, 40, 50)
#
# a = (10, 20, 30, 40, 50)
# print(a[::-1])
#
# OUTPUT::::
# (50, 40, 30, 20, 10)
###########################################################################################################
#Exercise 2: Access value 20 from the following tuple
#aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
#
# aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
# print(aTuple[1][1])
####################################################################################################
# Exercise 3: Create a tuple with single item 50

# a=(50,) # comma after a single digit is a must to differentiaite it from a value
# print(a)
####################################################################################
# Exercise 4: Unpack the following tuple into 4 variables
# aTuple = (10, 20, 30, 40)
#
# aTuple = (10, 20, 30, 40)
# a,b,c,d = aTuple
# print(a)
# print(b)
# print(c)
# print(d)
#
# OUTPUT::::
# 10
# 20
# 30
# 40
#################################################################################
#Exercise 5: Swap the following two tuples
#tuple1 = (11, 22)
#tuple2 = (99, 88)

# tuple1 = (11, 22)
# tuple2 = (99, 88)
#
# a,b=tuple1
# c,d=tuple2
#
# tuple1=c,d
# tuple2=a,b
#
# print(tuple1)
# print(tuple2)
#
# # tuple1, tuple2 = tuple2, tuple1
# # print(tuple2)
# # print(tuple1)
#
# OUTPUT:::::
# (99, 88)
# (11, 22)
#################################################################################################
# Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
# tuple1 = (11, 22, 33, 44, 55, 66)

# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:5]
# print(tuple2)
#
# OUTPUT::::
# (44, 55)
####################################################################################################
# Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
# tuple1 = (11, [22, 33], 44, 55)

# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]=222
#
# print(tuple1)
#
# OUTPUT::::
# (11, [222, 33], 44, 55)
##########################################################################################################
#Sorting in tuple
# org_list = [3, 1, 4, 5, 2]
#
# org_list.sort()
# print(org_list)
# # [1, 2, 3, 4, 5]
#
# #By default, the list is sorted in ascending order. If you want to sort in descending order, set the parameter reverse to True.
# org_list.sort(reverse=True)
# print(org_list)
# # [5, 4, 3, 2, 1]
#
# Specifying a list to sorted() returns a sorted list. The original list remains unchanged.
# org_list = [3, 1, 4, 5, 2]
# new_list = sorted(org_list)
# print(org_list)
# print(new_list)
# # [3, 1, 4, 5, 2]
# # [1, 2, 3, 4, 5]
#
# Passing a string to sorted() returns a list containing the sorted characters as elements.
# org_str = 'cebad'
# new_str_list = sorted(org_str)
# print(org_str)
# print(new_str_list)
# # cebad
# # ['a', 'b', 'c', 'd', 'e']
#
# Use the join() method to concatenate a list of characters into a single string.
# Concatenate strings in Python (+ operator, join, etc.)
# new_str = ''.join(new_str_list) ###### very important function for joining
# print(new_str)
# # abcde

################################################################################################################
# Exercise 8: Sort a tuple of tuples by 2nd item
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
#
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# tuple2 = sorted(tuple1, key=lambda x: x[1]) ### imp to understand
#
# print(tuple2)
#
# OUTPUT:::
# [('c', 11), ('a', 23), ('d', 29), ('b', 37)]
##################################################################################################################
#Exercise 9: Counts the number of occurrences of item 50 from a tuple
# tuple1 = (50, 10, 60, 70, 50)
# count=tuple1.count(50)
# print(count) #2
###########################################################################################################
# Exercise 10: Check if all items in the following tuple are the same
# tuple1 = (45, 45, 45, 45)

# tuple1 = (45, 45, 45, 45)
# for i in tuple1:
#     if i==45:
#         print ("True")
#     else:
#         print ("False")
#         i+=1

################################################################################################################