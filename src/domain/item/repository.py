from abc import ABC

from domain.item.models import Item, ItemUpdateDTO, ItemCreateDTO
from domain.repository.abstract import AbstractRepository


class AbstractItemRepository(AbstractRepository[Item, int, ItemCreateDTO, ItemUpdateDTO], ABC):
    ...