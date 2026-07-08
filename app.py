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
            return redirect(url_for('add_author'))
        except ValueError as e:
            flash(f'missing input {e}')

    return render_template('author_form.html')


if __name__ == '__main__':
    app.run(debug=True)
"""
# ran only once to create the db
with app.app_context():
  db.create_all()
"""
