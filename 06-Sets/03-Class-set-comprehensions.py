# Set iterables and comprihensions

consonents = { 'b' ,'c' , 'd' , 'f' , 'g' , 'h', 'i' ,'j'}

for items in consonents :
    print( items ) # print all items of set

# Set comprehensions

    ## Syntax ->
    
            #   my_set = { expression for item in iterable  if condition}

## Creating set of squares

squares = { x**2 for x in range( 1,6)}
print( squares ) # {1, 4, 9, 16, 25}