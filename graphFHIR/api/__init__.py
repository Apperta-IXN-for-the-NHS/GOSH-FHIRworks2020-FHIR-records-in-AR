'''
api/__init__.py: includes API blueprint constructor.
'''

from flask import Blueprint

# creates the Blueprint object
bp = Blueprint('api', __name__)

from graphFHIR.api import patients, errors, tokens
