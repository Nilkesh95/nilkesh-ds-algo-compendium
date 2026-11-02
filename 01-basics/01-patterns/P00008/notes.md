
## Approach

For each row i, we execute:
	-	row iterations for spaces.
	-	2n-2i-1 iterations for stars.

Total operations per row:<br>
 i+(2n-2i-1)=2n-i-1

Across all n rows:<br>
Summation of iterations from row i=0 to n-1 for the function (2n-i-1)<br>
```text
So,
  n(2n-1) - (0+1+2+3+….+n-1) 
= n(2n-1) - n(n-1)/2 
= (3n*n - n)/2
= O(n*n)
```
