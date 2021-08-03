#a=10 #GLOBAL VARIABLE
#def f1():
#    a=20 #LOCAL VARIABLE
#    print(a)
#def f2():
#    print(a)
#
#f1() #20 #CALLING FUNCTION 1
#f2() #10 #CALLING FUNCTION 2
################################################################################################

#a=10 #GLOBAL VARIABLE
#def f1():
#    global a #MAKING A LOCAL VARIABLE TO GLOBAL VARIABLE SO THAT f2 CAN ACCESS THE SAME
#    a=20 #LOCAL VARIABLE
#    print(a)
#def f2():
#    print(a)
#
#f1() #20 #CALLING FUNCTION 1
#f2() #20 #CALLING FUNCTION 2
################################################################################################
#SYNTAX FOR GLOBAL VARIABLE IS AS BELOW:
#global a
#a=some value
# CANNOT BE AS 'global a=some value'
################################################################################################

#LAMBDA FUNCTION:
#SYNTAX: lambda input_argument:expression

#s=lambda n:n*n
#for i in range(1,11):
#    print('The square of {} is: {}'.format(i,s(i)))
#Print square of a number
##########################################################################

#FILTER, MAP, REDUCE

from functools import reduce

#num = [2,4,3,5,8]
#even=list(filter(lambda n:n%2==0, num)) #filter even number from the list
#print(even)

#double=list(map(lambda n:n*2, even)) #dobling the filtered Even numbers from the given list
#print(double)

#sum=reduce(lambda a,b:a+b, double) #adding the values present in double list
#print(sum)

#[2, 4, 8]
#[4, 8, 16]
#28
################################################################################################################################################

#MAP function:

#l1=[2,3,4,5]
#l2=[5,10,15]

#l3=list(map(lambda x,y:x*y, l1, l2))
#print(l3)
###############################################################################################################################################

#eval() funnction:::will return the same type of input that we have entered

#x=eval(input('Enter your reqd input: '))
#print(type(x))
###################################################################################################################################

#x=eval('10+20+30**2//5-5')
#print(x,type(x))

#Output:::: 205 <class 'int'>
#######################################################################################################################################

#x=eval('13+19+30**2//13-5')
#print(x,type(x))

#96 <class 'int'>
#######################################################################################################################################

#FACTORIAL using RECURSION
#n=int(input('Enter a number = '))
#def fact(n):
#    if (n==0):
#        return 1
#    return n*fact(n-1)
#print(fact(n))
#####################################################################################################################################

