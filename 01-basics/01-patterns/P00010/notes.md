
# P00010 — Notes

## Approach

The pattern is divided into two halves:

- The first half prints an increasing number of stars from 1 to n.
- The second half prints a decreasing number of stars from n-1 to 1.

The second outer loop starts from `p=1` instead of `p=0` to avoid repeating the middle row containing n stars.

## Time Complexity

**First half:**

T1(n) = 1 + 2 + 3 + ... + n

T1(n) = n(n+1)/2

**Second half:**

T2(n) = (n-1) + (n-2) + ... + 1

T2(n) = n(n-1)/2

**Total:**

T(n) = n(n+1)/2 + n(n-1)/2

T(n) = (n²+n+n²-n)/2

T(n) = 2n²/2

T(n) = n²

**Time Complexity: O(n²)**

The program prints exactly **n² stars**.

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `i`, `j`, `p`, `l`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**
