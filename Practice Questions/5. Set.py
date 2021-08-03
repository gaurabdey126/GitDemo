# Method	                        Description
# add()	                        Adds an element to the set
# clear()	                        Removes all the elements from the set
# copy()	                        Returns a copy of the set
# difference()	                Returns a set containing the difference between two or more sets
# difference_update()	            Removes the items in this set that are also included in another, specified set
# discard()	                    Remove the specified item
# intersection()	                Returns a set, that is the intersection of two or more sets
# intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                Returns whether two sets have a intersection or not
# issubset()	                    Returns whether another set contains this set or not
# issuperset()	                Returns whether this set contains another set or not
# pop()	                        Removes an element from the set
# remove()	                    Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	                        Return a set containing the union of sets
# update()	                    Update the set with another set, or any other iterable

#####################################################################################################################
# Exercise 1: Add a list of elements to a given set
# Given:
# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red"]

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red"]
# sampleSet.update(sampleList)   ### with update, a new set can also be added
# print(sampleSet)
#
# OUTPUT::::
# {'Red', 'Green', 'Black', 'Yellow', 'Blue', 'Orange'}
###############################################################################################################
# Exercise 2: Return a new set of identical items from a given two set
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.intersection(set2)   ##### finding the common element between different sets
# print(set3)
#
# OUTPUT::::
# {40, 50, 30}
###########################################################################################################
# Exercise 3: Returns a new set with all items from both sets by removing duplicates
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.union(set2)             ##### combining sets and returning the unique values...SET will be unordered
# print (set3)
#
# OUTPUT:::::
# {70, 40, 10, 50, 20, 60, 30}
####################################################################################################
# Exercise 4: Given two Python sets, update the first set with items that exist only in the first set and not in the second set.
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
#
# set1.difference_update(set2)          #####Remove the items that exist in both sets
# print(set1)
#
# OUTPUT:::::
# {10, 30}
######################################################################################################
# Exercise 5: Remove items 10, 20, 30 from the following set at once
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})  ##Remove the items that exist in both sets
# print(set1)
#
# OUTPUT:::::
# {50, 40}
###################################################################################################
# Exercise 6: Return a set of all elements in either A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.symmetric_difference(set2)      ###Return a set that contains all items from both sets, except items that are present in both sets
# print(set3)
#
# OUTPUT::::
# {20, 70, 10, 60}
########################################################################################################
# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements.
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
#
# if set1.isdisjoint(set2):           ###Returns whether two sets have a intersection or not
#     print('Common element is NOT there')
# else:
#     print ('Common element is there')
#     print (set1.intersection(set2))
#
# OUTPUT::::
# Common element is there
# {10}
##########################################################################################################
# Exercise 8: Update set1 by adding items from set2, except common items
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# set1.symmetric_difference_update(set2)
# print(set1)

# OUTPUT::::
# {20, 70, 10, 60}
##################################################################################################################
# Exercise 9: Remove items from set1 that are not common to both set1 and set2
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# set1.intersection_update(set2)
# print(set1)
#
# OUTPUT::::
# {40, 50, 30}
###################################################################################################################

