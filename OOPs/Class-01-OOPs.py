# OOPs - ( Object Oriented Programming ) 

# class-> class is the blueprint or template of real world object
# Object -> Object is that real world object which properties and behavior is defined inside class.
#  
class Student:
    score = 100  # class attribute - It is common for all objects

# Default constructor
    def __init__(self):
        print("This is default constructor")

# this is constructor for initializing attributes 
    def __init__(self , name , grade):
        self.name = name  # Instance attribute - it is different for all objects
        self.grade = grade

# class methods or features
    def show_details(self):
        print(f"This is {self.name} from class {self.grade}")

# creating object
student1 = Student( "Ujjwal", 5)
student1.show_details() # This is Ujjwal from class 5


# self keyword -> this keyword pointing to current object 

## Features of OOPs-

# 1. Encapsulation
# 2. Inheritence
# 3. Abstraction
# 4. Polimorphism
