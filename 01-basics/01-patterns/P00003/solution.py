# Solution

n=int(input())

for row in range(0,n):
    for col in range(0,row+1):
        print(col+1,end="")
    print()

"""
TC: O(n*n)
SC: O(1)
"""
