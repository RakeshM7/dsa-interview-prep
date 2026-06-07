def is_anagram_brute(s: str, t: str) -> bool:
    if not s:
        return True
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def is_anagram_optimal(s: str, t: str) -> bool:
    if not s:
        return True
    if len(s) != len(t):
        return False

    tracker = {}
    for char in s:
        tracker[char] = tracker.get(char, 0) + 1

    for char in t:
        tracker[char] = tracker.get(char, 0) - 1

    return not any(tracker.values())



test_cases = [
    {"s": "anagram", "t": "nagaram", "expected": True},
    {"s": "rat", "t": "car", "expected": False},
    {"s": "abc", "t": "ab", "expected": False},
    {"s": "", "t": "", "expected": True},
    {"s": "a", "t": "a", "expected": True},
    {"s": "a", "t": "b", "expected": False},
    {"s": "Aa", "t": "aA", "expected": True},
    {"s": "Listen", "t": "Silent", "expected": False},
    {"s": "déjà", "t": "jàdé", "expected": True},
    {"s": "你好界", "t": "界好你", "expected": True},
    {"s": "你好", "t": "你号", "expected": False},
    {"s": "aab", "t": "abb", "expected": False}
]


def run_tests(solution):
    print(f"\nTesting {solution.__name__}")

    for test_number, test_case in enumerate(test_cases, start=1):
        actual = solution(test_case["s"], test_case["t"])
        status = "PASS" if actual == test_case["expected"] else "FAIL"
        print(
            f"Test {test_number}: {status} | "
            f"s={test_case['s']!r}, t={test_case['t']!r} | "
            f"expected={test_case['expected']} | actual={actual}"
        )


if __name__ == "__main__":
    run_tests(is_anagram_brute)
    run_tests(is_anagram_optimal)
