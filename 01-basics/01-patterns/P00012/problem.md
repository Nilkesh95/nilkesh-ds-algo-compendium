
# P00012 — Number Crown Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00012 |
| Title | Number Crown Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/problems/double-triangle-pattern-1662664259/1](https://www.geeksforgeeks.org/problems/double-triangle-pattern-1662664259/1) |


## Problem Statement

Given an integer N, the task is to print a symmetric number crown pattern consisting of increasing and decreasing sequences of numbers separated by spaces.

In this pattern:

- The left half contains numbers in increasing order from 1 to the current row number.
- The right half contains numbers in decreasing order from the current row number to 1.
- The number of spaces between the two halves decreases by 2 with each subsequent row.
- In the final row, both sequences meet without any spaces between them.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows.

For each row `i` (0-indexed):

- Print numbers from `1` to `i+1`.
- Print `2*n - 2*(i+1)` spaces.
- Print numbers from `i+1` down to `1`.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
1      1
12    21
123  321
12344321
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
1        1
12      21
123    321
1234  4321
1234554321
```

## Constraints

1 <= n <= 100
