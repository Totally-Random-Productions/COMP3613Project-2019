from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TimeField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=30)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=30)])
    university = StringField('University', validators=[InputRequired(), Length(min=4,max=70)])

class NewCourseForm(FlaskForm):
    code = StringField('Course Code', validators=[InputRequired(), Length(min=8, max=8, message="Invalid Course Code")])
    title = StringField('Course Title', validators=[InputRequired(), Length(min=4, max=50, message="Invalid Course")])
    lecturer = StringField('Lecturer', validators=[InputRequired(), Length(min=2, max=50, message="Invalid Lecturer")])
    location = StringField('Location', validators=[InputRequired(), Length(min=2, max=20, message="Invalid Location")])


