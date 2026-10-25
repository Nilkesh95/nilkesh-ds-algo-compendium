# P00005 — Inverted Right Triangle Star Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00005 |
| Title | Inverted Right Angled Triangle Star Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/dsa/program-to-print-inverted-right-half-pyramid-pattern-star-pattern/](https://www.geeksforgeeks.org/dsa/program-to-print-inverted-right-half-pyramid-pattern-star-pattern/) |

## Problem Statement

Given a positive integer `n`, print an inverted right-angled triangle pattern using the `*` character.

Each row should contain stars, with the count of stars decreasing by one in each successive row. The pattern contains n rows, with the first row containing n stars and each subsequent row containing one fewer star.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row contains exactly `n-i` stars.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
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
*****
****
***
**
*
```

## Constraints:

1 <= n <= 100
