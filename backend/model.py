from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    extend_existing=True
)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    surveys = db.relationship('Survey', backref='author', lazy=True)
    reports = db.relationship('Report', backref='author', lazy=True)

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    question1 = db.Column(db.String(100), nullable=False)
    question2 = db.Column(db.String(100), nullable=False)
    question3 = db.Column(db.String(100), nullable=False)
    question4 = db.Column(db.String(100), nullable=False)
    question5 = db.Column(db.String(100), nullable=False)
    question6 = db.Column(db.String(100), nullable=False)
    question7 = db.Column(db.String(100), nullable=False)
    question8 = db.Column(db.String(100), nullable=False)
    question9 = db.Column(db.String(100), nullable=False)
    question10 = db.Column(db.Text, nullable=False)  # Descriptive answer

    user = db.relationship('User', backref=db.backref('surveys', lazy=True))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_score = db.Column(db.Integer, nullable=False)
    report_data = db.Column(db.JSON, nullable=False)

    user = db.relationship('User', backref=db.backref('reports', lazy=True))
