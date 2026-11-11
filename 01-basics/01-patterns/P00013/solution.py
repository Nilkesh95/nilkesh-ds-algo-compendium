# Solution

n=int(input())

counter=0

for i in range(0,n):
    for j in range(0,i+1):
        counter+=1
        print(counter,end="")
    print()

"""
TC: O(n*n)
SC: O(1)
"""
