def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_number = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_number)
    return fib_series[:n]

n = 10
print(fibonacci(n))
