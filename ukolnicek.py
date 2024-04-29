from dataclasses import dataclass
import datetime

@dataclass
class Task:
    description: str
    timestamp: datetime