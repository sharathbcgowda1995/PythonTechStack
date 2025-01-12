class PrimeNumber():
    def check_number_is_prime_or_not(self, number):
        counter = 0
        if number >= 1:
            for i in range(1, number + 1):
                if number % i == 0:
                    counter += 1
        return counter <= 2

    def prime_number(self, number_array):
        return [num for num in number_array if self.check_number_is_prime_or_not(num)]

obj = PrimeNumber()
array = [1, 2, 100, 30, 50]
result = obj.prime_number(array)
print("Prime numbers in the array:", result)