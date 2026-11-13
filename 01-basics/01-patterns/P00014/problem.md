
# P00014 — Increasing Alphabet Triangle Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00014 |
| Title | Increasing Alphabet Triangle Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/c/c-program-to-print-character-pyramid-pattern/](https://www.geeksforgeeks.org/c/c-program-to-print-character-pyramid-pattern/) |

## Problem Statement

Given an integer N, the task is to print a right-angled alphabet triangle pattern consisting of consecutive uppercase English letters starting from 'A'.

In this pattern:

- The first row contains the letter A.
- The second row contains the letters AB.
- The third row contains the letters ABC.
- This continues until the Nth row contains N consecutive uppercase letters.
- Every row starts from A.
- No spaces are printed between consecutive letters.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row (1-indexed) contains exactly `i` consecutive uppercase English letters starting from A.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
A
AB
ABC
ABCD
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
A
AB
ABC
ABCD
ABCDE
```

## Constraints

1 <= n <= 26
