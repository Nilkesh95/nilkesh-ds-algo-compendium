
# P00014 — Notes

## Approach

- The outer loop controls the number of rows.
- The inner loop prints `i+1` characters in each row.
- Every row starts from the letter `A`.
- `chr(65+j)` converts the corresponding numeric code point into an uppercase letter.
- The value of `j` starts from 0 in every row, ensuring that each row begins with `A`.

## Important Concepts — ord() and chr()

In Python, there are two built-in functions for converting a character to its decimal equivalent and vice versa.

### 1. Character to Decimal — ord()

To convert a character (like 'a', 'b', or '1') into its decimal Unicode code point, we use the `ord()` function (short for ordinal).

```python
print(ord('a'))  # Output: 97
print(ord('A'))  # Output: 65
print(ord('0'))  # Output: 48
```

**Syntax:**

```python
ord(character)
```

- Accepts a single Unicode character.
- Returns its corresponding integer Unicode code point.
- For standard English letters and digits, these values also match their ASCII codes.

### 2. Decimal to Character — chr()

To do the exact reverse — converting a decimal Unicode code point back to its corresponding character — we use the `chr()` function (short for character).

```python
print(chr(97))    # Output: a
print(chr(65))    # Output: A
print(chr(2384))  # Output: ॐ
```

**Syntax:**

```python
chr(integer)
```

- Accepts an integer representing a valid Unicode code point.
- Returns the corresponding character.
- Uppercase English letters range from `chr(65)` to `chr(90)`.

### Relationship Between ord() and chr()

These functions perform reverse operations.

```python
print(ord('A'))       # 65
print(chr(65))        # A

print(chr(ord('B')))  # B
print(ord(chr(67)))   # 67
```

**Important Observation:**

Since the uppercase English alphabet starts at code point 65:

- `chr(65+0)` = A
- `chr(65+1)` = B
- `chr(65+2)` = C
- `chr(65+3)` = D
- `chr(65+4)` = E

Therefore, `chr(65+j)` allows us to print consecutive uppercase letters using the loop variable `j`.

## Time Complexity

The outer loop runs `n` times.

The inner loop executes:

1, 2, 3, ..., n

iterations across successive rows.

Therefore:

T(n) = Σ(i+1), for i = 0 to n-1

Using the arithmetic series formula:

T(n) = n(n+1)/2

Expanding:

T(n) = (n²+n)/2

Therefore:

**Time Complexity: O(n²)**

The program prints exactly **n(n+1)/2 characters**.

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `i`, `j`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**
