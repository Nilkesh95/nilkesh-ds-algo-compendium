
# P00012 — Notes

## Approach

I was trying to break down this problem into smaller problems.

### First Part — Increasing Number Triangle

```python
for i in range(0, n):
    for j in range(0, i+1):
        print(j+1, end="")
    print()
```

**Output for n = 5:**

```text
1
12
123
1234
12345
```

### Second Part — Inverted Right Triangle

```python
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="")

    for k in range(i+1, 0, -1):
        print(k, end="")

    print()
```

**Output for n = 5:**

```text
    1
   21
  321
 4321
54321
```

Using the above codes, I was trying to understand how to print the inverted right triangle pattern to see if I could get some help.

And I did get the idea of looping in reverse order from `i+1` to `0` (exclusive).

### Final Approach

```python
for i in range(0, n):
    for j in range(0, i+1):
        print(j+1, end="")

    for k in range(0, 2*n-(2*(i+1))):
        print(" ", end="")

    for l in range(i+1, 0, -1):
        print(l, end="")

    print()
```

## Time Complexity

For every row `i`, we print:

- Increasing numbers: `i+1`
- Spaces: `2n-2(i+1)`
- Decreasing numbers: `i+1`

**Total:**

T(i) = (i+1) + 2n - 2(i+1) + (i+1)

Everything except `2n` cancels out!

T(i) = 2n

**This means every row prints exactly 2n characters, regardless of the row index (for n <= 9).**

Since there are `n` rows:

T(n) = n * 2n

T(n) = 2n²

**Time Complexity: O(n²)**

This counts the character-printing iterations, excluding the newline calls.

## Auxiliary Space Complexity

Only a fixed number of variables (`n`, `i`, `j`, `k`, `l`) are used.

No additional data structures are created.

**Auxiliary Space Complexity: O(1)**

## Important Observation

**One subtle consideration:**

This code assumes that every printed number occupies one character.

For `n <= 9`, this works perfectly.

However, for `n >= 10`, numbers such as 10, 11, and 12 occupy multiple characters, so the visual alignment will change.

For example, for `n = 15`, the output will look something like this:

```text
1                            1
12                          21
123                        321
1234                      4321
12345                    54321
123456                  654321
1234567                7654321
12345678              87654321
123456789            987654321
12345678910          10987654321
1234567891011        1110987654321
123456789101112      121110987654321
12345678910111213    13121110987654321
1234567891011121314  1413121110987654321
123456789101112131415151413121110987654321
```

For typical pattern-printing exercises where `n <= 9`, the solution is perfectly fine.
