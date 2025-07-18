# 3. Inheritence -> Inheritence is process in which a class can inherite the properties and feature of other class.

# Parent Class or Base class - Jiske features and properties inherite ki jaygii
# Child class or subClass - Jo features and properties ko inherite krega


#Parent class or Super class
class Student:
    
    def __init__(self, name, grade, percentage ):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def show_details(self):
        print( f"He is {self.name} from grade {self.grade}. He got {self.percentage} marks. ")


# Child class or Subclass 
class GraduateStudent( Student ): # inherite the Student class
    
    def __init__(self, name, grade, percentage , stream):
        super().__init__(name, grade, percentage) # calls parent class initializer
        self.stream = stream # add new attribute in child class


# Creating object of child class
GradStudent = GraduateStudent("Kavita" , 12 ,98, "PCM") 

print( GradStudent.name)
print( GradStudent.grade)
print( GradStudent.percentage)
print( GradStudent.stream)

    

        