# __init__.py: Flask application instance

from flask import Flask
from config import Config

# The app variable is an instance of class Flask in the __init__.py script 
# which makes it a member of the graphFHIR package.
app = Flask(__name__)

# apply application configuration defined in config.py
app.config.from_object(Config)

from graphFHIR import routes