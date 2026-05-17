from pydantic import BaseModel

class FileShema(BaseModel):
    id: int
    name: str