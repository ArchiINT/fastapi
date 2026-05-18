from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class File():
    id: int
    name: str
    path: str

@dataclass(slots=True)
class FileCreateDTO():
    name: str

@dataclass(slots=True)
class FileUpdateDTO():
    name: Optional[str] = None