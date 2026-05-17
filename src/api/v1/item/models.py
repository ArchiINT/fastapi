from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    title: str


class ItemCreateSchema(BaseModel):
    title: str


class ItemUpdateSchema(BaseModel):
    title: str | None = None
