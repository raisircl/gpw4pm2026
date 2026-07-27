class Rect:
    '''This is empty Rect class'''
    def __init__(self, length=1, breadth=1):
        self.length = length # instance attribute
        self.breadth = breadth
    def display(self): # here self a reference variable which is used to access the instance attribute
        print(f"Length: {self.length} and Breadth: {self.breadth}")
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def __str__(self):
        return f"Length: {self.length} and Breadth: {self.breadth}"
    def __add__(self, r2):
        temp = Rect()
        temp.length = self.length + r2.length
        temp.breadth = self.breadth + r2.breadth
        return temp
    def __ge__(self, r2):
        if self.area() >= r2.area():
            return True
        else:
            return False
r1=Rect(10,20) # here constructor intialize the r1
r2=Rect(30,40) # here r1 and r2 these are known
r3=r1+r2 # here r3 is a new object which is created by adding r1 and r2
print(r3)

if r1 >= r2:
    print("r1 is greater than or equal to r2")
else:
    print("r1 is less than r2")
    