'''
Given 2 arrays (assume no duplicates)
is 1 array a rotation of another - return True/False
Rotation means same size and elements but start index is different (part of a list is shifted)

BigO(n) We are going through each array 2x, but O(2n) = O(n)

Select an indexed position in list1 and gets its value. Find same element in list2 and
check index for index from there. If any variation occurs, then we know its False.
Getting to last item without a False means True.
'''

def rotation(list1, list2):
    if len(list1) != len(list2):
        return False #list1 cannot be list2 rotation

    key = list1[0]
    key_index_in_l2 = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index_in_l2 = i
            break   #key index found

    # if no index found (list2 does not have key element)
    if key_index_in_l2 == 0:
        return False

    for x in range(len(list1)):
        l2_index = (key_index_in_l2 + x) % len(list1)

        if list1[x] != list2[l2_index]:
            return False
        
    return True

    
print(rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))       # True
print(rotation([1,2,3,4,5,6,7], [4,5,6,8,1,2,3]))       # False