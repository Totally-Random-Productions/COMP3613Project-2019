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
    code = StringField('Code', validators=[InputRequired(), Length(min=8, max=8, message = "Course Code Invalid")])
    title = StringField('Title', validators=[InputRequired(), Length(min=4, max=50, message = "Course Title Invalid")])

class AddClassForm(FlaskForm):
    classTime = TimeField('Class Time')
    lecturer = StringField('Lecturer', validators=[Length(min=0, max=50, message = "Lecturer Name Invalid")])
    classType = StringField('Class Type', validators=[InputRequired(), Length(min=3, max=20, message ="Class Type Invalid")])



