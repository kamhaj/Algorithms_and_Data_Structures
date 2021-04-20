'''
Given an array, find its most frequently occuring element.
'''

def find_most_frequent_element(lst):
    count = {}
    max_count = 0
    max_item = None
    result_dict= {}

    for i in lst:
        if i not in count:
            count[i] = 1
        else:   # element already spotted
            count[i] += 1

        if count[i] >= max_count:
            max_count = count[i]
            max_item = i
            result_dict[max_item] = max_count

    # for multiple solutions: return only those solutions with final counter equal to maximal counter found (max_count)
    return { k:v for k,v in result_dict.items() if v==max_count } 

print(find_most_frequent_element([1,3,3,2,1,1,1]))          # {1: 4}
print(find_most_frequent_element([1,2,3,4,5,6,7,8]))        # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
print(find_most_frequent_element([1,-3,-3,2,-1,-1,-3,-1]))  # {-3: 3, -1: 3}
print(find_most_frequent_element(['a', 'b','c', 'd', 'a', 'd', 'e', 'b', 'a', 'd']))    #{'a': 3, 'd': 3}