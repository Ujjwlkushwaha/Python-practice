'''
Nth Fibonacci Number
Difficulty: EasyAccuracy: 22.3%Submissions: 368K+Points: 2

Given a non-negative integer n, your task is to find the nth Fibonacci number.

The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

The Fibonacci sequence is defined as follows:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n > 1
'''

def fibonacciSeries( n ):
    ''' Printig Fibonacci series.'''

    n1 = 0 
    n2 = 1
    print( n1 , n2 , end=" ")

    while n > 0 :
        n3 = n1 + n2
        print( n3 , end = " ")

        n1 = n2 
        n2 = n3

        n -= 1 # Update loop variable



# Finding Nth element of series
def nthFibonacci(n: int) -> int:
        """Finding nth fibonacci series element"""
        # Base case 
        if( n == 0 ):
            return 0
            
        if n == 1:
            return 1
        
        # Recurance relation
        return nthFibonacci(n-1) + nthFibonacci(n - 2)

n = int ( input ("Enter a range :: "))
fibonacciSeries(n)
print( f'Nth fibonacci series element is : ' , nthFibonacci(n))