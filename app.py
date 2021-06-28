from flask import Flask, render_template, request, redirect, url_for, session, flash
from forms import RegistrationForm, LoginForm
# from flask_login import LoginManager
#
# login_manager = LoginManager()

app = Flask(__name__)

#Protect Against Cookie Modification
app.config['SECRET_KEY'] = 'f9a2fd8f07fae783cf24ae35997a2a7c'

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
# login_manager.init_app(app)

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
    form = RegistrationForm()
    if form.validate_on_submit():
        #flashes a meesage when validated; f'string' is a shortcut way to format strings
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'bingus' and form.password.data == 'bingus':
        #flashes a meesage when validated; f'string' is a shortcut way to format strings
            flash('Login Successful.', 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Wrong Credentials.', 'danger')

    return render_template('login.html', title= 'Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
