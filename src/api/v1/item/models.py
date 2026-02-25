from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int | int = None
    title: str

class ItemCreateSchema(ItemSchema):
    ...
class ItemUpdateSchema(ItemSchema):
    ...
class ItemListSchema(BaseModel):
    id: None | int = None
    title: str = 'Title'
