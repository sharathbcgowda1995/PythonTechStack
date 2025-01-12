class PalindromeNumber():
    @staticmethod
    def is_palindrome(number):

        original_number = number
        reversed_number = 0

        if number < 0:
            return False
        while(number>0):
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            number //= 10

        return  original_number == reversed_number

number = 121
if (PalindromeNumber.is_palindrome(number)):
    print("Palindrome number")
else :
    print("Not Palindrome number")

'''In each iteration of the loop, the last digit of the number (digit) is obtained using the modulo operator (%), and it is added to the reversed_number after shifting the existing digits to the left.
The last digit is removed from the original number by performing integer division (//).'''