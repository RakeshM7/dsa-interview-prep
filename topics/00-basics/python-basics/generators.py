# Problem: Test Data Generator
# Background
# Your load test needs to create 10,000 tickets in Freshservice. Loading all 10,000 into memory at once crashes the CI machine. You need a generator that produces one ticket at a time.
# Requirements
# Write a generator function called generate_test_tickets that:

# Takes count and priority as parameters
# Yields one ticket dict at a time with keys: id, subject, priority, email
# id starts at 1, not 0
# email format: testuser{id}@freshservice.com
# subject format: Auto ticket {id}

def generate_test_tickets(no_of_tickets: int, priority: str="high"):
    """ Return test tickets """
    for id in range(1,no_of_tickets+1):
        yield {
            "subject": f"Auto ticket {id}",
            "priority": priority,
            "email": f"testuser{id}@freshservice.com",
            "id": id
        }
tickets = generate_test_tickets(5)

count = 0
for ticket in generate_test_tickets(10_000):
    print(ticket)
    count += 1
    if count == 5:
        break

import sys
list_tickets = [{"subject": f"Auto ticket {id}", "priority": "high", "email": f"testuser{id}@freshservice.com", "id": id} for id in range(10_000)]      # list comprehension version
gen_tickets  = generate_test_tickets(10_000)  # generator version

print(sys.getsizeof(list_tickets))
print(sys.getsizeof(gen_tickets))