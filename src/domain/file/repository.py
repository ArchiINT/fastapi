from abc import ABC
from domain.repository.abstract import AbstractRepository
from src.domain.file.models import File, FileCreateDTO, FileUpdateDTO


class AbstractFileRepository(AbstractRepository[File, int, FileCreateDTO, FileUpdateDTO], ABC):
    ...