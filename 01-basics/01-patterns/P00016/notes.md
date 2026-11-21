
# P00016 — Notes

## Approach

- The outer loop runs `n` times and controls the number of rows.
- The inner loop runs `i+1` times for each row.
- The number of characters increases by 1 after every row.
- `chr(65+i)` converts the corresponding Unicode code point into an uppercase English letter.
- Since `i` remains constant throughout each iteration of the inner loop, the same character is printed repeatedly in that row.

## Important Observation

This pattern is similar to **P00014 — Alphabet Triangle Pattern**.

In Pattern 14, we used:

```python
print(chr(65+j), end="")
```

In Pattern 16, we use:

```python
print(chr(65+i), end="")
```

**The only difference is the variable used inside `chr()`.**

- Pattern 14 uses `j` (column index), so the character changes within each row.
- Pattern 16 uses `i` (row index), so the character remains the same throughout a row and changes only when moving to the next row.

For example:

| Row (i) | Character | Repetitions | Output |
|---|---|---|---|
| 0 | chr(65+0) = A | 1 | A |
| 1 | chr(65+1) = B | 2 | BB |
| 2 | chr(65+2) = C | 3 | CCC |
| 3 | chr(65+3) = D | 4 | DDDD |
| 4 | chr(65+4) = E | 5 | EEEEE |

## Time Complexity

The outer loop runs `n` times.

The inner loop executes:

1, 2, 3, ..., n

iterations across successive rows.

Therefore:

T(n) = Σ(i+1), for i = 0 to n-1

Using the arithmetic series formula:

T(n) = 1 + 2 + 3 + ... + n

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
