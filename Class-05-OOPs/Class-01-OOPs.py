#  👍 OOPs - ( Object Oriented Programming ) 

# class-> class is the blueprint or template of real world object
# Object -> Object is that real world object which properties and behavior is defined inside class.


# this is class---
class Student:
    score = 100  # class attribute - It is common for all objects

# Default constructor
    def __init__(self):
        print("This is default constructor")

# this is constructor for initializing attributes 
    def __init__(self , name , grade):
        self.name = name  # Instance attribute - it is different for all objects
        self.grade = grade

# instance methods or features
    def show_details(self): 
        print(f"This is {self.name} from class {self.grade}")


# creating object
student1 = Student( "Ujjwal", 5)
student1.show_details() # This is Ujjwal from class 5




# 👍 Methods of class 

# 1. Normal or Instance method  - are used to define features of object in the class.
# 2. Class method -> are used for modifing class attribute becouse other method can't do this.
# 3. Static mathod -> If a method used for only utitlity perposes and dont use any class attribute then we make it into static method.


class Strudents:

    school_name = "Kamla devi mahavidyalay" # class attribute

    def __init__(self , name , grade, rollNo) :
        self.name = name
        self.grade = grade
        self.rollNo = rollNo

    # Normal instance methon - use self keyword and used to access and modiy instance attribute
    def get_details(self):
        print(f"Std_name : {self.name} from class {self.grade}\nrollNo : {self.rollNo}")     

    @staticmethod  # this is decorator used to define static method
    def greeting():
        print(f"Hello Sir / Mam")   

    
    @classmethod  # this decorator used for definging class method 
    def change_schoolName(cls , name):
        cls.school_name = name # updating class attribute 


# creating student
std1 = Strudents("Ujjwal" , 12 , 1234)

std1.get_details()
print( f"School name is :: {std1.school_name}")    # School name is :: Kamla devi mahavidyalay
print( f"School name is :: {Strudents.school_name}") # School name is :: Kamla devi mahavidyalay

std1.greeting()  # Hello Sir / Mam

std1.change_schoolName("Kanpur university")
print( f"School name is :: {std1.school_name}")   # School name is :: Kanpur university
print( f"School name is :: {Strudents.school_name}") # School name is :: Kanpur university


## del keyword -> used for deleting object property or entire object

del std1.grade 
# print( std1.grade ) # 'Strudents' object has no attribute 'grade'

del std1 # To delete entire object 






