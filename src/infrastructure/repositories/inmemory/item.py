from typing import List, Dict, Optional

from domain.item.esception import ItemNotFoundError
from domain.item.models import Item, ItemCreateDTO, ItemUpdateDTO
from domain.item.repository import AbstractItemRepository


class InMemoryItemRepository(AbstractItemRepository):

    def __init__(self, storage: Optional[Dict[int, Item]] = None):
        self._storage: Dict[int, Item] = storage.copy() if storage else {} # copy storage if exist, else create void

    def get(self, item_id: int) -> Item:
        try:
            return self._storage[item_id]
        except KeyError:
            raise ItemNotFoundError(item_id)

    def list(self, *, limit: int = 100, offset: int = 0) -> List[Item]:
        try:
            items = list(self._storage.values())
            return items[offset: offset+ limit]
        except KeyError:
            raise {"message":"Get List Error"}

    def create(self, dto: ItemCreateDTO) -> Item:
        if self._storage:
            last_id = list(self._storage.keys())[-1]
        else:
            last_id = 0

        next_id = last_id + 1

        item = Item(
            id=next_id,
            title=dto.title
        )
        self._storage[next_id] = item
        return item


    def update(self, item_id: int, dto: ItemUpdateDTO) -> Item:
        if item_id not in self._storage:
            return ItemNotFoundError(item_id)

        existing = self._storage[item_id]
        updated = Item(
            id = existing.id,
            title= dto.title if dto.title is not None else existing.title
        )

        self._storage[item_id] = updated
        return updated

    def delete(self, item_id: int) -> None:
        if item_id not in self._storage:
            return ItemNotFoundError(item_id)
        del self._storage[item_id]

