
# P00013 — Notes

## Approach

- Initialize `counter = 0`.
- The outer loop controls the number of rows.
- The inner loop prints `i+1` numbers in each row.
- Increment `counter` before printing each number.
- The counter is not reset after each row, ensuring continuous numbering.

## Time Complexity

The outer loop runs `n` times.

The inner loop executes:

1, 2, 3, ..., n

iterations across successive rows.

Therefore:

T(n) = Σ(i+1), for i = 0 to n-1

Using the arithmetic series formula:

T(n) = n(n+1)/2

Expanding:

T(n) = (n²+n)/2

Therefore:

**Time Complexity: O(n²)**

This is asymptotically optimal in terms of the number of values printed because we must print exactly `n(n+1)/2` numbers.

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `counter`, `i`, `j`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**

## Important Observation

The counter is initialized only once, outside both loops.

This ensures that numbers continue sequentially across rows instead of restarting from 1.

The program prints exactly **n(n+1)/2 numbers**.
