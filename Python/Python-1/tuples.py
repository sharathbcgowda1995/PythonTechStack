#Tuples are similar to the lists but we can't do any changes on that.
#ref for how we have created the lists.
list=list([1,2])
print(list)

#Tuples creation
print("-------Tuples creation as below------")
t1=()#empty tuple
print(t1)

#Splicing and immutability
print("---------Splicing and immutability------")
t2= tuple([1,2,3,4])
print("Splicing : " ,t2[1:3])#splicing is also same as lists
print("type of the tuple : " , type(t2))#type
#print(t2.append(5))#we can't modify the tuple once that's created.we will get error AttributeError: 'tuple' object has no attribute 'append'
print()
print(t2)

print("-----Mixed data type data storage in tuples----")
t=tuple(["Sharath",1])
print("Mixed data type : " ,t)

t3=[1,3,4]
print(t3)

t4=(1,2,3,4)
print(t4)

t5=tuple("Sharath")
print(t5)#here also it printed as the list of char

#Tuple Functions
print("--------Tuples functions--------")
t1=(1,2,3,4,5)
print(max(t1))
print(min(t1))
print(sum(t1))
print(len(t1))

#Iterating tuple using for loop
print("---------Iterating tuple using for loop meth-1-----")
for i in range(len(t1)):
    print(i)

print("---------Iterating tuple using for loop meth-2-----")
for i in t1 :
    print(i)

#Retrieval of tuple
print("-----#Retrieval of tuple-------")
tuple = [1,2,3,4]
print(tuple[0])

"""#Other functionality
print("------Other Functionailty-----")
Tup=tuple[1,2,3]
print(Tup)"""

