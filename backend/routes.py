from flask import render_template, url_for, flash, redirect, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from backend.models import db, User, Role, Survey, Report
from backend.forms import RegistrationForm, LoginForm, SurveyForm
from backend.analysis import analyze_reports, calculate_total_score
import uuid
import json

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('index.html')

@main.route('/home')
@login_required
def home():
    # Fetch all reports for the current user
    reports = Report.query.filter_by(user_id=current_user.id).order_by(Report.date_posted.asc()).all()
    if reports:
        analysis = analyze_reports(reports)  # Analyze all reports
        return render_template('home.html', analysis=analysis)
    else:
        flash('New user, please take the survey.', 'info')
        return redirect(url_for('main.survey'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already exists. Please use a different one.', 'danger')
        else:
            try:
                user = User(
                    name=form.name.data,
                    email=form.email.data,
                    password=generate_password_hash(form.password.data)
                )
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created!', 'success')
                return redirect(url_for('main.login'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error creating account: {str(e)}', 'danger')
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'info')
    return redirect(url_for('main.index'))

@main.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        try:
            survey = Survey(
                user_id=current_user.id,
                question1=form.question_1.data,
                question2=form.question_2.data,
                question3=form.question_3.data,
                question4=form.question_4.data,
                question5=form.question_5.data,
                question6=form.question_6.data,
                question7=form.question_7.data,
                question8=form.question_8.data,
                question9=form.question_9.data,
                question10=form.question_10.data
            )
            db.session.add(survey)
            db.session.commit()

            # Calculate the total score and create a report
            total_score = calculate_total_score(survey)
            report = Report(
                user_id=current_user.id,
                total_score=total_score,
                report_data={
                    'survey_id': survey.id,
                    'total_score': total_score
                }
            )
            db.session.add(report)
            db.session.commit()

            flash('Your survey has been submitted!', 'success')
            return redirect(url_for('main.home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting survey: {str(e)}', 'danger')
    return render_template('survey.html', form=form)

@main.route('/resources')
def resources():
    return render_template('resources.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

def init_views(app):
    app.register_blueprint(main)
