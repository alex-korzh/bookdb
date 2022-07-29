__all__ = [
    "Book",
    "Author",
    "Genre",
]
from sqlalchemy.orm import relationship

from app.db import Base
from app.models.base import IdentifiableMixin
from sqlalchemy import Column, String, Integer, Table, ForeignKey

book_to_author = Table(
    'book_to_author',
    Base.metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('author_id', ForeignKey('authors.id')),
)


book_to_genre = Table(
    'book_to_genre',
    Base.metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('genre_id', ForeignKey('genres.id')),
)


class Book(Base, IdentifiableMixin):
    __tablename__ = "books"

    image = Column(String(255), nullable=True)
    isbn = Column(String(255), nullable=False, unique=True)
    language = Column(String(64), nullable=False)
    publisher = Column(String(255), nullable=False)
    size = Column(Integer, nullable=True)
    title = Column(String(64), nullable=False)
    year = Column(Integer, nullable=True)

    authors = relationship("Author", secondary=book_to_author, back_populates="books")
    genres = relationship("Genre", secondary=book_to_genre, back_populates="books")


class Author(Base, IdentifiableMixin):
    __tablename__ = "authors"

    name = Column(String(255), nullable=False)
    books = relationship("Book", secondary=book_to_author, back_populates="authors")


class Genre(Base, IdentifiableMixin):
    __tablename__ = "genres"

    name = Column(String(255), nullable=False)
    books = relationship("Book", secondary=book_to_genre, back_populates="genres")
