from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Item:
    id: int
    title: str


@dataclass(slots=True)
class ItemCreateDTO:
    title: str


@dataclass(slots=True)
class ItemUpdateDTO:
    title: Optional[str] = None