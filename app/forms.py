# This Python File will mainly be used for collecting info upon registering in the Forums.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_validators import DisposableEmail
from app.models import User

#Registration Form Class, Labeling out Form Fields Needed to be Filled Out
class RegistrationForm(FlaskForm):
    #attributes
    username = StringField('Username',
                           # validators - parameters to accept user input
                           validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Enter your Email here.',
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


class LoginForm(FlaskForm):
    #For logging in
    username = StringField('Username',
                           # validators - parameters to accept user input
                           validators=[DataRequired(), Length(min=2, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In!')

