# There are four methods to add elements to a List in Python.
#
# append(): append the object to the end of the list.
# insert(): inserts the object before the given index.
# extend(): extends the list by appending elements from the iterable.
# List Concatenation: We can use + operator to concatenate multiple lists and create a new list.

###########################################################################################################
# CREATING A NEW LIST:
# l=[]
# n=int(input('Enter number of items reqd in the list: '))
# for i in range (0,n):
#     item=int(input())
#     l.append(item)
# print(l)

######################################################################################################################
#Exercise 1: Reverse a given list in Python
#aLsit = [100, 200, 300, 400, 500]

# aLsit = [100, 200, 300, 400, 500]
# print(aLsit[::-1])
#
# OUTPUT:::
# [500, 400, 300, 200, 100]
########################################################################################################
# Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list4=zip(list1, list2)
# list4=set(list4)
# print(list4) ## {('i', 's'), ('M', 'y'), ('na', 'me'), ('Ke', 'lly')}
#
# list3 = [i+j for i, j in zip(list1, list2)]
# print(list3)

# OUTPUT::::
# ['My', 'name', 'is', 'Kelly']
#####################################################################################################

# # Python code to demonstrate the working of
# # zip()
#
# # initializing lists
# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]
#
# # using zip() to map values
# mapped = zip(name, roll_no, marks)
#
# # converting values to print as set
# mapped = set(mapped)
#
# # printing resultant values
# print("The zipped result is : ", end="")
# print(mapped)

# OUTPUT::::::::::::
# The zipped result is : {('Shambhavi', 3, 60), ('Astha', 2, 70),
# ('Manjeet', 4, 40), ('Nikhil', 1, 50)}
###################################################################################################################
#Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
# aList = [1, 2, 3, 4, 5, 6, 7]

# lst = [1, 2, 3, 4, 5, 6, 7]
# lst = [i*i for i in lst]
# print (lst)
#
# OUTPUT:::::
# [1, 4, 9, 16, 25, 36, 49]
#############################################################################################################
#Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# list3 = [i+j for i in list1 for j in list2]
# print(list3)

# OUTPUT::::
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
###############################################################################################################################
#Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# for i,j in zip(list1, list2[::-1]):
#     print(i, j)
#
# OUTPUT::::::::
# 10 400
# 20 300
# 30 200
# 40 100
##########################################################################################################################
#Exercise 6: Remove empty strings from the list of strings
#list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1 = list(filter(None,list1)) #list(filter())
# print(list1)
#
# OUTPUT::::::
# ['Mike', 'Emma', 'Kelly', 'Brad']
########################################################################################################################
# Exercise 7: Add item 7000 after 6000 in the following Python List
#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
#
# print(list1)
#
# OUTPUT::::::::::::::::
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
#####################################################################################################################
# Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
# # list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sublist= ["h", "i", "j"]
#
# list1[2][1][2].extend(sublist) ###extend functionalist as .append can take only one argument
# print(list1)
#
# OUTPUT:::::
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
###############################################################################################################################
## .INDEX() function
# list_name.index(element, start, end) --- Returns lowest index where the element appears. (start and end is optional)
#Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
#list1 = [5, 10, 15, 20, 25, 50, 20]
#
# list1 = [5, 10, 15, 20, 25, 50, 20]
#
# index=list1.index(20)
# print(index) #3, as the lowest index number of 20 is 3
#
# list1[index]=200
# print(list1)
#
# OUTPUT::::
# [5, 10, 15, 200, 25, 50, 20]
###################################################################################################################################
# Exercise 10: Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]

# list1 = [5, 20, 15, 20, 25, 50, 20]
#
# list1=list(filter(lambda i: i!=20, list1)) ## using lambda function in list
# print (list1)
#
# Output::::
# [5, 15, 25, 50]
########################################################################################################################################



