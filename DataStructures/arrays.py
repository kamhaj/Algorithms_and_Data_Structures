'''
In Python, LIST is implemented as DYNAMIC ARRAY.
(in other languages like Java or C++ we have both static and dynamic arrays).
Dynamic array means that we do not have to specify the length on initialization (this would be static).
Dynamic array means that we can add "infinite" number of elements. Python would allocate a little bit more of memory than needed for the array
and it will allocate more capacity/memory if it runs out of it (geometric progression - trying to leave more space to get ready for new insertions, not one by one).


Python can store different types of elements (e.g. int + strings) in the same array.
e.g. my_list = ["Aaa", "Bb", 5, 12.5, "xD"]

##how it look like in memory(concept, in Python it looks slightly different. Python uses objects and references)
0x00500         298
0x00504         305
0x00508         320
0x0050A         301
0x0050F         292


## How an INTEGER is represented
298 = 100101010  (9 bites)
298 = 00000000 000000000 00000001 00101010  (integers are stored in 4 bytes = 32 bits)

0x00500         00000000
0x00501         00000000
0x00502         00000001
0x00503         00101010

## how indexing work
stock_prices[0]   --> 0x00500
stock_prices[2]   --> 0x00500 + 2 * sizeof(integer)
stock_prices[2]   --> 0x00500 + 2 * 4
stock_prices[2]   --> 0x00508


'''

## an array (list) to store Apple's stock prices on a given day
stock_prices = [298, 305, 320, 301, 292]

## what was the price on day 3?    
## BigO(1)
day3_stock_price = stock_prices[2]


## on what day price was 301?  
## BigO(n) ~worst case
for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        pass
        #return i

## print all prices (traverse through data structure)
## BigO(n) 
for price in stock_prices:
    print(price)

## insert new price 284 at index 1 
## BigO(n) (it has to shift  (copy operations) all further elements by 1 
## "to the right" before inserting a new element and possibly allocate more memory 
## (geometrically: 5->10->20->40...)).

stock_prices.insert(1, 284)


## delete element at index ID or by element ELEM
## BigO(n) (it has to shift (copy operations) all further elements by 1 "to the left")
stock_prices.remove(284)
del stock_prices[-1]           # few elements possible, e.g. del stock_prices[1:4]


## 2D arrays
stock_prices_2D = [
    [2,3,5,6],
    [40,42,38,44],
    [78,89,71,66]
]





''' EXCERCISE '''
# You have a list of your favourite marvel super heros
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)

# 5. Sort the list in alphabetical order
heros.sort()
print(heros)