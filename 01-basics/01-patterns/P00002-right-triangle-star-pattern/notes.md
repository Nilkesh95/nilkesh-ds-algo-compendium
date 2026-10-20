## Approach

I, almost always, **think about the pattern problems in terms of rows & columns.** This makes it easy to understand what needs to be printed & how many times it needs to be printed.

In this problem, n rows of stars need to be printed. The first row will have 1 star & each subsequent row will have one more star than the previous row. So, the last row will have n stars.

And going by the above logic, row will take values from 0 to n-1. And subsequently, column will take values from 1 to n.  
**And that's why, for each value of row, col will go from 0 to row+1.**  
Which means:  
when row is 0, col will go from 0 to 1 (1 iteration of col as in python, the loop only goes till n-1). 
when row is 1, col will go from 0 to 2 (2 iterations of col). 
when row is 2, col will go from 0 to 3 (3 iterations of col). 
and so on...  

## Possible Mistakes/Lessons Learnt
Initially I did use the code mentioned below for col loop:

```python
for col in range(0,row):
```
-> In this case, the first loop doesn't work because col goes from 0 to 0 and it doesn't run even a single loop as the start & end points of col are same. As a result, this will be printed:

```text
        <blank line with no characters printed> -> as the first col loop doesn't run
*
**
***
****
```

