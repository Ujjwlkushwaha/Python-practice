## Encapsulation - Process of bundling attributes and methods inside a single unit which is class.
##                  - Encapsulation also provide data security feature mean you can set visibility feature.
#                    - who can access your data and who can not.

# public members : when you create a class by defualt every attribute and methods are set to be public.

# Private member- these members are only accessible inside the class.
#                       - Private member start with "__";
#                       - If I wanted to accesss private member outside the class we have to make a public getter method
class Parent:
    def __init__(self,name, caste, salary):
        self.name = name     # Public instance attribute
        self.__caste = caste  # Private instance attribute
        self.__salary = salary # Private instance attribute

    def get_salary(self):
        return self.__salary

obj = Parent("Ujjwal" , "hindi" , 3333)
# print(obj.__salary) # Show error -  'Parent' object has no attribute '__salary 

# get private values using public method

salary = obj.get_salary()  # this way you can access private members
print(salary) # 3333