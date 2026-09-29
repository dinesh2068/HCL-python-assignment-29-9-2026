'''
Question 10 – Student Ranking

The total marks obtained by five students are [245, 278, 219, 290, 256]. Use NumPy sorting and indexing operations to arrange the marks in order and determine the ranking of the students.

'''

import numpy as np

marks = np.array([245, 278, 219, 290, 256])

sorted_marks = np.sort(marks)[::-1]
ranking = np.argsort(marks)[::-1]

print("Total Marks =", marks)
print("Marks in Descending Order =", sorted_marks)
print("Student Ranking =")

for i in range(len(ranking)):
    print("Rank", i + 1, ": Student", ranking[i] + 1, "-", marks[ranking[i]])
