'''
forms.py: includes the web form classes.
The web forms use Flask-WTF extension and are represented as Python classes.
Each form class defines the fields of the form as class variables.
'''

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# Web form class for searching a patient by patient ID
class PatientIDForm(Form):
    patient_id = StringField('Patient ID: ', validators=[validators.required()])
    submit = SubmitField('Next')