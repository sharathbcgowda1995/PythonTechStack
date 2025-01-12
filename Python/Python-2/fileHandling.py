#File-Handling
#To read data from the file in read mode
print("--------read data from the file in read mode--------")
file=open("/Users/sharath.bc/Desktop/aut.txt","r")
print(file.read(4))#It prints upto the number of indexes we pass
print(file.readline())#It prints the first line in the text
print(file.readlines())#It prints all the data in the text file
file.close()#close the pointer once reading is done

#To write data to the file in write mode
print("--------To write data to the file in write mode--------")
file = open("/Users/sharath.bc/Desktop/write.txt","w")#if data is present that will be overriden (cleared before writing)
file.write("Amma I love you \n")
file.write("Not a good partner for you N \n")
file.close()

#To append the data at the last in the text file.
print("---------Append the data at the last in the text file----------")
file=open("/Users/sharath.bc/Desktop/write.txt","a")
file.write("Be a self made weapon")
file.close()

#Read the data using the for loop.
print("-------Read the data using the for loop-------")
file=open("/Users/sharath.bc/Desktop/aut.txt","r")
for read in file:
    print(read,end=" ")