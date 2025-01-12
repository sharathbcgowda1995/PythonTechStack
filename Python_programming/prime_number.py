class PrimeNumber():
    def check_number_is_prime_or_not(self,number):
        counter = 0
        if (number>=1):
            for i in range(1,number+1):
                if(number%i==0):
                    counter = counter+1
        print("Number given divided %d times"%(counter))
        return counter

obj = PrimeNumber()
number = 100
if(obj.check_number_is_prime_or_not(number)<=2):
    print("Prime number")
else :
    print("Not prime number")


