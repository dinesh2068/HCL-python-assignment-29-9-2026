"""
3.	Square of numbers using lambda

"""

numbers = [1, 2, 3, 4, 5]

square = lambda x: x * x

result = list(map(square, numbers))

print(result)