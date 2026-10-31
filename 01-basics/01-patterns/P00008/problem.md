# P00008 — Inverted Full Pyramid Star Pattern

## Problem Metadata

| Field | Value | 
|---|---|
| Problem ID | P00008 |
| Title | Inverted Full Pyramid Star Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/dsa/program-to-print-inverted-full-pyramid-pattern-star-pattern/](https://www.geeksforgeeks.org/dsa/program-to-print-inverted-full-pyramid-pattern-star-pattern/) |

## Problem Statement


Given an integer N, the task is to print an inverted full pyramid pattern with N rows. 

In this pattern, the first row has (2 * N - 1) stars, the second row has (2 * N - 3) stars, and so on until the Nth row, which has only 1 star. All stars are center-aligned.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row contains exactly `2*N-2*i-1` stars.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
*******
 *****
  ***
   *
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
**********
 *******
  *****
   ***
    *
```

## Constraints:

1 <= n <= 100
