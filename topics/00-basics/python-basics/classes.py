from dataclasses import dataclass, field
from enum import Enum

class Priority(Enum):
    P0 = 0
    P1 = 1
    P2 = 2
    P3 = 3

@dataclass
class Ticket:
    id: int
    subject: str
    priority: Priority = Priority.P2
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "Ticket":
        return cls(
            id=data.get("id"),
            subject=data.get("subject"),
            priority=Priority(data.get("priority",2)),
            tags=data.get("tags",[])
        )

    def __repr__(self) -> str:
        return f"The current ticket attributes are > Ticket ID: {self.id}, Ticket Subject: {self.subject!r}"

ticket_1 = Ticket(id=1, subject="test subject", priority=Priority.P1)
ticket_2 = Ticket.from_dict({
    "id": 123,
    "subject": "ticket subject",
    "priority": 1,
    "tags": ["edho", "onnu"]
})
print(ticket_1)

