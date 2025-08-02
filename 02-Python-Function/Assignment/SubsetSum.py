# Subset Sums - GFG ( medium )

# Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.


def subset_sums(arr):
    result = []

    def helper(index, current_sum):
        # Base case: if we reach the end of the array
        if index == len(arr):
            result.append(current_sum)
            return
        
        # Include the current element
        helper(index + 1, current_sum + arr[index])
        
        # Exclude the current element
        helper(index + 1, current_sum)

    # Start recursion from index 0 and initial sum 0
    helper(0, 0)
    return result


print(subset_sums([2, 3]))      # [0, 2, 3, 5]
print(subset_sums([1, 2, 1]))   # [0, 1, 1, 2, 2, 3, 3, 4]
