'''
Question 6 – Average Marks

The marks of five students in three subjects are represented using a NumPy matrix. Write a program to calculate the average marks of each student.

'''

import numpy as np

marks = np.array([[78, 85, 90],
                  [65, 72, 80],
                  [88, 91, 84],
                  [56, 62, 70],
                  [95, 89, 92]])

average = np.mean(marks, axis=1)

print("Marks =")
print(marks)
print("Average Marks of Each Student =", average)
