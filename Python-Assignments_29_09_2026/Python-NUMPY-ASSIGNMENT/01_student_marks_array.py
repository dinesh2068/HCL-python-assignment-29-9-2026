'''
Question 1 – Student Marks Array

The marks obtained by five students in a subject are given as [78, 65, 89, 56, 92]. Create a NumPy array and display the array along with its basic properties.

'''

import numpy as np

marks = np.array([78, 65, 89, 56, 92])

print("Marks =", marks)
print("Dimensions =", marks.ndim)
print("Shape =", marks.shape)
print("Size =", marks.size)
print("Data Type =", marks.dtype)
