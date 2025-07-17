def add(nums):
    """ Calculate addition """
    return sum([int(items) for items in nums])

def sub(num1 , num2):
    """ Calculate Subtraction """
    return int(num1) - int(num2)

def multiply(nums):
    """  multiplt """
    val = [int(items) for items in nums]
    ans = 1
    for i in val:
        ans *= i
    return ans

def division(num1 , num2):
    """ Calculate division """
    return int(num1) / int(num2)

def avg(nums):
    """ Calculate average """
    total = add(nums)
    return total/2


while(True):
    print("\n\n-<>- Choose your operation -<>- \n")

    print( "1. Addition")
    print( "2. Multiplication")
    print( "3. Division")
    print( "4. Subtraction")
    print( "5. Average")
    print("6. Exit from calculation ")

    op = int( input("Enter operation num : "))

    match op:
        case 1:
            val = input("Enter numbers :: ").split(" ")
            print(f"Your sum is {add(val)}") 
        case 2:
            val = input("Enter numbers :: ").split(" ")
            print(f"Your Multiplicaition is {multiply(val)}")
        case 3:
            val1 , val2 = input("Enter 2 numbers :: ").split()
            print(f"Your division is {division(val1,val2)}")
        case 4:
            val1 , val2 = input("Enter 2 numbers :: ").split()
            print(f"Your subtraction is {sub(val1,val2)}") 
        case 5:
            vall = input("Enter numbers :: ").split(" ")
            print(f"Your average is {avg(vall)}")
        case 6:
            print("\t \n Tqs for using me \n")
            exit()
        case _:
            print("Invalid operation")



