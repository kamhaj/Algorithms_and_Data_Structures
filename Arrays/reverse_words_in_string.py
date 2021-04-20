'''
Given a string of words, reverse all the words

Example:
    start = "This is the best"
    finish = "best the is This"
'''

## with build-in Python functions
def reverse_string(s):
    words = s.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


## without build-in Python functions
def reverse_string_2(s):
    length = len(s)
    spaces = [' ']
    words = []
    idx = 0

    while idx < length:
        if s[idx] not in spaces:      #if it is a letter, not a space (or other defined separator)
            word_start = idx

            while idx < length and s[idx] not in spaces:  # find where current word ends
                idx += 1
            
            words.insert(0, s[word_start:idx])  # idx exclusive (it is a space or string has ended)

        idx += 1 # skip if s[i] is in spaces or new word was just added

    return " ".join(words)
    

print(reverse_string("This is the best"))
print(reverse_string_2("This is the best"))