from flask import Flask, request, redirect, url_for, render_template
from models import Post, User, session

# a few configs due to the restructuing of
# the app folders/directories
configs = {
    'template_folder': '../templates',
    'static_folder': '../static'
}

app = Flask('app', **configs)

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