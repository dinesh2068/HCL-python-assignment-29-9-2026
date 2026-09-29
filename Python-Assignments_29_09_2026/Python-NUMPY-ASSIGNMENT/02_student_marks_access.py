'''
Question 2 – Student Marks Access

The marks of five students are stored in a NumPy array as [72, 85, 64, 90, 76]. Write a program to access and display specific student marks using NumPy indexing and slicing.

'''

import numpy as np

marks = np.array([72, 85, 64, 90, 76])

print("Marks =", marks)
print("First Student Mark =", marks[0])
print("Third Student Mark =", marks[2])
print("Last Student Mark =", marks[-1])
print("First Three Marks =", marks[:3])
print("Second to Fourth Marks =", marks[1:4])
