"""
2.	Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum.

"""

def sum_numbers(*args):
    total = 0

    for num in args:
        total += num

    return total


print(sum_numbers(10, 20, 30))