# Solution

n=int(input())

for row in range(0,n):
    for spaces in range(0,row):
        print(" ",end="")
    for stars in range(0,2*n-(2*row+1)):
        print("*",end="")
    print() 

    """
TC: O(n*n)
SC: O(1)
"""
