from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash
from models import Post, User, session

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        form = {
            'title': request.form['title'],
            'body':  request.form['body']
        }
        post = Post(**form)
        post.save()
    return render_template('add_post.html')

@app.route('/posts')
def show_posts():
    posts = session.query(Post).all()
    # import pdb; pdb.set_trace()
    return render_template('posts.html', posts=posts)