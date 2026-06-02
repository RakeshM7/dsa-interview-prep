class FrameworkException(Exception):
    """Base exception for all framework errors"""
    pass
class ElementNotFoundException(FrameworkException):
    """Element not found"""
    def __init__(self, locator: str, timeout: int):
        self.locator = locator
        self.timeout = timeout
        super().__init__(f"element {locator} not found within {timeout} seconds")
class PageNotLoadedException(FrameworkException):
    """Page not loaded"""
    def __init__(self, url: str, page_name: str):
        self.url = url
        self.page_name = page_name
        super().__init__(f"Page {page_name} failed to load at {url}")
class ApiTimeoutException(FrameworkException):
    """Api timeout exception"""
    def __init__(self, endpoint: str, timeout_ms: int):
        self.endpoint = endpoint
        self.timeout_ms = timeout_ms
        super().__init__(f"API endpoint {endpoint} failed to resolve within {timeout_ms}ms")

class NoSuchElementException(Exception):
    pass

def find_element(locator: str):
    raise NoSuchElementException(f"Element not found {locator}")

def click_element(locator: str, timeout: int=5):
    try:
        find_element(locator)
    except NoSuchElementException as e:
        raise ElementNotFoundException(locator, timeout) from e

try:
    click_element("#submit-btn")
except ElementNotFoundException as e:
    print(f"caught exception: {e}")
    print(f"Rootcause {e.__cause__}")



def fetch_ticket(ticket_id: int) -> dict:
    if ticket_id <= 0:
        raise ApiTimeoutException(f"https://rakesh.freshservice.com/tickets/{ticket_id}", 1_000)
    return {
        "id": ticket_id,
        "subject": f"{ticket_id} subject"
    }

def process_ticket(ticket: dict) -> None:
    print(f"Processing ticket: {ticket}")

print("--------[Valid ticket]--------")
try:
    ticket = fetch_ticket(1)
except ApiTimeoutException as e:
    print(f"Fetch ticket: {e}")
else:
    process_ticket(ticket)
finally:
    print("Cleanup always runs")

print("--------[Invalid ticket]--------")
try:
    ticket = fetch_ticket(-1)
except ApiTimeoutException as e:
    print(f"Fetch ticket: {e}")
else:
    process_ticket(ticket)
finally:
    print("Cleanup always runs")

try:
    ticket = requests.get(ticket_id)
except ConnectionError as e:
    raise ApiTimeoutException
else:
    requests.process(ticket)
finally:
    cleanup()