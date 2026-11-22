
# P00017 — Alpha Hill Pattern

## Problem Metadata

| Field | Value |
|---|---|
| Problem ID | P00017 |
| Title | Alpha Hill Pattern |
| Topic | Basics → Pattern Printing |
| Difficulty | Easy |
| Language | Python |
| Problem Link | [https://takeuforward.org/practice/dsa/pattern-17](https://takeuforward.org/practice/dsa/pattern-17) |

## Problem Statement

Given an integer N, the task is to print a centered pyramid-shaped alphabet pattern consisting of uppercase English letters arranged in increasing and then decreasing order.

In this pattern:

- The first row contains only the letter A.
- The second row contains ABA.
- The third row contains ABCBA.
- Each subsequent row introduces one additional letter in alphabetical order.
- After reaching the highest letter in a row, the letters decrease in reverse alphabetical order.
- Leading spaces decrease by 1 with each subsequent row to maintain the pyramid shape.
- The middle character of each row is printed only once.

## Input

A single positive integer `n`, representing the number of rows.

## Output

Print `n` rows.

For each row `i` (0-indexed):

- Print `n-i-1` leading spaces.
- Print `i+1` increasing uppercase letters starting from A.
- Print `i` decreasing uppercase letters, ending at A.

Each row contains exactly `2*i+1` alphabet characters.

## Examples

### Example 1

**Input:**
```text
n = 4
```

**Output:**
```text
   A
  ABA
 ABCBA
ABCDCBA
```

### Example 2

**Input:**
```text
n = 5
```

**Output:**
```text
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```

## Constraints

1 <= n <= 26
