num=int(input("Enter a 4 digit number: "))
s=0
s=s+num%10
num=num//10
s=s+num%10
num=num//10
s=s+num%10
num=num//10
s=s+num%10
num=num//10
print(f"The sum of the digits is {s}")
