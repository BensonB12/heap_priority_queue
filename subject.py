from pydantic import BaseModel


class Subject(BaseModel):
    key: int
    value: str
    priority: int
