
# P00015 — Notes

## Approach

- The outer loop runs `n` times and controls the number of rows.
- The inner loop runs `n-i` times for each row.
- The number of characters decreases by 1 after every row.
- `chr(65+j)` converts the corresponding Unicode code point into an uppercase English letter.
- Since `j` starts from 0 in every row, each row begins with `A`.

## Important Observation

This pattern is the reverse of **P00014 — Alphabet Triangle Pattern**.

In Pattern 14, the inner loop runs:

```python
for j in range(0, i+1):
```

In Pattern 15, the inner loop runs:

```python
for j in range(0, n-i):
```

The only difference is the number of iterations performed by the inner loop.

- Pattern 14: `1, 2, 3, ..., n`
- Pattern 15: `n, n-1, n-2, ..., 1`

Both patterns use `chr(65+j)` to print uppercase English letters.

## Time Complexity

The outer loop runs `n` times.

The inner loop executes:

n, n-1, n-2, ..., 1

iterations across successive rows.

Therefore:

T(n) = Σ(n-i), for i = 0 to n-1

Using the arithmetic series formula:

T(n) = n + (n-1) + (n-2) + ... + 1

T(n) = n(n+1)/2

Expanding:

T(n) = (n²+n)/2

Therefore:

**Time Complexity: O(n²)**

The program prints exactly **n(n+1)/2 characters**.

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `i`, `j`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**
