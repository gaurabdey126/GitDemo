#GENERATORS::::Python provides a generator to create your own iterator function.
# A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values.
# In a generator function, a yield statement is used rather than a return statement.


# def topten():
#     yield 5
#
# values=topten()
# print(values) #We need to add the __next__ iterator to get the vale
#
# Output::
# <generator object topten at 0x000001DE3DD09510>


#######################################################################################################################
# def topten():
#     yield 5
#
# values=topten()
# print(values.__next__())
#
# Output:::
# 5
###################################################################################################################

# def topten():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
# values=topten()
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
#
# #Output:::
# 1
# 2
# 3
###################################################################################################################
#Q. Print the perfect square of first ten numbers
#with For loop(generic)
# n=1
# for i in range(1,11):
#     sq=i*i
#     i+=1
#     print (sq)
###################################################################################################################
#Q. Print the perfect square of first ten numbers
#with Generator

# def topten():
#     n=1
#     while n<=10:
#         sq=n*n
#         yield sq
#         n+=1
#
# values = topten()
#
# for i in values:
#     print (i)
#
# Output:::
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
##############################################################################################################################

# def rangefunction(a=2, b=10, c=2):
for i in range(2,10,2):
        square = i * i
        i += 1
        print(square)