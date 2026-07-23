x=[44,21,44,22,11,31]
y=[i//2 for i in x]
z=[i for i in x if i%2==0]

print(f"Half Value List: {y}")
print(f"Even Value List: {z}")

a=[f"{i} is even" if i%2==0 else f"{i} is odd" for i in x]
print(f"Even or Odd List: {a}")

# age of persons list

age_list=[12, 15, 18, 20, 25, 30, 35, 40]
name_list=["Vivek","Ramesh","Anil","Ravi","Kamal","Suresh","Rohit","Amit"]

# lic elibibility list
# criteria age between 18 to 45
lic_eligible_list=[age for age in age_list if age>=18 if age<=45]
print(f"LIC Eligible List: {lic_eligible_list}")

lst1=[33,22,55]
lst2=[11,22]
lst3=[(i,j) for i in lst1 for j in lst2]

print(lst3)
