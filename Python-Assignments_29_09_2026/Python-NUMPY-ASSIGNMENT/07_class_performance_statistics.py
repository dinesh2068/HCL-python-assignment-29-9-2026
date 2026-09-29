'''
Question 7 – Class Performance Statistics

The marks obtained by five students are [67, 82, 91, 74, 58]. Using NumPy statistical functions, determine the total, average, highest, lowest, and standard deviation of the marks.

'''

import numpy as np

marks = np.array([67, 82, 91, 74, 58])

total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
standard_deviation = np.std(marks)

print("Marks =", marks)
print("Total =", total)
print("Average =", average)
print("Highest =", highest)
print("Lowest =", lowest)
print("Standard Deviation =", standard_deviation)
