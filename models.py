from sqlalchemy import Column, Integer, String
from database import Base  

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)  # FIXED
    publication_year = Column(Integer, nullable=False)
    description = Column(String(1000), nullable=False)  # You can still use large text here
