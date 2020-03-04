# routes.py: containing handlers for the application routes (the view functions)
# view functions are mapped to one or more route URLs 
# so that Flask knows what logic to execute when a client requests a given URL

from graphFHIR import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"