#Encapsulation can be achieved by using  the private variable and private methods.
print("---------Encapsulation [Way of accessing private type-1]--------")
class Encapsulation():
    __a=10
    def __meth(self):
        print("----private method-----")
    def meth2(self):
        print("----public method------")
        self.__meth()#private method
        print("private variable : ",self.__a)#private variable

e=Encapsulation()
e.meth2()#called the public method.

#Encapsulated private variables can be accessible by getters and setters.
print("---------Encapsulation [Way of accessing private variable type-2]--------")
class Encapsulation():
    __x=10
    def setPrivateVariable(self,value):
        self.__x=value
        print("Successfully set the private varibale.......")
    def getPrivateVariable(self):
        return self.__x

e=Encapsulation()
e.setPrivateVariable(100)
print(e.getPrivateVariable())


#Abstract class - when we know the requirment and we don't know the implementation then we usually go for the abstract method with abstract classes.
print("-------Abstract class implementation-1----------")
from abc import ABC , abstractmethod
class Mobile(ABC):
    @abstractmethod
    def display(self):
        None

class SubClass(Mobile):
    def display(self):
        print("Given body in the sub class......")

#a=Mobile()#can't be instantiated as it has extended the ABC class and as it has the abstract method.
s=SubClass()#it has implemented all the pending abstract classes hence we can create a object of it.
s.display()

print("-------Abstract class implementation-2----------")
class Mobile(ABC):
    @abstractmethod
    def display(self,msg):
        None

    @abstractmethod
    def calculator(self,val1,val2):
        pass

class Nokia(Mobile):
    def display(self,msg):
        print(msg,"--Display")

class Oneplus(Nokia):
    def calculator(self,val1,val2):
        print("Sum of two numbers is : ", val1+val2)

one=Oneplus() # I can instantiate this class as it has all the implementation....but I can't instantiate Nokia class as it only implemented the display abstract meth
                #To instantiate any class that should have all the abstract class implementation.
one.display("AMOLED")
one.calculator(100,1000)

#Constructor
print("----------Parent class Constructor inherits to the child class-----------")
class Calculator(ABC):
    def __init__(self,val1,val2):
        self.val1,self.val2=val1,val2#without declaring first also we can use the class variables using self kw.

    @abstractmethod
    def sum(self):
        None

class Casio(Calculator):
    """ def __init__(self):
        print("Hi ....")"""
    def sum(self):
        print("Sum of two numbers is : ", self.val1+self.val2)
#if we use the child class specific constructor then the constructor call won't call the parent class constructor and
#then the self.val1 and self.val2 will be uninitialised(As we have to call the parent class contructor for initialisation)
#hence we have to call the parent class constructor


'''c=Casio()'''
c=Casio(1,2)#By using the child class name we have to call the parent class constructor just by passing the arguments.
c.sum()