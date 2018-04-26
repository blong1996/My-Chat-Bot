from flask import Flask
from my_app.controllers.api_controllers import app_api

# Define app
app = Flask(__name__)

# # Configurations
app.config.from_object('config')


# Register blueprints
def register_blueprints(my_app):
    my_app.register_blueprint(app_api)


register_blueprints(app)