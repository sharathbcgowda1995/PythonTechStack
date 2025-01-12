class FizzBuzz():
    @staticmethod
    def find_fizz_buzz(number_range):
        for number in range(1,number_range+1):
            if (number%3==0 and number%5==0):
                print(f"Fizz Buzz :{number}")
            elif (number%3==0):
                print("Fizz : %d" % (number))
            elif (number%5==0):
                print("Buzz : %d "%(number))
            else:
                print(number)
FizzBuzz.find_fizz_buzz(100)