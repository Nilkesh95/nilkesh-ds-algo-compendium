
## Approach

For each row , we execute:

- n-row-1 iterations for spaces.
- 2*row+1 iterations for stars.

Total operations per row:
```text
(n-row-1)+(2*row+1)=n+row 
```

**Time Complexity**

Across all n rows:<br>
Summation of iterations from row=0 to n-1 for the function is (n+row)
```text
So, n(n) + 0+1+2+3+….+n-1 = n*n + n(n-1)/2 = (3n*n -n)/2 = O(n*n)
```

**Auxiliary Space Complexity: O(1)**<br>
We only use three loop variables (row, spaces, stars) and n. No additional data structures grow with the input.

So, S(n)=O(1)
