#Classes and Objects:

class Computer: #defining class...Class name should start with CAPITAL letter
    def config(self): #defing function(method) in class and self is used in that and it is a must when defining method in class
        print('i5, 16GB, 1TB')
com1=Computer() #mapping objects to class
com2=Computer() #mapping objects to class

com1.config() #calling method with object
com2.config() #calling method with object

Computer.config(com1) #calling method with class
Computer.config(com2) #calling method with class
################################################################################################################################

#__init__ method:
#it gets automatically called for every object in the class

class Computer: #defining class...Class name should start with CAPITAL letter

    def __init__(self, cpu, ram): #self is an object itself and we need cpu and ram
        self.cpu=cpu
        self.ram=ram

    def config(self): #defing function(method) in class and self is used in that and it is a must when defining method in class
        print('Config is: ',self.cpu, self.ram)

com1=Computer('i5,','4GB') #mapping objects to class
com2=Computer('Ryzen,','8GB') #mapping objects to class

com1.config() #calling method with object
com2.config() #calling method with object
