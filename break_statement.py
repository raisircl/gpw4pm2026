# break transfer the control outside the loop
# cause of break become emergency exit from the loop
# if break execute loop terminate immediately
# example enter a number and check whether it is prime or not
num=int(input("Enter a number:"))
i=2
while i<num: # if i and num are equal then the loop stops
    if num%i==0:
        break
    i=i+1

if num==i:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")    