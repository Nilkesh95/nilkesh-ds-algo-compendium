
## Approach

There's **one important observation** about this pattern:

The middle row:

```text
*********
*********
```

appears twice.

That's because:

- The first outer loop prints the complete upright pyramid, including its widest row.
- The second outer loop starts by printing the widest row again.

**If the question expects the middle row twice, the code is 100% correct.**
