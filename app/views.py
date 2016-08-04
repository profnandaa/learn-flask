from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, session
from models import Post, User

# a few configs due to the restructuing of
# the app folders/directories
configs = {
    'template_folder': '../templates',
    'static_folder': '../static'
}

app = Flask('app', **configs)
app.secret_key = '3ffa85b890bc3cf0aba84c2697dbe446c33a4c9'


# login-required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # register user
        form = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'username': request.form['last_name'],
            'password': request.form['password']
        }
        user = User(**form)
        try:
            user.save()
        except:
            user.rollback()

        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    next_ = request.values.get('next')
    if request.method == 'POST':
        form = {
            'username': request.form['username'],
            'password': request.form['password']
        }
        user = User.validate(**form)
        if user[0]:
            if request.form['next'] != '':
                session['user'] = {
                    'username': user[1].username,
                    'id': user[1].id
                }
                return redirect(request.form['next'])
            return redirect(url_for('home'))
    return render_template('login.html', next=next_)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = {
            'title': request.form['title'],
            'body': request.form['body']
        }
        post = Post(**form)
        try:
            post.save(session['user']['id'])
        except:
            post.rollback()
    return render_template('add_post.html')


@app.route('/posts')
def show_posts():
    posts = Post.get()
    return render_template('posts.html', posts=posts)


@app.route('/user/<int:id>')
def user_profile(id):
    user = User.get(id)
    if user:
        return render_template('user_profile.html', user=user)
    return redirect('/')
