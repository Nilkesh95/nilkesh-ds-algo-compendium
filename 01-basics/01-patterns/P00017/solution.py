# Solution


n = int(input())

for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ", end="")

    for k in range(0,i+1):
        print(chr(65+k),end="")

    for l in range(i,0,-1):
        print(chr(65+l-1),end="")

    print()

"""
TC: O(n*n)
SC: O(1)
"""
