from fastapi import APIRouter
from api.v1.item.views import  router as item_router
router = APIRouter(prefix="/api/v1")

router.include_router(item_router)