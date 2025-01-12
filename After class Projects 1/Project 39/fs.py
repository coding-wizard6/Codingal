def fibonacci(n):
    fib_series = []
    a = 0
    b = 1
    for _ in range(n):
        fib_series.append(b)
        a=b
        b=b+a


    return fib_series

# Example usage:
n = 10  # Number of Fibonacci numbers you want
print(fibonacci(n))