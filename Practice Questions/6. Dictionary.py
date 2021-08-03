# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# type() ----From Python's perspective, dictionaries are defined as objects with the data type 'dict'
# Get Keys-----The keys() method will return a list of all the keys in the dictionary.
# Get Values----The values() method will return a list of all the values in the dictionary.
# # dict.values() ----- to get the list of VALUES present in the dictionary named "dict"
# dict.keys() ----- to get the list of KEYS present in the dictionary named "dict"
# dict.items() ----- to get the list of KEYS+VALUES pair present in the dictionary named "dict"
# dict.pop() ---- removes the Key and its Values from the dictionary
# dict.clear() ------ Removes all Key-Value pair present in the dictionary
# dict1.update(dict2) ------- Adds all ELEMENTS from dict2 to dict1


# Exercise 1: Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# mydict = dict(zip(keys, values))   ###dict is used to create the dictionary
# print (mydict) # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#
# print(mydict.keys()) # dict_keys(['Ten', 'Twenty', 'Thirty'])
# print(mydict.values()) # dict_values([10, 20, 30])
# print(mydict.items()) # dict_items([('Ten', 10), ('Twenty', 20), ('Thirty', 30)])

# OUTPUT::::
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict_keys(['Ten', 'Twenty', 'Thirty'])
# dict_values([10, 20, 30])
# dict_items([('Ten', 10), ('Twenty', 20), ('Thirty', 30)])
#################################################################################################################
# Exercise 2: Merge following two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = (dict1,dict2)
# print (dict3) ## ({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
# dict1.update(dict2)
# print (dict1) ## {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
##########################################################################################################################
# Exercise 4: Initialize dictionary with default values
# Given:
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}

# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
#
# resDict = dict.fromkeys(employees, defaults)
# print(resDict)
#
# # Individual data
# print(resDict["Kelly"])
########################################################################################################################
# Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#Keys to extract------keys = ["name", "salary"]
#
# sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
#
# keys= ["name", "salary"]
# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)
#
# OUTPUT:::
# {'name': 'Kelly', 'salary': 8000}
####################################################################################################################################
#Exercise 6: Delete set of keys from a dictionary
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keysToRemove = ["name", "salary"]

# sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
#
# sampleDict.pop('name')
# sampleDict.pop('salary')
# print(sampleDict)
#
# OUTPUT::::
# {'age': 25, 'city': 'New york'}
###################################################################################################################################
# Exercise 7: Check if a value 200 exists in a dictionary
# sampleDict = {'a': 100, 'b': 200, 'c': 300}

# sampleDict = {'a': 100, 'b': 200, 'c': 300}
# print(200 in sampleDict.values()) #True
# print('c' in sampleDict.keys()) #True
#####################################################################################################################
# Exercise 8: Rename key city to location in the following dictionary
# # sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
#
# sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# sampleDict['location']=sampleDict.pop('city')
# print (sampleDict)
#
# OUTPUT::::
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
#####################################################################################################################
# Exercise 9: Get the key of a minimum value from the following dictionary
# sampleDict = {'Physics': 82,'Math': 65,'history': 75}
#
# sampleDict = {'Physics': 82,'Math': 65,'history': 75}
# print(min(sampleDict, key=sampleDict.get)) ##Math
#####################################################################################################################
# Exercise 10: Change Brad’s salary to 8500 from a given Python dictionary
# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# # }
#
#
# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }
# sampleDict['emp3']['salary']=8500
# print(sampleDict)
#
# OUTPUT:::::
# {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}
########################################################################################################################################
# Q. A python program to create a dictionary and find the sum of values.

# dict = eval(input('Enter elements in {}: '))
# s = sum(dict.values())
# print ('Sum of values in dictionary is: ', s)
#
# OUTPUT::::
# Enter elements in {}: {'A':10, 'B':20}
# Sum of values in dictionary is:  30
#########################################################################################################################
# Q. Python program to create a dictionary from keyboard and display the elements.
#
# x={}
# n=int(input('How many elements?: '))
#
# for i in range(n):
#     key=input()
#     value=input()
#     x.update({key:value})
# print ('New Dictionary: ', x)
#################################################################################################
# Q. Python Program to create a dictionary with cricket players name and scores in a match.
# Also, we are retrieving runs by entering the player's name.

# x = {}
# n=int(input('How many Players?: '))
#
# for i in range(n):
#     k = input ('Players Name: ')
#     v = input ('Runs: ')
#     x.update({k:v})
# print (x)
#
# print(x.keys())
# print(x.values())
#
# name = input('Enter Players Name: ')
# runs = x.get(name, -1)
# if (runs == -1):
#     print ('Player not found')
# else:
#     print ('{} made {} runs'.format(name, runs))
#
# OUTPUT::::
# How many Players?: 3
# Players Name: sachin
# Runs: 100
# Players Name: ganguly150
# Runs: 150
# Players Name: sehwag
# Runs: 80
# {'sachin': '100', 'ganguly150': '150', 'sehwag': '80'}
# dict_keys(['sachin', 'ganguly150', 'sehwag'])
# dict_values(['100', '150', '80'])
# Enter Players Name: ganguly150
# ganguly150 made 150 runs
# #########################################################################################################################
# # Q> Python program to show the usage of for loop and retrieve the value.
#
# colors = {'r':'red', 'g':'green', 'b':'blue'}
#
# for k in colors:
#     print (k)   ### use to print the keys
#
# for k in colors:
#     print (colors[k])  ### use to print the values
#
# for k,v in colors.items():   ### use to print all the items
#     print ('Key = {}, Value = {}'.format(k,v))
#
# OUTPUT::::
# r
# g
# b
# red
# green
# blue
# Key = r, Value = red
# Key = g, Value = green
# Key = b, Value = blue
######################################################################################################################
# Sorting in dictionary

# colors = {10:'red', 50:'green', 30:'blue'}
#
# c1 = sorted(colors.items(), key = lambda t:t[0])  ###0th element, i.e. sorting by key
# print (c1)
#
# c2 = sorted(colors.items(), key = lambda t:t[1])   ###1st element, i.e. sorting by value
# print (c2)
#
# OUTPUT::::
# [(10, 'red'), (30, 'blue'), (50, 'green')]
# [(30, 'blue'), (50, 'green'), (10, 'red')]
#########################################################################################################################

# List to Dictionary
# x=['red','green','blue']
# y=[10,30,15]
#
# z=zip(x,y)              ### zipping the list and converting it to dictionary
# newdict=dict(z)
# print(newdict)
#
# OUTPUT::::
# {'red': 10, 'green': 30, 'blue': 15}
########################################################################################################
# Dictionary to List

# mydict={'red': 10, 'green': 30, 'blue': 15}
#
# mylist=list(mydict.items())
# print (mylist)
#
# OUTPUT::::
# [('red', 10), ('green', 30), ('blue', 15)]
####################################################################################################################

# Converting STRINGS to DIctionary

# str = "sachin=20,ganguly=30,sehwag=50"
# lst = []
# for x in str.split(','):  # splitting the values with ,
#     #print (x)
#     y= x.split('=') # splitting the value with =
#     #print (y)
#     lst.append(y)
# d = dict(lst)
# print (d)
#
# OUTPUT::::
# {'sachin': '20', 'ganguly': '30', 'sehwag': '50'}
#######################################################################################################################




