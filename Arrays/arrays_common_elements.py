''' 
Find same elements that both arrays contain
Assume that arrays are sorted.

'''

def common_elements(a, b):
    if not a or not b:
        raise ValueError("At least one empty array specified.")
    
    idx_1 = 0
    idx_2 = 0

    result = []

    #while till at least one array ends
    while idx_1 < len(a) and idx_2 < len(b):
        # if same elements spotted, reindex
        if a[idx_1] == b[idx_2]:
            result.append(a[idx_1])
            idx_1 += 1
            idx_2 += 1
        
        elif a[idx_1] > b[idx_2]:
            idx_2 += 1

        else:
            idx_1 += 1
        
    return result

print(common_elements([1,2,4,6,7,9], [1,2,4,5,9,10]))       # returns [1, 2, 4, 9]
print(common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]))       # returns [1, 4, 9]