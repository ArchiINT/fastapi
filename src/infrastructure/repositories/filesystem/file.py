from typing import Dict, Optional
from domain.file.models import File, FileCreateDTO, FileUpdateDTO
from domain.file.repository import AbstractFileRepository
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(base_dir, "uploads")
class SystemFileRepository(AbstractFileRepository):
    def __init__(self):
        self._storage = read_files()

    def get(self, file_id: int):
        return self._storage.get(file_id)

    def list(self, *, limit: int = 100, offset: int = 0) -> List[File]:
        try:
            files = list(self._storage.values())
            return files[offset:offset+limit]
        except KeyError:
            raise {"message":"Get List Error"}

    def create(self, dto: FileCreateDTO) -> File:
        if self._storage:
            last_id = list(self._storage.keys())[-1]
        else:
            last_id = 0

        next_id = last_id + 1

        file = File(
            id=next_id,
            name=dto.name,
            path=upload_dir+'/'+dto.name
        )
        self._storage[next_id] = file
        return file

        
    def update(self, file_id, dto: FileUpdateDTO) -> File:
        if file_id not in self._storage:
            raise Exception(f"file {file_id} not found")
        existing = self._storage[file_id]
        updated = File(
            id=existing.id,
            name= dto.name if dto.name is not None else existing.name,
            path=existing.path,
        )
        return updated

        
    def delete(self, file_id) -> None:
        if file_id not in self._storage:
            raise Exception(f"file {file_id} not found")




def read_files():

    # Filtering only the files.
    storage: Dict[int, File] = {}
    files = [
            f for f in os.listdir(upload_dir)
            if os.path.isfile(os.path.join(upload_dir, f))
        ]
    for index, filename in enumerate(files, start=1):
        file = File(
            id=index,
            name=filename,
            path=upload_dir+'/'+filename
        )
        storage[index] = file
    return storage
        
    