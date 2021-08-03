#Exception Handling:An exception can be defined as an unusual condition in a program resulting in the interruption in the flow of the program.
# Whenever an exception occurs, the program stops the execution, and thus the further code is not executed.
# Therefore, an exception is the run-time errors that are unable to handle to Python script.
#try, except, finally

# a=5
# b=2
#
# try: #we have to put the complex statement under try block for which there are chances of error
#     print('Open') #this statement will always get executed
#
#     print(a/b) #if b=0, then there will be an error
#
#     k=int(input('Enter a number')) #this is added to see the different types of error
#     print (k)
#
# except ValueError as e: #this is for 'k' one...when value entered is invalid, this except bock will get executed....
#     print('Invalid Data entered')
#
# except ZeroDivisionError as e: # this is for (a/b), when b=0, this except block will be executed.....BASED on the ERROR, the except block will take place...if no such error mentioned, it will go to the below except block..
#     print('Zero division is not possible')
#
# except Exception: #it will come to this block if ANY ERROR exists (if b=0) or it will go to 'finally' block. if no such error mentioned, it will come to this except block
#     print('Something Wrong')
#
# finally:
#     print('Closed')
#
# OUTPUT::::
# Open
# Enter a number p
# Invalid Data entered
# Closed
#################################################################################################################################################

a = float(input('Enter Numerator: '))
b = float(input('Enter Denominator: '))

try:  # we have to put the complex statement under try block for which there are chances of error
    print('Open')  # this statement will always get executed
    print(int(a / b))  # if b=0, then there will be an error


    k = int(input('Enter a number: '))  # this is added to see the different types of error
    print(k)

except ZeroDivisionError as e:  # this is for (a/b), when b=0, this except block will be executed.....BASED on the ERROR, the except block will take place...if no such error mentioned, it will go to the below except block..
    print('Zero division is not possible')

except ValueError as e:  # this is for 'k' one...when value entered is invalid, this except bock will get executed....
    print('Invalid Data entered')

except Exception:  # it will come to this block if ANY ERROR exists (if b=0) or it will go to 'finally' block. if no such error mentioned, it will come to this except block
    print('Something Wrong')

finally:
    print('Closed')

