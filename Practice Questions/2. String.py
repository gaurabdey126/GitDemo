#len(str) ---- length of a string
# #Indexing, str[start:stop:step size], e.g. str[0:4:1]...it will always start from 0(1st element), upto 4 means upto the 3rd element
# a='HelloWorld'
# b='Why is that so?'
# print(a[0:2]) #Output:He
# print (a[-1]) #Output: d
# print (a[::-1]) #Output: dlroWolleH
#
# #Repeating a String:
# print (a[0:2]*5) #Output:::HeHeHeHeHe
#
# #Concatenation of String:
# print (a + b) #Output::: HelloWorldWhy is that so?

#removing spaces from String:
# qw="  Whats up??  "
# print(qw.lstrip()) #Output:::: Whats up??
# print(qw.rstrip()) #Output::::   Whats up??
# print(qw.strip()) #Output:::: Whats up??

#STRINGS are immutable.

# #Replacing a String with another String:
# str1="This is a beautiful day"
# s1='day'
# s2='car'
# str2=str1.replace(s1,s2)
# # print(str1) #OUTPUT::: This is a beautiful day
# # print(str2) #OUTPUT::: This is a beautiful car
#
# #Changing Case of a String:
# print(str1.upper()) #THIS IS A BEAUTIFUL DAY
# print(str1.lower()) #this is a beautiful day
# print(str1.swapcase()) #tHIS IS A BEAUTIFUL DAY
# print(str1.title()) #This Is A Beautiful Day

#Sorting a String
# str1.sort()

#isupper(), islower(), isnumeric()

###EXERCISE######EXERCISE####EXERCISE###########EXERCISE####EXERCISE#######EXERCISE############EXERCISE#######################################################################################
#Exercise 1: Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
# Case 1
# # str1 = "JhonDipPeta"
# Output
# # Dip

# Case 2
# # str2 = "JaSonAy"
# Output
# # Son

# str1="JhonDipPeta"
# str2="JaSonAy"
#
# str_v1=str1[4:7]
# str_v2=str2[2:5]
#
# print(str_v1, str_v2)

# OUTPUT:::::::::
# Dip Son
########################################################################################
#Exercise 2: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1

# s1='HELLO'
# s2='world'
# s3=s1[0:3]+s2+s1[3:]
# print(s3)
# OUTPUT:::::
# HELworldLO
################################################################################################
#Exercise Question 3: Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string
# s1 = "America"
# s2 = "Japan"
#
# def newstr(s1,s2):
#     first_chr=s1[0] + s2[0]
#     middle_chr= s1[int(len(s1)/2):int(len(s1)/2)+1] + s2[int(len(s2)/2):int(len(s2)/2)+1]
#     last_chr=s1[-1] + s2[-1]
#     mix_string = first_chr + middle_chr + last_chr
#     return mix_string
#
# print(newstr('America', 'Japan'))
# print(newstr('yuan', 'this'))

# Output::::
# AJrpan
#ytains
###########################################################################################################
#Exercise 4: Arrange string characters such that lowercase letters should come first
# Given an input string with the combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first.
# # Given: str1 = PyNaTive

# str1 = 'PyNaTive'
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         lower.append (char) #values getting added in lower[] list
#     else:
#         upper.append (char) #values getting added in upper[] list
# print (lower, upper) # ['y', 'a', 'i', 'v', 'e'] ['P', 'N', 'T']
# sorted_string = ''.join(lower+upper) # .join() is used to joining 2 list
# print(sorted_string)
#
# # Output::::
# #['y', 'a', 'i', 'v', 'e'] ['P', 'N', 'T']
# # yaivePNT
#########################################################################################################################
#Exercise 5: Count all lower case, upper case, digits, and special symbols from a given string
#str1 = "P@#yn26at^&i5ve"
# Total counts of chars, digits,and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

#str1="P@#yn26at^&i5ve"

# def count(str1):
#     charCount=0
#     digitCount=0
#     symbolsCount=0
#     for char in str1:
#         if char.islower() or char.isupper():
#             charCount+=1
#         elif char.isnumeric():
#             digitCount+=1
#         else:
#             symbolsCount+=1
#     print ('Chars =', charCount, 'Digits =', digitCount, 'Symbol =', symbolsCount)
#
# count("HJGJH&^%^$#33333")
# OUTPUT::::
# Chars = 5 Digits = 5 Symbol = 6
####################################################################################################################
# Exercise 6: Given two strings, s1 and s2, create a mixed String using the following rules
#Note: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
# Given:
# s1 = "Abc"
# s2 = "Xyz"
#
# Expected Output: AzbycX

# def s3(s1, s2):
#     s3=s1[0]+s2[-1]+s1[1]+s2[-2]+s1[2:]+s2[-3::-1]
#     print (s3)
#
# s3('InDiA','PaRiS')
#
# OUTPUT::::
# ISniDiARaP
##########################################################################################################################

# def mixstring(s1,s2):
#     s2=s2[::-1]
#     length1=len(s1)
#     length2=len(s2)
#     length=length1 if length1>length2 else length2
#     s3 ="" #eeping this new string blank as we have create it
#
#     for i in range(length):
#         if i<length1:
#             s3=s3 + s1[i]
#         if i<length2:
#             s3=s3+ s2[i]
#     print (s3)
#
# mixstring('InDiA', 'Australia')
# OUTPUT::::
# IaniDliaArtsuA
#########################################################################################################################################
# Exercise 7: String characters balance Test
# We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters’ position doesn’t matter.
# Given:
# s1 = "Yn"
# s2 = "PYnative"
# Expected Output: True
#
# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output: False

