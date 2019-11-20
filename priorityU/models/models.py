"""contains user data"""
from flask_login import UserMixin
from priorityU import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    last_task_id = db.Column(db.Integer)
    university = db.Column(db.String, nullable=False)
    tasks = db.relationship('Tasks', backref='poster')
    courses = db.relationship('Courses', backref='poster')

    def __init__(self, username=None, email=None, password=None, university=None):
        self.username = username
        self.email = email
        self.password = password
        self.university = university

    def __repr__(self):
        return '<User %r>' % self.name


class Tasks(db.Model):  # Dominic - is this necessary?
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, due_date, priority, status, user_id):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.user_id = user_id
        self.status = status

    def __repr__(self):
        return '<name %r>' % self.body


class Courses(db.Model):
    __tablename__ = 'courses'

    c_id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    lecturer = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, course_code=None, course_name=None, lecturer=None, location=None, user_id=None):
        self.course_code = course_code
        self.course_name = course_name
        self.lecturer = lecturer
        self.location = location
        self.user_id = user_id


class Assignment(db.Model): # Dominic 18/11- created model for assignment db
    __tablename__ = 'assignments'

    a_id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.course_code'))
    asg_name = db.Column(db.String, nullable=False)
    weighting = db.Column(db.Integer)
    due_date = db.Column(db.Date, nullable=False)
    due_time = db.Column(db.Time)
    complete = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, course_code=None, asg_name=None, weighting = 0, due_date=None, due_time=None, complete=False, user_id=None):
        self.course_code = course_code
        self.asg_name = asg_name
        self.weighting = weighting
        self.due_date = due_date
        self.due_time = due_time
        self.complete = complete
        self.user_id = user_id


class Exam(db.Model): # Dominic 18/11- created model for assignment db
    __tablename__ = 'exams'

    e_id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('courses.course_code'))
    weighting = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time)
    duration = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, course_code=None, weighting=0, date=None, time=None, duration=None, location=None, user_id=None):
        self.course_code = course_code
        self.weighting = weighting
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.user_id = user_id
          