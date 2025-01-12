#String related
print("------String related---------")
name = "Sharath"
name = 'Nagu' #re declaration of the same varibale with the different data type is possible in py.
name2= "Nagu"
name3=str("Amma")

print(name, name2 ,name3)
print(id(name),id(name2),id(name3))#if the same content is availble then the new object will not get created.
                                  # instead it will point to the existing obj. location : 4318714032 4318714032 4318946800


#Character - In python there is no python hence the character will be treated as string with the single char as below.
print("---Character >> In python there is no python hence the character will be treated as string----")
char = 'a'
print(char,type(char))

#Immutable - if we try to modify then it will create a new object
print("---Immutable - if we try to modify then it will create a new object-----")
name = "Sharath"
print(name,id(name))
name = name + 'Nagu'
print(name,id(name))

var = 1
print("Before Integers :",var,id(var))
var = var + 2
print("After Integers ",var,id(var))

#Operations on String - + concat , * reprtition
print("---Operation on String---")
firstName = "Sharath"
lastname = " B C"
print("concatenation by + is : ",firstName+lastname)
print("Repition by * is : ", firstName * 5)

#Slicing(SubString) of string by slicing operator - []
print("----Slicing or extracting SubString-----")
name = "Sharath C Gowda"
var=name[0:7]
print(var,type(var))#returns the str type only
print(name[:3])#till 3-1=2
print(name[1:])#start from 1
print(name[0:-2])#last 2 char excluded

#ord and chr functions
print("------ord and chr functions-------")
print(chr(75))#numberASCII to chr
print(ord("A"))#chr to numASCII

#len,max,min fun of str
print("-----len,max,min Func-------")
name = "Sharath"
print(max(name))
print(min(name))
print(len(name))

list = [1,3,4,5,6]
print(len(list))

#in & not in operator > Membership operator.
print("---------in & not in operator > Membership operator-------")
name = "Sharath is a SDET"
print("Sharath" in name)#case sensitive
print("Bharath" not in name)
print("Nagu" in name)

#String comparison - > , < ,>= ,<= ,== ,!=
print("------String Comparison------")
name1 = "Sharath"
name2 = "Bharath"
print(name1==name1)
print(name1>name2)
print(name2<name1)
print(name1>=name2)
print(name2!=name1)
print(name2<=name1)

#Iterate the String and extract each character.
print("--------Iterate the String and extract each character---------")
name = "Sharath"
for i in range(len(name)):
    print(name[i])#returns the str type

#Reverse a string program.
print("------Reeverse a string program-----")
name="Nagashree"
rev_name=str()
#print(rev_name)#empty string
#starting point should be -1 as it starts from full length 9 and index is of 8(0-8) ,
# -1 is end point because it will stop at 1 if we give 0 as per the syntax.
for i in range(len(name)-1,-1,-1):
    rev_name +=name[i]
print("Reversed name is : " , rev_name)

#We can iterate as below as well
print("---We can iterate as below as well-----")
for i in name:
    print(i)#it prints the characters

#Inbuilt string class methods.
print("-------Inbuilt string class methods set#1--------")
name = "Sharath 95 be independent"
print(name,name.isalnum(),name.isalpha(),name.isdigit(),name.isidentifier(),name.islower(),name.isupper())
name="SHARATH"
print(name.isupper())
print(" ".isspace())
print("123".isdigit())
print("Sharath 95 be independent".isalnum())#????
print("hgdhgd".islower())

print("----commonly used String meths set#2-----")
name = "Sharath C Gowda SDET"
print(name.endswith("ET"))
print(name.startswith("Sha"))
print(name.count("a"))
print(name.find('a'))#lower first index which appears first
print(name.rfind('a'))#highest last index position

print("-----String meths set#3------")
name ="shaRath c goWda"
print(name.capitalize())#first char will be capitalised
print(name.title())#Capitalises first letter of every word
print(name.lower())
print(name.upper())
print(name.swapcase())
print(name.replace("c","B C"))