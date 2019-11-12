from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TimeField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=30)])
    remember = BooleanField('remember me')  

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=30)])
    university = StringField('university', validators=[InputRequired(), Length(min=4,max=70)])

class NewCourseForm(FlaskForm):
    code = StringField('code', validators=[InputRequired(), Length(min=8, max=8, "Course Code Invalid")])
    title = StringField('title', validators=[InputRequired(), Length(min=4, max=50, "Course Title Invalid")])

class AddClassForm(FlaskForm):
    classTime = TimeField('classTime')
    lecturer = StringField('lecturer', validators=[Length(min=0, max=50, "Lecturer Name Invalid")])
    classType = StringField('classType', validators=[InputRequired(), Length(min=3, max=20, "Class Type Invalid")])



