# Printing Output using print() in Python ✅ 


print( " Hello World!! ") # Hello World!! 

print( "Hello" , 43 , 4.5 , True ) # Hello 43 4.5 True




## Output Formatting 👍

# Example 1: Using Format() ✔️
amount = 150.75
print("Amount: ${:.2f}".format(amount))


## Example 2: Using sep and end parameter ✔️ 

# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")  # Python@GeeksforGeeks

# Seprating with Comma
print('G', 'F', 'G', sep='') #GFG

# for formatting a date
print('09', '12', '2016', sep='-')  # 09-12-2016

# another example
print('pratik', 'geeksforgeeks', sep='@') # pratik@geeksforgeeks

## Example 3: Using f-string 
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")



# Taking input in Python ✅
# Python's input() function is used to take user input. By default, it returns the user input in form of a string. 

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")


# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)



# changing the type of input 
n = int(input("How many roses?: "))
print(n)

n = int(input("How many roses?: "))
print(n)


# input the array
arr = [int(x) for x in input().split()]
print( arr )