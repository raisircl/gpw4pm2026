def even_odd(x):
    if x%2==0:
        return f"{x} is even"
    else:
        return f"{x} is odd"

a=[4,21,12,5]
b=map(lambda x: x*x,a)
c=map(lambda x: f"{x} is even" if x%2==0 else f"{x} is odd",a)

d=map(even_odd,a)


print(list(b))

print(list(c))

print(list(d))
