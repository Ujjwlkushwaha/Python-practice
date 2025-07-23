# 1717. Maximum Score From Removing Substrings
# Medium
# Topics
# 
# Hint
# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

 

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.



def maximumGain(s: str, x: int, y: int) -> int:
        # brute force
        score = 0

        if x > y :
            while( s.find("ab") != -1 ):
                  i = s.find("ab")
                  s = s[:i] + s[i+2 : ] 
                  score = score+x

            while( s.find( "ba") != -1 ):
                  i = s.find("ba")
                  s = s[:i] + s[i+2 : ] 
                  score = score+y
        
        else:
            while( s.find( "ba") != -1 ):
                  i = s.find("ba")
                  s = s[:i] + s[i+2 : ] 
                  score = score+y

            while( s.find("ab") != -1 ):
                  i = s.find("ab")
                  s = s[:i] + s[i+2 : ] 
                  score = score+x  
                    
        return score

print( maximumGain("aabbaaxybbaabb" , 5 , 4 ))    



# Optimized Stack + greedy


def maximumGain2(s: str, x: int, y: int) -> int:
    def remove_pair(s: str, first: str, second: str, score: int) -> (str, int):
        stack = []
        total = 0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                total += score
            else:
                stack.append(ch)
        return ''.join(stack), total

    # Step 1: prioritize based on maximum score
    if x > y:
        s, score1 = remove_pair(s, 'a', 'b', x)  # remove "ab"
        _, score2 = remove_pair(s, 'b', 'a', y)  # remove "ba"
    else:
        s, score1 = remove_pair(s, 'b', 'a', y)  # remove "ba"
        _, score2 = remove_pair(s, 'a', 'b', x)  # remove "ab"

    return score1 + score2

# Test
print(maximumGain2("aabbaaxybbaabb", 5, 4))  # Output: 20

          