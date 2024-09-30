from pydantic import BaseModel

class Subject(BaseModel):
  key: int
  value: int
  priority: int