from fastapi import FastAPI
from api.v1.router import router as item_router

app = FastAPI()

app.include_router(item_router)

