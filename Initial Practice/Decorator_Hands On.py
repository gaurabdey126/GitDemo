#Decorator is used to modify an existing function: Adding function to an existing function...

def div(a,b): #existing function
    print(a/b)
                #if user enters a<b, then the value will be in fraction...I want tht Numerator should always take the greater value
def div2(func): #creating a new function to modify the existing one
    def inner(a,b): #nested function...
        if a<b:
            a,b=b,a #swapping should happen in order to take the bigger number as Numerator
            return func(a,b)
    return inner
div=div2(div)

div(2,8)
