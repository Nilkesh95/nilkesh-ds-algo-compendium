# Solution

n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
    
for p in range(1,n):
    for l in range(0,n-p):
        print("*",end="")
    print() 

"""
TC: O(n*n)
SC: O(1)
"""
