"""
Contains Duplicate
LeetCode #217 | Difficulty: Easy | Topic: Arrays & Hashing
"""

# ── Approach 1: Brute Force ───────────────────────────────────────────────────
# Compare every pair of indices.
# Time:  O(n²)
# Space: O(1)
def contains_duplicate_brute(nums: list[int]) -> bool:
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# ── Approach 2: Hash Set (Optimal) ────────────────────────────────────────────
# Single pass. If we've seen the value before, we have a duplicate.
# Otherwise, add it to the set.
#
# Time:  O(n)   — single pass
# Space: O(n)   — set stores up to n elements
def contains_duplicate(nums: list[int]) -> bool:
    tracker = set()
    for i in range(0, len(nums)):
        if nums[i] in tracker:
            return True
        else:
            tracker.add(nums[i])
    return False

def contains_duplicate_map(nums: list[int]) -> bool:
    tracker = {}
    for i in range(0, len(nums)):
        if nums[i] in tracker:
            return True
        else:
            tracker[nums[i]] = 0
    return False







# ── Test Cases ─────────────────────────────────────────────────────────────────
test_cases = [
    {"nums": [1, 2, 3, 1], "expected": True},
    {"nums": [1, 2, 3, 4], "expected": False},
    {"nums": [1, 1], "expected": True},
    {"nums": [], "expected": False},
    {"nums": [7], "expected": False},
    {"nums": [0, 0], "expected": True},
    {"nums": [-1, -2, -3, -1], "expected": True},
    {"nums": [-1, 0, 1, 2], "expected": False},
    {"nums": [5, 4, 3, 2, 1, 5], "expected": True},
    {"nums": [2, 2, 2, 2], "expected": True},
    {"nums": [1, 2, 3, 4, 4, 5], "expected": True},
    {"nums": [1000000000, -1000000000], "expected": False},
]


# ── Driver ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    solution = contains_duplicate

    for test_number, test_case in enumerate(test_cases, start=1):
        actual = solution(test_case["nums"])
        status = "PASS" if actual == test_case["expected"] else "FAIL"
        print(
            f"Test {test_number}: {status} | "
            f"input={test_case['nums']} | "
            f"expected={test_case['expected']} | actual={actual}"
        )
