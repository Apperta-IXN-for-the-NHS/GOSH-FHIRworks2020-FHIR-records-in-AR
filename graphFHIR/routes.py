'''
routes.py: contains handlers for the application routes (the view functions).
View functions are mapped to one or more route URLs so that Flask knows 
what logic to execute when a client requests a given URL.
'''

from flask import render_template, flash, redirect, request
from graphFHIR import app, data
from graphFHIR.forms import PatientIDForm


# Define and initialise global data fields

patient_name = None
patient_observations = []
# the observation dates for Blood Pressure, Diastolic Blood Pressure
# and Systolic Blood Pressure are the same
observation_date = []
patient_bp = []
patient_dbp = []
patient_sbp = []
bp_average = None
dbp_average = None
sbp_average = None


# Update a paitent's data into the global date fields according to patient ID
def getData(patient_id):
    # access the above global variables
    global patient_observations
    global patient_name
    global observation_date
    global patient_bp
    global patient_dbp
    global patient_sbp
    global bp_average
    global dbp_average
    global sbp_average

    patient_observations = data.get_patient_observations(patient_id)
    patient_name = data.get_patient_name(patient_id)

    bp_unit, patient_bp, patient_bp_date = data.patient_blood_presure(patient_observations)
    dbp_unit, patient_dbp, patient_dbp_date = data.patient_diastolic_blood_pressure(patient_observations)
    sbp_unit, patient_sbp, patient_sbp_date = data.patient_systolic_blood_pressure(patient_observations)

    observation_date = patient_bp_date

    bp_average = data.get_average(patient_bp)
    dbp_average = data.get_average(patient_dbp)
    sbp_average = data.get_average(patient_sbp)


# The index page 
# -- user inputs patient ID that is going to be searched and graphed
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    patient_id = None
    form = PatientIDForm(request.form)
    if request.method == 'POST':
        patient_id = request.form['patient_id']
    if form.validate() and data.check_patient_id(patient_id):
        getData(patient_id)
        # if the patient exists, proceed to graphing
        return redirect('/bar')
        
    # otherwise, the patiend doesn't exist
    return render_template('index.html', title='Home page', form=form)


# The bar chart page 
# -- display average blood pressure observation value for a single patient
@app.route('/bar')
def bar():
    bar_labels = []
    bar_values = []
    bar_colors = []
    bar_dataset_labels = []

    if (bp_average != 0.0):
        bar_labels.append('Average Blood Pressure')
        bar_values.append(bp_average)
        bar_colors.append("#F7464A")
        bar_dataset_labels.append("Blood Pressure")

    if (dbp_average != 0.0):
        bar_labels.append('Average Diastolic Blood Pressure')
        bar_values.append(dbp_average)
        bar_colors.append("#46BFBD")
        bar_dataset_labels.append("Diastolic Blood Pressure")

    if (sbp_average != 0.0):
        bar_labels.append('Average Systolic Blood Pressure')
        bar_values.append(sbp_average)
        bar_colors.append("#FDB45C")
        bar_dataset_labels.append("Systolic Blood Pressure")

    return render_template('bar_chart.html', title='Bar Chart', name=patient_name,
                            labels=bar_labels, values=bar_values, colors = bar_colors)


# The line chart page 
# -- display historical blood pressure observation data for a single patient
@app.route('/line')
def line():
    line_labels = observation_date
    line_values = []
    line_colors = ["#F7464A", "#46BFBD", "#FDB45C"]
    line_dataset_labels = ["Blood Pressure", "Diastolic Blood Pressure", "Systolic Blood Pressure"]

    if (not data.check_all_none(patient_bp)):
        line_values.append(patient_bp)
    else: line_values.append([0 for value in patient_bp])

    if (not data.check_all_none(patient_dbp)):
        line_values.append(patient_dbp)
    else: line_values.append([0 for value in patient_dbp])
    
    if (not data.check_all_none(patient_sbp)):
        line_values.append(patient_sbp)
    else: line_values.append([0 for value in patient_sbp])

    return render_template('line_chart.html', title='Line Graph', name=patient_name, labels=line_labels,
                            values=line_values, colors=line_colors, ds_labels=line_dataset_labels)
