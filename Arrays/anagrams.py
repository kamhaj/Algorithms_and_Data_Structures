''' Problem:

Given two strings, check to see if they are anagrams.

e.g. "dog" is an anagram of "God" or "d go".
     "clint eastwood" is an anagram of "old west action"

Ignore capitalization and spaces.

'''

## cheks if two strings are anagrams
def is_anagram(s1, s2):
    # remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # return boolean for sorted match
    return sorted(s1) == sorted(s2)



## cheks if two strings are anagrams, but do not use ready Python methods like sorted()
def is_anagram_base_operations(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # check if string have the same number of letters
    if len(s1) != len(s2):
        return False
    
    # count frequency of each letter
    count = {}

    for letter in s1:    # for every letter in string s1
        if letter in count:     # if letter already in dictionary
            count[letter] += 1
        else:
            count[letter] = 1

    # do reverse for string s2
    for letter in s2:    # for every letter in string s2
        if letter in count:     # if letter already in dictionary
            count[letter] -= 1
        else:
            return False        # new letter occured

    # check if all counters are 0 (should be if anagrams)
    for letter in count:
        if count[letter] != 0:
            return False

    return True



print(is_anagram("Clint Eastwood", "old west action"))
print(is_anagram("Ala ma kota", "Kot ma Alę"))
print(is_anagram_base_operations("Clint Eastwood", "old west action"))
print(is_anagram_base_operations("Ala ma kota", "Kot ma Alę"))