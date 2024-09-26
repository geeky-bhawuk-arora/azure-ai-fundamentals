# -----------------------------------------------------
# Define a class and create its object
# -----------------------------------------------------

class Student:
    # Create the atttributes of the class
    def __init__(self, fname, lname, gender, enrno):
        self.fname   = fname
        self.lname   = lname
        self.gender  = gender
        self.enrno   = enrno
    
    def hello(self):
        print("Hello ", self.fname)


s1 = Student("John", "Smith", "M", "E-001")

s1.hello()

print(s1.enrno)

class BIA:
    def __init__(self,emptype, location, name, age):
        self.emytype = emptype
        self.location = location
        self.name = name
        self.age = age
    
    def jalal(self):
        print("Your name is ", self.name)
        
        print("Your age is ", self. age)
        
        print("Your location is ", self.location)
        
        print("Employed or Non-Employed", self.emytype)

student1 = BIA("No", "Vashi","Ritik", "23")

student1.Introduction()


    






























