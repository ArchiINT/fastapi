from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from starlette.responses import JSONResponse

from api.v1.item.dependencies import get_item_repo
from api.v1.item.models import ItemSchema, ItemCreateSchema, ItemUpdateSchema
from domain.item.esception import ItemNotFoundError
from domain.item.models import ItemCreateDTO, ItemUpdateDTO
from domain.item.repository import AbstractItemRepository

router = APIRouter(prefix="/item")


@router.get("", response_model=list[ItemSchema])
def list_items(
    limit: int = 100,
    offset: int = 0,
    repo: AbstractItemRepository = Depends(get_item_repo),
):
    items = repo.list(limit=limit, offset=offset)
    return [ItemSchema(id=i.id, title=i.title) for i in items]


@router.get("/{item_id}", response_model=ItemSchema)
async def get_item(item_id: int, repo: AbstractItemRepository = Depends(get_item_repo)):
    try:
        item = repo.get(item_id)
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    return ItemSchema(id=item.id, title=item.title)


@router.post("", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreateSchema, repo: AbstractItemRepository = Depends(get_item_repo)):
    item = repo.create(ItemCreateDTO(title=payload.title))
    return ItemSchema(id=item.id, title=item.title)


@router.patch("/{item_id}", response_model=ItemSchema)
def update_item(
    item_id: int,
    payload: ItemUpdateSchema,
    repo: AbstractItemRepository = Depends(get_item_repo),
):
    try:
        item = repo.update(item_id, ItemUpdateDTO(title=payload.title))
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    return ItemSchema(id=item.id, title=item.title)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, repo: AbstractItemRepository = Depends(get_item_repo)):
    try:
        repo.delete(item_id)
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
