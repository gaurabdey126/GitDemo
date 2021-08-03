'''Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
# Code Starts from here -------------------------
year = int(input("Enter a Year = "))
if year%4==0:
    #print ('The entered year %d is a Leap year' %year)
    if year%400==0:
        print('The entered year %d is a Leap Year and also a Century Year' %year)
    else:
        print ('The entered year %d is a Leap year but NOT a Century Year' %year)
else:
    print ('The entered year %d is NOT a Leap year' %year)'''
#************************************************************************************************************************************

#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR".

#Code Starts here:
#age = int(input('Enter your age = '))
#sex = str(input('Sex? (M or F) = '))
#mar = str(input('Married? (Y or N) = '))
#if sex=='F':
 #   print('You will work only in urban areas')
#elif sex=='M' and 20<age<40:
 #   print('You Employee may work anywhere')
#elif sex=='M' and 40<age<60:
 #   print('You Employee will work in urban areas only')
#else:
 #   print("ERROR")
#********************************************************************************************************************************

#num = int(input('Enter a 4 digit number = '))
#if 1000<=num<=9999:
#    print('Your entered %d is fine as 4 digit number'%num)
#else:
#    print('Please enter a proper 4 digit number to proceed')
#*********************************************************************************************************************************

#A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
#INPUT : 1234        OUTPUT : 4321
#INPUT : 5982        OUTPUT : 2895
# Code Starts here

#num = int(input('Enter a 4 digit number = '))
#if 1000<=num<=9999:
#    print('Your entered %d is fine as 4 digit number'%num)
#    num2=str(num)
#    print('Your entered %d in reverse order is:' %num + num2[::-1])
#else:
#    print('Please enter a proper 4 digit number to proceed')
#***********************************************************************************************************

#Q6. Accept the kilometers covered and calculate the bill according to the following criteria:
#First 10 Km              Rs11/km
#Next 90Km               Rs 10/km
#After that               Rs9/km
#Code starts here

#km=float(input('Please enter the KM covered = '))
#if km<=10:
#    b=float(km*11)
#    print('Bill =%.2f '%b)
#elif 10<km<=100:
#    b = 110+((km - 10) * 10)
#    print('Bill =%.2f ' %b)
#else:
#    b = 1010+((km-100)*9)
#   print('Bill =%.2f ' %b)
##############################################################################################




