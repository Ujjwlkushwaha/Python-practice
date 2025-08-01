marks = int( input("Enter your marks :: "))

#check your marks
if( marks >=  95 ):
    print( "Excellent buddy🥰😍")

elif( marks < 95 and marks >= 75 ):
    print( "Average😏")

elif( marks < 75 and marks >= 50 ):
    print("Good😌")

elif ( marks < 50 and marks >= 33 ):
    print( "Poor😥")

else: 
    print("Fail😣")