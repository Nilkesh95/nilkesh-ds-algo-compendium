
# P00016 — Repeated Alphabet Triangle Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00016 |
| Title | Repeated Alphabet Triangle Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://takeuforward.org/practice/dsa/pattern-16](https://takeuforward.org/practice/dsa/pattern-16) |

## Problem Statement

Given an integer N, the task is to print a right-angled alphabet triangle pattern consisting of repeated uppercase English letters.

In this pattern:

- The first row contains the letter A once.
- The second row contains the letter B twice.
- The third row contains the letter C three times.
- This continues until the Nth row contains the Nth uppercase English letter repeated N times.
- Each row contains only one distinct letter.
- No spaces are printed between consecutive letters.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows, where the `i`-th row (0-indexed) contains exactly `i+1` occurrences of the character `chr(65+i)`.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
A
BB
CCC
DDDD
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
A
BB
CCC
DDDD
EEEEE
```

## Constraints

1 <= n <= 26
