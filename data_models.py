from typing import Optional
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

db = SQLAlchemy()


class Author(db.Model):
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birth_date: Optional[datetime] = Column(DateTime, nullable=True)
    date_of_death: Optional[datetime] = Column(DateTime, nullable=True)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, birth_date: {self.birth_date}, date_of_death: {self.date_of_death}'


    def __repr__(self):
        return f'Author(id: {self.id}(int), name: {self.name}(str), birth_date: {self.birth_date}(date), date_of_death: {self.date_of_death}(date))'

class Book(db.Model):
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String)
    title = Column(String)
    publication_year: Optional[int] = Column(Integer, nullable=True)
    author_id = db.Column(Integer, db.ForeignKey('author.author_id'))

    def __str__(self):
        return f'id: {self.id}, isbn: {self.isbn}, title: {self.title}, publication_year: {self.publication_year}, author_id: {self.author_id}'


    def __repr__(self):
        return f'Books(id: {self.id}(int), isbn: {self.isbn}(str), title: {self.title}(date), publication_year: {self.publication_year}(date), author_idL: {self.author_id})'

