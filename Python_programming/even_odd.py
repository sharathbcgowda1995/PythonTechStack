class EvenOdd():
    @staticmethod
    def find_even_odd(number):
        for num in range(0,number+1):
            if num%2==0:
                print(f"{num} is even number")
            else:
                print(f"{num} is odd number")

EvenOdd.find_even_odd(10)