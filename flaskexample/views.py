import os
import yaml

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    here = os.path.dirname(__file__)
    config = yaml.safe_load(open(os.path.join(here, 'config.yml')))
    print(config)
    app.config.from_mapping(config)
    app.logger.setLevel(config['logging']['level'])

    #db = SQLAlchemy(model_class=Base)
    #db.init_app(app)

    @app.route('/')
    def home():
        return render_template('index.html')

    add_context_processors(app)
    return app

def add_context_processors(app):
    """Add context processors for this app."""
    import datetime

    @app.context_processor
    def inject_now():
        """Enable {{now}} in templates, used by the footer."""
        return {'now': datetime.datetime.now(datetime.timezone.utc)}