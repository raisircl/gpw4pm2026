# unknown loop
# enter a number and count its digits
num=int(input("Enter a number:")) #512
x=0 
while num>0: # 512>0=>T, 51>0=>T, 5>0=T, 0>0=F 
    x=x+1 # 1, 2, 3
    num=num//10 # 512//10=51, 51//10=5, 5//10=0
    
print(f"Number of digits: {x}")

# enter a number sum of digits x=x+num%10
# enter a number and print reverse of that number
# x=x*10+num%10
# enter a number and check whether it is palindrome or not
# enter a number and check whether it is armstrong or not
# enter a number and print it in word
# 512 => Five One Two

# 5/2=> 2.5 , 5//2=> 2
