"""
3.	Write a function employee(**args) that accepts employee information such as name, ID, department and salary, 
then displays the information.

"""
def employee(**args):
    for key, value in args.items():
        print(key, ":", value)

employee(
    name="Dinesh",
    ID=101,
    department="IT",
    salary=50000
)