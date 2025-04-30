from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str | None = None
    publication_year: int | None = None
    description: str
    ai_tagline: str | None = None  # Optional field

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str | None = None
    publication_year: int | None = None
    description: str

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
