# Complexity Cheatsheet

## Big-O Quick Reference

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | HashMap get, array index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop, HashMap build |
| O(n log n) | Linearithmic | Merge sort, Arrays.sort |
| O(n²) | Quadratic | Nested loops, brute force pairs |
| O(2ⁿ) | Exponential | Recursive subsets |
| O(n!) | Factorial | Permutations |

---

## Data Structure Complexities

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| LinkedList | O(n) | O(n) | O(1) | O(1) |
| HashMap | — | O(1) avg | O(1) avg | O(1) avg |
| HashSet | — | O(1) avg | O(1) avg | O(1) avg |
| TreeMap | — | O(log n) | O(log n) | O(log n) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| MinHeap/MaxHeap | O(1) peek | O(n) | O(log n) | O(log n) |

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

---

## Pattern → Typical Complexity

| Pattern | Time | Space |
|---------|------|-------|
| HashMap / HashSet | O(n) | O(n) |
| Two Pointers (sorted) | O(n) | O(1) |
| Sliding Window | O(n) | O(1)–O(k) |
| Binary Search | O(log n) | O(1) |
| DFS / BFS | O(V + E) | O(V) |
| DP (1D) | O(n) | O(n) or O(1) |
| DP (2D) | O(n × m) | O(n × m) or O(m) |
