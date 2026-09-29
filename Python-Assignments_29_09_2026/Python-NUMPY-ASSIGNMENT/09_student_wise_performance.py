'''
Question 9 – Student-wise Performance

The marks of five students in three subjects are stored in a NumPy matrix. Write a program to calculate the total marks obtained by each student using an appropriate axis operation.

'''

import numpy as np

marks = np.array([[78, 85, 90],
                  [65, 72, 80],
                  [88, 91, 84],
                  [56, 62, 70],
                  [95, 89, 92]])

student_total = np.sum(marks, axis=1)

print("Marks =")
print(marks)
print("Total Marks of Each Student =", student_total)
