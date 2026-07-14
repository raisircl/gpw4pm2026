# enter a number and print sum of all nos up to this
num=int(input("Enter a number: ")) 
s=0
for i in range(1,num+1):
    print(f"{i}+", end="")
    s=s+i

print(f"\b={s}")

# enter a number and print its factorial
# 5 Ans. 5x4x3x2x1=120
