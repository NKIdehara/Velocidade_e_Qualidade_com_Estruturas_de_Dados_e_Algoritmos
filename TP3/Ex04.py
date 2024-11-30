def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = 10
print(f"Fibonacci de {n}: {fibonacci(n)}")
print(f"Fatorial de {n}: {fatorial(n)}")