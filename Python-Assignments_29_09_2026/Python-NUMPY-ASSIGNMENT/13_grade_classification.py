'''
Question 13 – Grade Classification

The marks obtained by five students are [95, 82, 74, 61, 45]. Using NumPy conditional operations, classify the students into appropriate grade categories based on their marks.

'''

import numpy as np

marks = np.array([95, 82, 74, 61, 45])

conditions = [
    marks >= 90,
    marks >= 80,
    marks >= 70,
    marks >= 60,
    marks < 60
]

grades = np.select(conditions, ["A", "B", "C", "D", "F"])

print("Marks =", marks)
print("Grades =", grades)
