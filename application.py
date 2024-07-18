import os
from flask import Flask
from flask_login import LoginManager
from backend.models import db, User, Role
from configuration import DevelopmentConfig  # or ProductionConfig
from backend.routes import init_views
import nltk
nltk.download('vader_lexicon')


def create_app():
    app = Flask(__name__, static_folder='frontend/static', template_folder='frontend/templates')
    app.config.from_object(DevelopmentConfig)  # Use the appropriate configuration
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Redirect to login page if not authenticated

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        init_views(app)

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
