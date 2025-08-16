# Sets in Python - datastructure used to store " unique values " 

my_set = { "item1" , "item2" , "item3" , "item4"} 
print( my_set ) # {'item3', 'item1', 'item2', 'item4'}

# Characteristics 
    # 1. Store unique values
    # 2. Mutable  -> add or remove values 
    # 3. Unordered -> means not manage indexes
    # 4. Value is immutable mean you can not update values


# Creating a set ✅

## method- 1 - 

fruits = { "Mango" , "Banana" , "Papaya", "Grapes"}
print( fruits )

## method - 2 - using constructor

days = set(["Sunday" , "Monday"  ,"Tuesday" , "Wednesday"])
print(days)  # {'Wednesday', 'Tuesday', 'Sunday', 'Monday'}


# Operations on set ✅

## 1. Adding value 👍

days.add("friday")
print( days ) # {'Tuesday', 'friday', 'Sunday', 'Monday', 'Wednesday'}

## 2. Removing value 👍

days.remove("friday") # It shows error if element not found 😣
print( days )

days.discard( "Sunday")  # It does not shows error if element not found
print( days ) # {'Monday', 'Tuesday', 'Wednesday', 'friday'}

days.clear() 
print( days ) # clear whole set
