# Set methods 

vowels = { 'a' , 'e' , 'i' , ' o' , 'u' } 
consonents = { 'b' ,'c' , 'd' , 'f' , 'g' , 'h', 'i' ,'j'}

# 1. union() - used for union two sets

alphabates = vowels.union(consonents)
print( alphabates ) # {'u', 'h', 'c', 'e', 'a', 'b', ' o', 'd', 'j', 'i', 'f', 'g'}


# 2 . intersection - used for common values

set1 = { 1 , 3 ,4 , 5 , 6}
set2 = { 4, 6 , 5 ,1 ,8 , 9}

print( set1.intersection(set2)) # {1, 4, 5, 6}


# 3. Difference - element present in 1st set but not in 2nd set 

res_set = set1 - set2 
print(res_set ) # {3}
#or
res_set2 = set1.difference(set2)
print(res_set ) # {3}


# 4. Symmetric difference - element present in any one set not both

ans_set1 = set1 ^ set2
print( ans_set1 ) # {3, 8, 9} 

#or
ans_set2 = set1.symmetric_difference( set2 )
print( ans_set2 ) # {3, 8, 9} 

