#Inheritance
print("------single level Inheritance-------")
class A:
    def meth(self):
        print("from class A")

class B(A):#This is ho we inherite the class.
    def meth2(self):
        print("from class B")

bobj=B()#To access both child specific and parent class meth's
bobj.meth()
bobj.meth2()

print("------multi level Inheritance-------")
class A:
    def meth(self):
        print("from class A")

class B(A):#This is ho we inherite the class.
    def meth2(self):
        print("from class B")

class C(B):
    def meth3(self):
        print("from class C")

cobj=C()#To access both child specific and parent class meth's
cobj.meth()
cobj.meth2()
cobj.meth3()

print("------Hirerachical Inheritance-------")
class A:
    def meth(self):
        print("from class A")

class B(A):#This is ho we inherite the class.
    def meth2(self):
        print("from class B")

class C(A):
    def meth3(self):
        print("from class C")

bobj=B()#To access child specific and parent class meth's
bobj.meth()
bobj.meth2()

cobj=C()#To access child specific and parent class meth's
cobj.meth()
cobj.meth3()

print("------multiple Inheritance-------")
class A:
    def meth(self):
        print("from class A")

class B:#This is ho we inherite the class.
    def meth2(self):
        print("from class B")

class C(A,B):
    def meth3(self):
        print("from class C")

cobj=C()
cobj.meth()
cobj.meth2()
cobj.meth3()

#Multiple inheritance with same name methods from parent
print("--------If it in case if both the classes has the same methods then how it will call the methods????-------")
class A:
    def meth(self):
        print("from class A")

class B:#This is ho we inherite the class.
    def meth(self):
        print("from class B")

class C(B,A):#it plays major roll in multiple inheritance.
    def meth3(self):
        print("from class C")

cobj=C()
cobj.meth()
cobj.meth()#same named method will be picked from the firstly inherited class.
cobj.meth3()

#Hybrid Inheritance -- Here also the one which get inherited first from that class the common method will be get executed.
print("------Hybrid Inheritance-------")
class A:
    def meth(self):
        print("from class A")

class B(A):#This is ho we inherite the class.
    def meth2(self):
        print("from class B meth-2")

    def meth3(self):
        print("from class B meth-3")

class C(A):
    def meth3(self):
        print("from class C meth-3")

    def meth4(self):
        print("from class C meth-4")

class D(C,B):
    def meth5(self):
        print("from class D")

dobj=D()
dobj.meth()
dobj.meth2()
dobj.meth3()
dobj.meth4()
dobj.meth5()