'''

Array Pair Sum
Given an integer array, find all unique pairts that sum up to a specific value K.

Example:
    pair_sum([1,3,2,2], 4)
    would return 2 pairs:
        (1,3)
        (2,2)
'''

def pair_sum(array, k):
    if len(array) < 2:
        raise ValueError("Array length too small.")
    
    # keep track of seen array pairs and found unique (set) solutions
    seen = set()
    output = set()

    for number in array:
        target = k - number #the other number we are looking for
        
        if target not in seen: 
            seen.add(number)
        else:  # "sibling" number is present in a set
            # add to output set (there will be no change if the pair was already included)
            output.add((min(number, target), max(number, target)))  # use min and max to avoid same pairs in diffrent order

    # print result
    print('\n'.join(map(str, list(output))))

pair_sum([1,3,2,2], 4)
    