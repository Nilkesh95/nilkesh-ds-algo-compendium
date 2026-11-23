
# P00017 — Notes

## Approach

For every row `i`, we execute three inner loops:

- **Loop 1:** Prints leading spaces.
- **Loop 2:** Prints alphabets in increasing order.
- **Loop 3:** Prints alphabets in decreasing order.

The third loop starts from `i` and goes down to `1`, ensuring that the middle character is not repeated.

## Time Complexity

For every row `i`, we execute three inner loops.

**Loop 1 — Spaces:**

n-i-1

**Loop 2 — Increasing alphabets:**

i+1

**Loop 3 — Decreasing alphabets:**

i

Total iterations per row:

T(i) = (n-i-1) + (i+1) + i

Simplifying:

T(i) = n+i

Across all `n` rows:

T(n) = Σ(n+i), for i = 0 to n-1

T(n) = n² + n(n-1)/2

T(n) = (3n²-n)/2

Therefore:

**Time Complexity: O(n²)**

This is asymptotically optimal because the pattern contains exactly **n² alphabet characters** across all rows.

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `i`, `j`, `k`, `l`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**

## Important Observation

The third loop can be simplified to:

```python
for l in range(i-1, -1, -1):
    print(chr(65+l), end="")
```

Both versions produce exactly the same output.

The original version is perfectly fine, though.

## Alternative Pattern

A different version of this problem is to print the pattern below:

```text
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
```

### Code

```python
n = int(input())

for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="")

    for k in range(0, 2*i+1):
        print(chr(65+k), end="")

    print()
```

### Observation

Unlike the original pattern, this version prints alphabets only in increasing order.

- The first loop prints the leading spaces.
- The second loop prints `2*i+1` consecutive uppercase letters.
- There is no decreasing alphabet loop.

**Time Complexity: O(n²)**

**Auxiliary Space Complexity: O(1)**
