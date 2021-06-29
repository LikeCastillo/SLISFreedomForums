# This Python File will mainly be used for collecting info upon registering in the Forums.

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_validators import DisposableEmail
from app.models import User



#Registration Form Class, Labeling out Form Fields Needed to be Filled Out
class RegistrationForm(FlaskForm):
    #attributes
    username = StringField('Username',
                           # validators - parameters to accept user input
                           validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), DisposableEmail()])
    password = PasswordField('Password', validators=[DataRequired()])

    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #Validating User Input in Registration
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Exists Already!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Exists Already!')

#Login Form for Registered Users
class LoginForm(FlaskForm):
    #For logging in
    username = StringField('Username',
                           # validators - parameters to accept user input
                           validators=[DataRequired(), Length(min=2, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In!')

class UpdateAccountForm(FlaskForm):
    #attributes
    username = StringField('Username',
                           # validators - parameters to accept user input
                           validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Enter your Email here.',
                        validators=[DataRequired(), DisposableEmail()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    #Validating User Input in Registration
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username Exists Already!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email Exists Already!')

#Form when posting something in the Freedom Foruma
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired(), Length(max=750)])
    submit = SubmitField("Post")
