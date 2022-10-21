def fibonacci_2(n):
    if n<0:
        return "Invalid Input"
    if n<=1:
        return n
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
n = int(input("Enter a number: "))
nth_fib = fibonacci_2(n)
print("The {} th fibonacci number is {}.".format(n, nth_fib))
