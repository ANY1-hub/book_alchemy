this is a learn project for using Flask, sqlalchemy and SQLite

# SETUP:
- After cloning, it is important to set the `FLASK_SECRET=` variable in the
`.env` file in a `config` folder, that you need to create in the root directory, with your own value.

- also create a `data` folder in the root of the project, then in the app.py run the following,
currently out commented code only once, in order to create your own Database :  
` # ran only once to create the db
   with app.app_context():
   db.create_all()`
after successfully created, comment it out again.




# Possible future features:

# Bonus ✨
Woo hoo, you did it! 🌟 You created a Flask application and connected it to a SQLite database using SQLAlchemy!
Here are some fun bonus exercises you can complete if you’d like to extend the capabilities of your library application. You can do one, some, or all of them.
# Bonus #1 - Use ChatGPT to Redesign the UI 🤖
In the recent live coding session with your Schoolmaster, you learned about using ChatGPT to redesign the UI of a website. Implement what you learned on your digital library app!
# Bonus #2 - Detail Pages 🔎
It would be nice to be able to click on a book title on your homepage and view details about the book in a new page.
Define Flask routes and create HTML pages that render detail pages for books and authors. Retrieve the relevant data from the database based on the provided author/book ID, then dynamically generate the content for each page.
# Bonus #3 - Delete an Author ❌
Create a route called /author/<int:author_id>/delete which deletes a specific author from the database when a POST request comes in. Redirect the user to the homepage (the “Library”) after a successful deletion, and display a success message indicating that the deletion of the author worked.
Add a “Delete Author” button to home.html. It should appear underneath or next to each author’s name, and it should delete ALL books in your database with Foreign Keys to that author. When you refresh the HTML page, those books should no longer appear in your digital library.
Suppose you delete a row from a table that contains a column that is a Foreign Key to another table. In our case, this would happen when you delete a row from the Book table because it contains a Foreign Key column to the Author table.
You get to decide how to handle the data that exists in the table that contains the Foreign Key; in our example, you get to decide how to handle the author data when deleting a book. The choices vary a bit depending on the database you’re using, but generally, you can delete the author, protect the author from being deleted, or update the author value to something else.
This decision can be specified with SQLAlchemy using the the cascade=all feature. You can look this up in the flask-sqlalchemy and/or the SQLAlchemy documentation.
# Bonus #4 - Book Ratings 🥇
Add functionality so you can provide a rating (1-10) for each book in your library.
# Bonus #5 - Suggest a Book to Read 💡
Create a page that uses Artificial Intelligence to generate a book recommendation based on the books in your library, and that optionally takes into account your book ratings (if you completed Bonus #3 above).
The Flask route should send all the books that the user has read to ChatGPT, and let ChatGPT generate recommendation. You could find a free AI API to use on RapidAPI (Look for any ChatGPT that allows a free plan with a hard limit).
