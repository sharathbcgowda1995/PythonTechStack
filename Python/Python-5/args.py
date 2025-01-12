#*args and **kwargs
#we use this to pass the data and recieve the data as param
#*args- * > represents the multiple values, args- is just variable name it acan be any customised name.
print("-------*args use tyepe-1-------")
class Calculation():
    def sum(self,*sharath):
        var=0
        for i in sharath:
            var+=i
        print("Sum is :",var)

    def multiplication(self,a,b,c):
        print("Multilied value is : ", a*b*c)

c=Calculation()
c.sum(1,2,3,4)#I can't pass here the lists
#s = [1,2,3,4]
#c.multiplication(*s)#need to check as we are not able to pass like this.

#**kwargs- we use it for key-value pair of data passing and recieving.
print("-------**kwargs use tyepe-2-------")
class Maths():
    def add(self,**kwargs):
        for i,j in kwargs.items():
            print(i,j)

    def mul(self,one,two,three):
        print("Values are : ",one,two,three)

m=Maths()
m.add(name="Sharath",Age=27)#the key can't be string here

dict={"one":1,"two":2,"three":3}
m.mul(**dict)

