from genericpath import isfile
from typing import Dict, Optional
from src.domain.file.models import File
from src.domain.file.repository import AbstractFileRepository

class SystemFileRepository(AbstractFileRepository):
    def __init__(self, storage: Optional[Dict[int, File]] = None):
        self._storage: Dict[int, File] = storage.copy() if storage else {}

    def get(self, file_id: int):
        return 





def read_files():
    import os
    Direc = "uploads/"
    files = os.listdir(Direc)
    # Filtering only the files.
    files = [f for f in files if os.path.isfile(Direc+'/'+f)]
    print(*files, sep="\n")