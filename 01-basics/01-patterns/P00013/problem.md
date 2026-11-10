
# P00013 — Floyd's Number Triangle Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00013 |
| Title | Floyd's Number Triangle Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/problems/floyds-triangle1222/1](https://www.geeksforgeeks.org/problems/floyds-triangle1222/1) |


## Problem Statement

Given an integer N, the task is to print a triangular number pattern consisting of consecutive natural numbers starting from 1.

In this pattern:

- The first row contains 1 number.
- The second row contains 2 numbers.
- The third row contains 3 numbers.
- This continues until the Nth row contains N numbers.
- Numbers are printed continuously in increasing order without resetting the counter at the beginning of each row.
- No spaces are printed between consecutive numbers.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row (1-indexed) contains exactly `i` consecutive natural numbers.

The numbers start from 1 and continue sequentially across all rows.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
1
23
456
78910
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
1
23
456
78910
1112131415
```

## Constraints

1 <= n <= 100
