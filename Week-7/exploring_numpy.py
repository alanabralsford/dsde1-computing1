'''
exploring_numpy.py

Getting comfortable with creating and manipulating
numpy arrays.
'''


# return an array 8 items that can be any number 
# i.e. doesn't matter what you fill it with, it's
# the size that is important

import numpy as np
import math

def create_array8():
    a = np.arange(8)
    return a
# return a 4 x 6 array filled with any number 
# i.e. doesn't matter what you fill it with, it's
# the size that is important
def create_array6_4():
    #b = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20,21, 22, 23, 24]])
    b = np.arange(24).reshape(6,4)
    return b

# return a 2x3 array of zeros w
# hint: you don't need to call array
def create_zeros2_3():
    c = np.zeros((2, 3))
    return c


# return a one-dimensional array that starts
# at 3 and counts up to 96
# 3, 4, 5 ... 94, 95, 96
def create96():
    d = np.arange(3, 97, 1)
    return d


# create a function that takes in the following:
#   - starting number
#   - number of rows
#   - number of columns
# return an array that starts at the starting number 
# and counts up ending at 
# starting number + rows x columns
# with the input number of rows and columns
# for example, starting at 3 and 3 rows with 4 columns:
#  [3, 4, 5, 6]
#  [7, 8, 9, 10]
#  [11, 12, 13, 14]
def algo_array1(start, row, column):
    end = start + row*column
    b = np.arange(start,end, 1).reshape(row, column)
    return b

# create a function that will return an array 
# that contains a number of values passed in
# as an input argument evenly spaced from 0 to 2*pi
# hint: you can generate it algorithmically
# with a numpy function
def algo_array2(step):
    c = np.linspace(0, 2*np.pi, step, endpoint=True, dtype = float)
    return c

# create a function with one input argument
# which takes an input value of a postive number
# it returns a dictionary with the following
#  key/value pairs:
#  'odd': array of odd numbers from 1 to input argument (inclusive)
#  'even': array of even numbers from 2 to input argument (inclusive)
# hint: you don't need a for loop
def odd_even(pos):
    thisDic = {'odd':np.arange(1., pos+1, 2), 'even':np.arange(2., pos+1, 2)}
    return thisDic


#test
print(create_array8())
print(create_array6_4())
print(create_zeros2_3())
print(create96())
print(algo_array1(3, 3,4))
print(algo_array2(5))
print(odd_even(8))