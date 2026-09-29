"""
1.	Write a function calculate(a, b, operation) that performs addition, subtraction, multiplication, or division 
based on the supplied operation.

"""


def calculate(a, b, operation):
    
    if(operation == '+'):
        return a+b
    
    elif(operation == '-'):
        return a-b
    
    elif(operation == '*'):
        return a*b
    
    elif(operation == '/'):
        return a/b
    
a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: "))
ch = input("Enter the symbol of the operation: ")

print(f"{a} {ch} {b} = {calculate(a,b,ch)}")