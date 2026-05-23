# Pattern Problems

**Difficulty:** Easy → Medium  
**Topic:** Basics / Pattern Printing / Nested Loops  
**Source:** Striver A2Z DSA Sheet  
**Interview Frequency:** Foundational

---

## Purpose of Pattern Problems

Pattern problems are not asked frequently in real interviews for experienced engineers.

However, they are extremely important for building:

- Nested loop understanding
- Row-column visualization
- Observation skills
- Symmetry recognition
- Mathematical thinking
- Loop boundary confidence
- Dry-run ability

These problems train your brain to think in terms of:

- Rows
- Columns
- Spaces
- Character placement
- Formula derivation from indices

Mastering patterns makes later DSA topics easier:

- Matrices
- Recursion
- Backtracking
- Dynamic Programming visualizations
- Graph traversal intuition

---

## Core Mental Model

Almost every pattern problem follows this structure:

```ruby
for row in 0...n
  for col in ...
    print something
  end
  puts
end
```

The outer loop controls:
- Number of rows

The inner loop controls:
- Number of columns
- Spaces
- Symbols
- Numbers

The real skill is identifying:

- What changes per row?
- What stays constant?
- How spaces behave?
- Whether symmetry exists?

---

## Types of Pattern Problems

### 1. Square Patterns

```text
* * * *
* * * *
* * * *
* * * *
```

Concepts:
- Constant rows and columns
- Fixed nested loops

---

### 2. Increasing Triangle Patterns

```text
*
* *
* * *
* * * *
```

Concepts:
- Inner loop depends on row index

---

### 3. Decreasing Triangle Patterns

```text
* * * *
* * *
* *
*
```

Concepts:
- Reverse loop relationships

---

### 4. Number Patterns

```text
1
1 2
1 2 3
1 2 3 4
```

Concepts:
- Column-based printing
- Number derivation from indices

---

### 5. Pyramid Patterns

```text
   *
  ***
 *****
*******
```

Concepts:
- Spaces + stars
- Symmetry
- Left/right balancing

---

### 6. Diamond Patterns

```text
   *
  ***
 *****
  ***
   *
```

Concepts:
- Combining increasing + decreasing pyramids

---

### 7. Hollow Patterns

```text
* * * *
*     *
*     *
* * * *
```

Concepts:
- Boundary conditions
- Edge detection

---

### 8. Concentric Patterns

```text
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
```

Concepts:
- Distance from boundaries
- Mathematical observations

---

## Common Beginner Mistakes

- Confusing rows and columns
- Incorrect space calculations
- Off-by-one loop errors
- Mixing `i` and `j`
- Forgetting symmetry rules
- Hardcoding instead of deriving logic

---

## Recommended Approach

For every pattern:

1. Draw row numbers
2. Observe spaces separately
3. Observe symbols separately
4. Derive formulas
5. Convert observations into loops
6. Dry run manually

---

## Pattern Difficulty Progression

Recommended learning order:

1. Square patterns
2. Triangle patterns
3. Reverse triangles
4. Number patterns
5. Pyramids
6. Reverse pyramids
7. Diamonds
8. Hollow patterns
9. Symmetric patterns
10. Concentric square patterns

---

## Important Insight

Do not memorize patterns.

If you memorize:
- You will forget quickly.

If you understand:
- Rows
- Columns
- Spaces
- Symmetry
- Formula derivation

Then you can solve almost any new pattern problem.

---

## Recommended Practice Source

- Striver A2Z DSA Sheet
- 22 Must-Do Pattern Problems

---

## Folder Structure

```text
topics/00-basics/patterns/
  problem.md      ← overview and concepts
  notes.md        ← observations, tricks, interview insights
```