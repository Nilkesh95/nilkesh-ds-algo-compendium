# P00007 — Centered Star Full Pyramid Pattern

## Problem Metadata

| Field | Value | 
|---|---|
| Problem ID | P00007 |
| Title | Centered Star Full Pyramid Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/dsa/program-to-print-full-pyramid-pattern-star-pattern/](https://www.geeksforgeeks.org/dsa/program-to-print-full-pyramid-pattern-star-pattern/) |

## Problem Statement


Given an integer N, the task is to print a full pyramid pattern with N rows. 

In this pattern, each row contains an odd number of stars, ranging from 1 star in the first row to (2 * N - 1) stars in the Nth row. All the stars are center-aligned.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row contains exactly `2*i-1` stars.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
   *
  ***
 *****
*******
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
    *
   ***
  *****
 *******
*********
```

## Constraints:

1 <= n <= 100
