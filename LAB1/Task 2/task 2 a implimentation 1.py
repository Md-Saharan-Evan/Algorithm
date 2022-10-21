
def fibonacci_1(n):
    if n < 0:
        print("Invalid input!")
    elif n <= 1:
        return n
    else:
        return fibonacci_1(n-1)+fibonacci_1(n-2)
n = int(input("Enter a number: "))
nth_fib = fibonacci_1(n)
print("The {} th fibonacci number is {}.".format(n, nth_fib))