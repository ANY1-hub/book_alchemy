from data_models import db, Author, Book
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, redirect, url_for
import os


load_dotenv('config/.env')
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = os.getenv('FLASK_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
# connect Flask app to flask-alchemy code
db.init_app(app)

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            if not name:
                flash('Name is required')
                return render_template('author_form.html')
            birth_date_str = request.form.get('birth_date')
            birth_date = None
            if birth_date_str:
                birth_date: datetime = datetime.strptime(birth_date_str, '%Y-%m-%d')
            date_of_death_str = request.form.get('date_of_death', None)
            date_of_death = None
            if date_of_death_str:
                date_of_death: datetime = datetime.strptime(date_of_death_str, '%Y-%m-%d')
            new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
            db.session.add(new_author)
            db.session.commit()
            flash('Data successfully recorded')
            # after successfull commit redirect (a new GET) so there can be no accidental double entry
            return redirect(url_for('add_author'))
        except ValueError as e:
            flash(f'missing input {e}')

    return render_template('author_form.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    authors = None
    publication_year = None
    if request.method == 'GET':
        try:
            authors = db.session.execute(db.select(Author)).scalars().all()
            if not authors:
                flash('There was a problem retrieving the list of authors')
        except Exception as e:
            flash(f'There was a problem, trying to retrieve the data: {e}')
        return render_template('book_form.html', authors=authors)

    if request.method == 'POST':
        try:
            title = request.form.get('title')
            if not title:
                flash('Title is required')
                return render_template('book_form.html')
            author_id = request.form.get('author_id')
            isbn = request.form.get('isbn')
            try:
                publication_year = int(request.form.get('publication_year', None))
                if not 1455 <= publication_year < (int(datetime.now().year) + 1):
                    flash('Please enter a valid year')
                    return render_template('book_form.html')
            except ValueError:
                flash('Please enter a valid year (4 digits)')
            new_book = Book(title=title, author_id=author_id, isbn=isbn, publication_year=publication_year)
            db.session.add(new_book)
            db.session.commit()
            flash('Data successfully recorded')
            return redirect(url_for('add_book'))
        except ValueError as e:
            flash(f'missing input {e}')

    return render_template('book_form.html')

@app.route('/', methods=['GET'])
def home():
    books = None
    try:
        books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
        if not books:
            flash('There was a problem retrieving the list of books')
    except Exception as e:
        flash(f'There was a problem, trying to retrieve the data: {e}')
    return render_template('home.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)

"""
# ran only once to create the db
with app.app_context():
  db.create_all()
"""