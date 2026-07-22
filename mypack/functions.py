def sum(num1,num2):
    "Return Sum of 2 numbers"
    return num1+num2

def table(num):
    "Print Table of a number"
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')

def factorial(num):
    "Return Factorial of a number"
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
