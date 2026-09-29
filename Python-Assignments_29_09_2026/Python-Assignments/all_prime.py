"""
1.	Print all prime numbers between input range (Ex – input 20 50, prints all prime numbers between 20 and 50).
"""

n = int(input())
m = int(input())

for i in range(n,m+1):
    if i < 2:
        continue
    
    prime = True
    
    for j in range(2,i):
        if i%j == 0:
            prime = False
            break
        
    if(prime):
        print(i)