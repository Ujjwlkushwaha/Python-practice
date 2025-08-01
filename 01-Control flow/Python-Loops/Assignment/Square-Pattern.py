"""
Print Square

Given an integer n, write a program to print the square of size n using "*" character. 

Examples :

Input: n = 4
Output:
* * * *
*      *
*      *
* * * *
Explanation: It's a square! Each side contains n = 4 .
"""

n = int(input())

for i in range( 0 , n):
    
    for j in range(0 , n) :

        if ( i == 0 or i == n-1):
            print('*' , end="")

        elif( j==0 or j==n-1):
            print('*' , end="")
        else:
            print(" " , end="")
    print()