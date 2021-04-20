'''
compare different computational costs (time) between functions
'Constant', 'Linear', 'Quadratic', 'Cubic'
'''
import numpy as np
import time


## O(const)
def func_constant(lst=[1,2,3]):
    '''
    prints first item in a list of values. Doesn't matter how big a list is.
    '''
    counter = 0
    #print(lst[0])
    counter += 1

## O(n)
def func_linear(lst=[1,2,3]):
    '''
    takes in a list and prints out all values
    '''
    counter = 0
    for value in lst:
        #print(value)
        counter += 1

## O(n^2)
def func_quadratic(lst=[1,2,3]):
    '''
    takes in a list and prints out all values
    '''
    counter = 0
    for value_1 in lst:
        for value_2 in lst:
            #print(value_1, value_2)
            counter += 1

## O(n^3)
def func_qubic(lst=[1,2,3]):
    '''
    takes in a list and prints out all values
    '''
    counter = 0
    for value_1 in lst:
        for value_2 in lst:
            for value_3 in lst:
                #print(value_1, value_2)
                counter += 1



''' run functions '''
my_list = range(0,500)

print('\n\n*** constant function ***')
start_time = time.time()
func_constant(lst=my_list)
print(f'--- {round(time.time() - start_time, 4)} seconds ---')


print('\n\n*** linear function ***')
start_time = time.time()
func_linear(lst=my_list)
print(f'--- {round(time.time() - start_time, 4)} seconds ---')


print('\n\n*** quadratic function ***')
start_time = time.time()
func_quadratic(lst=my_list)
print(f'--- {round(time.time() - start_time, 4)} seconds ---')


print('\n\n*** qubic function ***')
start_time = time.time()
func_qubic(lst=my_list)
print(f'--- {round(time.time() - start_time, 4)} seconds ---')



''' OUTPUT for 500 elements:

*** constant function ***
--- 0.0 seconds ---


*** linear function ***
--- 0.0 seconds ---


*** quadratic function ***
--- 0.024 seconds ---


*** qubic function ***
--- 11.9189 seconds ---

'''