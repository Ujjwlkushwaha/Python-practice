def plusOne(digits: list[int]) -> list[int]:
        # brute force approach
    number = 0
    for item in digits:
        number = number*10 + item 

    number += 1
    digits.clear()
    while( number != 0 ) :
        d = number % 10
        digits.insert(0,d)
        number //= 10
    
    return digits


print(plusOne([1,2,3,4]))
          