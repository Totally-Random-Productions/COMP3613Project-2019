from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TimeField, DateField, IntegerField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from priorityU.models.models import *


# JERREL: ADDED CUSTOM VALIDATORS FOR REGISTRATION, EXAM AND ASSIGNMENT FORMS 24/11/19
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)],
                           render_kw={"placeholder": "abcdefg"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)],
                             render_kw={"placeholder": "********"})
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)],
                        render_kw={"placeholder": "someone@email.com"})
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)],
                           render_kw={"placeholder": "abcdefg"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)],
                             render_kw={"placeholder": "********"})
    university = StringField('University', validators=[InputRequired(), Length(min=4, max=70)],
                             render_kw={"placeholder": "ConU"})


    def validate_email(self, email):
      e = bool(User.query.filter_by(email=email.data).first())
      if e == True:
        raise ValidationError("Email already affiliated with an account.")


    def validate_username(self, username):
      u = bool(User.query.filter_by(username=username.data).first())
      if u == True:
        raise ValidationError("User name already taken.")


class NewCourseForm(FlaskForm):
    code = StringField('Course Code', validators=[InputRequired(), Length(min=6, max=9, message="Invalid Course Code")],
                       render_kw={"placeholder": "COMP 354"})
    title = StringField('Course Title', validators=[InputRequired(), Length(min=4, max=50, message="Invalid Course")],
                        render_kw={"placeholder": "Software Engineering"})
    lecturer = StringField('Lecturer', validators=[InputRequired(), Length(min=2, max=50, message="Invalid Lecturer")],
                           render_kw={"placeholder": "Greg Butler"})
    location = StringField('Location', validators=[InputRequired(), Length(min=2, max=20, message="Invalid Location")],
                           render_kw={"placeholder": "Hall Building rm 820"})


class NewExamForm(FlaskForm):
    course_code = StringField('Course code', validators=[InputRequired(), Length(min=4, max=50, message="Invalid Course"
                                                                                 )],
                              render_kw={"placeholder": "COMP 354"})
    exam_name   = StringField('Exame Name', validators=[InputRequired(), Length(min=4, max=50, message="Invalid Exam Name")], render_kw={"placeholder":"Exam Name"})
    weighting = IntegerField('Exam Weighting (%)', validators=[InputRequired()],
                             render_kw={"placeholder": "100"})
    date = DateField('Exam Date', validators=[InputRequired()], format='%d/%m/%Y',
                     render_kw={"placeholder": "dd/mm/yyyy"})
    time = TimeField('Start Time', validators=[InputRequired()], format='%H:%M', render_kw={"placeholder":"2:00"})
    duration = IntegerField('Exam Duration (In hours)', validators=[InputRequired(message = 'Please enter whole '
                                                                                            'number values'), ],
                            render_kw={"placeholder": "HH"})
    location = StringField('Location', validators=[InputRequired(), Length(min=2, max=20, message="Invalid Location")],
                           render_kw={"placeholder": "Hall Building rm 820"})

    def validate_course_code(self, course_code):
       c =bool(Courses.query.filter_by(course_code=course_code.data).first())
       if c == False:
        raise ValidationError("It doesn't look like that Course exists...")



class NewAssignmentForm(FlaskForm):
    course_code = StringField('Course code', validators=[InputRequired(), Length(min=4, max=50, message="Invalid Course"
                                                                                 )],
                              render_kw={"placeholder": "COMP 354"})
    asg_name = StringField('Assignment Name', validators=[InputRequired(), Length(min=1, max=50,
                                                                                  message="Invalid Assignment Name")],
                           render_kw={"placeholder": "Assignment 1"})
    weighting = IntegerField('Assignment Weighting', validators=[InputRequired()],
                             render_kw={"placeholder": "100"})
    due_date = DateField('Due Date', validators=[InputRequired()], format='%d/%m/%Y',
                         render_kw={"placeholder": "dd/mm/yyyy"})
    due_time = TimeField('Due Time', validators=[InputRequired()], format='%H:%M',
                         render_kw={"placeholder": "2:00"})
    
    def validate_course_code(self,course_code):
      c =bool(Courses.query.filter_by(course_code=course_code.data).first())
      if c == False:
        raise ValidationError("It doesn't look like that Course exists...")