# def search(s1,s2):
#     if s1 in s2:
#         print ("True")
#     else:
#         print("False")
#
# search ('Yn','PYnative') #true
# search ('Ynf','PYnative') #False
#########################################################################################################################
#Exercise 8: Find all occurrences of “USA” in a given string ignoring the case
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?"

# str1 = "Welcome to USA. usa awesome, isn't it?, usa usa usa"
# str1=str1.lower()
# text = "USA"
# text=text.lower()
# print(str1)
# print(text)
## count = str1.count(text) #text is substring in str1
# print (count)
#
# OUTPUT::::
# welcome to usa. usa awesome, isn't it?, usa usa usa
# usa
# 5
########################################################################################################################
# Exercise 10: Given an input string, count occurrences of all characters within a string
# Given:str1 = "Apple"
# Expected Outcome:{'A': 1, 'p': 2, 'l': 1, 'e': 1}

# str1="ghghjgjhgjggjgjgjgjhgjhgjhgjhgjhgjhgjhgjhg"
# countdict=dict() #Creating a dictionary
# for char in str1:
#     count=str1.count(char)   #####.count functionality
#     countdict[char]=count #passing char value in dictionary
# print(countdict)
#
# OUTPUT::::
# {'g': 17, 'h': 11, 'j': 14}
######################################################################################################################
#Exercise 12: Find the last position of a substring “Emma” in a given string
# Given: str1 = "Emma is a data scientist who knows Python. Emma works at google."

##### rfind : The rfind() method returns the highest index of the specified substring (the last occurrence of the substring) in the given string.
# If the substring is not found, then it returns -1

# str1= "Emma is a data scientist who knows Python. Emma works at google."
# str2="Emma"
# index = str1.rfind(str2)
# print ('Last position of substring {} is:'.format(str2), index)
#
# Output::::
# Last position of substring Emma is: 43
##############################################################################################################################

# Given a string, return a string where for every char in the original, there are two chars.
# # double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


# def double_char(str):
#     length=len(str) # as range need to be in integer to iterate
#     for i in range(length):
#         str1 = ""
#         str1 = str1 + str[i]
#         print(str1 * 2, end='')
#         i+=1
#
# double_char('Hi-There') # OUTPUT::::: HHii--TThheerree
#########################################################################################################################
# Exercise 14: Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# print ("Original List of String:")
# print (str_list)
#
# new_str_list= list(filter(None, str_list))  ####### use built-in function filter to filter empty value
# print("After Removing the Empty Strings:")
# print(new_str_list)
#
# OUTPUT::::
# Original List of String:
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# After Removing the Empty Strings:
# ['Emma', 'Jon', 'Kelly', 'Eric']
#######################################################################################################################
#Exercise 15: Remove special symbols/Punctuation from a given string
# str1 = "/*Jon is @developer & musician"

# import string
#
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)
#
# # use translate function of a string
# # and maketrans function of str class
# new_str = str1.translate(str.maketrans('', '', string.punctuation))
#
# print("New string is ", new_str)
#
# OUTPUT:::::
# Original string is  /*Jon is @developer & musician
# New string is  Jon is developer  musician
#######################################################################################################
#TRANSLATE Method and MAKE TRAN method
#string.punctuation

#Exercise 15: Remove special symbols/Punctuation from a given string
# str1 = "/*Jon is @developer & musician"

# import string #need to import string function for string.punctuation
# str = "/*Jon is @developer & musician"
#
# str1=''
# str2=''
# str3=string.punctuation
#
# # table=str.maketrans('','',string.punctuation)
# table=str.maketrans(str1, str2, str3) ###this is where maketrans(s1, s2, s3) is taking place, s1-characters to be replaced, s2-replacement characters, s3-characters for deletion
#
# print ("Original Text:", end="")
# print(str)
#
# print ("After Removal of special characters:", end="")
# print(str.translate(table)) ###this is where translate() is taking place

# OUTPUT::::
# Original Text:/*Jon is @developer & musician
# After Removal of special characters:  Jon is  developer & musician
########################################################################################################################
#Exercise 17: Find words with both alphabets and numbers
# str1 = "Emma25 is Data scientist50 and AI Expert"
#
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print ('Original Text: ', str1)
#
# res=[]
# temp = str1.split()
# print (temp)
#
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)
#
# print('Displaying words with both alphabets and numbers: ')
# for i in res:
#     print(i, end='\t')
#
# OUTPUT:::::
# Original Text:  Emma25 is Data scientist50 and AI Expert
# ['Emma25', 'is', 'Data', 'scientist50', 'and', 'AI', 'Expert']
# Displaying words with both alphabets and numbers:
# Emma25	scientist50
###############################################################################################################################
## .replace function
#Exercise 18: Replace each punctuation with # in the following string
#str1 = '/*Jon is @developer & musician!!'
#
# from string import punctuation #for FOR function
# str1 = '/*Jon is @developer & musician!!'
# print ('Original Text::::: ', str1)
#
# replace_char="#"
#
# for char in punctuation:
#     str1=str1.replace(char, replace_char) ###.replace function
#
# print(str1)
#
# OUTPUT::::
# Original Text:::::  /*Jon is @developer & musician!!
# ##Jon is #developer # musician##
##############################################################################################################################



