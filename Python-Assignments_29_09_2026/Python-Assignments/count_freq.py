"""
5.	Count frequency of characters in a string

"""

s = input("Enter the String: ")

freq = {}

for ch in s:
    freq[ch] = s.count(ch)
    # if ch in freq:
    #     freq[ch] += 1
    # else:
    #     freq[ch] = 1
    
print(freq)