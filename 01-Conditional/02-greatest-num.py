num1 = int(input("Enter the numbers: "))
num2 = int(input("Enter the numbers: "))
num3 = int(input("Enter the numbers: "))

#finding greatest number
if( num1 > num2 ):
    if( num1 > num3 ):
        print( "Greatest number is ", num1)
    else:
        print( "Greatest number is ", num3)
elif( num2 > num3 ):
    print( "Greatest number is ", num2)
else:
    print( "Greatest number is ", num3)