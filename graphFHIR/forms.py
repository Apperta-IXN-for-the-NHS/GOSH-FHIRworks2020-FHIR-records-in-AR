from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class PatientIDForm(Form):
    patient_id = StringField('Patient ID: ', validators=[validators.required()])
    submit = SubmitField('Next')