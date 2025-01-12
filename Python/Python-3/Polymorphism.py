#Polymorphism is possible when there is Inheritance - runtime(overriding) , compliletime(overloading).
print("--------Method and Variable overriding possible in Python----------")
class Bank:
    ROI=10
    def rateOfIntrest(self):
        return 10

class HDFC(Bank):
    ROI=12.5
    def rateOfIntrest(self):
        return 12.5

bobj=HDFC()
print(bobj.ROI)
print(bobj.rateOfIntrest())

print("-------------Method overriding type-1---------")
class Human:
    def job(self,person):
        if person=="Cricketer":
            print("Playing cricket")
        if person=="Soldier":
            print("Protecting the nation")
        if person=="Actor":
            print("Entertain the people")

h=Human()
h.job("Cricketer")
h.job("Soldier")
h.job("Actor")

print("-------------Method overriding type-2---------")
#This approach is not possible in python because when we write a same method then the latest one will be considered and
#Firstly written methods will no longer be in consideration.
class Facebook:
    """def login(self,UN,PWD):
        print("Logged in using the : ",UN,PWD)
    def login(self,UN,Mobilenumber,OTP):
        print("Logged in using the :",UN,Mobilenumber,OTP)"""

    def login(self,UN,EmaiId,OTP):
        print("Logged in using the :",UN,EmaiId,OTP)

f=Facebook()

"""f.login("Sharath",12345)
f.login("Sharath",9591354391,3344)"""

f.login("Sharath","sharathbcgowda@gmail.com",1122)