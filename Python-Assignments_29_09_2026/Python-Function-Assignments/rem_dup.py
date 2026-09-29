"""
4.	Write a function remove_duplicates(lst) that returns a list containing only unique elements while 
preserving their original order.

"""

def remove_duplicates(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)

    return unique


numbers = [1, 2, 2, 3, 4, 3, 5, 1]

print(remove_duplicates(numbers))