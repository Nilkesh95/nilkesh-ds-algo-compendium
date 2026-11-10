# Solution


n = int(input())

for i in range(0, n):
    for j in range(0, i+1):
        print(j+1, end="")

    for k in range(0, 2*n-(2*(i+1))):
        print(" ", end="")

    for l in range(i+1, 0, -1):
        print(l, end="")

    print()
