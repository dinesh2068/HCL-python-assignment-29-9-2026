'''
Question 8 – Subject-wise Performance

The marks of five students in three subjects are stored in a NumPy matrix. Write a program to calculate the total marks obtained in each subject using an appropriate axis operation.

'''

import numpy as np

marks = np.array([[78, 85, 90],
                  [65, 72, 80],
                  [88, 91, 84],
                  [56, 62, 70],
                  [95, 89, 92]])

subject_total = np.sum(marks, axis=0)

print("Marks =")
print(marks)
print("Total Marks in Each Subject =", subject_total)
