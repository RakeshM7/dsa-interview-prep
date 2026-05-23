# Pattern Problems — Notes

## Why Pattern Problems Matter

Pattern problems are not about memorizing outputs.

They train:

- Nested loop thinking
- Observation skills
- Mathematical derivation
- Space handling
- Symmetry recognition
- Dry-run ability
- Confidence with indices

If someone struggles with patterns, they usually struggle later with:

- Matrix traversal
- Backtracking
- Dynamic Programming tables
- Graph visualization
- Coordinate-based problems

---

## Core Observation

Every pattern problem has:

- Rows
- Columns
- Spaces
- Symbols / numbers
- A repeating rule

The real task is:

> Find the relationship between the current row and what gets printed.

---

## Universal Pattern Template

```ruby
for row in 0...n

  # spaces
  for col in ...
    print " "
  end

  # symbols/numbers
  for col in ...
    print "*"
  end

  puts
end
```

Almost every pattern can be broken into:

1. Left spaces
2. Main content
3. Right spaces (sometimes)

---

## Most Important Insight

### Outer Loop → Rows

```ruby
for row in 0...n
```

Controls:
- Total rows
- Current row number

---

### Inner Loop → What gets printed

```ruby
for col in 0...something
```

Controls:
- Spaces
- Stars
- Numbers
- Characters

---

## Common Pattern Categories

### 1. Fixed Square Patterns

```text
* * * *
* * * *
* * * *
* * * *
```

Observation:
- Rows constant
- Columns constant

Formula:

```text
rows = n
cols = n
```

---

### 2. Increasing Triangle

```text
*
* *
* * *
* * * *
```

Observation:
- Current row determines star count

Formula:

```text
stars = row + 1
```

---

### 3. Decreasing Triangle

```text
* * * *
* * *
* *
*
```

Formula:

```text
stars = n - row
```

---

### 4. Pyramid Patterns

```text
   *
  ***
 *****
*******
```

Observation:
- Spaces decrease
- Stars increase

Formula:

```text
spaces = n - row - 1
stars = 2 * row + 1
```

This is one of the most important formulas in pattern printing.

---

### 5. Reverse Pyramid

```text
*******
 *****
  ***
   *
```

Formula:

```text
spaces = row
stars = 2 * (n - row) - 1
```

---

### 6. Diamond Patterns

Upper half:
- increasing pyramid

Lower half:
- reverse pyramid

Key insight:
- Many hard patterns are just combinations of simpler patterns.

---

### 7. Hollow Patterns

```text
* * * *
*     *
*     *
* * * *
```

Observation:
Print stars only when:

```text
row == 0
row == n - 1
col == 0
col == n - 1
```

This introduces:
- Boundary checking
- Edge detection

---

### 8. Number Patterns

```text
1
1 2
1 2 3
```

Observation:
- Column index often determines value

---

### 9. Symmetric Number Patterns

```text
1 2 3 2 1
```

Observation:
- Increasing + decreasing sequence
- Often split into two loops

---

### 10. Concentric Square Patterns

```text
4 4 4 4 4
4 3 3 3 4
4 3 2 3 4
4 3 3 3 4
4 4 4 4 4
```

Most important insight:

Each cell value depends on:

```text
minimum distance from any boundary
```

Formula:

```text
min(top, left, bottom, right)
```

This is one of the most powerful observation-based problems.

---

## Interview Discussion Points

### Q: Are pattern problems important for interviews?

For freshers:
- Yes, very common.

For experienced engineers:
- Rarely asked directly.

But they reveal:
- Logical clarity
- Loop confidence
- Problem breakdown ability

---

### Q: Why do beginners struggle with patterns?

Because they try to:
- Memorize outputs

Instead of understanding:
- Relationships
- Formulas
- Symmetry
- Spaces

---

### Q: How do you solve any new pattern?

Follow this order:

1. Count rows
2. Count spaces
3. Count symbols
4. Observe symmetry
5. Derive formulas
6. Convert formulas into loops

---

## Traps to Avoid

- Off-by-one loop errors
- Mixing row and column indices
- Printing spaces incorrectly
- Forgetting newline placement
- Hardcoding outputs
- Not separating spaces and symbols logically

---

## Golden Rule

Never start coding immediately.

First:
- Draw the pattern
- Number the rows
- Write formulas

Then code.

---

## Best Way to Practice

Do patterns in this order:

1. Squares
2. Triangles
3. Reverse triangles
4. Number patterns
5. Pyramids
6. Reverse pyramids
7. Diamonds
8. Hollow patterns
9. Symmetric patterns
10. Concentric patterns

---

## Key Takeaway

Pattern problems are not about printing stars.

They teach:

- Problem decomposition
- Observation
- Mathematical thinking
- Visual reasoning
- Loop mastery

Those skills transfer directly into real DSA problems.