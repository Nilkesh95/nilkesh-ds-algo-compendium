## Approach

I, almost always, **think about the pattern problems in terms of rows & columns.** This makes it easy to understand what needs to be printed & how many times it needs to be printed.

In this problem, n rows of numbers need to be printed. The first row will have 1 number(number 1) & each subsequent row will have one more number than the previous row. So, the last row will have n numbers from 1 to n.

And going by the above logic, row will take values from 0 to n-1. And subsequently, column will take values from 1 to n.  
**And that's why, for each value of row, col will go from 0 to row+1.**  
Which means:  
when row is 0, col will go from 0 to 1 (1 iteration of col as in python, the loop only goes till n-1)<br>
when row is 1, col will go from 0 to 2 (2 iterations of col)<br>
when row is 2, col will go from 0 to 3 (3 iterations of col)<br>
and so on...<br>

It follows exactly the same pattern as problem# P00002 but here we just need to print numbers instead of stars.

And so in terms of what to print,<br>
when row is 0, col should print 1,<br> 
when row is 1, col should print 1&2,<br>
when row is 2, col should print 1,2&3,<br>
and so on...<br>
So col starts printing from the state row+1.

## Possible Mistakes/Lessons Learnt
If we make the same mistake as we did in pattern P00002(mentioned below), 

```python
for col in range(0,row):
```

Then we will get something like this:

```text
        <blank line with no characters printed> -> as the first col loop doesn't run
1
12
123
1234
        A final newline is added due to print(). The cursor moves to the start of a brand new, empty sixth line, leaving the final output cleanly terminated.
```

## Concepts

### Cursor & end argument

```text
1A
B12
123
1234
12345
```

After the col loop completes for the first time,<br> 
1 is printed, row is still 0, col becomes 1 and the loop terminates -> at this point the cursor is at position A(as shown in the output text above), that is, the cursor stays immediately after 1(to the right side of 1) on the first line. 

Why?? --> Because after 1 is printed, the default 'end' parameter of the print() function is modified by end="" --> This makes the result to have no space after printing the character '1', rather a new line is added after printing the character '1'.

Then once the col loop is terminated, the next executable line is print() and print() automatically adds a new line via the default parameter end="\n" & moves the cursor to the start of the second line, that is, at position B.

Why?? --> Because by default, print() automatically adds its own newline character (end="\n") at the right of charater '1' which moves the cursor to the start of second line at position B from from the end of first line at position A. **Which means that there is a default (end"\n") parameter inbuilt which comes along with the print() function.**

### Separator argument

Unrelated to this problem, but there is also a separator argument that print function takes.<br> 
Default value it takes: ' ' (a single space)<br>   
What it does: Specifies what character or string should be inserted between multiple positional arguments.<br> 

```python
print("apple", "banana", "cherry", sep=", ")
```

```text
#Output: apple, banana, cherry
```
