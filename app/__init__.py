from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].init_app(app)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app)

    # Login Manager Setup
    login_manager.login_view = '/login'

    @login_manager.user_loader
    def load_user(user_id):
        from .models.user import User
        return db.session.query(User).filter_by(id=user_id).first()

    @login_manager.unauthorized_handler
    def unauthorized():
        app.logger.warning('User unauthorized')
        # do stuff
        return redirect(url_for('users.login'))

    # Blueprint
    from .blueprints.auth import auth
    from .blueprints.misc import misc

    app.register_blueprint(auth)
    app.register_blueprint(misc)

    return app
