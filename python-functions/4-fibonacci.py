def fibonacci_sequence(n):
    if n <= 0:
        return []
    fibonacci_sequence = (0, 1)
    n = n_(n-1) + n_(n-2) 
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))

