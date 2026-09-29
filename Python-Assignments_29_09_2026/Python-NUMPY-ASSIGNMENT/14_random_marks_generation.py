'''
Question 14 – Random Marks Generation

Generate marks for five students using NumPy's random number generation functionality. Perform basic statistical analysis on the generated marks.

'''

import numpy as np

marks = np.random.randint(0, 101, 5)

print("Generated Marks =", marks)
print("Total =", np.sum(marks))
print("Average =", np.mean(marks))
print("Highest =", np.max(marks))
print("Lowest =", np.min(marks))
print("Standard Deviation =", np.std(marks))
