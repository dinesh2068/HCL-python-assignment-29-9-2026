'''
Question 15 – Student Performance Analysis

The marks of five students in three subjects are stored in a NumPy array. Develop a program to perform a complete student performance analysis by calculating the total marks, average marks, highest marks, lowest marks, and identifying students who perform above the class average.

'''

import numpy as np

marks = np.array([[78, 85, 90],
                  [65, 72, 80],
                  [88, 91, 84],
                  [56, 62, 70],
                  [95, 89, 92]])

total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)
highest = np.max(marks, axis=1)
lowest = np.min(marks, axis=1)
class_average = np.mean(average)

print("Marks =")
print(marks)
print("Total Marks =", total)
print("Average Marks =", average)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Class Average =", class_average)
print("Students Above Class Average =", np.where(average > class_average)[0] + 1)
