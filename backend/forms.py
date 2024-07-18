from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    roles = SelectMultipleField('Roles', choices=[('employee', 'Employee')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SurveyForm(FlaskForm):
    question_1 = RadioField('Q.1 How often do you take breaks during work?', choices=[('0', 'Never'), ('1', 'Sometimes'), ('3', 'Often')], validators=[DataRequired()])
    question_2 = RadioField('Q.2 How often do you exercise in a week?', choices=[('0', 'Never'), ('1', 'Once'), ('3', 'Three or more times')], validators=[DataRequired()])
    question_3 = RadioField('Q.3 How many servings of vegetables do you eat daily?', choices=[('0', 'None'), ('1', 'One serving'), ('3', 'Three or more servings')], validators=[DataRequired()])
    question_4 = RadioField('Q.4 How many hours of sleep do you get per night?', choices=[('0', 'Less than 5 hours'), ('1', '5-7 hours'), ('3', 'More than 7 hours')], validators=[DataRequired()])
    question_5 = RadioField('Q.5 How often do you feel stressed?', choices=[('0', 'Always'), ('1', 'Sometimes'), ('3', 'Rarely')], validators=[DataRequired()])
    question_6 = RadioField('Q.6 How satisfied are you with your work-life balance?', choices=[('0', 'Not satisfied'), ('1', 'Somewhat satisfied'), ('3', 'Very satisfied')], validators=[DataRequired()])
    question_7 = RadioField('Q.7 How often do you participate in recreational activities?', choices=[('0', 'Never'), ('1', 'Sometimes'), ('3', 'Often')], validators=[DataRequired()])
    question_8 = RadioField('Q.8 How would you rate your overall health?', choices=[('0', 'Poor'), ('1', 'Fair'), ('3', 'Good')], validators=[DataRequired()])
    question_9 = RadioField('Q.9 If you\'re happy and you know it clap your hands. How many times did you clap:', choices=[('0', '0'), ('1', '1'), ('3', '3')], validators=[DataRequired()])
    question_10 = TextAreaField('Q.10 Please describe any other factors that affect your wellness:', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Survey')
