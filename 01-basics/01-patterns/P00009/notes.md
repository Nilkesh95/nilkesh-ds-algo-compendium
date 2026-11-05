
## Approach

There's **one important observation** about this pattern:

The middle row:

```text
*********
*********
```

appears twice.

That's because:

- The first outer loop prints the complete upright pyramid, including its widest row.
- The second outer loop starts by printing the widest row again.

**If the question expects the middle row twice, the code is 100% correct.**

However, if the question expects a standard diamond pattern, the widest row should appear only once:

```text
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

Then, this can be achieved by changing just one line.

**Approach 1:** Update the second outer loop to start from `p=1` instead of `p=0`.

**Approach 2:** Keep the outer loop from `p=0`, however the inner loops should only run when `p>0` or `p!=0`.

**Approach 1 is always better.**

## Alternative Approach

Another way to write this code where the middle row appears only once:

```python
n = int(input())

x = (n // 2) + 1

# First part
for i in range(x):
    for j in range(1, x - i):
        print(".", end="")

    for j in range(1, (2 * i) + 2):
        print("*", end="")

    print()

# Second part
for i in range(1, (n - x) + 1):
    for j in range(i):
        print(".", end="")

    for j in range(1, n - (2 * i) + 1):
        print("*", end="")

    print()
```

**Note:** The alternative approach uses `n` as the total number of rows and is intended for odd values of `n`. It also prints `.` instead of spaces for indentation.

## Time Complexity

For the first half, each row prints `n-i-1` spaces and `2*i+1` stars.

For the second half, each row prints `p` spaces and `2*n-(2*p+1)` stars.

Both halves execute a quadratic number of printing iterations.

Therefore:

**Time Complexity: O(n²)**

## Auxiliary Space Complexity

Only a fixed number of loop variables and `n` are used. No additional data structures grow with the input.

**Auxiliary Space Complexity: O(1)**
