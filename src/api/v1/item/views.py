from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/item")

@router.get("/")
async def get():
    return {"message": "hi"}