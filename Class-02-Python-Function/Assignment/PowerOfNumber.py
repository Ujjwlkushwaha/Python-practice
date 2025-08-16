# Power Of Numbers ( GFG - medium )

# Given a number n, find the value of n raised to the power of its own reverse.
# Note: The result will always fit into a 32-bit signed integer.

# Examples:

# Input: n = 2
# Output: 4
# Explanation: The reverse of 2 is 2, and 22 = 4.

# Input: n = 10
# Output: 10
# Explanation: The reverse of 10 is 1 (leading zero is discarded), and 10 raised to the power 1 is 10.


def reverseNum( n ) :
    revNum = 0
    while( n != 0 ):
        r = n % 10
        revNum = (revNum*10)+r
        n //= 10
    return revNum

def reverseexponentiation( n ):
    pw = reverseNum( n )
    return n**pw

n = int(input("enter number :: "))
print( reverseexponentiation( n ))