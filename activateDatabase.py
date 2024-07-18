from application import app
from backend.models import db, User, Role
from werkzeug.security import generate_password_hash
import uuid

with app.app_context():
    db.create_all()

    # Create roles
    if not Role.query.filter_by(name='admin').first():
        admin_role = Role(name='admin', description='User is an Admin')
        db.session.add(admin_role)

    if not Role.query.filter_by(name='employee').first():
        employee_role = Role(name='employee', description='User is an Employee')
        db.session.add(employee_role)

    db.session.commit()

    # Create an admin user if not exists
    if not User.query.filter_by(email='admin@email.com').first():
        admin_user = User(
            name='admin',
            email='admin@email.com',
            password=generate_password_hash('admin', method='sha256'),
            fs_uniquifier=str(uuid.uuid4())
        )
        admin_user.roles.append(admin_role)
        db.session.add(admin_user)

    db.session.commit()
