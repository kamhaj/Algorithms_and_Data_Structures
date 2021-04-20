'''
Take an array with positive and negative integers.
Find the maximum CONTINUOUS sum of that array.

We assume "sum" can mean one number only, or more numbers added up
'''

# find largest continuous sum [it can include some negative numbers, no problem :) ]
def largest_continuous_sum(arr):
    if len(arr) == 0:
        raise ValueError("Array too short.")
    
    max_sum = current_sum = arr[0]

    # loop through array, first element was already accounted for
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


print(largest_continuous_sum([7,1,2,-1,3,4,10,-12,3,21,-19]))     # returns 38