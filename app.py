# all the imports
import sqlite3
from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash
from basic_models import Post, session

# configuration
DATABASE = 'db/app.db'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


# Routes

@app.route('/')
def home():
	return render_template('home.html')


# for basic demonstration

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        form = {
            'title': request.form['title'],
            'body':  request.form['body']
        }
        entry = Post(**form)
        entry.save()
    return render_template('add_entry.html')

@app.route('/entries')
def show_entries():
    entries = session.query(Post).all()
    # import pdb; pdb.set_trace()
    return render_template('show_entries.html', entries=entries)


if __name__ == '__main__':
    app.run(debug=True, port=8004)

