# Variables act as placeholders for data. They allow us to store and reuse values in our program.


# Variable 'x' stores the integer value 10
x = 5

# Variable 'name' stores the string "Samantha"
name = "Samantha"  

print(x)
print(name)


# Assigning Values to Variables
age = 21
_colour = "lilac"
total_score = 90.5


# Multiple Assignments
a = b = c = 10
print( a , b, c ) # 10 10 10

x, y, z = 1, 2.5, "Python"
print(x, y, z)  # 1 2.5 Python


# Type Casting a Variable

# Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.

# Basic Casting Functions
    # int() - Converts compatible values to an integer.
    # float() - Transforms values into floating-point numbers.
    # str() - Converts any data type into a string.
    # Examples of Casting:

# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(f)  
print(s2)