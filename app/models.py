from datetime import  datetime
from app import db, loginm
#UserMixin adds all methods and attributes needed for the User Model
from flask_login import UserMixin

#takes user id as argument (for logging in)
@loginm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Unique ID for each user/entry in the user database
#User Info Class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    prof_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #shows relationship of posts made to a single author that wrote them, backref is adding pseudo column to post model
    posts = db.relationship('Post', backref='author', lazy=True)
    #How our user object (info) will be printed
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.prof_pic}')"

#Class for posts made in the Freedom Forums
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
