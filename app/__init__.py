from flask import Flask

from config import config

def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].init_app(app)

    return app
