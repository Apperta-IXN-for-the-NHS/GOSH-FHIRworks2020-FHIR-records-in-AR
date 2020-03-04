# __init__.py: Flask application instance

from flask import Flask

# The app variable is an instance of class Flask in the __init__.py script 
# which makes it a member of the graphFHIR package.
app = Flask(__name__)

from graphFHIR import routes