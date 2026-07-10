# nested if else - when we use an if else into another if else
#Biggest between 3 nos
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))
if a>b:
    if a>c:
        print(f"Print A is biggest and number is {a}")
    else:
        print(f"C is Biggest and number is {c}")
else:
    if b>c:
        print(f"B is biggest and number is {b}")
    else:
        print(f"C is Biggest and number is {c}")