import collections
# here student is a named tupple 
# attributes of student are name, rollno, marks
student=collections.namedtuple("student",["name","rollno","marks"])
s1=student("John", 101, 85)
s2=student("Alice", 102, 90)
print(s1.rollno)  # Output: John


    