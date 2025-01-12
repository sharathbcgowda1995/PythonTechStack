#Lambda - A function which has no name is called as Lambda function and the syntac is al below.
#Lambda functions by default returns the values as output.
print("----Lambda functions------")
x=lambda a :a+10
print(x(10))

y=lambda a,b,c : a+b+c
print(y(2,3,4))

#Exception Handling- in python, all the exceptions are treated as errors.
print("-----Exception handling condition-1 No exceptions---------")
#In this case only else and finally blocks will be get executed.
var=10
try :
    var/2
except ZeroDivisionError :
    print("ZeroDivisionError Handled")
except SyntaxError :
    print("Syntex error is handled")
except TypeError :
    print("Type error is handled")
else:
    print("No exceptions/Errors has been occured.....")
finally:
    print("Whether the exceptions occurs or not but i don't care hen i execute always.....")


print("-----Exception handling condition-2 with exceptions---------")
#In this case excepy and finally block will be get executed.
var=10
try :
    var/0
except ZeroDivisionError :
    print("ZeroDivisionError Handled")
except SyntaxError :
    print("Syntex error is handled")
except TypeError :
    print("Type error is handled")
else:
    print("No exceptions/Errors has been occured.....")
finally:
    print("Whether the exceptions occurs or not but i don't care hen i execute always.....")


#Need to check how to raise the custom exception in the python as I'm getting error now
print("-----Custom exception handling-------")
def valueError(param):
    pass

def age(number):
    if(number<0):
        raise valueError("Number should be positive")
"""try :
    age(-1)
except valueError :
    print("Enter the positive number")
except :
    print("Something is wrong...")#we can write the except kw alone as above."""


# using exception objects.

try :

    name = one #its string but not defined

except NameError as ex :

    print(ex)
