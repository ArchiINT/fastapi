from fastapi import APIRouter

router = APIRouter(prefix="/files")


@router.get("", response_model=none)
def list_files(limit: int = 10, offset: int = 0):
    return
    
@router.get("/{file_id}", response_model=none)
def get_file(file_id: int, file_name: str):
    
