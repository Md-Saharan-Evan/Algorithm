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


import time
import math
import matplotlib.pyplot as plt
import numpy as np
#change the value of n for your own experimentation
n = 40
x = [i for i in range(n)]
y = [0 for i in range(n)]
z = [0 for i in range(n)]
for i in range(n-1):
    start = time.time()
    fibonacci_1(x[i+1])
    y[i+1]= time.time()-start
    start = time.time()
    fibonacci_2(x[i+1])
    z[i+1]= time.time()-start
x_interval = math.ceil(n/10)
plt.plot(x, y, 'r')
plt.plot(x, z, 'b')
plt.xticks(np.arange(min(x), max(x)+1, x_interval))
plt.xlabel('n-th position')
plt.ylabel('time')
plt.title('Comparing Time Complexity!')
plt.show()