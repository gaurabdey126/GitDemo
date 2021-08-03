#No link any of the classes
# class A:
#     def feat1(self):
#         print ('feat1 is working')
#
#     def feat2(self):
#         print ('feat2 is working')
#
# class B:
#     def feat3(self):
#         print('feat3 is working')
#
#     def feat4(self):
#         print('feat4 is working')
#
# class C:
#     def feat5(self):
#         print ('feat5 is working')
#
# a1=A()
# b1=B()
# c1=C()
#
# a1.     #can access only feat1 and feat2
# b1.     #can access only feat3 and feat4
# c1.     #can access only feat5
###############################################################################################################################
##SINGLE LEVEL INHERITANCE BETWEEN A and B
##MULTI LEVEL INHERITANCE BETWEEN A and C
# class A:
#     def feat1(self):
#         print ('feat1 is working')
#
#     def feat2(self):
#         print ('feat2 is working')
#
# class B(A):
#     def feat3(self):
#         print('feat3 is working')
#
#     def feat4(self):
#         print('feat4 is working')
#
# class C(B):
#     def feat5(self):
#         print ('feat5 is working')
#
# a1=A()
# b1=B()
# c1=C()
#
# a1.     #can access only feat1 and feat2
# b1.     #can access only feat1 2 3 4
# c1.     #can access only feat1 2 3 4 5

#####################################################################################################################################
## C can access features from both A and B (MULTIPLE INHERITANCE)
# class A:
#     def feat1(self):
#         print ('feat1 is working')
#
#     def feat2(self):
#         print ('feat2 is working')
#
# class B():
#     def feat3(self):
#         print('feat3 is working')
#
#     def feat4(self):
#         print('feat4 is working')
#
# class C(A,B):
#     def feat5(self):
#         print ('feat5 is working')
#
# a1=A()
# b1=B()
# c1=C()
#
# a1.     #can access only feat1 and feat2
# b1.     #can access only feat3 4
# c1.     #can access only feat1 2 3 4 5
#################################################################################################################################

#CONSTRUCTOR IN INHERITANCE:
#1

# class A:
#     def __init__(self):
#         print('init A')
#
#     def feat1(self):
#         print ('feat1 is working')
#
#     def feat2(self):
#         print ('feat2 is working')
#
# class B(A):
#     def feat3(self):
#         print('feat3 is working')
#
#     def feat4(self):
#         print('feat4 is working')
#
# a1 = B() #since B doesnt have constructor, it will the constructor from A

# Output:::::
# init A
###########################################################################
#2

# class A:
#     def __init__(self):
#         print('init A')
#
#     def feat1(self):
#         print ('feat1 is working')
#
#     def feat2(self):
#         print ('feat2 is working')
#
# class B(A):
#     def __init__(self):
#         print('init B')
#
#     def feat3(self):
#         print('feat3 is working')
#
#     def feat4(self):
#         print('feat4 is working')
#
# # a1 = B() #since B HAVE a own constructor, it will take that rather than getting from classA
#
# # Output::::
# # init B
# ###################################################################################
# #3
#
# class A:
#     def __init__(self):
#         print('init A')
#
#     def feat1(self):
#         print ('feat1 is working')
#
#     def feat2(self):
#         print ('feat2 is working')
#
# class B(A):
#     def __init__(self):
#         print('init B')
#         super().__init__() #this will call the Consructor from Super Class A
#
#     def feat3(self):
#         print('feat3 is working')
#
#     def feat4(self):
#         print('feat4 is working')
#
# a1 = B() #since B HAVE a own constructor, it will take that rather than getting from classA
#
# Output::::
# init B
# init A
#######################################################################################################################
#4

class A:
    def __init__(self):
        print('init A')

    def feat1(self):
        print ('feat1 is working')

    def feat2(self):
        print ('feat2 is working')

class B: #B is not sub class of A
    def __init__(self):
        print('init B')

    def feat3(self):
        print('feat3 is working')

    def feat4(self):
        print('feat4 is working')

class C(B,A):

    def __init__(self):
        super().__init__()
        print('init C')

    def feat5(self):
        print ('feat5 is working')

a1 = C() #Object creation in C and calling the constructor

# OUTPUT:::::::::
# init A #It takes the order from Left to Right (A, B)
# init C

# init B #It takes the order from Left to Right (B, A)
# init C