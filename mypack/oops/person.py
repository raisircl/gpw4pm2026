class person:
    '''This is empty person class'''
    def __init__(self, name="NA", age=1):
        self.name = name # instance attribute
        self.age = age
    def display(self): # here self a reference variable which is used to access the instance attribute
        print(f"Name: {self.name} and Age: {self.age}")

p1=person("Anil",20) # here constructor intialize the p1
p2=person() # here p1 and p2 these are known as instance or object

# self is ref variable which is representative of current object and it is used 
# inside the class.



p2.name="Alice"
p2.age=25

p1.display()
p2.display()

# Rect , Instance Attribute : length, breadth, Instance Method: display, area, perimeter
