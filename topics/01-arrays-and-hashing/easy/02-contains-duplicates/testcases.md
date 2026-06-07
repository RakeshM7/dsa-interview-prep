# Contains Duplicate - Test Cases

Use these cases to test your implementation. The solution files are intentionally
not modified here.

| # | Input | Expected | Purpose |
|---|-------|----------|---------|
| 1 | `[1, 2, 3, 1]` | `true` | Duplicate at the end |
| 2 | `[1, 2, 3, 4]` | `false` | All values are unique |
| 3 | `[1, 1]` | `true` | Smallest duplicate case |
| 4 | `[]` | `false` | Empty array |
| 5 | `[7]` | `false` | Single value |
| 6 | `[0, 0]` | `true` | Duplicate zero |
| 7 | `[-1, -2, -3, -1]` | `true` | Duplicate negative value |
| 8 | `[-1, 0, 1, 2]` | `false` | Unique mixed-sign values |
| 9 | `[5, 4, 3, 2, 1, 5]` | `true` | Duplicate values far apart |
| 10 | `[2, 2, 2, 2]` | `true` | Same value repeated many times |
| 11 | `[1, 2, 3, 4, 4, 5]` | `true` | Adjacent duplicate |
| 12 | `[1000000000, -1000000000]` | `false` | Constraint boundary values |

## Copy-Friendly Data

```text
nums = [1, 2, 3, 1]                     expected = true
nums = [1, 2, 3, 4]                     expected = false
nums = [1, 1]                           expected = true
nums = []                               expected = false
nums = [7]                              expected = false
nums = [0, 0]                           expected = true
nums = [-1, -2, -3, -1]                expected = true
nums = [-1, 0, 1, 2]                   expected = false
nums = [5, 4, 3, 2, 1, 5]             expected = true
nums = [2, 2, 2, 2]                    expected = true
nums = [1, 2, 3, 4, 4, 5]             expected = true
nums = [1000000000, -1000000000]       expected = false
```
