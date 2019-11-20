"""application routes"""
from flask import render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from priorityU import app, db, login_manager
from priorityU.models.models import User, Tasks, Courses, Assignment, Exam
from priorityU.models.forms import LoginForm, RegisterForm, NewCourseForm, NewExamForm



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#create tables
db.create_all()

#dummydata
#course=Courses(course_code='COMP3613',course_name='TOC',lecturer='Mohan',location='TCB14',user_id='1')
#task=Tasks(name='doit',due_date='',priority=5,status='c',user_id='1')

#db.session.add(course)
#db.session.add(task)
#db.session.commit()


#VIEWS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        return '<h1>Invalid username or password combination</h1>'
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, university=form.university.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/dashboard/calendar')
@login_required
def calendar():
    return render_template('calendar.html')

@app.route('/dashboard/courses')
@login_required
def courses():
    user_courses = Courses.query.filter_by(user_id=current_user.get_id()).order_by(Courses.course_code.desc()).all() # Dominic 18/11- user course data query
    return render_template('courses.html', name=current_user.username, courses=user_courses)

@app.route('/dashboard/courses/add', methods=['GET', 'POST'])
@login_required
def addCourse():
    form = NewCourseForm()
    if form.validate_on_submit():
        course = Courses(course_code=form.code.data, course_name=form.title.data, lecturer=form.lecturer.data, location=form.location.data, user_id=current_user.get_id())
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses'))
    return render_template('addCourse.html', form=form)

@app.route('/dashboard/courses/<c_id>', methods=['GET', 'POST'])
@login_required
def deleteCourse(c_id):
    course = Courses.query.filter_by(c_id=c_id).first()
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('courses'))

@app.route('/dashboard/completed')
@login_required
def completed():
    return render_template('completed.html')

@app.route('/dashboard/exams')
@login_required
def exams():
    user_exams = Exam.query.filter_by(user_id=current_user.get_id()).order_by(Exam.date.asc()).all() # Dominic 18/11- user exam data query
    return render_template('exams.html', exams=user_exams)

@app.route('/dashboard/exams/add', methods=['GET', 'POST'])
@login_required
def addExam():
    form = NewExamForm()
    if form.validate_on_submit():  # Needs too check if course exists first
        exam = Exam(course_code=form.course_code.data, weighting=form.weighting.data,
                    date=form.date.data, time=form.time.data, duration=form.duration.data,
                    user_id=current_user.get_id())
        db.session.add(exam)
        db.session.commit()
        return redirect(url_for('exams'))
    return render_template('addExam.html', form=form)

@app.route('/dashboard/exams/<e_id>', methods=['GET', 'POST'])
@login_required
def deleteExam(e_id):
    exam = Exam.query.filter_by(e_id=e_id).first()
    db.session.delete(exam)
    db.session.commit()
    return redirect(url_for('exams'))

@app.route('/dashboard/assignments')
@login_required
def assignments():
    user_asgs = Assignment.query.filter_by(user_id=current_user.get_id()).order_by(Assignment.due_date.asc()).all() # Dominic 18/11- user assignment data query
    return render_template('assignments.html', asgs=user_asgs)


@app.route('/dashboard/assignments/<a_id>', methods=['GET', 'POST'])
@login_required
def deleteAssignment(a_id):
    assignment = Assignement.query.filter_by(a_id).first()
    db.session.delete(assignment)
    db.session.commit()
    return redirect(url_for('assignments'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__': # Dominic - is this necessary?
    app.run(debug=True)
    