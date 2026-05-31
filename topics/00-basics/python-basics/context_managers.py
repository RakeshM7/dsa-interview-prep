# Problem: Managed Browser Session
# Background
# Your Selenium framework creates and destroys a browser for every test. Three things must always happen regardless of whether the test passes or fails:

# Browser launches before the test
# A screenshot is taken if the test fails
# Browser quits after the test — always

# Requirements
# Write a context manager called managed_browser that:

# Takes browser as a parameter — "chrome" or "firefox"
# Yields a simulated driver object {"browser": browser, "session_id": "abc123"}
# If an exception occurs inside the with block — prints [SCREENSHOT] capturing failure screenshot then re-raises
# Always prints [TEARDOWN] quitting browser on exit regardless of pass or fail

# Expected output for a passing test:
# [SETUP] launching chrome
# [TEST] running test on session abc123
# [TEARDOWN] quitting chrome
# Expected output for a failing test:
# [SETUP] launching firefox
# [TEST] running test on session abc123
# [SCREENSHOT] capturing failure screenshot
# [TEARDOWN] quitting firefox
# Constraint
# The exception must propagate to the caller — the test must still fail.

from contextlib import contextmanager

@contextmanager
def managed_browser(browser: str = "chrome"):
    print(f"[SETUP] launching {browser}")
    driver = {
        "browser": browser,
        "session": "abc123"
    }
    try:
        yield driver
    except Exception as e:
        print(f"[SCREENSHOT] Test failed: {e}")
        raise
    finally:
        print(f"[TEARDOWN] quitting {browser}")

print("------[Success case]------")
with managed_browser("chrome") as driver:
    print(f"[TEST]Browser test running on {driver["browser"]}")

print()

print("------[Failure case]------")
try:
    with managed_browser("firefox") as driver:
        print(f"[TEST]Browser test running on {driver["browser"]}")
        raise RuntimeError("element not found")
except RuntimeError as e:
    pass

