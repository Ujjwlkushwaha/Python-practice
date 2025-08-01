#  For Loops - iterate over sequences such as a list, tuple, string or range.

n = 6

for i in range ( 0 , n ):
    print(f"Loop is printing line {i}")
print()


# Loop with else statement
for i in range( 0,n ):
    print("loop is running")
else: 
    print("Loops end ho gyaa") # Execute when loop is finished


# Iterating a string
name = "Anaconda"
for letter in name:
    print( letter , end=" - ")
print()


# Iterating a list
marks = [45,65,76,87,32] 
for mark in marks:
    print(mark ,end=" ")
print()


# Iterating a tuple
tup = (3,4,5,6,72,4,2)
for t in tup:
    print(t , end=" ")
print()

# Range in loops
"""
    range() function have three parameteres--

        start     end     inc/dec

    by default python for loop increase value by 1 at time

    But if i want to increament by other value so you can...........

"""

r = 10

for i in range( 0 , n ):
    print( i , end=" ") # 0 1 2 3 4 5
print()


for i in range( 0 , n , 2):
    print(i , end=" ") # 0 2 4
print()


for i in range( n , 0 , -1 ): # loop run reverse
    print( i , end=" ") # 6 5 4 3 2 1
print()



# While Loop in Python- > Condition based loop

n = 10 # initialization
 
while n>0 : 
    print("while loop in running")

    n = n-1; # Updation is must for stop the loop



