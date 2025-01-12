#Dictionaries which stores the data in K-V pair like map in Java.
#Creation of map:
dict={
    "Name":"Sharath",
    "Job":"SDET",
    1:"One"
}#Key and Value can be anything as you can see above.
print(dict)
'''
Below mentioned operations are much required for List,Dictionary and Tuples
1.Add
2.Retrieve
3.Update
4.Remove
5.Iteration
'''
#Retrieving the specific key- value
dict={
    "Name":"Sharath",
    "Job":"SDET",
    1:"One"
}
print("------Retrieving the specific key- value---------")
var = dict["Name"]
print(type(var),var)

#Retrieval ,By using the built in meth
print("---------Retrieval ,By using the built in meth------")
print(dict.get("Name"))

#Adding the data to the Dict
print("-------Adding the specific key- value to the dict----------")
dict["Dream"] = "Successfull"
print(dict)

#Modify the Dict
print("---------Modify the Dict---------")
dict["Dream"] = "To be Successfull"
print(dict)

#Deletion there are total 3 methods - del , pop(K) ,popitem()
print("--------Delete the key--------")
del dict["Dream"]
print(dict)

#pop the key
dict={
    "Name":"Sharath",
    "Job":"SDET",
    1:"One"
}
print("-----popitem - up or removes any random key-value and pop(key) remove specific from the dictionary------")
print(dict.pop("Job"))
#print(dict["Job"])
print(dict.popitem())#random key-val will be removed

print("----Clear the dictionary----")
print(dict.clear())#returns none

#Iterate the dict using for loop
print("----------Iterate the dict using for loop-----------")
Details={
    "Name":"Sharath",
    "Job":"SDET",
    1:"One"
}
for i in Details:
    print(i,":",Details[i])

print("-----How to find the length of the dict------")
print(len(Details))

#How to compare 2 dictionaries.
Details1={
    "Name":"Sharath",
    "Job":"SDET"
}
Details2={
    "Job":"SDET",
    "Name":"Sharath"
}
Details1={
    "Name":"Sharath",
    "Job":"SDET"
}
Details3={
    "Job":"SDE",
    "Name":"Sharath"
}
print("Two objects are equls : " , Details1==Details2)#it checks whether two (Dictionaries)object keys holding the same value or not.
print("Two dictionaries are not equal : " , Details2 != Details3)

#Get k-v from dictionary
print("-------Retreive k-v----")
Details1={
    "Name":"Sharath",
    "Job":"SDET"
}
print(Details1.keys())#dict_keys(['Name', 'Job'])
print(Details1.values())#dict_values(['Sharath', 'SDET'])