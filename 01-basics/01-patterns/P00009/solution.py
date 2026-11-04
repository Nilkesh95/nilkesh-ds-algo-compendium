# Solution

n=int(input())

for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()
    
for p in range(0,n):
    for l in range(0,p):
        print(" ",end="")
    for m in range(0,2*n-(2*p+1)):
        print("*",end="")
    print() 

"""
TC: O(n*n)
SC: O(1)
"""
