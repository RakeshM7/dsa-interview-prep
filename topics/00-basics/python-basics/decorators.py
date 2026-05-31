import functools
import time
import random


def retry(max_attempts: int = 3, poll_duration: float = 0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"[RETRY] Attempting {attempt+1}/{max_attempts} times. Exception: {e}")
                time.sleep(poll_duration)
        return wrapper
    return decorator

@retry(max_attempts=5, poll_duration=0.5)
def fetch_tickets(ticket_id: int) -> dict:
    """Fetching tickets"""
    if random.random() < 0.7:
        raise ConnectionError(f"Timeout error: {ticket_id}")
    return {
        "id": ticket_id,
        "subject": "Ticket Subject"
    }

result = fetch_tickets(ticket_id=100)

print(result)


# check if meta data is preserved
print(fetch_tickets.__name__)
print(fetch_tickets.__doc__)
print(fetch_tickets.__annotations__)

print("------------------------------------------------------------------------------------------------------------------------")

# Decorators test

# Problem: Execution Timer Decorator
# Background
# - Your test framework runs 500 Selenium tests overnight. 
# - The next morning the CI report shows the suite took 4 hours — but you have no idea which individual tests are slow.
# - You need a decorator that measures and logs how long any function takes to execute.

# Requirements
# 1. Basic timer
# Write a decorator called timer that:

# - Records the time before the function runs
# - Records the time after the function runs
# - Prints the elapsed time in milliseconds
# - Works on any function regardless of its signature
# - Preserves the original function's name and docstring

# Expected output:
# [TIMER] fetch_ticket took 120.45ms
# [TIMER] create_ticket took 340.12ms

# 2. Threshold alert
# Extend the decorator to accept a threshold_ms argument. If the function takes longer than the threshold, print a warning:

# [TIMER] fetch_ticket took 120.45ms
# [WARN]  fetch_ticket exceeded threshold (100ms) — actual: 120.45ms

# 3. Return value must pass through
# The decorated function must still return its original value. This must work:

# result = fetch_ticket(101)
# print(result)   # {"id": 101, "subject": "Login broken"}

# Test your decorator against these functions

# import time

# def fetch_ticket(ticket_id: int) -> dict:
#     """Fetches a single ticket"""
#     time.sleep(0.12)   # simulates 120ms API call
#     return {"id": ticket_id, "subject": "Login broken"}

# def create_ticket(subject: str, priority: int) -> dict:
#     """Creates a new ticket"""
#     time.sleep(0.35)   # simulates 350ms API call
#     return {"subject": subject, "priority": priority}

# Constraints

#     - Do not use any external libraries except functools and time
#     - Must use the three-layer structure — decorator factory, decorator, wrapper
#     - Must use @functools.wraps
#     - threshold_ms must have a sensible default if not provided


import functools
import time


def timer(threshold_ms: int = 100):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_ms = (end_time - start_time) * 1000

            print(f"[TIMER] {func.__name__} took {elapsed_ms:.2f}ms")
            if threshold_ms < elapsed_ms:
                print(
                    f"[WARN] {func.__name__} exceeded threshold({threshold_ms}) "
                    f"- actual: {elapsed_ms:.2f}ms"
                )

            return result

        return wrapper

    return decorator

@timer(threshold_ms=100)
def fetch_ticket(ticket_id: int) -> dict:
    """Fetches a single ticket"""
    time.sleep(0.12)
    return {
        "id": ticket_id,
        "subject": "Login broken"
    }

@timer()
def create_ticket(subject: str, priority: int) -> dict:
    """Creates a new ticket"""
    time.sleep(0.35)
    return {
        "subject": subject,
        "priority": priority
    }

print(fetch_ticket(1001))
print(create_ticket(subject="Some subject", priority=1))
