#Modules are python files there we can define the Functions , methods and classes.
print("--------Method-1 To access the functions from the different module------------")
import ModulesOfPython #ModulesOfPython is a python file which contails functions
ModulesOfPython.add(2, 3)
ModulesOfPython.sub(5, 2)

print("--------Method-2 To access the functions from the different module------------")
from ModulesOfPython import add,sub
add(1,2)
sub(5,2)

print("--------Method-3 To access the functions from the different module------------")
from ModulesOfPython import *
add(1,2)
sub(5,2)

print("--------Method-4 To access the functions from the different module with same methods in each module------------")
from Animal import *
eat()#the method will be picked from the very recently imported module if both module has the same functions.

print("------Method-5 in the above case we have to use the below method or any above mentioned method")
from Birds import eat
eat()
from Animal import eat
eat()

print("---------Accessing the clsses present in the different module-------")
#from modulesMultipleClasses import *#dir(modulename won't work with this type of import)
#Type-1
print("-------Type-1------------")
import modulesMultipleClasses
print(dir(modulesMultipleClasses))

modulesMultipleClasses.Birds().fly()

a= modulesMultipleClasses.Animal()
a.eat()

#Type-2
print("-------Type-2------------")
from modulesMultipleClasses import Animal ,Human ,Birds
Animal().eat()

b=Birds()
b.fly()

Human().live()

