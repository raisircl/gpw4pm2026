# when a function call itself then that function is known 
# as recursive function and process is known as recursion
def factorial(n): 
    if n==1:
        return 1 
    else:
        return n*factorial(n-1) 
    
f=factorial(5) 
print(f"Factorial is: {f}")
