
# P00015 — Inverted Alphabet Triangle Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00015 |
| Title | Inverted Alphabet Triangle Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/c/c-program-to-print-character-pyramid-pattern/](https://www.geeksforgeeks.org/c/c-program-to-print-character-pyramid-pattern/) |

## Problem Statement

Given an integer N, the task is to print an inverted right-angled alphabet triangle pattern consisting of consecutive uppercase English letters starting from 'A'.

In this pattern:

- The first row contains N consecutive uppercase letters starting from A.
- The second row contains N-1 letters.
- The number of letters decreases by 1 in each subsequent row.
- The final row contains only the letter A.
- Every row starts from A.
- No spaces are printed between consecutive letters.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row (0-indexed) contains exactly `n-i` consecutive uppercase English letters starting from A.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
ABCD
ABC
AB
A
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
ABCDE
ABCD
ABC
AB
A
```

## Constraints

1 <= n <= 26
