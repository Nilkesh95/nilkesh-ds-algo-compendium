
# P00011 — Notes

## Approach

The pattern consists of binary digits (0 and 1), where the output depends on the parity of the row index `i` and column index `j`.

| Row (i) | Column (j) | Output |
|---|---|---|
| Even | Even | 1 |
| Even | Odd | 0 |
| Odd | Even | 0 |
| Odd | Odd | 1 |

**Important observation: Whenever i and j have the same parity, we print 1. Otherwise, we print 0.**

This observation allows us to simplify the code considerably.

## Better Approach

```python
n = int(input())

for i in range(0, n):
    for j in range(0, i+1):
        if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):
            print(1, end="")
        else:
            print(0, end="")
    print()
```

## More Elegant Approach

```python
n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(1 if (i + j) % 2 == 0 else 0, end="")
    print()
```

### Why does this work?

Because we have observed that:

- When both `i` and `j` are even, the output is 1.
- When both `i` and `j` are odd, the output is 1.

And we know that:

- Even + Even = Even
- Odd + Odd = Even
- Any other combination of even and odd gives an odd number.

Hence, if `i+j` is even, our output should be 1; otherwise, 0.

## Time Complexity

The outer loop runs `n` times, and the inner loop runs `i+1` times for each row.

T(n) = 1 + 2 + 3 + ... + n

T(n) = n(n+1)/2

T(n) = (n²+n)/2

**Time Complexity: O(n²)**

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `i`, `j`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**
