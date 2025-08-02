# Example 1: Simple generator using yield
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  # Output: 1 2 3 4 5

# Example 2: Generator expression
squares = (x*x for x in range(6))
for sq in squares:
    print(sq)  # Output: 0 1 4 9 16 25

# Example 3: Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for f in fibonacci(10):
    print(f)  # Output: 0 1

# Example 4: Prime number generator (complicated)
def prime_generator(limit):
    primes = []
    num = 2
    while num < limit:
        for p in primes:
            if num % p == 0:
                break
        else:
            yield num
            primes.append(num)
        num += 1

print("Prime numbers up to 30:")
for p in prime_generator(30):
    print(p, end=' ')  # Output: 2 3 5 7 11 13 17 19 23 29