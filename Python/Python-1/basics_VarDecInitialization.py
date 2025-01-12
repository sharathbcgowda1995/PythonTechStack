#To print
print('------First program------')
print('First hello program : ', "Hello")

#to check all the keywords present in python.
print("------to check all the keywords present in python------")
import keyword
print('keywords are : ', keyword.kwlist)

#Reinitialisation and Declaration is possible
print('--------Reinitilization-------')
a=10
a='sharath'
print('latest data type and value will be added : ',a)

#variables and dif data types
print('--------ariables and dif data types---------')
a=10
b=10.55
b=10.55
c="Amma"
d='appa'
e=True
print("printing the values like this : ",a,'---','---',b,'---',c,'---',d,'---',e)#we use , instead of + in java.
print("Data type of the variable can be known by type meth like this : " , type(e))

#Different ways of declaring the variables.
print('----------Different ways of declaring the variables.----------')
x,y,z=1,2,3
print("Dif way of declaration : " , x,y,z)

x=y=z=10 #re initialization is possible in python
print("Assigning same val to multiple var - ",x,y,z)

#swapping
print("-------swapping-----------")
m=10
n=12
m,n=n,m
print("swapped without any third variable : " , m,n)

#concatenation - it's possible with same data type family
print('--------Concatenation----------')
a=10
b=5.5
name = "Sharath"
name2= 'Nagu'
btype = False
btype2 =True
print('Same data type can be concatenated : (int + float =number family ) --' ,a+b)
print('String and string : ',name,name2)
print('int + double+0(false)',a+b+btype)
print("int+double + 1(true)",a+b+btype2)
##print("Dif data type can't be concatenated",(a+name),(btype+name2))

#Deletion of the variable
print('-------#Deletion of the variable -------')
z=10
print("Before deletion : ", z)
del z
##print("after deletion : ", z) #NameError: name 'z' is not defined

#CASTING CONCEPTS EXPLAINED WITH USER INPUT
'''#Get input from the user
print("---------Get input from the user----------")
a=input("Enter input : ")
b=input("Enter input again : ")
print("Sum of the input is : ",a+b)#ans is  11 because input only accepts string type hence they are concatenated.

#Get input from the user to CASTING
print("---------Get input from the user to cast it for int type(meth1)----------")
a=int(input("Enter input : "))
b=int(input("Enter input again : "))
print("Sum of the input is : ",a+b)

print("---------Get input from the user to cast it for int type(meth2)----------")
a=input("Enter input : ")
b=input("Enter input again : ")
print("Sum of the input is : ",int(a)+int(b))'''

##we can comment by using [""" ----- """"] or [''' --- ''']

'''#Get input from the user to int - int and float possible
print("---------Get input from the user ----------")
a=float(input("Enter input : ")) #10
b=int(input("Enter input again : ")) #10
print("Sum of the input is : ",a+b) #ans will be 20.0 in float

#Get input from the user to float - float only and can't be int
print("---------Get input from the user ----------")
a=float(input("Enter input : ")) #10.5
##b=int(input("Enter input again : ")) #10.5 - ValueError: invalid literal for int() with base 10: '10.5'
##print("Sum of the input is : ",a+b)'''

#FORMATTING OUTPUT
print("-------#FORMATTING OUTPUT--------")
name = "Sharath"
age = 27
salary =1.5
print("Formatting with %s %d %f or g-----",'Name:%s Age:%d Salary:%f' %(name,age,salary)) #type error we will get if we pass the wrong param
print("Formatting with {}----",'Name:{} Age:{} Salary:{} '.format(name,age, salary))
print("Formatting with {Indexing}----",'Name:{0} Age:{1} Salary:{2} '.format(name,age, salary))


