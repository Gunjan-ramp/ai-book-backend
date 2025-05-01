from fastapi import FastAPI, Depends, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine, Base, get_db
from ai import generate_ai_tagline  # Import the function from the ai.py module


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=False,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", status_code=200)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}

@app.get("/search/book")
async def search_books(title: str = "", author: str = "", db: Session = Depends(get_db)):
    return crud.search_books(db, title, author)


@app.get("/books/{book_id}/ai-insights", response_model=schemas.BookBase)
def get_book_ai_insight(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    ai_tagline = generate_ai_tagline(book.title, book.author, book.description)
    print(ai_tagline)

    return schemas.BookBase(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        publication_year=book.publication_year,
        description=book.description,
        ai_tagline=ai_tagline
    )
