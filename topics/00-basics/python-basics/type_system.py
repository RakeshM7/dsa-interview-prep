from typing import Literal, Protocol, TypedDict

def get_ticket_subject(ticket_id: int) -> str | None:
    tickets = {
        1: "Login broken",
        2: "Slow Dashboard"
    }
    return tickets.get(ticket_id)

def get_ticket(ticket_id: int | str) -> dict:
    return {
        "id": ticket_id,
        "subject": "Login broken"
    }

BrowserTypes = Literal["chrome", "safari", "firefox"]
Priority = Literal[1,2,3,4]

class TicketResponse(TypedDict):
    subject: str
    id: int
    priotity: int
    status: int

def create_ticket(subject: str, id: int):
    return {
        "subject": subject,
        "id": id
    }

def parse_ticket(ticket_payload: TicketResponse) -> str | int:
    return ticket_payload["subject"]


def launch_browser(browser_name: BrowserTypes) -> None:
    print(f"Launching {browser_name}")

class Clickable(Protocol):
    def click(self, locator: str) -> None: ...
    def get_text(self, locator: str) -> str: ...

class ChromePage:
    def click(self, locator: str) -> None:
        print(f"element: {locator} is being clicked")
    def get_text(self, locator: str) -> str:
        return "some text"

def run_test(page: Clickable) -> None:
    page.click("#submit")
    text = page.get_text("#result")
    print(f"Got text: {text}")

if __name__ == "__main__":
    # 1. Optional
    print(get_ticket_subject(1))    # Login broken
    print(get_ticket_subject(99))   # None
    # 2. Union
    print(get_ticket(101))
    print(get_ticket("INC-1001"))

    # 3. Literal
    launch_browser("chrome")
    print(create_ticket("API broken", 1))

    # 4. TypedDict
    ticket: TicketResponse = {
        "id": 1,
        "subject": "Login Broken",
        "priority": 1,
        "status": 2
    }
    print(parse_ticket(ticket))

    # 5. Protocol
    page = ChromePage()
    run_test(page)

