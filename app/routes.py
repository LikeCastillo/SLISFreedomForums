from flask import render_template, request, redirect, url_for, session, flash
from app import app, db, encode
from app.forms import RegistrationForm, LoginForm
from app.models import User,Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author' : 'Jan Francis',
        'username' : 'LikeCastillo',
        'title' : 'My First SLIS Post',
        'content' : 'Hello!',
        'date_posted': 'June 27, 2021'
    },
    {
        'author' : 'Jiez and Coral',
        'username' : 'CoralAndJiez',
        'title' : 'My Second SLIS Post',
        'content' : 'Goodbye!',
        'date_posted': 'June 27, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    # if 'username' in session:
    #     return f'Logged in as {session["username"]}'
    # return 'You are not logged in'
    return render_template('home.html', posts=posts)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('index'))
#     return render_template('login.html', title='Login', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashy = encode.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashy)
        db.session.add(user)
        db.session.commit()
        #flashes a meesage when validated; f'string' is a shortcut way to format strings
        flash(f'Welcome to SLIS Freedom Forums! You may now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and encode.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            #code to redirect us to the "next page (account)" once we have met certain parameters
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

# <a class="nav-item nav-link" href="/register">Register</a>
