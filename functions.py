#  function is set of instructions under a name
#  it is part of program known as sub program
'''
def funname(param, param2, ...):
    .....
    ....
    return value

    '''

def sayhello(name='Guest'):
    print(f"Hello {name}")

def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def result(h,e,m,sci,sst):
    total = h + e + m + sci + sst
    percentage = (total / 500) * 100
    return total, percentage
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

# to take the output from function we need to call it
sayhello("Anami") # call 

sayhello("Anami")

table(num=70)

hindi=90
eng=70
math=78
sci=90
sst=68
t,p=result(h=hindi,e=eng,m=math,sci=sci,sst=sst)
print(f"Total: {t}, Percentage: {p}")

num=5
x=fact(num)
print(f"Factorial of {num} is {x}")

# the data which we pass to function is known as argument
# the variable which accept the argument is known as parameter
# if we are calling a function again 
# it mean it provides reuseability of code
# function always ready to perform a job need to call it 
# and with this if function accept arguments then these arguments
# should be passed to function when we call it