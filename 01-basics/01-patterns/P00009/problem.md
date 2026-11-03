
# P00009 — Diamond Star Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00009 |
| Title | Diamond Star Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://learn.modernagecoders.com/blog/star-pattern-programs-in-python#11-diamond](https://learn.modernagecoders.com/blog/star-pattern-programs-in-python#11-diamond) |

## Problem Statement

Given an integer N, the task is to print a diamond-shaped star pattern consisting of an upright full pyramid followed by an inverted full pyramid.

The first row contains 1 star, the second row contains 3 stars, and so on until the Nth row, which contains (2 * N - 1) stars.

The widest row is printed twice. After that, the number of stars decreases by 2 in each subsequent row until the final row contains only 1 star.

All stars are center-aligned.

## Input

A single positive integer `n`, representing the number of rows in each half of the pattern.

## Output

Print `2 * n` rows.

- The first `n` rows form an upright full pyramid.
- The next `n` rows form an inverted full pyramid.
- The middle row containing `2 * n - 1` stars appears twice.

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
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
```

## Constraints

1 <= n <= 100
