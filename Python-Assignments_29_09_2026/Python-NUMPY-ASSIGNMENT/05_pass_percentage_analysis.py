'''
Question 5 – Pass Percentage Analysis

The marks obtained by five students are [45, 78, 56, 32, 91]. Using NumPy Boolean masking, identify the students who have secured 50 marks or above.

'''

import numpy as np

marks = np.array([45, 78, 56, 32, 91])

passed = marks[marks >= 50]

print("Marks =", marks)
print("Students with 50 marks or above =", passed)
