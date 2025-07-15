# Dictionary in Python -> Datastructure to store items( key : value)👍 

first_dict = { }  # this is empty dictionary
print( type(first_dict)) # <class 'dict'>

# dictionary 
student = { 
    "name"  : "Ujjwal",
    "age" : 12,
    "address" : "Kanpur"
}

print( student)  # {'name': 'Ujjwal', 'age': 12, 'address': 'Kanpur'}

# Creation of dictionary 👍👍 

## method - 1
student_1 = { "name" : "Ujjwal" , "school" : "Rama Visvavidhyalay"}

## method - 2 - using dict() constructor
student_2 = dict(name = "Krishna" , school = "Maharana")
print( student_2 ) # {'name': 'Krishna', 'school': 'Maharana'}

## method - 3 - using list of tuples of items
student_3 = dict([("name" , "Abhay") , ("school" , "Heritage") , ("age" , 43)])
print( student_3 ) # {'name': 'Abhay', 'school': 'Heritage', 'age': 43}


# Accessing items of dictionary

## method - 1 - using []
print( student_3["name"]) # Abhay

## method - 2 - using get()
print( student_3.get("name")) # Abhay


# Methods of disctionary

## Accessing 👍 

print( student_3.keys()) # list of keys
print( student_3.values()) # list of values
print( student_3.items()) # list of items

## Updation  👍

student_3["name"] = "Kallu"
print( student_3 ) # {'name': 'Kallu', 'school': 'Heritage', 'age': 43}

student_3.update({'name':"Abhay"})
print( student_3 ) # {'name': 'Abhay', 'school': 'Heritage', 'age': 43}

# Deletion 👍

print( student_3.pop("age") ) # 43 -> return removed value
print( student_3.popitem() ) # remove last item and return it -> ('school', 'Heritage')

student_3.clear() # clear whole dictionary
print( student_3 ) # {}