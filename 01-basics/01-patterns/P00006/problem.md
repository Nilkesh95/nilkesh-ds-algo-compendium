# P00006 — Inverted Right Triangle Increasing Number Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00006 |
| Title | Inverted Right Angled Triangle Increasing Number Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://www.geeksforgeeks.org/c/c-program-for-printing-inverted-pyramid/](https://www.geeksforgeeks.org/c/c-program-for-printing-inverted-pyramid/) |

## Problem Statement

Given a positive integer `n`, print an inverted right-angled triangle pattern using numbers.

Each row should contain numbers, with the count of numbers decreasing by one in each successive row. The pattern contains n rows, with the first row containing n numbers from 1 to n and each subsequent row containing one fewer number.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row contains exactly `n-i` numbers.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
1234
123
12
1
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
12345
1234
123
12
1
```

## Constraints:

1 <= n <= 100
