# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = 'db/app.db'
DEBUG = True
SECRET_KEY = 'xhjshjhsnd'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    # print app.config(['DATABASE'])
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# Routes

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/entries/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)






if __name__ == '__main__':
    app.run(port=8001)

