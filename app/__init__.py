import os
from app.config import Config
from flask import Flask
from app.home import homeBp
from app.gempa import gempaBp
from app.extension import *
# from app.gempa.routes import insert_data_from_csv
def create_app(config_class = Config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # fungsi untuk insert bulk ke database
    # with app.app_context():
    #     file_path = os.path.abspath(os.path.dirname(__file__)) + "/gempa/data/gempa_terkini.csv"
    #     insert_data_from_csv(file_path)

    app.register_blueprint(homeBp, url_prefix="/")
    app.register_blueprint(gempaBp, url_prefix="/api")

    return app

app = create_app()