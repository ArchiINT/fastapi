from fastapi import FastAPI, APIRouter, status
from fastapi.params import Depends
from starlette.responses import JSONResponse

from api.v1.item.dependencies import get_item_repo
from api.v1.item.models import ItemSchema, ItemCreateSchema
from domain.item.esception import ItemNotFoundError
from domain.item.models import ItemCreateDTO
from domain.item.repository import AbstractItemRepository

router = APIRouter(prefix="/item")



@router.get("/{item_id}")
async def get_item(item_id: int, repo: AbstractItemRepository = Depends(get_item_repo)):
    try:
        item = repo.get(item_id)
    except ItemNotFoundError as exc:
        print(exc)
        return JSONResponse(content={}, status_code= status.HTTP_404_NOT_FOUND)

    item_schema = ItemSchema(
        id = item.id,
        title = item.title
    )

    return JSONResponse(content=item_schema.model_dump(), status_code=status.HTTP_200_OK)

@router.post("")
def create_item(payload: ItemCreateSchema, repo: AbstractItemRepository = Depends(get_item_repo)) -> JSONResponse:
    dto = ItemCreateDTO(
        title = payload.title
    )
    item = repo.create(dto)

    item_schema = ItemSchema(
        id=item.id,
        title=item.title
    )
    return JSONResponse(content=item_schema.model_dump(), status_code=status.HTTP_200_OK)
