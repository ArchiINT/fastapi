from abc import ABC

from api.domain.item.models import Item, ItemUpdateDTO, ItemCreateDTO
from api.domain.repository.abstract import AbstractRepository


class AbstractItemRepository(AbstractRepository[Item, int, ItemCreateDTO, ItemUpdateDTO], ABC):
    ...