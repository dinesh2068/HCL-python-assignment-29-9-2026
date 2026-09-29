'''
Question 4 – Internal and External Marks

The internal and external examination marks of five students are stored in two NumPy arrays. Write a program to calculate the final marks of each student using NumPy array operations.

'''

import numpy as np

internal = np.array([25, 28, 22, 27, 24])
external = np.array([60, 55, 65, 58, 62])

final_marks = internal + external

print("Internal Marks =", internal)
print("External Marks =", external)
print("Final Marks =", final_marks)
