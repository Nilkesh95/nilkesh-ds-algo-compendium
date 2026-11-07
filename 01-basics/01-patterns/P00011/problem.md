
# P00011 — Binary Number Triangle Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00011 |
| Title | Binary Number Triangle Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | Not provided |

## Problem Statement

Given an integer N, the task is to print a binary number triangle pattern consisting of 0s and 1s.

The first row contains 1 digit, the second row contains 2 digits, and so on until the Nth row, which contains N digits.

The digits alternate between 0 and 1 within each row.

- Odd-numbered rows start with 1.
- Even-numbered rows start with 0.
- The first row starts with 1.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row (1-indexed) contains exactly `i` binary digits.

The digit printed at each position depends on the parity of the row and column indices.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
1
01
101
0101
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
1
01
101
0101
10101
```

## Constraints

1 <= n <= 100
