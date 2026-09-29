'''
Question 3 – Subject-wise Marks

The marks obtained by five students in three subjects are given below. Create a NumPy array to represent the data and reshape it into an appropriate matrix format.

[78, 85, 90, 65, 72, 80, 88, 91, 84, 56, 62, 70, 95, 89, 92]

'''

import numpy as np

marks = np.array([78, 85, 90, 65, 72, 80, 88, 91, 84, 56, 62, 70, 95, 89, 92])

matrix = marks.reshape(5, 3)

print("Marks =", marks)
print("Subject-wise Marks =")
print(matrix)
