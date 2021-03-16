#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:01:09 2021

@author: jayne
"""
import numpy as np
"""
Exercise 1: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
Expected Output:

Creating 5X2 array using numpy.arange
[[100 110]
 [120 130]
 [140 150]
 [160 170]
 [180 190]]
"""

num_array = np.arange(100, 200, 10)
num_array = num_array.reshape(5,2)
print(num_array)

"""
Exercise 2: Following is the provided numPy array. return array of items in the third column from all rows
import numpy
sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
Expected Output:

Printing Input Array
[[11 22 33]
 [44 55 66]
 [77 88 99]]

 Printing array of items in the third column from all rows
[33 66 99]
"""

sample_array = np.array([(11,22,33),(44,55,66),(77,88,99)])

print(sample_array[0:,2])

"""
Exercise 3: Add the following two NumPy arrays and Modify a result array by calculating the square of each element
import numpy

arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
Expected Output:

addition of two arrays is 

[[20 39 33]
 [25 25 28]]

Result array after calculating the square root of all elements

[[ 400 1521 1089]
 [ 625  625  784]]
"""

array_one = np.array([[5, 6, 9], [21 ,18, 27]])
array_two = np.array([[15 ,33, 24], [4 ,7, 1]])
array_sum = array_one + array_two
print(np.square(array_sum))






