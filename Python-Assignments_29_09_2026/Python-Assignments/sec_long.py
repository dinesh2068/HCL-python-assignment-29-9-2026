"""
4.	Find the second largest element in a list

"""
numbers = [10, 5, 8, 20, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest =", second_largest)