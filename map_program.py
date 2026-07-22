from functools import reduce
def isprime(n):
    i=2
    while i<n:
        if n%i==0:
            break
        i=i+1

    if i==n:
        return True
    else:
        return False
def add(x,y):
    return x+y

x=[44,22,31,56,2,6,7,11,9,10]

squares=list(map(lambda n: n*n, x))
prime_numbers=list(filter(isprime, x))
total=reduce(add, x)
print(total)
print(squares)

print(prime_numbers)
