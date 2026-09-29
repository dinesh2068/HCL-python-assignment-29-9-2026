'''
Question 11 – Duplicate Marks Analysis

The marks obtained by five students are [85, 92, 85, 76, 92]. Use NumPy functions to identify the unique marks obtained by the students.

'''

import numpy as np

marks = np.array([85, 92, 85, 76, 92])

unique_marks = np.unique(marks)

print("Marks =", marks)
print("Unique Marks =", unique_marks)
