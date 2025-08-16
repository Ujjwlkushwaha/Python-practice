#  LIST IN PYTHON 

"""
        1. List is mutable in nature 
        2. Order
        3. Allow duplicates
        4. Changable

"""


# 👋 CREATING LIST 

my_list = ['banana' , 'apple' , 'mango']   

print( my_list )              # ['banana', 'apple', 'mango']
print ( type ( my_list ))   # <class 'list'>



# 👋 ACCESSING ELEMENTS 

print ( my_list[1])   # apple
    
for item in my_list:
    print( item , end=" ") # banana apple mango



# 👋 LIST METHODS-

my_list.append( " Guava ")       # Adding new element
my_list.insert( 0 , "Litchii")   # Adding element at given index

print(my_list)  #['Litchii', 'banana', 'apple', 'mango', ' Guava ']

my_list.pop()  # remove last element
my_list.pop(0) # remove indexed element

my_list.remove("apple")   # remove specific element


nums = [3,5,2,7,8,4,1,23,21]   

nums.sort()     #sort in ascending order
print( nums )  # [1, 2, 3, 4, 5, 7, 8, 21, 23]

nums.reverse()
print(nums)   # [23, 21, 8, 7, 5, 4, 3, 2, 1]
