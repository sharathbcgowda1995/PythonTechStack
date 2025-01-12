#list in python are very simillar to arrays in java
print("----Lists in python-----")
list1 = list()#initialsises the empty list.
list2 = [1,2,3,4] #Synt- 1
list3 = list([4,5,6,7])#synt - 2
list4= list(["Amma","Nagu","Putti"])
list5=list("Sharath")# Synt - 3 It gives the list with characters VIMP
list6=(1,2,3,4)
print(list1,list2,list3,list4,list5,list6)


print("--------How to access the lists in Python[Indexing]------")
list = [1,2,3,4,5,6]
print(len(list))#to get length
print(list[0])#Index usually starts from 0

print("---------List accepts all the types of data------")
list=[1,2,3,"Sharath","Bharath"]
print(list) #[1, 2, 3, 'Sharath', 'Bharath']

print('----common operations on lists >>min,max,in,not in,len,sum-----')
list=[11,22,1,2,99]
print(len(list))#it supports for all data in a list
print(max(list))#"Sharath","Bharath"--- it doesn't support for mixed data
print(min(list))
print(sum(list))
print(1 in list,100 not in list)

print("-----List slicing[same as string slicing using[]]------")
list=[1,2,3,"Sharath","Nagu"]
print(list[0:2])
print(list[:3])
print(list[2:])
print(list[0:-2])

print('----- + and * opearators [same as in strings]------')
list1=[1,2,3,4,"Sharath"]
list2=[10,20,30,40,"Nagu"]
print(list1+list2)#concatenates- [1, 2, 3, 4, 'Sharath', 10, 20, 30, 40, 'Nagu']
print(list1*3)#Repetition - [1, 2, 3, 4, 'Sharath', 1, 2, 3, 4, 'Sharath', 1, 2, 3, 4, 'Sharath']

print("-----Traversing the list using for loop meth-1-----")
list1=[1,2,3,4,"Sharath"]
for i in list1:
    print(i,end=" ")#end=" " to print on the same line with a sapce

print("\n-----Traversing the list using for loop meth-2-----")#\n for new line ,\t for giving tab
list1=[1,2,3,4,"Sharath"]
for i in range(len(list1)):
    print(list1[i])

print("----commonly used list methods with return type-----")
list=[1,2,3,1,4,5,6]

list.append(100)#it will add the given element in at the last
print(list)

print(list.count(1))#it will check how many times the given element is occured in the list.

list2=[10,20]
list.append(list2)#we can store the list inside the list in an index by passing it in the append as param
print(list)

list.extend(list2)#it will add the element at the last
print(list)

print(list.index(4))#it will give the index of the passed element.
print(list.index([10,20]))#it will give the index of the passed element even though if we have stored the list in an index.

list.insert(1,1000)#inserts an element at the given index and existing element will be shifted to next indexes
print(list)

list=[1,2,3,4,1,5]
list.remove(1)#removes the first occured element from the list -- [2, 3, 1, 2, 3]
print(list)

list=[1,2,3,4,1,5]
print(list.pop(5))#returns the popped element.
print(list)

list.reverse()#reverse the complete list.
print(list)

list.sort()
print(list)#sorts in an ascending order -- [1, 2, 2, 3, 3]

#how to store the values in list using the for loop
print("--------how to store the values in list using the for loop logic-1--------")
list= [ i for i in range(10)]
print(list)

print("--------how to store the values in list using the for loop logic-2--------")
list=[ i+1 for i in range(10)]
print(list)

print("--------how to store the values in list using the for loop logic-3--------")
list=[i for i in range(10) if (i%2==0)]
print(list)