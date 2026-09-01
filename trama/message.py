from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

@dataclass
class Message:
    id: UUID
    body: str
    created_at: datetime
    @staticmethod
    def create(body: str):
        return Message(
            id=uuid4(),
            body=body,
            created_at=datetime.now()
        )