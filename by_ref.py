def fun(x): # x is formal argument 
    print(f"Before change in X Id of x {id(x)} and value of x is {x}")
    #x=20
    x.append(20)
    print(f"After change in X Id of x {id(x)} and value of x is {x}")
    


y=[10]
print(f"Before call Id of y {id(y)} and value of y is {y}")
fun(y) # y is actual argument
print(f"After call Id of y {id(y)} and value of y is {y}")

# here a and y id is same it mean x and y has same block of ram
# its prove by default in python arguments passes as ref
# if any change in x then python reserve new block for x and it does not affect y
# id of x now is different from y 
# so in immutable object if any change in formal argument does not affect actual argument
# in mutable object if any change in formal it affect actual argument
