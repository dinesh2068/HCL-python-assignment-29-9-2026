'''
Question 12 – Missing Marks

The marks of five students are represented as [78, 85, np.nan, 92, 67], where np.nan represents a missing mark. Write a NumPy program to calculate the average marks without considering the missing value.

'''

import numpy as np

marks = np.array([78, 85, np.nan, 92, 67])

average = np.nanmean(marks)

print("Marks =", marks)
print("Average without Missing Value =", average)
