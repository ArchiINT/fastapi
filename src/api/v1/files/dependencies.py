

from infrastructure.repositories.filesystem.file import SystemFileRepository


file = SystemFileRepository()

def get_file_repo():
    return file