from app import createApp
import os

app = createApp(os.getenv('FLASK_CONFIG') or 'default')
