from pydantic import BaseModel, Field

class User(BaseModel):
    id: str | None = None
    name: str = Field(min_length=1, max_length=20, pattern=r'^[A-Z][a-z]+$')
    lastName: str = Field(min_length=1, max_length=30, pattern=r'^[A-Z][a-z]+$')
    telephone: str = Field(min_length=8, max_length=10, pattern=r'^[0-9]+$')