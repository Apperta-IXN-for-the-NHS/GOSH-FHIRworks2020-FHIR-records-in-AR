'''
config.py: defines configuration variables and configuration sets for the application.
'''

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # ... add more variables here if needed in the future