
# P00010 — Symmetric Right Triangle Star Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00010 |
| Title | Symmetric Right Triangle Star Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/dsa/program-to-print-half-diamond-star-pattern/](https://www.geeksforgeeks.org/dsa/program-to-print-half-diamond-star-pattern/) |

## Problem Statement

Given an integer N, the task is to print a symmetric star triangle pattern consisting of an increasing right-angled triangle followed by a decreasing right-angled triangle.

The first row contains 1 star, the second row contains 2 stars, and so on until the Nth row, which contains N stars.

After reaching N stars, the number of stars decreases by 1 in each subsequent row until the final row contains only 1 star.

The widest row is printed only once.

## Input

A single positive integer `n`, representing the maximum number of stars in a row.

## Output

Print `2 * n - 1` rows.

- The first `n` rows form an increasing right-angled triangle.
- The next `n - 1` rows form a decreasing right-angled triangle.
- The middle row containing `n` stars appears only once.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
*
**
***
****
***
**
*
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
*
**
***
****
*****
****
***
**
*
```

## Constraints

1 <= n <= 100
