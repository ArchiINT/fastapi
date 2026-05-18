from fastapi import APIRouter
from fastapi.params import Depends
from api.v1.files.dependencies import get_file_repo
from api.v1.files.model import FileShema
from domain.file.repository import AbstractFileRepository

router = APIRouter(prefix="/files")


@router.get("", response_model=list[FileShema])
def list_files( 
    limit: int = 10, 
    offset: int = 0, 
    repo: AbstractFileRepository = Depends(get_file_repo),
):
    files = repo.list(limit=limit, offset=offset)
    return [FileShema(id=i.id, name = i.name, path=i.path) for i in files]
    
@router.get("/{file_id}", response_model=FileShema)
def get_file(file_id: int):
    return {
        "id": file_id,
        "name": "test.txt"
    }
    
