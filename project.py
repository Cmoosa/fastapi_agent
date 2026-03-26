from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class BookStore(BaseModel):
    title: str
    author: str
    publish_date: str

@app.post("/books")
def create_book(book: BookStore, db: Session = Depends(get_db)):
    new_book = model.Book(title=book.title, author=book.author, publish_date=book.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(model.Book).all()
    return books