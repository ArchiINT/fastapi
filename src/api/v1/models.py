from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    available: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    available: bool | None = None


class Item(ItemBase):
    id: int
