# Solution 1

n=int(input())

k=n
while n>0:
    print("*" * k)
    n-=1

"""
TC: O(n*n)
SC: O(n) # for constructing a string of size n
"""
