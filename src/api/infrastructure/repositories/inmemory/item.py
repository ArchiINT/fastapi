from typing import List, Dict

from api.domain.item.esception import ItemNotFoundError
from api.domain.item.models import Item, ItemCreateDTO, ItemUpdateDTO
from api.domain.item.repository import AbstractItemRepository
from api.domain.repository.abstract import TId, TEntity, TCreateDTO

class InMemoryItemRepository(AbstractItemRepository):

    def __init__(self, storage: Dict[int, Item] | None):
        self._storage: Dict[int, Item] = storage.copy() if storage else {} # copy storage if exist, else create void

    def get(self, item_id: int) -> Item:
        try:
            return self._storage[item_id]
        except KeyError:
            raise ItemNotFoundError(item_id)

    def list(self, *, limit: int = 100, offset: int = 0) -> List[Item]:
        pass

    def create(self, dto: ItemCreateDTO) -> Item:
        pass

    def update(self, item_id: int, dto: ItemUpdateDTO) -> Item:
        pass

    def delete(self, item_id: int) -> None:
        pass

