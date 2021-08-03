#ITERATORS:::: Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration. ...
# This method raises a StopIteration to signal the end of the iteration.

#Iterators allow lazy evaluation, only generating the next element of an iterable object when requested.
# This is useful for very large data sets. Iterators and generators can only be iterated over once. Generator Functions are better than Iterators.

# nums=[2,3,4,5]
# it=iter(nums)
#
# print(it.__next__()) #2
# print(it.__next__()) #3
#
# print(next(it)) #4
################################################################################################################
# #Q. Need to print the first 10 numbers.
#
# class Topten:
#     def __init__(self):
#         self.num=1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <=10:
#             val=self.num
#             self.num +=1
#             return val
#
#         else:
#             raise StopIteration
#
# values = Topten()
#
# for i in values:
#     print (i)
#
# OUTPUT::::
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
###################################################################################################################################

#Q. Need to print the first 10 numbers.

class Topten:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val=self.num
            self.num +=1
            return val

        else:
            raise StopIteration #it STOPS the iteration till the range

values = Topten()

print(next(values)) # it will print 1
print(next(values)) #it will print 2

for i in values: #it will take up the value after 2
    print(i)

Output:::
1
2
3
4
5
6
7
8
9
10
