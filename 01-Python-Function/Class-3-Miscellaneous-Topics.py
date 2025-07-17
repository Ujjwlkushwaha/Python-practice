# 1️⃣ DocStrings - Document string used to describe the functionality of function

def isEven( num ) :
    """ This function checks number is even or not """ # docString
    print(isEven.__doc__) # printing docString
    if( num % 2 == 0 ):
        return True
    else:
        return False

print(f"6 is Even :: {isEven(6)}")


# 2️⃣ . Nested function - function inside another function

def outer():
    print( " This is outer function ")
    def inner():
        print( " This is inner function ")

    inner() # calling inner function 

outer() # calling outer function
# inner() # we can not call inner function from outside of outer function


# 3️⃣ Recursion - when function calling itself

def factorial( n ):
    """ Function calculate factorial """

    # base case - where function stop running
    if n==0:
        return 1
    
    # Recursive relation
    return n*factorial(n-1)

fact = factorial( 5 )
print( f"Factorial is : {fact}")


# 4️⃣ Returning function from function

def outer_fun():
    print( "Outer function is running ")

    def inner_fun():
        print( "Inner function is running ")

    return inner_fun # return a function

msg = outer_fun() # Outer function is running 

# This msg variable become a function
msg() # Inner function is running

