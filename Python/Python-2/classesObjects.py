#Basic class and method creation.
class Basic :#class
    def meth(self,name):#method declaration, self menas it belongs to this class.
        print(name)
    def meth2(self):
        pass#Even though if we don't have any body we can mention pass instead of whole body.

obj=Basic()
obj.meth("Amma miss you")

#Another way of declaring the class is as below.
class Amma():#we can use brackets after the class name that is also valid.
    def m1(self):
        pass

#Satic concepts and instance or class variable use inside the class.
print("-------Satic concepts and instance or class variable use inside the class-----")
class Calculation:
    a,b=10,20
    def sum(self):
        c=self.a+self.b #we can use the instance or class variables by using the self ketword.
        print("Sum of two numbers is : ", c)
    @staticmethod
    def statmeth():
        print("we can have only static method not variables....")

obj=Calculation()
obj.sum()#instance methods should be called with the obj reference.
Calculation.statmeth()#static methods can be called by using the class name as in java.

#Global-Class/Instance-Local variables
print("----Global-Class/Instance-Local variables cond : 1 - all variables names are different-----")
g=100#Global variable outside the class
class variables():
    x,y=10,20
    def sum(self,a,b):
        print(a+b)#directly accessible as its local
        print(self.x+self.y)#accessible with self keyword as its instance/class varibale
        print(g)#directly accessible as its global
obj=variables()
obj.sum(2,3)

print("----Global-Class/Instance-Local variables cond : 1 - all type of variables names are same-----")
x,y=100,200#Global variable outside the class
class variables():
    x,y=10,20#instance variables
    def sum(self,x,y):#local varibale
        print(x+y)#no need to spevify anything.
        print(self.x+self.y)#accessible with self keyword as its instance/class varibale
        print(globals()['x']+globals()['y'])#globals()['varname']
obj=variables()
obj.sum(2,3)

#Named object ,name less object and multiple object creation.
print("------Named object ,name less object and multiple object creation----------")
class creation():
    def amma(self,a):
        print(a)

obj1=creation()
obj1.amma(10)#instance meths can be accessbible by named object(ref)

creation().amma(20)# Instance or class meths can be accessible by Nameless Object like this

obj2=creation()
obj2.amma(30)#multiple objects can be created and all are independent as they stored in dif mem loc

#Check memory location - id ,To check whether the ref var is pointing to the same object or not we have -- is ,is not
print("-------Memory location - id(ref var) ,is , is not ----------")
class memory():
    def meth(self):
        pass
m1=memory()
m2=memory()
m3=m1 #both m1 and m3 are pointing to the same object

print("Checking the location and whether they pointing to same var or not : ",id(m1),id(m3),m1 is m3)
print("Objects are not equal : ",id(m1),id(m2),m1 is not m2)