class Fibonacci():
    @staticmethod
    def get_fibonacci_series(n):
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(n):
            sum=n1+n2
            print(sum)
            n1=n2
            n2=sum
Fibonacci.get_fibonacci_series(10)

# 0  1  1   2  3 5 8.....
# n1 n2 sum
#    n1 n2  sum