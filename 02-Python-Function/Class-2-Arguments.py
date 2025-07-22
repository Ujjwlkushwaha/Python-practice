# Type of function Arguments ✅ 

## 1️⃣. Positional or required arguments - you must pass 

def student_details( name , age , grade ):
    """ This function print student details """
    print(f"Hay, I am {name} and I am {age} yrs old.\n I study in class {grade}th" )

student_details("Aditya" , 12 , 6 )  # these are required argument that you have to pass   


## 2️⃣. Default Argument - set default value as argument in fun() parameters

def parants_details( name="X" , children = "Y"):
    """ This function print parants details """
    print(f"Hay I am {name} and I am gradian of {children}" )

#Passing required argument 
parants_details("Aditya" , "Alok") # Hay I am Aditya and I am gradian of Alok

#Not passing any argument
parants_details() # Hay I am X and I am gradian of Y


## 3️⃣. Named arguments - give the name to fun() arguments

def student_details2( name , age , grade ):
    """ This function print student details """
    print(f"Hay, I am {name} and I am {age} yrs old. I study in class {grade}th" )

# It gives wrong output ❌
student_details2(12 , 6, "Aditya") #Hay, I am 12 and I am 6 yrs old. I study in class Adityath

## It gives right output ✅
student_details2(age=12 , grade=6, name="Aditya")  #these are Named arguments



## 4️⃣ Arbitrary arguments and Arbitrary keyword arguments

### *args -> manage tuple to store multiple arguments
### **kargs -> manage dictionary to store multiple keyword or named arguments

def fruits_name( *fruits ): # arbitrary argument
    """ This function is printing fruits name """
    for fruit in fruits:
        print( fruit )  

fruits_name("Apple" , "Banana")# passing 2 arguments
fruits_name("Apple" , "Banana", "Pineapple")# passing 3 arguments
fruits_name("Apple" , "Banana", "Guava", "plum" , "Grapers")# passing 5 arguments


def std_details( **details ): #arbitrary keyword arguments
    """ This funtion uses arbitrary keyword argument to store details """
    for key , value in details.items():
        print( f"{key} = {value}")

std_details( name="Ujjwal" , age=21, address="Kanpur")# Passing keyword arguments
std_details( name="Ujjwal" , age=21)# Passing keyword arguments