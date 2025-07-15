# Nested Dictionary 

student = {
    "name" :"Ujjwal",
    "age" : 34,
    "address" : "Mandhna kanpur",
    "subjects" : [ "Hindi" , "English" , "Maths"],
    "marks" : {
        "Hindi" : 54,
        "English" : 66,
        "Maths" : 78
    }
}

# printing value of nested dictionary
print( student["marks"]["Maths"]) # 78

# iterate over keys  👍

for key in student:
    print( key ) # print all keys

#or

for key in student.keys():
    print( key ) # print all keys


# iterate over values 👍 

for value in student.values():
    print( value ) # print all values

# iteratre both   👍 

for key, value in student.items():
    print( key ," " , value) # print both key value



## Dictionary comprehension 👍👍 

        # Sorter way of creating dictionary based on some logic
        # syntax- 
            ## dict = { key-exp : value-exp for item in iterable if conditon }

# creating dictionary of square values

squares = { x : x*x for x in range(1 , 6 )} 
print( squares ) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}