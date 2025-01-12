#Number type coversion
print("------Number type coversion------")
a=10
b=10.5
print(float(a))#int - float
print(int(b))#float - int(Decimal values will be lost)

#Buillt in functions max , min
print("---------Buillt in functions------------")
list = [1,100,3,900,1000]
maxl ={
    "One" : 1,
    "Two":2
}
print("by passing the list : ", max(list))#list
print("by passing the dict : ",max(maxl))#Dict
print(min(list))
print(max(1,2,3,4,1,4))#normally passed
print(min(3,1,400,23))