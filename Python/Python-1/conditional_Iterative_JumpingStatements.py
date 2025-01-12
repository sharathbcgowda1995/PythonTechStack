#Conditional statements - True or False
#for loop :
print('----for lop------')
for i in range(10):#it print from 0 to till 9
    print(i)

#if condition
print('-----if condition -1----')
a=9
if a==10:
    print("hey it's equal")
else:
    print('False')

print('-----if condition -2 ----')
if True :
    print(("Okay its True"))
else:
    print("False")

if False :
    print(("Okay its True"))
else:
    print("False")


print('-----if condition -3 ----')
if 0 :
    print(("Okay its True"))
else:
    print("False")

if 1 :
    print(("Okay its True"))
else:
    print("False")

print('-----Single line if else-----')
print('True printed') if True else print("False printed")

print('10 greater') if (10>11) else print("10 is lesser")

{print("Welcome"),print("Python")} if True else {print("Quit"),print("Python")}

#Even or odd using for loop
print("-------Even or Odd Program---------")
for i in range(10):
    if(i%2==0):
        print('even number is : ',i)
    else :
        print('odd number is : ' ,i)

#Find the biggest number using the elif conditional statement.
print("-----Find the biggest number using the elif conditional statement----------")
a=10
b=20
c=30
if (a>b and a>c) :
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else :
    print("c is greater")


#Function of the range function:
print("------Function of the range function:--------")
print(list(range(10)))
print(list(range(1,5)))
print(list(range(1,6,2)))#1-strt 6-1=5 end point 2-inc
print(list(range(5,1,-1)))
print(list(range(-5,10)))#in minus the higher val with minus is smaller it will come towrds zero

#For loop
print("------For loop-------")
for i in range(1,10,2):
    print(i)

#while loop
print("----While loop------")
i=10
while(i>0):
    print(i)
    i -= 1

#Jumping statements - break
print("------Jumping statements - break---------")
for i in range(1,10):
    if(i==5):
        print("Condition met hence the whole next iteration has been stopped")
        break
    else:
        print(i)

#Jumping statements - continue
print("------Jumping statements - continue---------")
for i in range(1,10):
    if(i==5):
        print("Condition met hence this specific iteration has been skipped")
        continue
    else:
        print(i)



