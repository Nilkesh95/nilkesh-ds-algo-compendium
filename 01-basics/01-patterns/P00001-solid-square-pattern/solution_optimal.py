# Solution 2

n=int(input())

for row in range(0,n):
    for col in range(0,n):
        print("*",end="")
    print()

"""
TC: O(n*n)
SC: O(1)
"""